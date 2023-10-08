#include "pysdl2.inc"
import sdl2
import biui

###
##
##
class ScrollPane(biui.ContainerWidget.ContainerWidget):
    
    ###
    ##
    ##
    def __init__(self):
        super().__init__()

        self.layoutManager.columnWidths = [0,1]
        self.layoutManager.rowHeights = [0,1]
        
        self.__contentPane = biui.Pane()
        self.__contentPane.alignment = biui.Alignment.FILL
        self.__contentPane.onScrollPositionChanged.add(self.__hndOnScrollPositionChanged)
        super().addChild(self.__contentPane,0,0)
        
        ##
        self.onScrollPositionChanged = biui.EventManager()
        ##
        self.__verticalScrollbar = None
        ##
        self.__horizontalScrollbar = None
        
    def __hndOnScrollPositionChanged(self,ev):
        self.onScrollPositionChanged.provoke(biui.Event(self))
        
    ###
    ##
    ##
    def connectScrollNavigator(self,navigator):
        if navigator.onScrollPositionChanged.has(self.__hndOnScrollPositionChanged):
            return
        
        navigator.connectPane(self.__contentPane)

    ###
    ##
    ##
    def disconnectScrollNavigator(self,navigator):
        navigator.disconnectPane(self.__contentPane)
            
    ###
    ##
    ##
    @property
    def verticalScrollbar(self):
        return self.__verticalScrollbar != None
    
    ###
    ##
    ##
    @verticalScrollbar.setter
    def verticalScrollbar(self,value):
        if value and self.__verticalScrollbar:
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
        sn = biui.ScrollNavigator()
        sn.alignment = biui.Alignment.FILL
        sn.isVertical = True
        self.__contentPane.connectScrollNavigator(sn)
        super().addChild(sn,1,0)
        self.__verticalScrollbar = sn
        
    ###
    ##
    ##
    @property
    def horizontalScrollbar(self):
        return self.__horizontalScrollbar != None
    
    ###
    ##
    ##
    @horizontalScrollbar.setter
    def horizontalScrollbar(self,value):
        if value and self.__horizontalScrollbar:
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
        sn = biui.ScrollNavigator()
        sn.alignment = biui.Alignment.FILL
        sn.isHorizontal = True
        self.__contentPane.connectScrollNavigator(sn)
        super().addChild(sn,0,1)
        self.__horizontalScrollbar = sn
        
    ### @see: biui.ContainerWidget.removeChild
    ##
    ##   
    def removeChild(self,child):
        self.__contentPane.removeChild(child)
     
    ### @see: biui.ContainerWidget.addChild
    ##
    ##       
    def addChild(self,child,x=0,y=0):
        self.__contentPane.addChild(child,x,y)
        
    ### Returns the current scroll position.
    ##
    ##  @return            A tuple representing the position.
    ##
    @property
    def scrollPosition(self):
        return self.__contentPane.scrollPosition 
    
    ### Returns the x/y position of the GUI element.
    ##
    ##  @return            A tuple representing the size.
    ##
    @property
    def scrollSize(self):
        return self.__contentPane.scrollSize
            
    ### Returns the maximum scroll position in x direction.
    ##
    ##  @return            
    ##
    @property
    def scrollWidth(self):
        return self.__contentPane.scrollWidth
    
    ### Returns the maximum scroll position in y direction.
    ##
    ##  @return            
    ##
    @property
    def scrollHeight(self):
        return self.__contentPane.scrollHeight
    
    ### Returns the current scroll position in x direction.
    ##
    ##  @return            
    ##
    @property
    def scrollX(self):
        return self.__contentPane.scrollX
    
    ### Sets the current scroll position in x direction. 
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##
    @scrollX.setter
    def scrollX(self, value):
        self.__contentPane.scrollX = value
        
    ### Returns the current scroll position in y direction.
    ##
    ##  @return            
    ##
    @property
    def scrollY(self):
        return self.__contentPane.scrollY
    
    ### Sets the current scroll position in y direction. 
    ##
    ##  @param value       A integer value.
    ##  @return            None
    ##
    @scrollY.setter
    def scrollY(self, value):
        self.__contentPane.scrollY = value
        
