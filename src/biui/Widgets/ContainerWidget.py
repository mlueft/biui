#include "biui.inc"
#include "pysdl2.inc"

from typing import  List,Callable
import sdl2
import biui
from biui.Events import Event
from biui.Events import MouseEvent
from biui.Events import KeyEvent
from biui.Events import EventManager
from biui.Enum import Alignment 
from biui.LayoutManager import LayoutManager
from biui.Widgets import Widget

### Base class for all container widgets.
##
##
class ContainerWidget(Widget):
    
    def __init__(self):
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::__init__():{}".format(self))
        #endif
        super().__init__()
        ##
        self._children:List[Widget] = []
        
        ##
        self._layoutManager:LayoutManager = LayoutManager()
        
        ### Is provoked when a child is added
        ##
        self.onChildAdded:EventManager = EventManager()
        
        ### Is provoked when a child is removed
        ##
        self.onChildRemoved:EventManager = EventManager()

        ### Is provoked when the scroll position is changed.
        ##
        self.onScrollPositionChanged:EventManager = EventManager()
                
        ##
        ## todo: hinting
        self._texture = None
        ## A reference to the theme function which is used to draw the widget forground.
        theme = biui.getTheme()
        self._themeForegroundfunction:Callable = theme.drawEmpty
        
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
    
    ###
    ##
    ##
    def __dir__(self):
        result = super().__dir__()
        result = result + [
            "onChildAdded",   "onChildRemoved", "onScrollPositionChanged",
            
            "scrollPosition", "scrollSize",     "scrollWidth", 
            "scrollHeight",   "scrollX",        "scrollY",
            "layoutManager",  "renderRect",
            
            "connectScrollNavigator", "disconnectScrollNavigator", "hasChildren",
            "getChildren",            "hasChild",                  "removeChild",
            "addChild",               "getChildAt",                "isInvalide",
            "toLocal",                "toGlobal",
            
            "_calculateLayout",       "_render",       "_invalidate",   "_recordDirtyRect",
            "_onMouseDown",           "_onMouseUp",    "_onMouseClick", "_onMouseWheel",
            "_onMouseEnter",          "_onMouseLeave", "_onMouseMove",  "_onKeyDown",
            "_onKeyUp",               "_onTextInput",  "_onShortcut",   "_onBeforeDraw",
            "_onAfterDraw",           "_onScrollPositionChanged",       "_onChildRemoved",
            "_onChildAdded"
        ]
        result.sort()
        return list(set(result))
    FUNCTIONEND
    
    ###
    ##
    ##
    def __del__(self):
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::__del__:{}".format(self))
        #endif
        if self._texture != None:
            PYSDL2_DESTROYTEXTURE( self._texture )
    FUNCTIONEND
                 
    def debug(self,prefix=""):
        
        super().debug(prefix)
        self.layoutManager.debug("{}  ".format(prefix))
        
        print("{}  CHILDREN:".format(prefix))
        for c in self._children:
            c.debug( "{}      ".format(prefix) )
            
    ###
    ##
    ##
    def __hndOnScrollPositionChanged(self,ev:Event)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::__hndOnScrollPositionChanged():{}".format(self))
        #endif
        sp = ev.eventSource.draggerPosition
        if ev.eventSource.isHorizontal: #pylint: disable=no-else-return
            self.scrollX = self.scrollWidth*sp[0]
            return 
        elif ev.eventSource.isVertical:
            self.scrollY = self.scrollHeight*sp[1]
            return
  
        self.scrollX = self.scrollWidth*sp[0]
        self.scrollY = self.scrollHeight*sp[1]
    FUNCTIONEND
    
    ###
    ##
    def connectScrollNavigator(self,navigator)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::connectScrollNavigation():{}".format(self))
        #endif
        if navigator.onScrollPositionChanged.has(self.__hndOnScrollPositionChanged):
            return
        
        navigator.onScrollPositionChanged.add(self.__hndOnScrollPositionChanged)
        navigator.connectPane(self)
    FUNCTIONEND
        
    ###
    ##
    def disconnectScrollNavigator(self,navigator)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::disconnectScrollNavigation():{}".format(self))
        #endif
        if not navigator.onScrollPositionChanged.has(self.__hndOnScrollPositionChanged):
            return
        
        navigator.onScrollPositionChanged.remove(self.__hndOnScrollPositionChanged)
        navigator.disconnectPane(self)
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
    def scrollSize(self)->tuple[int,int]:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::scrollSize_get():{}".format(self))
        #endif
        return (self.scrollWidth, self.scrollHeight)
    FUNCTIONEND
    
    ### Returns the maximum scroll position in x direction.
    ##
    ##  @return            
    ##
    @property
    def scrollWidth(self)->int:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::scrollWidth_get():{}".format(self))
        #endif
        return self._scrollWidth-self.width
    FUNCTIONEND
    
    ### Returns the maximum scroll position in y direction.
    ##
    ##  @return            
    ##
    @property
    def scrollHeight(self)->int:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::scrollHeight_get():{}".format(self))
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
        
        value = min(value,self.scrollWidth)
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
        
        value = min(value,self.scrollHeight)
        value = max(value,0)
        
        self._scrollY = value
        self._invalidate()
        self._onScrollPositionChanged(Event(self))
    FUNCTIONEND
    
    ###
    ##
    ##
    @property
    def hasChildren(self):
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::hasChildren():{}".format(self))
        #endif
        return len(self._children) > 0
    FUNCTIONEND
    
    ### Returns all child elements.
    ##
    ##  @return               A list with Widgets.
    ##
    ## TODO: Should this be property children?
    def getChildren(self)->list[Widget]:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::getChildren():{}".format(self))
        #endif
        return self._children
    FUNCTIONEND
    
    ### @see Widget.hasChild
    ##
    ##
    def hasChild(self,child:Widget)->bool:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::hasChild():{}".format(self))
        #endif
        for c in self._children:
            if c.hasChild(child):
                return True
            
        return self == child
    FUNCTIONEND
    
    ###  Removes the given child element.
    ##
    ##  @param child         A Widget instance.
    ##   
    def removeChild(self,child:Widget)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::removeChild():{}".format(self))
        #endif
        self._layoutManager.removeChild(child)
        if child in self._children:
            self._children.remove(child)
            if isinstance(child,ContainerWidget):
                child.onChildAdded.remove(self.__hndChildAdded)
                child.onChildRemoved.remove(self.__hndChildRemoved)
            
            self._onChildRemoved(Event(child))
            ## TODO: Is it correct to trigger an event from outside the widget?
            child._onGotRemoved()
    FUNCTIONEND
    
    ### Adds a child element to the container.
    ##
    ##  @param child         A Widget instance.
    ##  @param x             Column for layout manager to add the child to. 
    ##  @param y             Row for layout manager to add the child to.
    ##       
    def addChild(self,child:Widget,x:int=0,y:int=0)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::addChild():{}".format(self))
        #endif
        child.parent = self
        ##self._children.insert(0,child)
        self._children.append(child)
        self._layoutManager.addChild(child,x,y)
        self._invalidate()
        if isinstance(child,ContainerWidget):
            child.onChildAdded.add(self.__hndChildAdded)
            child.onChildRemoved.add(self.__hndChildRemoved)
        self._onChildAdded(Event(child))
        ## TODO: Is it correct to trigger an event from outside the widget?
        child._onGotAdded()
    FUNCTIONEND
    
    ###
    ##
    ##  TODO: What is this event handling for?
    def __hndChildAdded(self,ev:EventManager)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::__hndChildAdded():{}".format(self))
        #endif
        self._onChildAdded(ev)
        ##print("childAdded")
    FUNCTIONEND
    
    ###
    ##
    ##  TODO: What is this event handling for?
    def __hndChildRemoved(self,ev:EventManager)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::__hndChildRemoved():{}".format(self))
        #endif
        self._onChildRemoved(ev)
        ##print("childAdded")
    FUNCTIONEND
    
    ### Returns the child element at the given position, itself or None.
    ##
    ##  @param pos             A tuple representing a position in the
    ##                         element´s coordinate system.
    ##  @return                None or a Widget
    ##
    def getChildAt(self, pos:tuple[int,int])->Widget:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::getChildAt():{}".format(self))
        #endif
                
        for c in reversed(self._children):
            cPos = self.toGlobal(c.position)
            if cPos[0] <= pos[0]:
                if cPos[0]+c.width >= pos[0]: 
                    if cPos[1] <= pos[1]:
                        if cPos[1]+c.height >= pos[1]:
                            return c.getChildAt(pos)
                    
        return self
    FUNCTIONEND
    
    ### @see Widget.isInvalide
    ##
    ##
    def isInvalide(self)->bool:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::isInvalide():{}".format(self))
        #endif
        
        for c in self._children:
            if c.isInvalide():
                return True
    
        return super().isInvalide()
    FUNCTIONEND
    
    ### Returns the layout manager.
    ##
    ##  @return            A LayoutManager.
    ##  todo: hinting
    @property
    def layoutManager(self):
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::layoutManager_get():{}".format(self))
        #endif
        return self._layoutManager
    FUNCTIONEND
    
    ###
    ##
    ##  @param value       A ayoutManager.
    ##  @return            None
    ##  todo: hinting
    @layoutManager.setter
    def layoutManager(self, value)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::layoutManager_set():{}".format(self))
        #endif
        self._layoutManager = value
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
        self._scrollWidth = sw
        self._scrollHeight = sh
        
        ## Next we let all children recalculate
        for c in self._children:
            c._calculateLayout()

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
    
    ###
    ##
    ##
    def _main(self):
        super()._main()
        for c in self._children:
            c._main()
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
    
    ### @see Widget._invalidate
    ##
    ##   
    def _invalidate(self)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::_invalidate():{}".format(self))
        #endif
        PYSDL2_DESTROYTEXTURE(self._texture)
        self._texture = None
        
        ## Here we can´t call super()
        ## because super sends the position
        ## here we need (0,0)
        ##box = (0,0,self._scrollWidth,self._scrollHeight)
        ##self._recordDirtyRect(box)
        
        ## set flag to recalculate the layout.
        ## set flag to redraw widget
        self._isInvalide = True# pylint:disable=attribute-defined-outside-init
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

    ### @see Widget._onMouseDown
    ##
    ##
    def _onMouseDown(self,ev:MouseEvent)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::_onMouseDown():{}".format(self))
        #endif
        ## phase down
        super()._onMouseDown(ev)
        if ev.propagationStopped:
            return
        
        childFound = False
        for c in self._children:
            if c.hasChild(ev.eventSource):
                c._onMouseDown(ev)
                childFound = True
                if c == ev.eventSource:
                    ## we set event phase to up!
                    ## This is the case if c is not a ContainerWidget.
                    ev._nextPhase()
                break
        
        ## if no child has got the event.
        ## the event has reached the deepest level.
        if not childFound:
            ## we set event phase to up!
            ev._nextPhase()
        else:
            ## pahse up
            if ev.propagationStopped:
                return
            super()._onMouseDown(ev)
    FUNCTIONEND
    
    ### @see Widget._onMouseUp
    ##
    ##
    def _onMouseUp(self,ev:MouseEvent)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::_onMouseUp():{}".format(self))
        #endif
        ## phase down
        super()._onMouseUp(ev)
        if ev.propagationStopped:
            return
        
        childFound = False
        for c in self._children:   
            if c.hasChild(ev.eventSource):
                c._onMouseUp(ev)
                childFound = True
                if c == ev.eventSource:
                    ## we set event phase to up!
                    ## This is the case if c is not a ContainerWidget.
                    ev._nextPhase()
                break
 
        ## if no child has got the event.
        ## the event has reached the deepest level.
        if not childFound:
            ## we set event phase to up!
            ev._nextPhase()
        else:
            ## pahse up
            if ev.propagationStopped:
                return
            super()._onMouseUp(ev)
    FUNCTIONEND
    
    ### @see Widget._onMouseClick
    ##
    ##
    def _onMouseClick(self,ev:MouseEvent)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::_onMouseClick():{}".format(self))
        #endif
        ## phase down
        super()._onMouseClick(ev)
        if ev.propagationStopped:
            return
        
        childFound = False
        for c in self._children:
            if c.hasChild(ev.eventSource):
                c._onMouseClick(ev)
                childFound = True
                if c == ev.eventSource:
                    ## we set event phase to up!
                    ## This is the case if c is not a ContainerWidget.
                    ev._nextPhase()
                break
                    
        ## if no child has got the event.
        ## the event has reached the deepest level.
        if not childFound:
            ## we set event phase to up!
            ev._nextPhase()
        else:
            ## pahse up
            if ev.propagationStopped:
                return
            super()._onMouseClick(ev)
    FUNCTIONEND
    
    ### @see Widget._onMouseWheel
    ##
    ##    
    def _onMouseWheel(self,ev:MouseEvent)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::_onMouseSheel():{}".format(self))
        #endif
        ## phase down
        super()._onMouseWheel(ev)
        if ev.propagationStopped:
            return
        
        childFound = False
        for c in self._children:
            if c.hasChild(ev.eventSource):
                c._onMouseWheel(ev)
                childFound = True
                if c == ev.eventSource:
                    ## we set event phase to up!
                    ## This is the case if c is not a ContainerWidget.
                    ev._nextPhase()
                break
        
        ## if no child has got the event.
        ## the event has reached the deepest level.
        if not childFound:
            ## we set event phase to up!
            ev._nextPhase()
        else:
            ## pahse up
            if ev.propagationStopped:
                return
            super()._onMouseWheel(ev)
    FUNCTIONEND
    
    ### @see Widget._onMouseEnter
    ##
    ##    
    def _onMouseEnter(self,ev:MouseEvent)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::_onMouseEnter():{}".format(self))
        #endif
        ## phase down
        super()._onMouseEnter(ev)
        if ev.propagationStopped:
            return
        
        childFound = False
        for c in self._children:
            if c.hasChild(ev.eventSource):
                c._onMouseEnter(ev)
                childFound = True
                if c == ev.eventSource:
                    ## we set event phase to up!
                    ## This is the case if c is not a ContainerWidget.
                    ev._nextPhase()
                break
        
        ## if no child has got the event.
        ## the event has reached the deepest level.
        if not childFound:
            ## we set event phase to up!
            ev._nextPhase()
        else:
            ## pahse up
            if ev.propagationStopped:
                return
            super()._onMouseEnter(ev)
    FUNCTIONEND
    
    ### @see Widget._onMouseLeave
    ##
    ##    
    def _onMouseLeave(self,ev:MouseEvent)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::_onMouseLeave():{}".format(self))
        #endif
        ## phase down
        super()._onMouseLeave(ev)
        if ev.propagationStopped:
            return
        
        childFound = False
        for c in self._children:
            if c.hasChild(ev.eventSource):
                c._onMouseLeave(ev)
                childFound = True
                if c == ev.eventSource:
                    ## we set event phase to up!
                    ## This is the case if c is not a ContainerWidget.
                    ev._nextPhase()
                break
        
        ## if no child has got the event.
        ## the event has reached the deepest level.
        if not childFound:
            ## we set event phase to up!
            ev._nextPhase()
        else:
            ## pahse up
            if ev.propagationStopped:
                return
            super()._onMouseLeave(ev)
    FUNCTIONEND
    
    ### @see Widget._onMouseMove
    ##
    ##    
    def _onMouseMove(self,ev:MouseEvent)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::_onMouseMove():{}".format(self))
        #endif
        ## phase down
        super()._onMouseMove(ev)
        if ev.propagationStopped:
            return
        
        childFound = False
        for c in self._children:
            if c.hasChild(ev.eventSource):
                c._onMouseMove(ev)
                childFound = True
                if c == ev.eventSource:
                    ## we set event phase to up!
                    ## This is the case if c is not a ContainerWidget.
                    ev._nextPhase()
                break
        
        ## if no child has got the event.
        ## the event has reached the deepest level.
        if not childFound:
            ## we set event phase to up!
            ev._nextPhase()
        else:
            ## pahse up
            if ev.propagationStopped:
                return
            super()._onMouseMove(ev)
    FUNCTIONEND
    
    ### @see Widget._onKeyDown
    ##
    ##    
    def _onKeyDown(self,ev:KeyEvent)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::_onKeyDown():{}".format(self))
        #endif
        ##print("{} ContainerWidget::sdlOnKeyDown".format(self))
        ##phase down
        super()._onKeyDown(ev)
        if ev.propagationStopped:
            return
        
        childFound = False
        for c in self._children:
            if c.hasChild(ev.eventSource):
                c._onKeyDown(ev)
                childFound = True
                if c == ev.eventSource:
                    ## we set event phase to up!
                    ## This is the case if c is not a ContainerWidget.
                    ev._nextPhase()
                break
            
        ## if no child has got the event.
        ## the event has reached the deepest level.
        if not childFound:
            ## we set event phase to up!
            ev._nextPhase()
        else:
            ## pahse up
            if ev.propagationStopped:
                return
            super()._onKeyDown(ev)
    FUNCTIONEND
    
    ### @see Widget._onKeyUp
    ##
    ##    
    def _onKeyUp(self,ev:KeyEvent)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::_onKeyUp():{}".format(self))
        #endif
        ##phase down
        super()._onKeyUp(ev)
        if ev.propagationStopped:
            return
        
        childFound = False
        for c in self._children:
            if c.hasChild(ev.eventSource):
                c._onKeyUp(ev)
                childFound = True
                if c == ev.eventSource:
                    ## we set event phase to up!
                    ## This is the case if c is not a ContainerWidget.
                    ev._nextPhase()
                break
        
        ## if no child has got the event.
        ## the event has reached the deepest level.
        if not childFound:
            ## we set event phase to up!
            ev._nextPhase()
        else:
            ## pahse up
            if ev.propagationStopped:
                return
            super()._onKeyUp(ev)
    FUNCTIONEND
    
    ### @see Widget._onTextInput
    ##
    ##   
    def _onTextInput(self,ev:KeyEvent)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::_onTextInput():{}".format(self))
        #endif
        ##phase down
        super()._onTextInput(ev)
        if ev.propagationStopped:
            return
        
        childFound = False
        for c in self._children:
            if c.hasChild(ev.eventSource):
                c._onTextInput(ev)
                childFound = True
                if c == ev.eventSource:
                    ## we set event phase to up!
                    ## This is the case if c is not a ContainerWidget.
                    ev._nextPhase()
                break
                
        ## if no child has got the event.
        ## the event has reached the deepest level.
        if not childFound:
            ## we set event phase to up!
            ev._nextPhase()
        else:
            ## pahse up
            if ev.propagationStopped:
                return
            super()._onTextInput(ev)
    FUNCTIONEND

    ### @see Widget._onShortCut
    ##
    ##  TODO: This function name is confusing!
    def _onShortcut(self,ev:Event)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::_onShortcut():{}".format(self))
        #endif
        ##print("ContainerWidget::_onShortCut ({})".format(self.name))
        
        ##phase down
        super()._onShortcut(ev)
        if ev.propagationStopped:
            return
        
        childFound = False
        for c in self._children:
            if c.hasChild(ev.eventSource):
                c._onShortcut(ev)
                childFound = True
                if c == ev.eventSource:
                    ## we set event phase to up!
                    ## This is the case if c is not a ContainerWidget.
                    ev._nextPhase()
                break
            
        ## if no child has got the event.
        ## the event has reached the deepest level.
        if not childFound:
            ## we set event phase to up!
            ev._nextPhase()
        else:
            ## pahse up
            if ev.propagationStopped:
                return
            super()._onShortcut(ev)
    FUNCTIONEND
    
    ### @see Widget._onBeforeDraw
    ##
    ##
    def _onBeforeRender(self)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::_onBeforeRender():{}".format(self))
        #endif
        for c in self._children:
            c._onBeforeRender()
        super()._onBeforeRender()
    FUNCTIONEND
    
    ### @see Widget._onAfterRender
    ##
    ##
    def _onAfterRender(self)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("ContainerWidget::_onAfterRender():{}".format(self))
        #endif
        for c in self._children:
            c._onAfterRender()
        super()._onAfterRender()
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
    def _onChildRemoved(self,ev):
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::_onChildRemoved():{}".format(self))
        #endif
        self.onChildRemoved.provoke(ev)
    FUNCTIONEND
    
    ##
    #
    #
    def _onChildAdded(self,ev):
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::_onChildAdded():{}".format(self))
        #endif
        self.onChildAdded.provoke(ev)            
    FUNCTIONEND
            
            
            
            
            