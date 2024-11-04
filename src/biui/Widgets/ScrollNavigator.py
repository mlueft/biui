#include "pysdl2.inc"
#include "biui.inc"

import sdl2

import biui
from biui.Widgets import ContainerWidget
from biui.Widgets import Spacer
from biui.Events import EventManager
from biui.Events import Event

###
##
##
class ScrollNavigator(ContainerWidget):
    
    ###
    ##
    ##
    def __init__(self):
        super().__init__()
        theme = biui.getTheme()
        self._themeBackgroundfunction = theme.drawScrollNavigatorBeforeChildren
        self._themeForegroundfunction = theme.drawScrollNavigatorAfterChildren
        
        self.__isHorizontal = False
        self.__isVertical = False
        
        self.__dragger = self.createDragger()
        self.__dragger.onMouseDown.add(self.__hndDraggerOnMouseDown)
        self.addChild(self.__dragger)
        
        self.__draggerDownPosition = None
        
        ##
        self.onScrollPositionChanged = EventManager()
        
        self.onResized.add(self.__hndOnResized)
        
        self.__scrollPosition = [0,0]
    FUNCTIONEND
    
    ###
    ##
    ##
    def createDragger(self):
        result = Spacer()
        result.width = 30
        result.height = 30
        return result
    FUNCTIONEND
    
    ###
    ##
    ##
    def __hndOnResized(self,ev):
        self.__dragger.x = (self.width-self.__dragger.width)*self.__scrollPosition[0]
        self.__dragger.y = (self.height-self.__dragger.height)*self.__scrollPosition[1]
    FUNCTIONEND
        
    ### @see: biui.Widget.width
    ##
    ##
    @property
    def width(self):
        return super().width
    FUNCTIONEND
        
    ### @see: biui.Widget.width
    ##
    @width.setter     
    def width(self, value):
        if value == super().width:
            return
        super(ScrollNavigator,self.__class__).width.fset(self,value)
        if self.__isHorizontal:
            self.__dragger.y = 0
            self.__dragger.height = self.height
            self._invalidate()
    FUNCTIONEND
    
    ## @see: biui.Widget.height
    ##
    ##
    @property
    def height(self):
        return super().height
    FUNCTIONEND
    
    ### @see: biui.Widget.height
    ##
    ##
    @height.setter
    def height(self, value):
        if value == super().height:
            return
        super(ScrollNavigator,self.__class__).height.fset(self,value)
        if self.__isVertical:
            self.__dragger.x = 0
            self.__dragger.width = self.width
            self._invalidate()
    FUNCTIONEND
    
    ###
    ##
    ##
    def connectPane(self,pane):
        if pane.onScrollPositionChanged.has(self.__hndPaneOnScrollPositionChanged):
            return
    
        pane.onScrollPositionChanged.add(self.__hndPaneOnScrollPositionChanged)
        pane.connectScrollNavigator(self)
    FUNCTIONEND
      
    ###
    ##
    ##
    def disconnectPane(self,pane):
        if not pane.onScrollPositionChanged.has(self.__hndPaneOnScrollPositionChanged):
            return
    
        pane.onScrollPositionChanged.remove(self.__hndPaneOnScrollPositionChanged)
        pane.disconnectScrollNavigator(self)
        
    ###
    ##
    ##
    def __hndPaneOnScrollPositionChanged(self,ev):
        es = ev.eventSource
        sp = es.scrollPosition
        if self.isHorizontal:
            if es.scrollWidth > 0:
                self.__scrollPosition[0] = sp[0]/es.scrollWidth
                self.__dragger.x = (self.width-self.__dragger.width)*sp[0]/es.scrollWidth
            else:
                self.__scrollPosition[0] = 0
                self.__dragger.x = 0
            ##return 
        elif self.isVertical:
            if es.scrollHeight > 0:
                self.__scrollPosition[1] = sp[1]/es.scrollHeight
                self.__dragger.y = (self.height-self.__dragger.height)*sp[1]/es.scrollHeight
            else:
                self.__scrollPosition[1] = 0
                self.__dragger.y = 0
            ##return 
        else:
            if es.scrollWidth > 0:
                self.__scrollPosition[0] = sp[0]/es.scrollWidth
                self.__dragger.x = (self.width-self.__dragger.width)*sp[0]/es.scrollWidth
            else:
                self.__scrollPosition[0] = 0
                self.__dragger.x = 0
            ##return
            if es.scrollHeight > 0:
                self.__scrollPosition[1] = sp[1]/es.scrollHeight
                self.__dragger.y = (self.height-self.__dragger.height)*sp[1]/es.scrollHeight
            else:
                self.__scrollPosition[1] = 0
                self.__dragger.y = 0
        self._invalidate()
    FUNCTIONEND
    
    ### Returns the State if the Scroll navigator is used as 
    ##  horizontal scroll bar.
    ##
    ##  @return            A boolean value.
    ##
    @property
    def isHorizontal(self):
        return self.__isHorizontal
    FUNCTIONEND
        
    ### Defines if the scroll navigator is used as a 
    ##  hotizontal scroll bar.
    ##
    ##  @param value       An boolean value.
    ##  @return            None
    ##
    @isHorizontal.setter
    def isHorizontal(self, value):
        if value == self.__isHorizontal:
            return
        
        if value:
            self.__dragger.y = 0
            self.__dragger.height = self.height
            
        self.__isHorizontal = value
        self._invalidate()
    FUNCTIONEND
            
    ### Returns the State if the Scroll navigator is used as 
    ##  vertical scroll bar.
    ##
    ##  @return            A boolean value.
    ##
    @property
    def isVertical(self):
        return self.__isVertical
    FUNCTIONEND
        
    ### Defines if the scroll navigator is used as a 
    ##  vertical scroll bar.
    ##
    ##  @param value       An boolean value.
    ##  @return            None
    ##
    @isVertical.setter
    def isVertical(self, value):
        if value == self.__isVertical:
            return
        
        if value:
            self.__dragger.x = 0
            self.__dragger.width = self.width
                    
        self.__isVertical = value
        self._invalidate()
    FUNCTIONEND
    
    ###
    ##
    ##
    def __hndWindowStopDragging(self,ev=None):
        print("ScrollNavigator::__hndWindowStopDragging")
        self.window.onMouseMove.remove(self.__hndWindowOnMouseMove)
        self.window.onMouseUp.remove(self.__hndWindowStopDragging)
    FUNCTIONEND
    
    ###
    ##
    ##
    def __hndDraggerOnMouseDown(self,ev):
        print("ScrollNavigator::__hndDraggerOnMouseDown")
        self.__draggerDownPosition = ev.eventSource.toLocal(ev.position)
        self.window.onMouseMove.add(self.__hndWindowOnMouseMove)
        self.window.onMouseUp.add(self.__hndWindowStopDragging)
        ##self.window.onWindowLeave.add( self.__hndWindowStopDragging )
    FUNCTIONEND
    
    ###
    ##
    ##
    def __hndWindowOnMouseMove(self,ev):
        ##print("ScrollNavigator::__hndWindowOnMouseMove")
        currentPos = self.toLocal(ev.position)
        
        x = self.__dragger.x
        y = self.__dragger.y
        
        self.__dragger.x = currentPos[0]-self.__draggerDownPosition[0]
        self.__dragger.y = currentPos[1]-self.__draggerDownPosition[1]
        
        self.__dragger.x = min(
            max(0,self.__dragger.x),
            self.width-self.__dragger.width
        )
        
        self.__dragger.y = min(
            max(0,self.__dragger.y),
            self.height-self.__dragger.height
        )
        
        if x != self.__dragger.x or y != self.__dragger.y:
            self.onScrollPositionChanged.provoke(Event(self))
        self._invalidate()
    FUNCTIONEND
    
    ### Returns a tuple with x and y of the current scrollposition.
    ##  Values are between 0 and 1 for 0% and 100%.
    ##
    ##  @return
    ##
    @property
    def draggerPosition(self):
        
        x = self.__dragger.x
        y = self.__dragger.y
        
        w = self.width-self.__dragger.width
        h = self.height-self.__dragger.height
        
        if w == 0:
            x = 0
        else:
            x = x/w
            
        if h == 0:
            y = 0
        else:
            y = y/h
        
        self.__scrollPosition = [x,y]
        return self.__scrollPosition
    FUNCTIONEND
    
        