#include "biui.inc"
#include "pysdl2.inc"
import sdl2 

import biui
from biui.Widgets import ContainerWidget
from biui.Widgets import ScrollNavigator
from biui.Enum import Alignment
from biui.Events import Event, EventManager

###
##
##
class Pane(ContainerWidget):
    
    ###
    ##
    ##
    def __init__(self):
        
        super().__init__()
        self.__contentPane = self._createContainerWidget()
        self.__contentPane.alignment = Alignment.FILL
        self.__contentPane.onScrollSizeChanged.add(self.__hndScrollSizeChanged )
        
        super().addChild(self.__contentPane,0,0)
        
        ##
        self.__verticalScrollbar = None
        ##
        self.__horizontalScrollbar = None
        
        self.layoutManager.columnWidths = [0]
        self.layoutManager.rowHeights = [0]
        
        theme = biui.getTheme()
        self._themeBackgroundfunction = theme.drawPaneBeforeChildren
        self._themeForegroundfunction = theme.drawPaneAfterChildren
        
        ###
        ##
        ##
        self.onScrollSizeChanged:EventManager = EventManager()
    FUNCTIONEND
    
    ###
    ##
    ##
    FUNCTIONEND
    
    def _createContainerWidget(self):
        result = ContainerWidget()
        return result
    FUNCTIONEND
    
    def _createScrollNavigator(self):
        resut = ScrollNavigator()
        return result
    FUNCTIONEND
    
    ###
    ##
    ##
    def __hndScrollSizeChanged(self,ev):
        ##print("Pane::__hndScrollSizeChanged()")
        self.onScrollSizeChanged.provoke( Event(self) )
    FUNCTIONEND
    
    ###
    ##
    ##
    def connectScrollNavigator(self,navigator):
        ##if navigator.onScrollPositionChanged.has(self.__hndOnScrollPositionChanged):
        ##    return
        navigator.connectPane(self.__contentPane)
    FUNCTIONEND
        
    ###
    ##
    ##
    def disconnectScrollNavigator(self,navigator):
        navigator.disconnectPane(self.__contentPane)
    FUNCTIONEND
            
    ###
    ##
    ##
    @property
    def layoutManager(self):
        return self.__contentPane.layoutManager
    FUNCTIONEND
    
    @property
    def verticalScrollbar(self):
        return self.__verticalScrollbar != None
    FUNCTIONEND
    
    ###
    ##
    ##
    @verticalScrollbar.setter
    def verticalScrollbar(self,value):
        if value and self.__verticalScrollbar:
            return

        if not value and not self.__verticalScrollbar:
            return
                
        if not value:
            ## remove scrollbar
            self.__contentPane.disconnectScrollNavigator(self.__verticalScrollbar)
            super().removeChild(self.__verticalScrollbar)
            super().layoutManager.columnWidths = [0,1]
            self.__verticalScrollbar = None
            return 
        
        ## add scrollbar
        super().layoutManager.columnWidths = [0,20]
        ##sn = self._createScrollNavigator()
        sn = ScrollNavigator()
        sn.alignment = Alignment.FILL
        sn.isVertical = True
        self.__contentPane.connectScrollNavigator(sn)
        super().addChild(sn,1,0)
        self.__verticalScrollbar = sn
    FUNCTIONEND
        
    ###
    ##
    ##
    @property
    def horizontalScrollbar(self):
        return self.__horizontalScrollbar != None
    FUNCTIONEND
    
    ###
    ##
    ##
    @horizontalScrollbar.setter
    def horizontalScrollbar(self,value):
        if value and self.__horizontalScrollbar:
            return
        
        if not value and not self.__verticalScrollbar:
            return
                
        if not value:
            ## remove scrollbar
            super().layoutManager.rowHeights = [0,1]
            super().removeChild(self.__horizontalScrollbar)
            self.__contentPane.disconnectScrollNavigator(self.__horizontalScrollbar)
            self.__horizontalScrollbar = None
            return 
        
        ## add scrollbar
        super().layoutManager.rowHeights = [0,20]
        ##sn = self._createScrollNavigator()
        sn = ScrollNavigator()
        sn.alignment = Alignment.FILL
        sn.isHorizontal = True
        self.__contentPane.connectScrollNavigator(sn)
        super().addChild(sn,0,1)
        self.__horizontalScrollbar = sn
    FUNCTIONEND
        
    def hasChildren(self):
        #ifdef SHOW_FUNCTIONNAMES
        print("Pane::hasChildren():{}".format(self))
        #endif
        return self.__contentPane.hasChildren()
    FUNCTIONEND

    @property
    def children(self):
        #ifdef SHOW_FUNCTIONNAMES
        print("Pane::children():{}".format(self))
        #endif
        return self.__contentPane.children
    FUNCTIONEND
        
    def hasChild(self,child):
        #ifdef SHOW_FUNCTIONNAMES
        print("Pane::hasChild():{}".format(self))
        #endif
        
        ## TODO: Scrollbars are actually not children
        ## of the pane :-/(
        ## This is necassary to make mouse events
        ## working for scrollbars
        result = self.__contentPane.hasChild(child) or super().hasChild(child)
        
        return result
    FUNCTIONEND
    
    ### @see: biui.ContainerWidget.removeChild
    ##
    ##   
    def removeChild(self,child):
        self.__contentPane.removeChild(child)
    FUNCTIONEND
     
    ### @see: biui.ContainerWidget.addChild
    ##
    ##       
    def addChild(self,child,x=0,y=0):
        self.__contentPane.addChild(child,x,y)
    FUNCTIONEND
        
    ### Returns the current scroll position.
    ##
    ##  @return            A tuple representing the position.
    ##
    @property
    def scrollPosition(self):
        return self.__contentPane.scrollPosition 
    FUNCTIONEND
    
    ### Returns the x/y position of the GUI element.
    ##
    ##  @return            A tuple representing the size.
    ##
    @property
    def maxScrollPosition(self):
        return self.__contentPane.maxScrollPosition
    FUNCTIONEND
            
    ### Returns the maximum scroll position in x direction.
    ##
    ##  @return            
    ##
    @property
    def maxScrollX(self):
        return self.__contentPane.maxScrollX
    FUNCTIONEND
    
    ### Returns the maximum scroll position in y direction.
    ##
    ##  @return            
    ##
    @property
    def maxScrollY(self):
        return self.__contentPane.maxScrollY
    FUNCTIONEND
    
    ### Returns the current scroll position in x direction.
    ##
    ##  @return            
    ##
    @property
    def scrollX(self):
        return self.__contentPane.scrollX
    FUNCTIONEND
    
    ### Sets the current scroll position in x direction. 
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##
    @scrollX.setter
    def scrollX(self, value):
        self.__contentPane.scrollX = value
    FUNCTIONEND
        
    ### Returns the current scroll position in y direction.
    ##
    ##  @return            
    ##
    @property
    def scrollY(self):
        return self.__contentPane.scrollY
    FUNCTIONEND
    
    ### Sets the current scroll position in y direction. 
    ##
    ##  @param value       A integer value.
    ##  @return            None
    ##
    @scrollY.setter
    def scrollY(self, value):
        self.__contentPane.scrollY = value
    FUNCTIONEND
        
    ### Returns the width of the scroll area.
    ##
    ##
    @property
    def scrollWidth(self):
        return self.__contentPane.scrollWidth
    FUNCTIONEND
    
    ### Returns the height of the scroll area.
    ##
    ##
    @property
    def scrollHeight(self):
        return self.__contentPane.scrollHeight
    FUNCTIONEND
    
    ###
    ##
    ##
    @property
    def scrollSize(self):
        return self.__contentPane.scrollSize
    FUNCTIONEND
        
    ###
    ##
    ##
    @property
    def renderRect(self):
        return (0,0,self._width,self._height)
    FUNCTIONEND
    
    