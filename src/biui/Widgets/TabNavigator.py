#include "biui.inc"

import biui
from biui.Widgets import Pane, ButtonGroup
from biui.Widgets.ToggleButton import ToggleButton
from biui.Enum import Alignment
from biui.Events import EventManager, Event

class TabNavigator(Pane):
    
    def __init__(self):
        super().__init__()
        
        ##
        self.__buttonPane = self.createButtonPane()
        self.__buttonPane.onChanged.add(self.__hndNavChanged)
        self.__buttonPane.alignment = Alignment.FILL
        self.addChild(self.__buttonPane)
        
        self.height = 30
        
        ##
        self.__activeTab = 0
        
        ##
        self.__buttons = []
        
        self.layoutManager.rowWidths = [0,1]
        self.layoutManager.columnHeights = [0]
        
        ##
        self.onTabChanged = EventManager()
    FUNCTIONEND
    
    ###
    ##
    ##
    def _onTabChanged(self):
        self.onTabChanged.provoke( Event(self) )
    FUNCTIONEND
    
    ###
    ##
    ##
    def __hndNavChanged(self,ev):
        self._onTabChanged()
    FUNCTIONEND
    
    ###
    ##
    ##
    def createButtonPane(self):
        result = ButtonGroup()
        return result
    FUNCTIONEND
    
    ###
    ##
    ##
    def createTabButton(self, name):
        result = ToggleButton()
        result.value = name
        result.alignment = Alignment.DOCK_LEFT
        return result
    FUNCTIONEND
    
    ###
    ##
    ##
    def addTab(self, name):
        button = self.createTabButton(name)
        self.__buttonPane.addChild(button)
        self.__buttons.append(button)
        self.__activeTab = len(self.__buttons)
        
        if self.alignment in [Alignment.DOCK_TOP,Alignment.DOCK_BOTTOM]:
            button.alignment = Alignment.DOCK_LEFT
        else:
            button.alignment = Alignment.DOCK_TOP
            
        return button
    FUNCTIONEND
    
    ###
    ##
    ##  child is a Button or the index
    def removeTab(self, child=0):
        if type(child) is int:
            child = self.__buttons[child]
        self.__buttonPane.removeChild(child)
        self.__buttons.remove(child)
    FUNCTIONEND
    
    ###
    ##
    ##
    @property
    def activeTab(self):
        return self.__buttonPane.activeChild
    FUNCTIONEND
     
    ###
    ##
    ##
    @activeTab.setter
    def activeTab(self,index):
        self.__buttonPane.activeChild = index
    FUNCTIONEND
    
    @property
    def alignment(self):
        return super().alignment
    FUNCTIONEND
    
    @alignment.setter
    def alignment(self,value):
        super(TabNavigator,self.__class__).alignment.fset(self,value)
        ##self.__buttonPane.alignment = value 
        
        if value in [Alignment.DOCK_TOP,Alignment.DOCK_BOTTOM]:
            for b in self.__buttons:
                b.alignment = Alignment.DOCK_LEFT
        else:
            for b in self.__buttons:
                b.alignment = Alignment.DOCK_TOP
    FUNCTIONEND
    

    
    
    