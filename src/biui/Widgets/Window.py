#include "biui.inc"
#include "pysdl2.inc"

from typing import Callable,NoReturn,Any,Union
import ctypes
from time import time
import sdl2
from sdl2.mouse import  SDL_BUTTON_MIDDLE, SDL_BUTTON_RIGHT, SDL_BUTTON_LEFT, SDL_BUTTON_X1, SDL_BUTTON_X2

import biui
from biui.Widgets.Widget import Widget
from biui.Widgets.ContainerWidget import ContainerWidget

from biui.Events import KeyEvent
from biui.Events import MouseEvent
from biui.Events import Event
from biui.Events import EventManager

from biui.DirtyRectangleManager import DirtyRectangleManager
from biui.Color import Color

###
##
##
class Window(ContainerWidget):
    
    ###
    ##
    ##
    def __init__(self,width,height):
        
        
        PYSDL2_CREATEWINDOW((width,height),self._window)
        super().__init__()

        PYSDL2_GET_WINDOW_ID(self._window,self._id:str)
        
        self._title:str = ""
        ##PYSDL2_CREATERENDERER(self._window,-1,sdl2.SDL_RENDERER_ACCELERATED | sdl2.SDL_RENDERER_ACCELERATED,self._renderer)
        PYSDL2_CREATERENDERER(self._window,-1,0,self._renderer)
        
        ##
        self.onWindowClose:EventManager = EventManager()
        ##
        self.onWindowShown:EventManager = EventManager()
        ##
        self.onWindowHidden:EventManager = EventManager()
        ##
        self.onWindowExposed:EventManager = EventManager()
        ##
        self.onWindowMoved:EventManager = EventManager()
        ##
        self.onWindowResized:EventManager = EventManager()
        ##
        self.onWindowSizeChanged:EventManager = EventManager()
        ##
        self.onWindowMinimized:EventManager = EventManager()
        ##
        self.onWindowMaximized:EventManager = EventManager()
        ##
        self.onWindowRestored:EventManager = EventManager()
        ##
        self.onWindowEnter:EventManager = EventManager()
        ##
        self.onWindowLeave:EventManager = EventManager()
        ##
        self.onWindowFocusGained:EventManager = EventManager()
        ##
        self.onWindowFocusLost:EventManager = EventManager()
        ##
        self.onWindowFocus:EventManager = EventManager()

        ##
        self.__mouseDownTime:Union(None,float) = None
        
        ##
        self.__mousePosition:list[int,int] = None
        
        ## todo: hinting
        self.__overlays:dict = {}

        #ifdef SHOW_UPDATE_BOX
        ## todo: hinting
        self.__guiTexture = None
        #endif
        
        ##
        self.__dr:biui.DirtyRectangleManager = DirtyRectangleManager()
        
        ### Stored a reference to the Widget the mouse is over.
        self.__hoverWidget:biui.Widget = None
        
        ##
        self.__tooltipCallback:Callable = ctypes.CFUNCTYPE(ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p)(self.__hndTooltipTimer)
        
        ##
        self.__tooltipTimerId:Union(None,int) = None

        
        self.width:int = width
        self.height:int = height
        ##
        self.onChildRemoved.add(self.__hndOnChildRemoved)
        ##
        self.onWindowFocusLost.add(self.__hndOnWndFocusLost)
        ##
        self.backColor:biui.Color = Color(50,50,50,255)
        ##
        self.__focusedWidget = None
         
        ##print(dir(self._window))
        ## '__bool__', '__class__', '__ctypes_from_outparam__',
        ## '__delattr__', '__delitem__', '__dict__', '__dir__',
        ## '__doc__', '__eq__', '__format__', '__ge__',
        ## '__getattribute__', '__getitem__', '__gt__',
        ## '__hash__', '__init__', '__init_subclass__', '__le__',
        ## '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
        ## '__reduce_ex__', '__repr__', '__setattr__', '__setitem__',
        ## '__setstate__', '__sizeof__', '__str__', '__subclasshook__',
        ## '__weakref__', '_b_base_', '_b_needsfree_', '_objects',
        ## '_type_', 'contents']
        ##print(dir(self._window.contents))
        ## '__bool__', '__class__', '__ctypes_from_outparam__',
        ## '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
        ## '__format__', '__ge__', '__getattribute__', '__gt__',
        ## '__hash__', '__init__', '__init_subclass__', '__le__',
        ## '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
        ## '__reduce_ex__', '__repr__', '__setattr__', '__setstate__',
        ## '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
        ## '_b_base_', '_b_needsfree_', '_objects', '_type_', 'from_param',
        ## 'value']
        
        self.onWindowClose.add(self.__hndOnWndClose)
        
        biui._addWindow(self)
        
        ## Added in Widget. But Window does not need it.
        self.onMouseDown.remove(self.hndMouseDown)
        
    
    ## SDL_GetWindowPosition
    ## SDL_SetWindowPosition
    
    ## SDL_GetWindowSize
    ## SDL_SetWindowSize

    ## SDL_GetWindowMaximumSize
    ## SDL_SetWindowMaximumSize

    ## SDL_GetWindowMinimumSize
    ## SDL_SetWindowMinimumSize
    
    ## SDL_ShowWindow
    ## SDL_HideWindow
    ## SDL_MaximizeWindow
    ## SDL_MinimizeWindow
    ## SDL_RaiseWindow
    ## SDL_RestoreWindow
    
    ### Sets the currently focused widget.
    ##
    ##
    def setFocus(self,widget):
        
        if self.__focusedWidget == widget:
            return
        
        ## defocus old widget
        if self.__focusedWidget:
            self.__focusedWidget.onFocusLost.provoke(Event(self.__focusedWidget));
        
        self.__focusedWidget = widget
        
        ## focus new widget
        self.__focusedWidget.onFocus.provoke(Event(self.__focusedWidget));
            
    ###
    ##
    ##
    def __hndOnWndFocusLost(self,ev:Event)->None:##pylint: disable=unused-argument
        ## SNIPPET: REMOVE TOOLTIP
        if self.__tooltipTimerId is None:
            return
        
        sdl2.SDL_RemoveTimer( self.__tooltipTimerId )
        self.__tooltipTimerId = None
        self.removeOverlay("tooltip")
            
    ###
    ##
    ## todo: hinting
    def __hndTooltipTimer(self,interval:int, param)->int:##pylint: disable=unused-argument
        child = self.getChildAt(self.__mousePosition)
        if child.tooltip is None:
            return 0
        ## TODO: generate Tooltip widget
        ##print("Show tooltip '{}' at {}!".format(child.tooltip,self.__mousePosition))
        ##self.showOverlay("tooltip")
        theme = biui.getTheme()
        tt = theme.getTooltip(child)
        tt.value = child.tooltip
        tt.x = self.__mousePosition[0]+10
        tt.y = self.__mousePosition[1]+10
        self.showOverlay(tt,"tooltip")
        return 0
    
        
    ###
    ##
    ##
    def showOverlay(self, child:Widget, overlayname:str)->None:
        self.removeOverlay(overlayname)
        self.addOverlay(child, overlayname)
    
    ###
    ##
    ##
    def removeOverlay(self,overlayname:str)->None:
        if overlayname in self.__overlays:
            for i in self.__overlays[overlayname]:
                self.removeChild(i)
            self.__overlays[overlayname] = []        
    ###
    ##
    ##
    def addOverlay(self, child:Widget, overlayname:str)->None:
        if not overlayname in self.__overlays:
            self.__overlays[overlayname] = []        
        self.__overlays[overlayname].append(child)
        self.addChild(child)
    
       
    ### @see biui.Widget.x
    ##
    ##    
    @property
    def x(self)->int:
        PYSDL2_GETWINDOWPOS(self._window,x,y)##pylint: disable=unused-variable
        return x
    
    ### @see biui.Widget.x
    ##
    ##
    @x.setter
    def x(self, value:int)->None:
        if value == self.x:
            return
        PYSDL2_SETWINDOWPOS(self._window,value,self.y)
    
    ### @see biui.Widget.y
    ##
    ##
    @property
    def y(self)->int:
        PYSDL2_GETWINDOWPOS(self._window,x,y)##pylint: disable=unused-variable
        return y

    ### @see biui.Widget.y
    ##
    ##
    @y.setter
    def y(self, value:int)->None:
        if value == self.y:
            return
        PYSDL2_SETWINDOWPOS(self._window,self.x,value)

    ### @see biui.Widget.width
    ##
    ##
    @property
    def width(self)->int:
        PYSDL2_GETWINDOWSIZE(self._window,w,h)##pylint: disable=unused-variable
        return w
    
    ### @see biui.Widget.width
    ##
    ##
    @width.setter
    def width(self, value:int)->None:
        if value == self.width:
            return
        if value > self.width:
            self._invalidate()
        PYSDL2_SETWINDOWSIZE(self._window,value,self.height)
    
    ### @see biui.Widget.height
    ##
    ##
    @property    
    def height(self)->int:
        PYSDL2_GETWINDOWSIZE(self._window,w,h)##pylint: disable=unused-variable
        return h
    
    ### @see biui.Widget.height
    ##
    ##
    @height.setter
    def height(self, value:int)->None:
        if value == self.height:
            return
        if value > self.height:
            self._invalidate()
        PYSDL2_SETWINDOWSIZE(self._window,self.width,value)


    ## Returns the title of the window.
    ##
    ##  @return            An string value.
    ##
    @property
    def title(self)->str:
        return self._title

    ### Sets the title of the window.
    ##
    ##  @param value       An string value.
    ##  @return            None    
    ##
    @title.setter
    def title(self, value:str)->None:
        PYSDL2_SETWINDOWTITLE(self._window,value)
        self._title = value
    
    ###
    ##
    ##
    def __hndOnWndClose(self,ev:Event)->None:##pylint: disable=unused-argument
        ## TODO: clean up all eventmanagers
        
        PYSDL2_DESTROYTEXTURE(self._window)
        biui._removeWindow(self)
    
    ### Handles the SDL mouse event for this window
    ##
    ##  todo: hinting
    def sdlOnMouseDown(self,event)->None:
        ## SNIPPET: REMOVE TOOLTIP
        if self.__tooltipTimerId is not None:
            sdl2.SDL_RemoveTimer( self.__tooltipTimerId )
            self.__tooltipTimerId = None
            self.removeOverlay("tooltip")
                    
        mevent = event.motion
        pos = (mevent.x,mevent.y)
        
        self.__mouseDownTime = time()
        
        bStates = [
            (mevent.state & SDL_BUTTON_LEFT) != 0,
            (mevent.state & SDL_BUTTON_MIDDLE) != 0,
            (mevent.state & SDL_BUTTON_RIGHT) != 0,
            (mevent.state & SDL_BUTTON_X1) != 0,
            (mevent.state & SDL_BUTTON_X2) != 0
        ]
        
        receiver = self.getChildAt(pos)
        ev = MouseEvent(receiver,bStates,pos,0,0)
        self._onMouseDown(ev)

    ### Handles the SDL mouse event for this window
    ##
    ##  todo: hinting
    def sdlOnMouseUp(self,event)->None:
        ## SNIPPET: REMOVE TOOLTIP
        if self.__tooltipTimerId is not None:
            sdl2.SDL_RemoveTimer( self.__tooltipTimerId )
            self.__tooltipTimerId = None
            self.removeOverlay("tooltip")
                    
        mevent = event.motion
        pos = (mevent.x,mevent.y)
        
        bStates = [
            (mevent.state & SDL_BUTTON_LEFT) != 0,
            (mevent.state & SDL_BUTTON_MIDDLE) != 0,
            (mevent.state & SDL_BUTTON_RIGHT) != 0,
            (mevent.state & SDL_BUTTON_X1) != 0,
            (mevent.state & SDL_BUTTON_X2) != 0
        ]
        
        receiver = self.getChildAt(pos)
        ev = MouseEvent(receiver,bStates,pos,0,0)
        if time()-self.__mouseDownTime < BIUI_CLICKDURATION:
            self._onMouseClick(ev)

        self._onMouseUp(ev)
            
    ### Handles the SDL mouse event for this window
    ##
    ##  todo: hinting
    def sdlOnMouseWheel(self,event)->None:
        ## SNIPPET: REMOVE TOOLTIP
        if self.__tooltipTimerId is not None:
            sdl2.SDL_RemoveTimer( self.__tooltipTimerId )
            self.__tooltipTimerId = None
            self.removeOverlay("tooltip")
                    
        mevent = event.motion
        ##print(event.wheel.direction)
        ##print(event.wheel.preciseX)
        ##print(event.wheel.preciseY)
        ##print(event.wheel.timestamp)
        ##print(event.wheel.type)
        ##print(event.wheel.which)
        ##print(event.wheel.windowID)
        ##print(event.wheel.x)
        ##print(event.wheel.y)
        ##print("--------------------")
        pos = (mevent.x,mevent.y)                

        bStates = [
            (mevent.state & SDL_BUTTON_LEFT) != 0,
            (mevent.state & SDL_BUTTON_MIDDLE) != 0,
            (mevent.state & SDL_BUTTON_RIGHT) != 0,
            (mevent.state & SDL_BUTTON_X1) != 0,
            (mevent.state & SDL_BUTTON_X2) != 0
        ]
        
        receiver = self.getChildAt(pos)
        ev = MouseEvent(receiver,bStates,pos,event.wheel.x,event.wheel.y)
        self._onMouseWheel(ev)
    
    ### Handles the SDL mouse event for this window
    ##
    ##  todo: hinting
    def sdlOnMouseMotion(self,event)->None:
    
        ## SNIPPET: REMOVE TOOLTIP
        if self.__tooltipTimerId is not None:
            sdl2.SDL_RemoveTimer( self.__tooltipTimerId )
            self.__tooltipTimerId = None
            self.removeOverlay("tooltip")
        
        self.__tooltipTimerId = sdl2.SDL_AddTimer(1000, self.__tooltipCallback, None )
    
    
        mevent = event.motion
        pos = [mevent.x,mevent.y]
        self.__mousePosition = pos
        bStates = [
            (mevent.state & SDL_BUTTON_LEFT) != 0,
            (mevent.state & SDL_BUTTON_MIDDLE) != 0,
            (mevent.state & SDL_BUTTON_RIGHT) != 0,
            (mevent.state & SDL_BUTTON_X1) != 0,
            (mevent.state & SDL_BUTTON_X2) != 0
        ]
        receiver = self.getChildAt(pos)
        
        ev = MouseEvent(receiver,bStates,pos,0,0)
        
        if receiver != self.__hoverWidget:
            if self.__hoverWidget is not None:
                evLeave = MouseEvent(self.__hoverWidget,bStates,pos,0,0)
                self._onMouseLeave(evLeave)
            self.__hoverWidget = receiver
            self.__hoverWidget._onMouseEnter(ev)
        else:
            self._onMouseMove(ev)

    ### 
    ##
    ##
    def sdlOnKeyDown(self,event)->None:
        ##print("sdlOnKeyDown")
        ev = KeyEvent(
            self.__focusedWidget,
            event.key.keysym.sym,
            event.key.keysym.scancode,
            event.key.keysym.mod,
            event.key.repeat,
            event.key.timestamp
        )
        self._onKeyDown(ev)
        
    ### 
    ##
    ##
    def sdlOnKeyUp(self,event)->None:
        ##print("sdlOnKeyUp")
        ev = KeyEvent(
            self.__focusedWidget,
            event.key.keysym.sym,
            event.key.keysym.scancode,
            event.key.keysym.mod,
            event.key.repeat,
            event.key.timestamp
        )
        self._onKeyUp(ev)
    
    ### 
    ##
    ##
    def sdlOnTextInput(self,event)->None:
        ##print( "sdlOnTextInput {}".format(event.text.text) )
        ##self._onTextInput(event)
        pass
    
    ### Handles the sdl window event for this window
    ##
    ##  todo: hinting
    def sdlOnWindowEvent(self,event)->None:##pylint: disable=too-many-branches,too-many-statements
        ev = Event(self)
        
        if event.window.event == sdl2.SDL_WINDOWEVENT_CLOSE:
            print("SDL_WINDOWEVENT_CLOSE")
            self.onWindowClose.provoke(ev)
        elif event.window.event == sdl2.SDL_WINDOWEVENT_SHOWN:
            print("SDL_WINDOWEVENT_SHOWN")
            self.onWindowShown.provoke(ev)
            self._invalidate()
        elif event.window.event == sdl2.SDL_WINDOWEVENT_HIDDEN:
            print("SDL_WINDOWEVENT_HIDDEN")
            self.onWindowHidden.provoke(ev)
        elif event.window.event == sdl2.SDL_WINDOWEVENT_EXPOSED:
            print("SDL_WINDOWEVENT_EXPOSED")
            self.onWindowExposed.provoke(ev)
            self._invalidate()
        elif event.window.event == sdl2.SDL_WINDOWEVENT_MOVED:
            ##print("SDL_WINDOWEVENT_MOVED")
            if self.x != event.window.data1 or self.y != event.window.data2:
                PYSDL2_SETWINDOWSIZE(
                    self._window,
                    event.window.data1,
                    event.window.data2
                )
                self.onWindowMoved.provoke(ev)
        elif event.window.event == sdl2.SDL_WINDOWEVENT_RESIZED:
            ##print("SDL_WINDOWEVENT_RESIZED")
            if self.width != event.window.data1 or self.height != event.window.data2:
                PYSDL2_SETWINDOWSIZE(
                    self._window,
                    event.window.data1,
                    event.window.data2
                )
                self.onWindowResized.provoke(ev)
                self._invalidate()
        elif event.window.event == sdl2.SDL_WINDOWEVENT_SIZE_CHANGED:
            ##print("SDL_WINDOWEVENT_SIZE_CHANGED(%s,%s)",event.window.data1,event.window.data2)
            if self.width != event.window.data1 or self.height != event.window.data2:
                PYSDL2_SETWINDOWSIZE(self._window,event.window.data1,event.window.data2)
                self.onWindowSizeChanged.provoke(ev)
                self._invalidate()
        elif event.window.event == sdl2.SDL_WINDOWEVENT_MINIMIZED:
            print("SDL_WINDOWEVENT_MINIMIZED")
            self.onWindowMinimized.provoke(ev)
        elif event.window.event == sdl2.SDL_WINDOWEVENT_MAXIMIZED:
            print("SDL_WINDOWEVENT_MAXIMIZED")
            self.onWindowMaximized.provoke(ev)
        elif event.window.event == sdl2.SDL_WINDOWEVENT_RESTORED:
            print("SDL_WINDOWEVENT_RESTORED")
            self.onWindowRestored.provoke(ev)
            self._invalidate()
        elif event.window.event == sdl2.SDL_WINDOWEVENT_ENTER:
            print("SDL_WINDOWEVENT_ENTER")
            self.onWindowEnter.provoke(ev)
        elif event.window.event == sdl2.SDL_WINDOWEVENT_LEAVE:
            print("SDL_WINDOWEVENT_LEAVE")
            self.onWindowLeave.provoke(ev)
        elif event.window.event == sdl2.SDL_WINDOWEVENT_FOCUS_GAINED:
            print("SDL_WINDOWEVENT_FOCUS_GAINED")
            self.onWindowFocusGained.provoke(ev)
        elif event.window.event == sdl2.SDL_WINDOWEVENT_FOCUS_LOST:
            print("SDL_WINDOWEVENT_FOCUS_LOST")
            self.onWindowFocusLost.provoke(ev)
        elif event.window.event == sdl2.SDL_WINDOWEVENT_TAKE_FOCUS:
            ##print("SDL_WINDOWEVENT_TAKE_FOCUS")
            ##self.onWindowFocus.provoke(ev)
            ##self._invalidate()
            pass
        else:
            print("*Unknown Windowevent.")

    ### Returns the current mouse position on the window.
    ##
    ##  @return         A tuple with x andy position of the
    ##                  mouse pointer.
    ##
    ##def getMousePosition(self):
    ##    return biui.Mouse.getPosition()
    
    ### Returns the windows internal id.
    ##
    ##
    @property
    def id(self)->str:
        return self._id 
                
    ###
    ##
    ##
    def _onQuit(self)->None:
        pass

    ### Returns the window´s renderer.
    ##
    ##  todo: hinting
    @property
    def renderer(self):
        return self._renderer

    ### @see biui.Widget._redraw
    ##
    ##
    def _redraw(self, forceRedraw:bool=False):
                
        #ifdef SHOW_UPDATE_BOX
        if self.__guiTexture is not None:
            r = (0,0,self.width,self.height)
            
            PYSDL2_RENDER_COPY(self.renderer,self.__guiTexture,r,r)
            
            PYSDL2_DESTROYTEXTURE(self.__guiTexture)
            
            self.__guiTexture = None
            PYSDL2_PRESENT(self.renderer)
            return 
        #endif
        
        if not self.isInvalide():
            if not forceRedraw:
                return
        
        ##print("window::redraw----------------------------------------",forceRedraw)
        
        for c in self._children:
            c._onBeforeDraw()
        
        self._calculateLayout()
        
        theme = biui.getTheme()
        
        if self._texture is None:##pylint: disable=access-member-before-definition
            ## pylint false positive about attribute-defined-outside-init
            PYSDL2_CREATETEXTURE(self.renderer,self.width,self.height, self._texture)
            self.__guiTexture = self._texture##pylint: diable=attribute-defined-outside-init
            forceRedraw = True
        
        #ifdef SHOW_UPDATE_BOX
        PYSDL2_CREATETEXTURE(self.renderer,self.width,self.height, self.__guiTexture)
        forceRedraw = True
        #endif
        
        ##PYSDL2_SETRENDERCONTEXT(self.renderer,self.__guiTexture)
        
        theme.drawWindowBeforeChildren(self,self.__guiTexture)
        
        for c in self._children:
            tx = c._redraw(forceRedraw)
            ## We copy it at the childs position in the childs size.
            sp = (0,0)
            if isinstance(c, ContainerWidget):
                sp = c.scrollPosition
            p = c.position
            tgt = (p[0],p[1],c.width,c.height)
            src = (sp[0],sp[1],c.width,c.height)
            PYSDL2_RENDER_COPY1(self.renderer,self.__guiTexture,tx,tgt,src)
            ## Finally we have to destroy the texture returned by the child
            PYSDL2_DESTROYTEXTURE( tx )
        
        theme.drawWindowAfterChildren(self,self.__guiTexture)
        
        dr = self.__dr.getRectangles()
        
        #ifdef SHOW_UPDATE_BOX
        ## Draw update boxes        
        PYSDL2_CREATETEXTURE(self.renderer,self.width,self.height,boxTexture)
        for r in dr:
            r = list(r)
            ## r must not reach over the widow´s texture
            r[0] = max(0,r[0])
            r[1] = max(0,r[1])
            r[2] = min(r[2],self.width-r[0])
            r[3] = min(r[3],self.height-r[1])                
            PYSDL2_DRAWRECT(self.renderer,boxTexture,(255,255,0,255),r)
            
        r = (0,0,self.width,self.height)
        PYSDL2_RENDER_COPY(self.renderer,self.__guiTexture,r,r)
        PYSDL2_RENDER_COPY(self.renderer,boxTexture,r,r)
        PYSDL2_DESTROYTEXTURE(boxTexture)
        #else
        ## just render dirty rectangles
        for r in dr:
            r = list(r)
            ## r must not reach over the widow´s texture
            r[0] = max(0,r[0])
            r[1] = max(0,r[1])
            r[2] = min(r[2],self.width-r[0])
            r[3] = min(r[3],self.height-r[1])
            
            PYSDL2_RENDER_COPY(self.renderer,self.__guiTexture,r,r)
        #endif
            
        PYSDL2_PRESENT(self.renderer)
        
        self._isInvalide = False##pylint: disable=attribute-defined-outside-init
        
        for c in self._children:
            c._onAfterDraw()
                    
    ### @see biui.Widget._recordDirtyRect
    ##
    ##    
    def _recordDirtyRect(self,box:tuple[int,int,int,int])->None:
        
        ## Check if the box is outside of the visible area
        if box[0] > self.width:
            return 
        if box[1] > self.height:
            return
        if box[0]+box[2] < 0:
            return 
        if box[1]+box[3] < 0:
            return
                
        self.__dr.add(box)
        
    ### Transforms a screen position to a window position.
    ##
    ##
    def toWindow(self,coordinates:tuple[int,int])->tuple[int,int]:
        return (coordinates[0]-self.x,coordinates[1]-self.y)
    
    ### Transformsa window position to a screen position.
    ##
    ##
    def toScreen(self,coordinates:tuple[int,int])->tuple[int,int]:
        return (coordinates[0]+self.x,coordinates[1]+self.y)
    
    def __hndOnChildRemoved(self,ev):##pylint: disable=unused-argument
        self._invalidate()
        
    
        
    ##def _onKeyDown(self,ev:KeyEvent)->None:
    ##    print("_onKeyDown")
    ##    super()._onKeyDown(ev)
    
    ##def _onKeyUp(self,ev:KeyEvent)->None:
    ##    print("_onKeyUp")
    ##    super()._onKeyUp(ev)
    
    ##def _onTextInput(self,ev:KeyEvent)->None:
    ##    print("_onTextInput")
    ##    super()._onTextInput(ev)
        
        
        