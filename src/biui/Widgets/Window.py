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
from biui.Events import ShortcutEvent

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
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::_init__():{}".format(self))
        #endif
        
        PYSDL2_CREATEWINDOW((width,height),self._window)
        super().__init__()

        self.maxWidth = 100000
        self.maxHeight = self.maxWidth
        
        PYSDL2_GET_WINDOW_ID(self._window,self._id:str)
        
        self._title:str = ""
        ##PYSDL2_CREATERENDERER(self._window,-1,sdl2.SDL_RENDERER_ACCELERATED | sdl2.SDL_RENDERER_ACCELERATED,self._renderer)
        PYSDL2_CREATERENDERER(self._window,-1,10,self._renderer)
        
        ###
        ##
        self.onWindowClose:EventManager = EventManager()
        
        ###
        ##
        self.onWindowShown:EventManager = EventManager()
        
        ###
        ##
        self.onWindowHidden:EventManager = EventManager()
        
        ###
        ##
        self.onWindowExposed:EventManager = EventManager()
        
        ###
        ##
        self.onWindowMoved:EventManager = EventManager()
        
        ###
        ##
        self.onWindowResized:EventManager = EventManager()
        
        ###
        ##
        self.onWindowSizeChanged:EventManager = EventManager()
        
        ###
        ##
        self.onWindowMinimized:EventManager = EventManager()
        
        ###
        ##
        self.onWindowMaximized:EventManager = EventManager()
        
        ###
        ##
        self.onWindowRestored:EventManager = EventManager()
        
        ###
        ##
        self.onWindowEnter:EventManager = EventManager()
        
        ###
        ##
        self.onWindowLeave:EventManager = EventManager()
        
        ###
        ##
        self.onWindowFocusGained:EventManager = EventManager()
        
        ###
        ##
        self.onWindowFocusLost:EventManager = EventManager()
        
        ###
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
        ##self.onMouseDown.remove(self.__hndMouseDown)
        
        biui.ShortcutControl.onShortcut.add(self.__hndOnShortcut)
    
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
    FUNCTIONEND
        
    ###
    ##
    ##
    def __dir__(self):
        result = super().__dir__()
        result = result + [
            "onWindowClose",       "onWindowShown",       "onWindowHidden", 
            "onWindowExposed",     "onWindowMoved",       "onWindowResized",
            "onWindowSizeChanged", "onWindowMinimized",   "onWindowMaximized",
            "onWindowRestored",    "onWindowEnter",       "onWindowFocus",
            "onWindowLeave",       "onWindowFocusGained", "onWindowFocusLost", 
            
            
             "window",    "x",     "y",  "width",
             "height",    "title", "id", "renderer",
              
            "sdlOnMouseDown",   "sdlOnMouseUp",   "sdlOnMouseWheel",
            "sdlOnMouseMotion", "sdlOnKeyDown",   "sdlOnKeyUp",
            "sdlOnTextInput",   "sdlOnWindowEvent", 
            
            "showOverlay", "removeOverlay", "addOverlay", "setFocus",
            "toWindow",    "toScreen",
             
            "_onQuit",            "_render",              "_recordDirtyRect",   "_onWindowClosed",
            "_onWindowShown",     "_onWindowHidden",      "_onWindowExposed",   "_onWindowMoved",
            "_onWindowResized",   "_onWindowSizeChanged", "_onWindowMinimized", "_onWindowMaximized", 
            "_onWindowRestored",  "_onWindowEnter",       "_onWindowLeave",     "_onWindowFocusGained",
            "_onWindowFocusLost", "_onWindowFocus"
        ]
        result.sort()
        return list(set(result))
    FUNCTIONEND
    
    ###
    ##
    ##
    def __del__(self):
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::__del__:{}".format(self))
        #endif
        super().__del__()
        if self.__guiTexture != None:
            PYSDL2_DESTROYTEXTURE( self.__guiTexture )
        biui._removeWindow(self)
    FUNCTIONEND
        
    ### Sets the currently focused widget.
    ##
    ##
    def setFocus(self,widget):
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::setFocus():{}".format(self))
        #endif
        if self.__focusedWidget == widget:
            return
        
        ## TODO: Is it correct to trigger an event from outside the focused widget?
        ## defocus old widget
        if self.__focusedWidget:
            self.__focusedWidget._onFocusLost(Event(self.__focusedWidget));
        
        self.__focusedWidget = widget
        
        ## focus new widget
        self.__focusedWidget._onFocus(Event(self.__focusedWidget));
    FUNCTIONEND
    
    ###
    ##
    ##
    def __hndOnWndFocusLost(self,ev:Event)->None:##pylint: disable=unused-argument
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::__hndOnWndFocusLost():{}".format(self))
        #endif
        ## SNIPPET: REMOVE TOOLTIP
        if self.__tooltipTimerId is None:
            return
        
        sdl2.SDL_RemoveTimer( self.__tooltipTimerId )
        self.__tooltipTimerId = None
        self.removeOverlay("tooltip")
    FUNCTIONEND
    
    ###
    ##
    ## todo: hinting
    def __hndTooltipTimer(self,interval:int, param)->int:##pylint: disable=unused-argument
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::__hndTooltipTimer():{}".format(self))
        #endif
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
    FUNCTIONEND
        
    ###
    ##
    ##
    def __hndOnWndClose(self,ev:Event)->None:##pylint: disable=unused-argument
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::__hndOnWndClose():{}".format(self))
        #endif
        ## TODO: clean up all eventmanagers
        
        biui._removeWindow(self)
    FUNCTIONEND
    
    ###
    ##
    ##
    def showOverlay(self, child:Widget, overlayname:str)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::showOverlay():{}".format(self))
        #endif
        self.removeOverlay(overlayname)
        self.addOverlay(child, overlayname)
    FUNCTIONEND
    
    ###
    ##
    ##
    def removeOverlay(self,overlayname:str)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::removeOverlay():{}".format(self))
        #endif
        if overlayname in self.__overlays:
            for i in self.__overlays[overlayname]:
                self.removeChild(i)
            self.__overlays[overlayname] = []
    FUNCTIONEND
    
    ###
    ##
    ##
    def addOverlay(self, child:Widget, overlayname:str)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::addOverlay():{}".format(self))
        #endif
        if not overlayname in self.__overlays:
            self.__overlays[overlayname] = []        
        self.__overlays[overlayname].append(child)
        self.addChild(child)
    FUNCTIONEND
    
    ### @see biui.Widget.x
    ##
    ##    
    @property
    def window(self):#pylint: disable=inconsistent-return-statements
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::window_get():{}".format(self))
        #endif
        return self
    FUNCTIONEND
    
    @property
    def x(self)->int:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::x_get():{}".format(self))
        #endif
        PYSDL2_GETWINDOWPOS(self._window,x,y)##pylint: disable=unused-variable
        return x
    FUNCTIONEND
    
    ### @see biui.Widget.x
    ##
    ##
    @x.setter
    def x(self, value:int)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::x_set():{}".format(self))
        #endif
        if value == self.x:
            return
        PYSDL2_SETWINDOWPOS(self._window,value,self.y)
    FUNCTIONEND
    
    ### @see biui.Widget.y
    ##
    ##
    @property
    def y(self)->int:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::y_get():{}".format(self))
        #endif
        PYSDL2_GETWINDOWPOS(self._window,x,y)##pylint: disable=unused-variable
        return y
    FUNCTIONEND
    
    ### @see biui.Widget.y
    ##
    ##
    @y.setter
    def y(self, value:int)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::y_set():{}".format(self))
        #endif
        if value == self.y:
            return
        PYSDL2_SETWINDOWPOS(self._window,self.x,value)
    FUNCTIONEND
        
    ### @see biui.Widget.width
    ##
    ##
    @property
    def width(self)->int:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::width_get():{}".format(self))
        #endif
        PYSDL2_GETWINDOWSIZE(self._window,w,h)##pylint: disable=unused-variable
        return w
    FUNCTIONEND
    
    ### @see biui.Widget.width
    ##
    ##
    @width.setter
    def width(self, value:int)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::width_set():{}".format(self))
        #endif
        ##if value == self.width:
        ##    return
        if value > self.width:
            self._invalidate()
        PYSDL2_SETWINDOWSIZE(self._window,value,self.height)
    FUNCTIONEND
    
    ### @see biui.Widget.height
    ##
    ##
    @property    
    def height(self)->int:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::height_get():{}".format(self))
        #endif
        PYSDL2_GETWINDOWSIZE(self._window,w,h)##pylint: disable=unused-variable
        return h
    FUNCTIONEND
    
    ### @see biui.Widget.height
    ##
    ##
    @height.setter
    def height(self, value:int)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::height_set():{}".format(self))
        #endif
        ##if value == self.height:
        ##    return
        if value > self.height:
            self._invalidate()
        PYSDL2_SETWINDOWSIZE(self._window,self.width,value)
    FUNCTIONEND
    
    ## Returns the title of the window.
    ##
    ##  @return            An string value.
    ##
    @property
    def title(self)->str:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::title_get():{}".format(self))
        #endif
        return self._title
    FUNCTIONEND
    
    ### Sets the title of the window.
    ##
    ##  @param value       An string value.
    ##  @return            None    
    ##
    @title.setter
    def title(self, value:str)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::title_set():{}".format(self))
        #endif
        PYSDL2_SETWINDOWTITLE(self._window,value)
        self._title = value
    FUNCTIONEND
     
    ### Handles the SDL mouse event for this window
    ##
    ##  todo: hinting
    def sdlOnMouseDown(self,event)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::sdlOnMouseDown():{}".format(self))
        #endif
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
    FUNCTIONEND
    
    ### Handles the SDL mouse event for this window
    ##
    ##  todo: hinting
    def sdlOnMouseUp(self,event)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::sdlOnMouseUp():{}".format(self))
        #endif
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
    FUNCTIONEND
     
    ### Handles the SDL mouse event for this window
    ##
    ##  todo: hinting
    def sdlOnMouseWheel(self,event)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::sdlOnMouseWheel():{}".format(self))
        #endif
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
    FUNCTIONEND
    
    ### Handles the SDL mouse event for this window
    ##
    ##  todo: hinting
    def sdlOnMouseMotion(self,event)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::sdlOnMouseMotion():{}".format(self))
        #endif
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
    FUNCTIONEND
    
    ### 
    ##
    ##
    def sdlOnKeyDown(self,event)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::sdlOnKeyDown():{}".format(self))
        #endif
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
    FUNCTIONEND
    
    ### 
    ##
    ##
    def sdlOnKeyUp(self,event)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::sdlOnKeyUp():{}".format(self))
        #endif
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
    FUNCTIONEND
    
    ### 
    ##
    ##
    def sdlOnTextInput(self,event)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::sdlOnTextInput():{}".format(self))
        #endif
        ##print( "sdlOnTextInput {}".format(event.text.text) )
        ##self._onTextInput(event)
        pass
    FUNCTIONEND
    
    ### Handles the sdl window event for this window
    ##
    ##  todo: hinting
    def sdlOnWindowEvent(self,event)->None:##pylint: disable=too-many-branches,too-many-statements
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::sdlOnWindowEvent():{}".format(self))
        #endif
        ev = Event(self)
        
        if event.window.event == sdl2.SDL_WINDOWEVENT_CLOSE:
            print("SDL_WINDOWEVENT_CLOSE")
            self._onWindowClose(ev)
        elif event.window.event == sdl2.SDL_WINDOWEVENT_SHOWN:
            ##print("SDL_WINDOWEVENT_SHOWN")
            self._onWindowShown(ev)
            self._invalidate()
        elif event.window.event == sdl2.SDL_WINDOWEVENT_HIDDEN:
            ##print("SDL_WINDOWEVENT_HIDDEN")
            self._onWindowHidden(ev)
        elif event.window.event == sdl2.SDL_WINDOWEVENT_EXPOSED:
            ##print("SDL_WINDOWEVENT_EXPOSED")
            self._onWindowExposed(ev)
            self._invalidate()
        elif event.window.event == sdl2.SDL_WINDOWEVENT_MOVED:
            ##print("SDL_WINDOWEVENT_MOVED")
            if self.x != event.window.data1 or self.y != event.window.data2:
                PYSDL2_SETWINDOWSIZE(
                    self._window,
                    event.window.data1,
                    event.window.data2
                )
                self._onWindowMoved(ev)
        elif event.window.event == sdl2.SDL_WINDOWEVENT_RESIZED:
            ##print("SDL_WINDOWEVENT_RESIZED")
            if self.width != event.window.data1 or self.height != event.window.data2 or True:
                ##PYSDL2_SETWINDOWSIZE(
                ##    self._window,
                ##    event.window.data1,
                ##    event.window.data2
                ##)
                ##self.width = event.window.data1
                ##self.height = event.window.data2
                self._onWindowResized(ev)
                self._invalidate()
        elif event.window.event == sdl2.SDL_WINDOWEVENT_SIZE_CHANGED:
            print("SDL_WINDOWEVENT_SIZE_CHANGED(%s,%s) (%s,%s)",event.window.data1,event.window.data2,self.width,self.height)
            if self.width != event.window.data1 or self.height != event.window.data2 or True:
                ##PYSDL2_SETWINDOWSIZE(
                ##    self._window,
                ##    event.window.data1,
                ##    event.window.data2
                ##)
                ##self.width = event.window.data1
                ##self.height = event.window.data2
                self._onWindowSizeChanged(ev)
                self._invalidate()
        elif event.window.event == sdl2.SDL_WINDOWEVENT_MINIMIZED:
            print("SDL_WINDOWEVENT_MINIMIZED")
            self._onWindowMinimized(ev)
        elif event.window.event == sdl2.SDL_WINDOWEVENT_MAXIMIZED:
            print("SDL_WINDOWEVENT_MAXIMIZED")
            self._onWindowMaximized(ev)
        elif event.window.event == sdl2.SDL_WINDOWEVENT_RESTORED:
            print("SDL_WINDOWEVENT_RESTORED")
            self._onWindowRestored(ev)
            self._invalidate()
        elif event.window.event == sdl2.SDL_WINDOWEVENT_ENTER:
            print("SDL_WINDOWEVENT_ENTER")
            self._onWindowEnter(ev)
        elif event.window.event == sdl2.SDL_WINDOWEVENT_LEAVE:
            print("SDL_WINDOWEVENT_LEAVE")
            self._onWindowLeave(ev)
        elif event.window.event == sdl2.SDL_WINDOWEVENT_FOCUS_GAINED:
            print("SDL_WINDOWEVENT_FOCUS_GAINED")
            self._onWindowFocusGained(ev)
        elif event.window.event == sdl2.SDL_WINDOWEVENT_FOCUS_LOST:
            print("SDL_WINDOWEVENT_FOCUS_LOST")
            self._onWindowFocusLost(ev)
        elif event.window.event == sdl2.SDL_WINDOWEVENT_TAKE_FOCUS:
            ##print("SDL_WINDOWEVENT_TAKE_FOCUS")
            ##self._onWindowFocus(ev)
            ##self._invalidate()
            pass
        else:
            print("*Unknown Windowevent.")
    FUNCTIONEND
    
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
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::id_get():{}".format(self))
        #endif
        return self._id 
    FUNCTIONEND
    
    ###
    ##
    ##
    def _onQuit(self)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::_onQuit():{}".format(self))
        #endif
        pass
    FUNCTIONEND
    
    ### Returns the window´s renderer.
    ##
    ##  todo: hinting
    @property
    def renderer(self):
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::renderer_get():{}".format(self))
        #endif
        return self._renderer
    FUNCTIONEND
    
    ### @see biui.Widget._redraw
    ##
    ## Event order at rendering:
    ## 1. _onBeforeRender
    ## 2. _calculateLayout
    ## 3. _render
    ## 4. _onAfterRender
    ##        
    def _render(self, forceRedraw:bool=False):
        #ifdef SHOW_FUNCTIONNAMES
        ##print("Window::_render():{}".format(self))
        #endif
                
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
        
        for c in self._children:
            c._onBeforeRender()
        
        self._calculateLayout()
        
        theme = biui.getTheme()

        if self._texture is None:##pylint: disable=access-member-before-definition
            ## pylint false positive about attribute-defined-outside-init
            PYSDL2_CREATETEXTURE(self.renderer,self.width,self.height, self._texture)
            self.__guiTexture = self._texture##pylint: diable=attribute-defined-outside-init
            self._recordDirtyRect([0,0,self.width,self.height])
            forceRedraw = True
            ##print("new texture")
        
        #ifdef SHOW_UPDATE_BOX
        PYSDL2_CREATETEXTURE(self.renderer,self.width,self.height, self.__guiTexture)
        forceRedraw = True
        #endif
        
        theme.drawWindowBeforeChildren(self,self.__guiTexture)
        
        for c in self._children:
            tx = c._render(forceRedraw)
            ## We copy it at the childs position in the childs size.
            src = c.renderRect
            tgt = (c.x,c.y,src[2],src[3])
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
        #endif
        pass
        
        #ifndef SHOW_UPDATE_BOX
        ## just render dirty rectangles
        ##dr = [[0,0,self.width,self.height]]
        for r in dr:
            r = list(r)
            ## r must not reach over the widow´s texture
            r[0] = max(0,r[0])
            r[1] = max(0,r[1])
            r[2] = min(r[2],self.width-r[0])
            r[3] = min(r[3],self.height-r[1])
            ##print(r)            
            PYSDL2_RENDER_COPY(self.renderer,self.__guiTexture,r,r)
        #endif
        
        ## Show it on screen.  
        PYSDL2_PRESENT(self.renderer)
        
        self._isInvalide = False##pylint: disable=attribute-defined-outside-init
        
        for c in self._children:
            c._onAfterRender()
    FUNCTIONEND
        
    ### @see biui.Widget._recordDirtyRect
    ##
    ##    
    def _recordDirtyRect(self,box:tuple[int,int,int,int])->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::_recordDirtyRect():{}".format(self))
        #endif
        ## Check if the box is outside of the visible area
        if box[0] > self.width:
            return 
        if box[1] > self.height:
            return
        if box[0]+box[2] < 0:
            return 
        if box[1]+box[3] < 0:
            return
        ##print(box)
        
        self.__dr.add(box)
    FUNCTIONEND
    
    ### Transforms a screen position to a window position.
    ##
    ##
    def toWindow(self,coordinates:tuple[int,int])->tuple[int,int]:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::toWindow():{}".format(self))
        #endif
        return (coordinates[0]-self.x,coordinates[1]-self.y)
    FUNCTIONEND
    
    ### Transforms a window position to a screen position.
    ##
    ##
    def toScreen(self,coordinates:tuple[int,int])->tuple[int,int]:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::toScreen():{}".format(self))
        #endif
        return (coordinates[0]+self.x,coordinates[1]+self.y)
    FUNCTIONEND
    
    def __hndOnChildRemoved(self,ev):##pylint: disable=unused-argument
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::_hndOnChildRemoved():{}".format(self))
        #endif
        self._invalidate()
    FUNCTIONEND    
        
    ##def _onKeyDown(self,ev:KeyEvent)->None:
    ##    print("_onKeyDown")
    ##    super()._onKeyDown(ev)
    
    ##def _onKeyUp(self,ev:KeyEvent)->None:
    ##    print("_onKeyUp")
    ##    super()._onKeyUp(ev)
    
    ##def _onTextInput(self,ev:KeyEvent)->None:
    ##    print("_onTextInput")
    ##    super()._onTextInput(ev)
        
    def __hndOnShortcut(self,event)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::__hndOnShortcut():{}".format(self))
        #endif
        ##print("Window::__hndOnShortCut")
        event.eventSource = self.__focusedWidget
        
        self._onShortcut(event)
    FUNCTIONEND
    
    def _onWindowClose(self,ev)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::_onWindowClose():{}".format(self))
        #endif
        self.onWindowClose.provoke(ev)
    FUNCTIONEND
    
    def _onWindowShown(self,ev)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::_onWindowShown():{}".format(self))
        #endif
        self.onWindowShown.provoke(ev)
    FUNCTIONEND
    
    def _onWindowHidden(self,ev)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::_onWindowHidden():{}".format(self))
        #endif
        self.onWindowHidden.provoke(ev)        
    FUNCTIONEND
    
    def _onWindowExposed(self,ev)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::_onWindowExposed():{}".format(self))
        #endif
        self.onWindowExposed.provoke(ev)        
    FUNCTIONEND
    
    def _onWindowMoved(self,ev)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::_onWindowMoved():{}".format(self))
        #endif
        self.onWindowMoved.provoke(ev)
    FUNCTIONEND
    
    def _onWindowResized(self,ev)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::_onWindowResized():{}".format(self))
        #endif
        self.onWindowResized.provoke(ev)    
    FUNCTIONEND
    
    def _onWindowSizeChanged(self,ev)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::_onWindowSizeChanged():{}".format(self))
        #endif
        self.onWindowSizeChanged.provoke(ev)            
    FUNCTIONEND
    
    def _onWindowMinimized(self,ev)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::_onWindowMinimized():{}".format(self))
        #endif
        self.onWindowMinimized.provoke(ev)
    FUNCTIONEND
    
    def _onWindowMaximized(self,ev)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::_onWindowMaximized():{}".format(self))
        #endif
        self.onWindowMaximized.provoke(ev)
    FUNCTIONEND
    
    def _onWindowRestored(self,ev)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::_onWindowRestored():{}".format(self))
        #endif
        self.onWindowRestored.provoke(ev)
    FUNCTIONEND
    
    def _onWindowEnter(self,ev)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::_onWindowEnter():{}".format(self))
        #endif
        self.onWindowEnter.provoke(ev)
    FUNCTIONEND
    
    def _onWindowLeave(self,ev)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::_onWindowLeave():{}".format(self))
        #endif
        self.onWindowLeave.provoke(ev)
    FUNCTIONEND
    
    def _onWindowFocusGained(self,ev)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::_onWindowFocusGained():{}".format(self))
        #endif
        self.onWindowFocusGained.provoke(ev)
    FUNCTIONEND
    
    def _onWindowFocusLost(self,ev)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::_onWindowFocusLost():{}".format(self))
        #endif
        self.onWindowFocusLost.provoke(ev)
    FUNCTIONEND
    
    def _onWindowFocus(self,ev)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Window::_onWindowFocus():{}".format(self))
        #endif
        self.onWindowFocus.provoke(ev)
    FUNCTIONEND
          