#include "biui.inc"
#include "pysdl2.inc"

from typing import Callable,NoReturn,Any,Union
import sdl2

import biui
from biui.Widgets.ContainerWidget import ContainerWidget
from biui.Events import EventManager, Event

###
##
##
class ScrollableContainerWidget(ContainerWidget):
    
    ###
    ##
    ##
    def __init__(self):
        #ifdef SHOW_FUNCTIONNAMES
        print("ScrollableContainerWidget::__init__():{}".format(self))
        #endif        
        super().__init__()
        
        ### Is provoked when the scroll position is changed.
        ##
        self.onScrollPositionChanged:EventManager = EventManager()
                
        ###
        ##
        ##
        self.onScrollSizeChanged:EventManager = EventManager()
        
        ## Contains the size of the scrollarea
        ## Scrollarea is a boundingbox starting at (0,0)
        ## containing all children
        ## Minimum the size of self
        self._scrollWidth:int = self.width
        self._scrollHeight:int = self.height
        
        ## Current top left corner of the
        ## visible area
        self._scrollX:int = 0
        self._scrollY:int = 0
    FUNCTIONEND
    
    ### Returns the current scroll position.
    ##
    ##  @return            A tuple representing the position.
    ##
    @property
    def scrollPosition(self)->tuple[int,int]:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::scrollPosition_get():{}".format(self))
        #endif
        return (self._scrollX, self._scrollY)
    FUNCTIONEND
    
    ### Returns the x/y position of the GUI element.
    ##
    ##  @return            A tuple representing the size.
    ##
    @property
    def maxScrollPosition(self)->tuple[int,int]:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::maxScrollPosition_get():{}".format(self))
        #endif
        return (self.maxScrollX, self.maxScrollY)
    FUNCTIONEND
    
    ### Returns the maximum scroll position in x direction.
    ##
    ##  @return            
    ##
    @property
    def maxScrollX(self)->int:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::maxScrollX_get():{}".format(self))
        #endif
        return self._scrollWidth-self.width
    FUNCTIONEND
    
    ### Returns the maximum scroll position in y direction.
    ##
    ##  @return            
    ##
    @property
    def maxScrollY(self)->int:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::maxScrollY_get():{}".format(self))
        #endif
        return self._scrollHeight-self.height
    FUNCTIONEND
    
    ### Returns the current scroll position in x direction.
    ##
    ##  @return            
    ##
    @property
    def scrollX(self)->int:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::scrollX_get():{}".format(self))
        #endif
        return self._scrollX
    FUNCTIONEND
    
    ### Sets the current scroll position in x direction. 
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##
    @scrollX.setter
    def scrollX(self, value:int)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::scrollX_set():{}".format(self))
        #endif
        value = int(value)
        if value == self._scrollX:
            return
        
        value = min(value,self.maxScrollX)
        value = max(value,0)
        
        self._scrollX = value
        self._invalidate()
        self._onScrollPositionChanged(Event(self))
    FUNCTIONEND
    
    ### Returns the current scroll position in y direction.
    ##
    ##  @return            
    ##
    @property
    def scrollY(self)->int:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::scrollY_get():{}".format(self))
        #endif
        return self._scrollY
    FUNCTIONEND
    
    ### Sets the current scroll position in y direction. 
    ##
    ##  @param value       A integer value.
    ##  @return            None
    ##
    @scrollY.setter
    def scrollY(self, value:int)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::scrollY_set():{}".format(self))
        #endif
        value = int(value)
        if value == self._scrollY:
            return
        
        value = min(value,self.maxScrollY)
        value = max(value,0)
        
        self._scrollY = value
        self._invalidate()
        self._onScrollPositionChanged(Event(self))
    FUNCTIONEND
    
    ### Returns the width of the scroll area.
    ##
    ##
    @property
    def scrollWidth(self):
        return self._scrollWidth
    FUNCTIONEND
    
    ### Returns the height of the scroll area.
    ##
    ##
    @property
    def scrollHeight(self):
        return self._scrollHeight
    FUNCTIONEND
    
    ###
    ##
    ##
    @property
    def scrollSize(self):
        return (self.scrollWidth,self.scrollHeight)
    FUNCTIONEND
    
    
    ##
    #
    #
    def _onScrollPositionChanged(self,ev):
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::_onScrollPositionChanged():{}".format(self))
        #endif
        self.onScrollPositionChanged.provoke(ev)    
    FUNCTIONEND
    
    ##
    #
    #
    def _onScrollSizeChanged(self,ev):
        self.onScrollSizeChanged.provoke( ev )
    FUNCTIONEND
    
    ### @see Widget._calculateLayout
    ##
    ##
    def _calculateLayout(self)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::_calculateLayout():{}".format(self))
        #endif
        
        ## First we calculate our own size
        self._layoutManager._calculateLayout(self.size)
        
        ## And determine scroll size
        sw = self.width
        sh = self.height
        ##print(sw,sh)
        for child in self._children:
            sw = max(sw,child.right)
            sh = max(sh,child.bottom)
            
        scrollSizeChanged = self._scrollWidth != sw or self._scrollHeight != sh
        self._scrollWidth = sw
        self._scrollHeight = sh
        
        ## Next we let all children recalculate
        for c in self._children:
            c._calculateLayout()

        if scrollSizeChanged:
            self._onScrollSizeChanged( Event(self) )
        
        ## Finally we let super class record dirty rects.
        super()._calculateLayout()
    FUNCTIONEND
    
    ### See Widget.
    ##
    ##
    def recordDirtyRect(self):
        box = (0,0,self._scrollWidth,self._scrollHeight)
        self._recordDirtyRect(box)
    FUNCTIONEND
    
    ###
    ##
    ##
    @property
    def renderRect(self):
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::renderRect():{}".format(self))
        #endif
        return (self._scrollX,self._scrollY,self.width,self.height)
    FUNCTIONEND
        
    ### @see Widget._render
    ##
    ##  todo: hinting        
    def _render(self, forceRedraw:bool=False ):
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::_render():{}".format(self))
        #endif
        if not self.isInvalide():
            if not forceRedraw:
                return

        ##print("ContainerWidget::_render(): {}".format(self))
        
        ##print( "redraw:{} {}x{} {}".format(self.name,self.x,self.y,forceRedraw))
 
        wnd = self.window
        renderer = self.window.renderer
        
        PYSDL2_CREATETEXTURE(renderer,self._scrollWidth,self._scrollHeight,texture)
              
        pos = self.position
        
        self._themeBackgroundfunction(self,texture)
 
        forceRedraw = self._isInvalide or forceRedraw
        
        for c in self._children:
            
            ## Each child returns a texture where it has drawn itself at (0,0)
            tx = c._render(forceRedraw)
            src = c.renderRect
            tgt = (c.x,c.y,src[2],src[3])

            PYSDL2_RENDER_COPY1(renderer,texture,tx,tgt,src)
            ## Finally we have to destroy the texture returned by the child
            PYSDL2_DESTROYTEXTURE( tx )
                    
        self._themeForegroundfunction(self,texture)
        
        self._isInvalide = False# pylint:disable=attribute-defined-outside-init
        
        return texture
    FUNCTIONEND
    
    ### @see Widget.toLocal
    ##
    ##
    def toLocal(self, coordinates:tuple[int,int])->tuple[int,int]:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::toLocal():{}".format(self))
        #endif
        result = ( coordinates[0]-self._x+self._scrollX,coordinates[1]-self._y+self._scrollY)
        if self._parent is not None:
            result = self._parent.toLocal(result)
        
        return result
    FUNCTIONEND
    
    ### @see Widget.toGlobal
    ##
    ##
    def toGlobal(self,coordinates:tuple[int,int])->tuple[int,int]:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::toGlobal():{}".format(self))
        #endif
        result = ( self._x-self._scrollX+coordinates[0],self._y-self._scrollY+coordinates[1])
        if self._parent is not None:
            result = self._parent.toGlobal(result)
        
        return result
    FUNCTIONEND
    ### @see Widget._recordDirtyRect
    ##
    ##    
    def _recordDirtyRect(self, box:tuple[int,int,int,int])->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::_recordDirtyRect():{}".format(self))
        #endif
        sx = self._scrollX
        sy = self._scrollY
        
        if self.parent is None:
            return
        if self.window is None:
            return
        
        ## Check if the box is outside of the visible area
        if box[0]-sx > self.width:
            return 
        if box[1]-sy > self.height:
            return
        if box[0]+box[2]-sx < 0:
            return 
        if box[1]+box[3]-sy < 0:
            return
            
        ## We cut the box if it´s not complete in the visible area.
        
        ## We cut the box at the top/left visible border
        bx = max( 0, box[0] - sx )
        by = max( 0, box[1] - sy )
        ## We cut the box at the right/bottom visible border
        br = min( box[0]+box[2]-sx, self.x+self.width )
        bb = min( box[1]+box[3]-sy, self.y+self.height )
        
        ## we translate the box to the parent´s coordinate system
        ## and we cut of if it´s reaching over the edgees.
        box = (
            self.x+bx,
            self.y+by,
            br-bx,
            bb-by
        )
        self.parent._recordDirtyRect(box)
    FUNCTIONEND
    
    
    
    
    
    
    