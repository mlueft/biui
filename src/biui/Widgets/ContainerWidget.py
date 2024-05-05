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
        super().__init__()
        ##
        self._children:List[Widget] = []
        
        ##
        self._layoutManager:LayoutManager = LayoutManager()
        
        ## Is provoked when a child is added
        self.onChildAdded:EventManager = EventManager()
        
        ## Is provoked when a child is removed
        self.onChildRemoved:EventManager = EventManager()

        ## Is provoked when the scroll position is changed.
        self.onScrollPositionChanged:EventManager = EventManager()
                
        ##
        ## todo: hinting
        self._texture = None
        ## A reference to the theme function which is used to draw the widget forground.
        theme = biui.getTheme()
        self._themeForegroundfunction:Callable = theme.drawEmpty
        self.onResized.add(self.__hndOnResized)
        
        
        
        self._scrollWidth:int = self.width
        self._scrollHeight:int = self.height
        self._scrollX:int = 0
        self._scrollY:int = 0
        
        
           
    ###
    ##
    ##
    def __hndOnResized(self,ev:Event)->None:
        ##self.__dragger.x = (self.width-self.__dragger.width)*self.__scrollPosition[0]
        ##self.__dragger.y = (self.height-self.__dragger.height)*self.__scrollPosition[1]
        pass
    
    
    ###
    ##
    ## todo: hinting
    def connectScrollNavigator(self,navigator)->None:
        if navigator.onScrollPositionChanged.has(self.__hndOnScrollPositionChanged):
            return
        
        navigator.onScrollPositionChanged.add(self.__hndOnScrollPositionChanged)
        navigator.connectPane(self)

    ###
    ##
    ##  todo: hinting
    def disconnectScrollNavigator(self,navigator)->None:
        if not navigator.onScrollPositionChanged.has(self.__hndOnScrollPositionChanged):
            return
        
        navigator.onScrollPositionChanged.remove(self.__hndOnScrollPositionChanged)
        navigator.disconnectPane(self)
            
    ###
    ##
    ##
    def __hndOnScrollPositionChanged(self,ev:Event)->None:
        sp = ev.eventSource.draggerPosition
        if ev.eventSource.isHorizontal: #pylint: disable=no-else-return
            self.scrollX = self.scrollWidth*sp[0]
            return 
        elif ev.eventSource.isVertical:
            self.scrollY = self.scrollHeight*sp[1]
            return
  
        self.scrollX = self.scrollWidth*sp[0]
        self.scrollY = self.scrollHeight*sp[1]
        return
        
    ### Returns the current scroll position.
    ##
    ##  @return            A tuple representing the position.
    ##
    @property
    def scrollPosition(self)->tuple[int,int]:
        return (self._scrollX, self._scrollY)
    
    ### Returns the x/y position of the GUI element.
    ##
    ##  @return            A tuple representing the size.
    ##
    @property
    def scrollSize(self)->tuple[int,int]:
        return (self.scrollWidth, self.scrollHeight)
            
    ### Returns the maximum scroll position in x direction.
    ##
    ##  @return            
    ##
    @property
    def scrollWidth(self)->int:
        return self._scrollWidth-self.width
    
    ### Returns the maximum scroll position in y direction.
    ##
    ##  @return            
    ##
    @property
    def scrollHeight(self)->int:
        return self._scrollHeight-self.height
    
    ### Returns the current scroll position in x direction.
    ##
    ##  @return            
    ##
    @property
    def scrollX(self)->int:
        return self._scrollX
    
    ### Sets the current scroll position in x direction. 
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##
    @scrollX.setter
    def scrollX(self, value:int)->None:
        value = int(value)
        if value == self._scrollX:
            return
        
        value = min(value,self.scrollWidth)
        value = max(value,0)
        
        self._scrollX = value
        self._invalidate()
        self.onScrollPositionChanged.provoke(Event(self))
        
    ### Returns the current scroll position in y direction.
    ##
    ##  @return            
    ##
    @property
    def scrollY(self)->int:
        return self._scrollY
    
    ### Sets the current scroll position in y direction. 
    ##
    ##  @param value       A integer value.
    ##  @return            None
    ##
    @scrollY.setter
    def scrollY(self, value:int)->None:
        value = int(value)
        if value == self._scrollY:
            return
        
        value = min(value,self.scrollHeight)
        value = max(value,0)
        
        self._scrollY = value
        self._invalidate()
        self.onScrollPositionChanged.provoke(Event(self))
                
    ###
    ##
    ##
    @property
    def hasChildren(self):
        return len(self._children) > 0
    
    ### Returns all child elements.
    ##
    ##  @return               A list with Widgets.
    ##
    def getChildren(self)->list[Widget]:
        return self._children
     
    ### @see Widget.hasChild
    ##
    ##
    def hasChild(self,child:Widget)->bool:
        for c in self._children:
            if c.hasChild(child):
                return True
            
        return self == child
    
    ###  Removes the given child element.
    ##
    ##  @param child         A Widget instance.
    ##   
    def removeChild(self,child:Widget)->None:
        self._layoutManager.removeChild(child)
        if child in self._children:
            self._children.remove(child)
            if isinstance(child,ContainerWidget):
                child.onChildAdded.remove(self.__hndChildAdded)
                child.onChildRemoved.remove(self.__hndChildRemoved)
            
            self.onChildRemoved.provoke(Event(child))
            child._onGotRemoved()
     
    ### Adds a child element to the container.
    ##
    ##  @param child         A Widget instance.
    ##  @param x             Column for layout manager to add the child to. 
    ##  @param y             Row for layout manager to add the child to.
    ##       
    def addChild(self,child:Widget,x:int=0,y:int=0)->None:
        child.parent = self
        ##self._children.insert(0,child)
        self._children.append(child)
        self._layoutManager.addChild(child,x,y)
        self._invalidate()
        if isinstance(child,ContainerWidget):
            child.onChildAdded.add(self.__hndChildAdded)
            child.onChildRemoved.add(self.__hndChildRemoved)
        self.onChildAdded.provoke(Event(child))
        child._onGotAdded()
 
    ###
    ##
    ##
    def __hndChildAdded(self,ev:EventManager)->None:
        self.onChildAdded.provoke(ev)
        ##print("childAdded")
            
    ###
    ##
    ##
    def __hndChildRemoved(self,ev:EventManager)->None:
        self.onChildRemoved.provoke(ev)
        ##print("childAdded")
        
    ### Returns the child element at the given position, itself or None.
    ##
    ##  @param pos             A tuple representing a position in the
    ##                         element´s coordinate system.
    ##  @return                None or a Widget
    ##

    def getChildAt(self, pos:tuple[int,int])->Widget:
                
        for c in reversed(self._children):
            cPos = self.toGlobal(c.position)
            if cPos[0] <= pos[0]:
                if cPos[0]+c.width >= pos[0]: 
                    if cPos[1] <= pos[1]:
                        if cPos[1]+c.height >= pos[1]:
                            return c.getChildAt(pos)
                    
        return self
    
    ### @see Widget.isInvalide
    ##
    ##
    def isInvalide(self)->bool:
        
        for c in self._children:
            if c.isInvalide():
                return True
    
        return super().isInvalide()
    
    ### Returns the layout manager.
    ##
    ##  @return            A LayoutManager.
    ##  todo: hinting
    @property
    def layoutManager(self):
        return self._layoutManager
        
    ###
    ##
    ##  @param value       A ayoutManager.
    ##  @return            None
    ##  todo: hinting
    @layoutManager.setter
    def layoutManager(self, value)->None:
        self._layoutManager = value
        
    ### @see Widget._calculateLayout
    ##
    ##
    def _calculateLayout(self)->None:
        super()._calculateLayout()
        mySize = self.size
        
        self._layoutManager._calculateLayout(mySize)
        
        for c in self._children:
            c._calculateLayout()
        
    ### @see Widget._onBeforeDraw
    ##
    ##
    def _onBeforeDraw(self)->None:
        for c in self._children:
            c._onBeforeDraw()
        super()._onBeforeDraw()
    
    ### @see Widget._onAfterDraw
    ##
    ##
    def _onAfterDraw(self)->None:
        for c in self._children:
            c._onAfterDraw()
        super()._onAfterDraw()
    
    ### @see Widget._redraw
    ##
    ##  todo: hinting
    
    ###
    ##
    ##
    @property
    def renderRect(self):
        return (self._scrollX,self._scrollY,self._width,self._height)
        
    def _render(self, forceRedraw:bool=False ):
        if not self.isInvalide():
            if not forceRedraw:
                return
        ##print("ContainerWidget::_render(): {}".format(self))
        
        ##print( "redraw:{} {}x{} {}".format(self.name,self.x,self.y,forceRedraw))
 
        wnd = self.window
        renderer = self.window.renderer
        sw = self.width
        sh = self.height
        ##print(sw,sh)
        for child in self._children:
            sw = max(sw,child.right)
            sh = max(sh,child.bottom)
            ##print("         ",sw,sh)
        ##print("------------")
        self._scrollWidth = sw
        self._scrollHeight = sh
        
        PYSDL2_CREATETEXTURE(renderer,sw,sh,texture)
              
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
        
    ### @see Widget._onMouseDown
    ##
    ##
    def _onMouseDown(self,ev:MouseEvent)->None:
        
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
        
    ### @see Widget._onMouseUp
    ##
    ##
    def _onMouseUp(self,ev:MouseEvent)->None:
        
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
    
    ### @see Widget._onMouseClick
    ##
    ##
    def _onMouseClick(self,ev:MouseEvent)->None:
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
                
    ### @see Widget._onMouseWheel
    ##
    ##    
    def _onMouseWheel(self,ev:MouseEvent)->None:
        
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
            
    ### @see Widget._onMouseEnter
    ##
    ##    
    def _onMouseEnter(self,ev:MouseEvent)->None:
        
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
            
    ### @see Widget._onMouseLeave
    ##
    ##    
    def _onMouseLeave(self,ev:MouseEvent)->None:
        
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
            
    ### @see Widget._onMouseMove
    ##
    ##    
    def _onMouseMove(self,ev:MouseEvent)->None:
        
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
                
    ### @see Widget._onKeyDown
    ##
    ##    
    def _onKeyDown(self,ev:KeyEvent)->None:
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
            
    ### @see Widget._onKeyUp
    ##
    ##    
    def _onKeyUp(self,ev:KeyEvent)->None:
        
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
    
    ### @see Widget._onTextInput
    ##
    ##   
    def _onTextInput(self,ev:KeyEvent)->None:
        
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
                 
    ### @see Widget._invalidate
    ##
    ##   
    def _invalidate(self)->None:
        PYSDL2_DESTROYTEXTURE(self._texture)
        self._texture = None
        
        ## Here we can´t call super()
        ## because super sends the position
        ## here we need (0,0)
        box = (0,0,self._scrollWidth,self._scrollHeight)
        self._recordDirtyRect(box)
        ## set flag to recalculate the layout.
        ## set flag to redraw widget
        self._isInvalide = True# pylint:disable=attribute-defined-outside-init
        
    ### @see Widget.toLocal
    ##
    ##
    def toLocal(self, coordinates:tuple[int,int])->tuple[int,int]:
        result = ( coordinates[0]-self._x+self._scrollX,coordinates[1]-self._y+self._scrollY)
        if self._parent is not None:
            result = self._parent.toLocal(result)
        
        return result
    
    ### @see Widget.toGlobal
    ##
    ##
    def toGlobal(self,coordinates:tuple[int,int])->tuple[int,int]:
        result = ( self._x-self._scrollX+coordinates[0],self._y-self._scrollY+coordinates[1])
        if self._parent is not None:
            result = self._parent.toGlobal(result)
        
        return result
            
    ### @see Widget._recordDirtyRect
    ##
    ##    
    def _recordDirtyRect(self, box:tuple[int,int,int,int])->None:
        
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
        
        ## we translate the box to the parent´S coordinate system
        ## and we cut of if it´s reaching over the edgees.
        box = (
            self.x+bx,
            self.y+by,
            br-bx,
            bb-by
        )
        self.parent._recordDirtyRect(box)

    ### @see Widget._onShortCut
    ##
    ##
    def _onShortcut(self,ev:Event)->None:
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
            