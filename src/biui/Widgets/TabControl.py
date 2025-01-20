#include "biui.inc"

import biui
from biui.Widgets import Pane,TabNavigator
from biui.Enum import Alignment
from biui.Events import EventManager, Event

class TabControl(Pane):
    
    def __init__(self):
        super().__init__()
    
        self.__contentPane = self.createTabPane()
        self.__contentPane.alignment = Alignment.FILL
        self.addChild(self.__contentPane)
        
        self.__tabNavigator = self.createTabNavigator()
        self.__tabNavigator.alignment = Alignment.DOCK_TOP
        self.__tabNavigator.onTabChanged.add(self.__hndNavChanged)
        self.addChild(self.__tabNavigator)
        
        ##
        self.__tabWidth = 150
        self.__tabHeight = 30
        
        self.__activeItem = None
        self.__activeIndex = None
        self.__tabs = []
        
        self.onTabShown = EventManager()
        self.onTabHidden = EventManager()
        self.onTabChanged = EventManager()
    FUNCTIONEND

    def _onTabShown(self, tab):
        self.onTabShown.provoke(Event(tab))
    FUNCTIONEND
    
    def _onTabHidden(self,tab):
        self.onTabHidden.provoke(Event(tab))
    FUNCTIONEND
    
    def _onTabChanged(self):
        self.onTabChanged.provoke(Event(self))
    FUNCTIONEND
    
     
    def createTabPane(self):
        result = Pane()
        result.alignment = Alignment.FILL
        return result
    FUNCTIONEND
    
    def createTabNavigator(self):
        result = TabNavigator()

        return result
    FUNCTIONEND
    
    def __setActiveTab(self, index, setNav = True):
        if len(self.__tabs) == 0:
            return
        
        index = max(0,min(index,len(self.__tabs)-1))
        nextTab = self.__tabs[index]
        
        if index == self.__activeIndex:
            return
        
        
        if self.__activeItem != None:
            self.__contentPane.removeChild(self.__activeItem)
            self._onTabHidden(self.__activeItem)
                
        self.__contentPane.addChild(nextTab)
        nextTab.alignment = Alignment.FILL
        self.__activeItem = nextTab
        self.__activeIndex = index
        
        if setNav:
            self.__tabNavigator.activeTab = index
            
        self._onTabShown(self.__activeItem)
        self._onTabChanged()
    FUNCTIONEND
        
    def __hndNavChanged(self,ev):
        self.__setActiveTab(self.__tabNavigator.activeTab,False)
    FUNCTIONEND
    
    def addTab(self,tab):
        self.__tabs.append(tab)
        self.__tabNavigator.addTab(tab.name)
        self.activeTab = len(self.__tabs)
    FUNCTIONEND
    
    def removeTab(self,child):
        if type(child) is int:
            child = self.__tabs[child]
            
        if child not in self.__tabs:
            return
        
        index = 0
        for i,c in enumerate(self.__tabs):
            if c == child:
                index = i
                break
        
        self.__tabNavigator.removeTab(index)
        self.__contentPane.removeChild(child)
        self.__tabs.remove(child)
        self.__activeItem = None
        self.__activeIndex = None
        self.activeTab = index
    FUNCTIONEND
    
    @property
    def activeTab(self):
        for i,t in enumerate(self.__tabs):
            if t == self.__activeItem:
                return i
    FUNCTIONEND
    
    @activeTab.setter
    def activeTab(self,index):
        self.__setActiveTab(index,True)
    FUNCTIONEND
    
    ##
    #
    #
    @property
    def tabCount(self):
        return len(self.__tabs)
    FUNCTIONEND
    
    ###
    ##
    ##
    @property
    def activeItem(self):
        return self.__activeItem
    FUNCTIONEND
    
    @property
    def tabAlignment(self):
        return self.__tabNavigator.alignment
    FUNCTIONEND
    
    @tabAlignment.setter
    def tabAlignment(self,value):
        if value not in [Alignment.DOCK_TOP,Alignment.DOCK_RIGHT,Alignment.DOCK_BOTTOM,Alignment.DOCK_LEFT]:
            value = Alignment.DOCK_TOP
            
        self.__tabNavigator.alignment = value
        
        if value in [Alignment.DOCK_TOP,Alignment.DOCK_BOTTOM]:
            self.__tabNavigator.height = self.__tabHeight
        else:
            self.__tabNavigator.width = self.__tabWidth
        
    FUNCTIONEND
    
    ###
    ##
    ##
    @property
    def tabWidth(self):
        return self.__tabWidth
    FUNCTIONEND
        
    ###
    ##
    ##
    @tabWidth.setter
    def tabWidth(self,value):
        self.__tabWidth = value
        if self.__tabNavigator.alignment in [Alignment.DOCK_LEFT,Alignment.DOCK_RIGHT]:
            self.__tabNavigator.width = value
    FUNCTIONEND
    
    ###
    ##
    ##
    @property
    def tabHeight(self):
        return self.__tabHeight
    FUNCTIONEND
    
    ###
    ##
    ##
    @tabHeight.setter
    def tabHeight(self,value):
        self.__tabHeight = value
        if self.__tabNavigator.alignment in [Alignment.DOCK_TOP,Alignment.DOCK_BOTTOM]:
            self.__tabNavigator.height = value
    FUNCTIONEND
    
    @property
    def showNavigation(self):
        pass
    FUNCTIONEND
    
    @showNavigation.setter
    def showNavigation(self, value):
        print("show tabs : {}".format(value))
        if value and not self.hasChild(self.__tabNavigator):
            self.addChild(self.__tabNavigator)
        elif not value and self.hasChild(self.__tabNavigator):
            self.removeChild(self.__tabNavigator)
            
    FUNCTIONEND
    