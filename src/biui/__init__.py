
import os
from time import time

import sdl2
import sdl2.ext

import biui.Color
import biui.EventPhase
import biui.Event
import biui.DOMEvent
import biui.MouseEvent
import biui.KeyEvent
import biui.EventTypes
import biui.EventManager
import biui.Theme
import biui.Keys
import biui.KeyModifiers
import biui.Widget
import biui.ContainerWidget
import biui.Window
import biui.Pane
import biui.Button
import biui.ButtonStates
import biui.ToggleButton
import biui.ButtonGroup
import biui.LayoutManager
import biui.Alignment
import biui.FlexPane
import biui.FlexSpacer
import biui.FlexGrid
import biui.Label
import biui.Font
import biui.NumberSlider
import biui.ImageLibrary
import biui.Spacer
import biui.Progressbar
import biui.Checkbox
import biui.DL
import biui.Hinting
import biui.Style
import biui.Direction
import biui.DirtyRectangleManager
import biui.Mouse


from sdl2.surface import SDL_CreateRGBSurface
from sdl2.mouse import SDL_BUTTON_LMASK, SDL_BUTTON_MIDDLE, SDL_BUTTON_RIGHT, SDL_BUTTON_LEFT, SDL_BUTTON_X1, SDL_BUTTON_X2


Color = biui.Color.Color
EventPhase = biui.EventPhase.EventPhase
DOMEvent = biui.DOMEvent.DOMEvent
Event = biui.Event.Event
MouseEvent = biui.MouseEvent.MouseEvent
KeyEvent = biui.KeyEvent.KeyEvent
EventTypes = biui.EventTypes.EventTypes
EventManager = biui.EventManager.EventManager
Widget = biui.Widget.Widget
Window = biui.Window.Window
Pane = biui.Pane.Pane
KeyModifiers = biui.KeyModifiers.KeyMofifiers
Keys = biui.Keys.Keys
Button = biui.Button.Button
ButtonStates = biui.ButtonStates.ButtonStates
ToggleButton = biui.ToggleButton.ToggleButton
ButtonGroup = biui.ButtonGroup.ButtonGroup
LayoutManager = biui.LayoutManager.LayoutManager
Alignment = biui.Alignment.Alignment
FlexPane = biui.FlexPane.FlexPane
FlexSpacer = biui.FlexSpacer.FlexSpacer
FlexGrid = biui.FlexGrid.FlexGrid
Label = biui.Label.Label
Font = biui.Font.Font
NumberSlider = biui.NumberSlider.NumberSlider
ImageLibrary = biui.ImageLibrary.ImageLibrary
Spacer = biui.Spacer.Spacer
Progressbar = biui.Progressbar.Progressbar
Checkbox = biui.Checkbox.Checkbox
DL = biui.DL.DL
Hinting = biui.Hinting.Hinting
Style = biui.Style.Style
Direction = biui.Direction.Direction
DirtyRectangleManager = biui.DirtyRectangleManager.DirtyRectangleManager
Mouse = biui.Mouse.SingletonMouse()

##
##_pixelFormat = sdl2.SDL_AllocFormat( sdl2.SDL_PIXELFORMAT_RGBA32 )

##
__clickTime = 0.25

##
__themeFolder = "themes"

## Stores the Instance of Theme.
__theme = None

## Defines if all directy rects are drawn on screen.
## For debug use. This makes everything slower.
__SHOWUPDATEBOXES = True

## Stores if pygame is initialized.
__initialized__ = False

### Stored a reference to the Widget the mouse is over.
__hoverWidget = None

### Stored a reference to the Widget with the focus.
__focusedWidget = None

### Stores all window objects.
##  Pygame allows just one window.
__windows = []

## Stores the time of the mouseDown event.
__mouseDownTime = None

## Folders in which biui is  looking for font files
__fontFolders = []

##
__fonts = []

##
themeDebug = False

##def profile(fnc):
##    import cProfile, pstats
##    profiler = cProfile.Profile()
##    profiler.enable()
##    fnc()
##    profiler.disable()
##    stats = pstats.Stats(profiler).sort_stats('tottime')
##    stats.print_stats()
    
### Initializes biui and sub systems. Can be called more than once.
##  It takes care about multiple calls.
##
def init():
    global __initialized__
    if __initialized__:
        return 
    
    sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)
    sdl2.ext.init()
    sdl2.sdlttf.TTF_Init()
    biui.DL.init()
    

    biui.__fillFontFolders()
    biui.scanFonts()
    __initialized__ = True
    
    ##
    ## TODO: Look for platform specific font folders
    ##       and add them to __fontFolders.
    ##
 
###
##
##
def quit():
    __theme.quit()
    biui.DL.quit()
    sdl2.ext.quit()
    sdl2.SDL_Quit()
    __initialized__ = False

###
##
##
def addFontFolder(path):
    
    if not os.path.exists(path):
        return False
    
    if path not in __fontFolders:
        __fontFolders.append(path)
    
    return True

###
##
##
def getFontFolders():
    return __fontFolders

###
##
##
def getFonts():
    return __fonts

###
##
##
def scanFonts():
    global __fonts
    __fonts = []
    
    for f in __fontFolders:
        for file in os.listdir(f):
            subject = os.path.join(f,file)
            if os.path.isfile(subject):
                if subject[-4:].lower() == ".ttf":
                    __fonts.append( [file,subject] )
                    
    return __fonts

###
##
##
def getFontPath(fontName):
    
    for f  in __fonts:
        if f[0] == fontName:
            return f[1]

    ## TODO: react if no font is found.
    pass
    
###
##
##
def getDefaultFont():
    return biui.getFontPath("padmaa.ttf")
    return biui.getFontPath("GlacialIndifference-Regular.ttf")

###
##
##
def __fillFontFolders():
    
    ## DEFAULT
    biui.addFontFolder( os.path.abspath("./../../fonts") )
    
    ## UBUNTU
    base = "/usr/share/fonts/truetype"
    for path in os.listdir(base):
        subject = os.path.join(base,path)
        if os.path.isdir(subject):
            biui.addFontFolder( subject )
    
    ## WINDOWS
    biui.addFontFolder( "c:\windows\fonts" )
    
    ## MACOS
    
###
##
##
def _removeWindow(window):
    __windows.remove(window)
    
###
##
##
def _addWindow(window):
    __windows.insert(0,window)

### Returns the Widget at the given position.
##  Currently the function doesn't care about
##  the window, beecause there is just one.
##
##  @param pos               A tuple representing a position.
##  @return                  A Widget object
##
def __getChildAt(pos):
    global __windows
    
    for w in __windows:
        return w.getChildAt(pos)

### Returns a defaault value if value is None
##  If value is not None value is returned.
##  Otherwise default is returned.
##
##  @param value      A python literal.
##  @param default    A default value.
##  @return           vValue or default.
##
def default(value,default):
    if value != None:
        return value
    return default

###
##
##
def setThemeFolder(folder):
    global __themeFolder
    __themeFolder = folder

###
##
##
def selectTheme(name="default"):
    theme = getTheme()
    theme.selectTheme(name)

### Returns the Theme instance. If necassary it is created.
##
##  @return             A Theme object.
##
def getTheme():
    global __theme
    ##print( os.getcwd())
    if __theme == None:
        __theme = biui.Theme.Theme( os.path.join(os.getcwd(),__themeFolder) )
        selectTheme()
    return __theme

 
### The biui main loop.
##  Cares about event distribution and drawing of the GUI.
##
##  @return        True as long as a window is open.
##
def _main():
    global __windows, __hoverWidget, __mouseDownTime, __clickTime
        
    ## ++++++++++++++++++++++++++++++++++++++++++++++
    ##                                 Event handling
    ## ++++++++++++++++++++++++++++++++++++++++++++++
    events =  pygame.event.get()

    for event in events:
        
        ##
        ## Mouse events
        ##
        ## Mouse events are send directly to the widget.
        ##
        if event.type == pygame.MOUSEMOTION:
            bStates = pygame.mouse.get_pressed(num_buttons=5)
            receiver = biui.__getChildAt(event.pos)
            ev = biui.MouseEvent(receiver,bStates,event.pos,0,0)
            if receiver != __hoverWidget:
                if __hoverWidget != None:
                    evLeave = biui.MouseEvent(__hoverWidget,bStates,event.pos,0,0)
                    for w in __windows:
                        w._onMouseLeave(evLeave)
                __hoverWidget = receiver
                __hoverWidget._onMouseEnter(ev)
            else:
                for w in __windows:
                    w._onMouseMove(ev)

            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ## Filter wheel action.
            if event.button not in [4,5]:
                __mouseDownTime = time()
                bStates = pygame.mouse.get_pressed(num_buttons=5)
                receiver = biui.__getChildAt(event.pos)
                ev = biui.MouseEvent(receiver,bStates,event.pos,0,0)
                for w in __windows:
                    w._onMouseDown(ev)
                    
        elif event.type == pygame.MOUSEBUTTONUP:
            ## Filter wheel action.
            if event.button not in [4,5]:
                ##print(time()-__mouseDownTime)                
                bStates = pygame.mouse.get_pressed(num_buttons=5)
                receiver = biui.__getChildAt(event.pos)
                ev = biui.MouseEvent(receiver,bStates,event.pos,0,0)
                if time()-__mouseDownTime < __clickTime:
                    for w in __windows:
                        w._onMouseClick(ev)

                for w in __windows:
                    w._onMouseUp(ev)
                        
        elif event.type == pygame.MOUSEWHEEL:
            mpos = pygame.mouse.get_pos()
            bStates = pygame.mouse.get_pressed(num_buttons=5)
            receiver = biui.__getChildAt(mpos)
            ev = biui.MouseEvent(receiver,bStates,mpos,event.x,event.y)
            for w in __windows:
                w._onMouseWheel(ev)
            
            
        ##
        ## Keyboard events
        ##
        ## Keyboard events are send throw the DOM structure.
        ##
        elif event.type == pygame.KEYDOWN:
            ##print( "keydown: "+ str(event) )
            for w in __windows:
                ev = biui.KeyEvent(
                    w,
                    event.unicode,
                    event.key,
                    event.scancode,
                    event.mod
                )
                w._onKeyDown(ev)
        elif event.type == pygame.KEYUP:
            ##print( "keyup: "+ str(event) )
            for w in __windows:
                ev = biui.KeyEvent(
                    w,
                    event.unicode,
                    event.key,
                    event.scancode,
                    event.mod
                )        
                w._onKeyUp(ev)
        elif event.type == pygame.TEXTINPUT:
            ##print( "textinput: "+ str(event) )
            for w in __windows:
                ev = biui.KeyEvent(
                    w,
                    event.text
                )            
                w._onTextInput(ev)
            
            
        ##
        ## Window events
        ## We have to find the focused window.
        ## Currently we have just one!
        ##
        ## Window events are send directly to the window.
        ##
        elif event.type == pygame.WINDOWLEAVE:
            for w in __windows:
                w._onWindowLeave(biui.Event(w))
        elif event.type == pygame.WINDOWENTER:
            for w in __windows:
                w._onWindowEnter(biui.Event(w))
        elif event.type == pygame.ACTIVEEVENT:
            for w in __windows:
                w._onWindowFocus(biui.Event(w))
        elif event.type == pygame.WINDOWFOCUSLOST:
            for w in __windows:
                w._onWindowFocusLost(biui.Event(w))
        elif event.type == pygame.WINDOWHIDDEN:
            for w in __windows:
                w._onWindowHidden(biui.Event(w))
        elif event.type == pygame.WINDOWMINIMIZED:
            for w in __windows:
                w._onWindowMinimized(biui.Event(w))
        elif event.type == pygame.WINDOWRESTORED:
            for w in __windows:
                w._onWindowRestored(biui.Event(w))
        elif event.type == pygame.WINDOWSHOWN:
            for w in __windows:
                w._onWindowShown(biui.Event(w))
        elif event.type == pygame.WINDOWFOCUSGAINED:
            for w in __windows:
                w._onWindowFocusGained(biui.Event(w))
        elif event.type == pygame.WINDOWTAKEFOCUS:
            for w in __windows:
                w._onWindowTakeFocus(biui.Event(w))
        elif event.type == pygame.WINDOWCLOSE:
            for w in __windows:
                w._onWindowClose(biui.Event(w))
        elif event.type == pygame.WINDOWMAXIMIZED:
            for w in __windows:
                w._onWindowMaximized(biui.Event(w))
        elif event.type == pygame.WINDOWMOVED:
            for w in __windows:
                w._onWindowMoved(biui.Event(w))
        elif event.type == pygame.WINDOWSIZECHANGED:
            for w in __windows:
                w.width = event.x
                w.height = event.y
                w._onWindowSizeChanged(biui.Event(w))
        elif event.type == pygame.WINDOWRESIZED:
            for w in __windows:
                w.width = event.x
                w.height = event.y
                w._onWindowResized(biui.Event(w))
        elif event.type == pygame.WINDOWEXPOSED:
            for w in __windows:
                w._onWindowExposed(biui.Event(w))
        elif event.type == pygame.VIDEORESIZE:
            pass
        elif event.type == pygame.VIDEOEXPOSE:
            pass
              
              
        ##
        ## MISC
        ##
        elif event.type == pygame.QUIT:
            for w in __windows:
                w._onWindowExposed(biui.Event(w))
            return False
        
        
        ##
        ## Else
        ##
        else:
            ##print("Event: "+ str(pygame.event.event_name(event.type)))
            pass
            
            
    ## ++++++++++++++++++++++++++++++++++++++++++++++
    ##                                     Redraw GUI
    ## ++++++++++++++++++++++++++++++++++++++++++++++
    dr = []
    for w in __windows:
        w._redraw()
        dr += w._getDirtyRectangles()
        
        if __SHOWUPDATEBOXES:
            for r in dr:
                pygame.draw.rect(w._getSurface(),(255,0,0),r,1)
                ##pygame.display.update()
    
    if len(dr) >0:            
        pygame.display.update(dr)
    
    return True

def main():
    global __windows, __hoverWidget, __mouseDownTime, __clickTime
    
    running = True
    ##while running:
    
    events = sdl2.ext.get_events()
    for event in events:

        ###############################################################
        ##                                                          APP
        ###############################################################
        if event.type == sdl2.SDL_APP_TERMINATING:
            ##print("SDL_APP_TERMINATING")
            pass
        elif event.type == sdl2.SDL_APP_LOWMEMORY:
            ##print("SDL_APP_LOWMEMORY")
            pass
        elif event.type == sdl2.SDL_APP_WILLENTERBACKGROUND:
            ##print("SDL_APP_WILLENTERBACKGROUND")
            pass
        elif event.type == sdl2.SDL_APP_DIDENTERBACKGROUND:
            ##print("SDL_APP_DIDENTERBACKGROUND")
            pass
        elif event.type == sdl2.SDL_APP_WILLENTERFOREGROUND:
            ##print("SDL_APP_WILLENTERFOREGROUND")
            pass
        elif event.type == sdl2.SDL_APP_DIDENTERFOREGROUND:
            ##print("SDL_APP_DIDENTERFOREGROUND")
            pass
        
        ###############################################################
        ##                                                        MOUSE
        ###############################################################
        elif event.type == sdl2.SDL_MOUSEMOTION:
            ##print("SDL_MOUSEMOTION")
            mevent = event.motion
            pos = (mevent.x,mevent.y)
            
            bStates = [
                (mevent.state & SDL_BUTTON_LEFT) != 0,
                (mevent.state & SDL_BUTTON_MIDDLE) != 0,
                (mevent.state & SDL_BUTTON_RIGHT) != 0,
                (mevent.state & SDL_BUTTON_X1) != 0,
                (mevent.state & SDL_BUTTON_X2) != 0
            ]
            receiver = biui.__getChildAt( pos )
            
            ev = biui.MouseEvent(receiver,bStates,pos,0,0)
            
            if receiver != __hoverWidget:
                if __hoverWidget != None:
                    evLeave = biui.MouseEvent(__hoverWidget,bStates,pos,0,0)
                    for w in __windows:
                        w._onMouseLeave(evLeave)
                __hoverWidget = receiver
                __hoverWidget._onMouseEnter(ev)
            else:
                for w in __windows:
                    w._onMouseMove(ev)
        
        elif event.type == sdl2.SDL_MOUSEBUTTONDOWN:
            ##print("SDL_MOUSEBUTTONDOWN")
            
            mevent = event.motion
            pos = (mevent.x,mevent.y)
            
            __mouseDownTime = time()
            
            bStates = [
                (mevent.state & SDL_BUTTON_LEFT) != 0,
                (mevent.state & SDL_BUTTON_MIDDLE) != 0,
                (mevent.state & SDL_BUTTON_RIGHT) != 0,
                (mevent.state & SDL_BUTTON_X1) != 0,
                (mevent.state & SDL_BUTTON_X2) != 0
            ]
            
            receiver = biui.__getChildAt(pos)
            ev = biui.MouseEvent(receiver,bStates,pos,0,0)
            for w in __windows:
                w._onMouseDown(ev)
            
        elif event.type == sdl2.SDL_MOUSEBUTTONUP:
            ##print("SDL_MOUSEBUTTONUP")

            mevent = event.motion
            pos = (mevent.x,mevent.y)
            
            bStates = [
                (mevent.state & SDL_BUTTON_LEFT) != 0,
                (mevent.state & SDL_BUTTON_MIDDLE) != 0,
                (mevent.state & SDL_BUTTON_RIGHT) != 0,
                (mevent.state & SDL_BUTTON_X1) != 0,
                (mevent.state & SDL_BUTTON_X2) != 0
            ]
            
            receiver = biui.__getChildAt(pos)
            ev = biui.MouseEvent(receiver,bStates,pos,0,0)
            if time()-__mouseDownTime < __clickTime:
                for w in __windows:
                    w._onMouseClick(ev)

            for w in __windows:
                w._onMouseUp(ev)
                                
        elif event.type == sdl2.SDL_MOUSEWHEEL:
            ##print("SDL_MOUSEWHEEL")
            
            mevent = event.motion
            pos = (mevent.x,mevent.y)                

            bStates = [
                (mevent.state & SDL_BUTTON_LEFT) != 0,
                (mevent.state & SDL_BUTTON_MIDDLE) != 0,
                (mevent.state & SDL_BUTTON_RIGHT) != 0,
                (mevent.state & SDL_BUTTON_X1) != 0,
                (mevent.state & SDL_BUTTON_X2) != 0
            ]
            
            receiver = biui.__getChildAt(pos)
            ev = biui.MouseEvent(receiver,bStates,pos,event.x,event.y)
            for w in __windows:
                w._onMouseWheel(ev)
        
        ###############################################################
        ##                                                     KEYBOARD
        ###############################################################
        elif event.type == sdl2.SDL_KEYDOWN:
            ##print("SDL_KEYDOWN")

            ##print(dir(event))
            ## 'adevice', 'button', 'caxis', 'cbutton', 'cdevice', 'common', 
            ## 'csensor', 'ctouchpad', 'dgesture', 'display', 'drop', 'edit',
            ## 'jaxis', 'jball', 'jbutton', 'jdevice', 'jhat', 'key', 'mgesture',
            ## 'motion', 'padding', 'quit', 'sensor', 'syswm', 'text', 'tfinger',
            ## 'type', 'user', 'wheel', 'window'
            
            pass
        elif event.type == sdl2.SDL_KEYUP:
            ##print("SDL_KEYUP")
            pass
        elif event.type == sdl2.SDL_KEYMAPCHANGED:
            ## strg, alt, ...
            ##print("SDL_KEYMAPCHANGED")
            pass
        elif event.type == sdl2.SDL_TEXTINPUT:
            ##print("SDL_TEXTINPUT")
            pass
        elif event.type == sdl2.SDL_TEXTEDITING:
            ##print("SDL_TEXTEDITING")
            pass

        
        ###############################################################
        ##                                                     JOYSTICK
        ###############################################################
        elif event.type == sdl2.SDL_JOYAXISMOTION:
            ##print("SDL_JOYAXISMOTION")
            pass
        elif event.type == sdl2.SDL_JOYBALLMOTION:
            ##print("SDL_JOYBALLMOTION")
            pass
        elif event.type == sdl2.SDL_JOYHATMOTION:
            ##print("SDL_JOYHATMOTION")
            pass
        elif event.type == sdl2.SDL_JOYBUTTONDOWN:
            ##print("SDL_JOYBUTTONDOWN")
            pass
        elif event.type == sdl2.SDL_JOYBUTTONUP:
            ##print("SDL_JOYBUTTONUP")
            pass
        elif event.type == sdl2.SDL_JOYDEVICEADDED:
            ##print("SDL_JOYDEVICEADDED")
            pass
        elif event.type == sdl2.SDL_JOYDEVICEREMOVED:
            ##print("SDL_JOYDEVICEREMOVED")
            pass
        
        ###############################################################
        ##                                                   CONTROLLER
        ###############################################################
        elif event.type == sdl2.SDL_CONTROLLERAXISMOTION:
            ##print("SDL_CONTROLLERAXISMOTION")
            pass
        elif event.type == sdl2.SDL_CONTROLLERBUTTONDOWN:
            ##print("SDL_CONTROLLERBUTTONDOWN")
            pass
        elif event.type == sdl2.SDL_CONTROLLERBUTTONUP:
            ##print("SDL_CONTROLLERBUTTONUP")
            pass
        elif event.type == sdl2.SDL_CONTROLLERDEVICEADDED:
            ##print("SDL_CONTROLLERDEVICEADDED")
            pass
        elif event.type == sdl2.SDL_CONTROLLERDEVICEREMAPPED:
            ##print("SDL_CONTROLLERDEVICEREMAPPED")
            pass
        elif event.type == sdl2.SDL_CONTROLLERDEVICEREMOVED:
            ##print("SDL_CONTROLLERDEVICEREMOVED")
            pass 
        
        ###############################################################
        ##                                                       WINDOW
        ###############################################################
        elif event.type == sdl2.SDL_WINDOWEVENT:
            ##print("SDL_WINDOWEVENT")
            ##print( dir(event) )
            ## 'adevice', 'button', 'caxis', 'cbutton', 'cdevice', 'common', 'csensor',
            ## 'ctouchpad', 'dgesture', 'display', 'drop', 'edit', 'jaxis', 'jball',
            ## 'jbutton', 'jdevice', 'jhat', 'key', 'mgesture', 'motion', 'padding',
            ## 'quit', 'sensor', 'syswm', 'text', 'tfinger', 'type', 'user', 'wheel',
            ## 'window'
            
            ##print( dir(event.window) )
            ## '__class__', '__ctypes_from_outparam__', '__delattr__',
            ## '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
            ## '__ge__', '__getattribute__', '__gt__', '__hash__', 
            ## '__init__', '__init_subclass__', '__le__', '__lt__',
            ## '__module__', '__ne__', '__new__', '__reduce__', 
            ## '__reduce_ex__', '__repr__', '__setattr__', '__setstate__',
            ## '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
            ## '_b_base_', '_b_needsfree_', '_fields_', '_objects', 'data1',
            ## 'data2', 'event', 'padding1', 'padding2', 'padding3',
            ## 'timestamp', 'type', 'windowID']
            
            ##print(event.window.windowID)
            window = None
            for w in __windows:
                if w.id ==  event.window.windowID:
                    window = w
            
            window._onWindowEvent(event)
            
        elif event.type == sdl2.SDL_SYSWMEVENT:
            ##print("SDL_SYSWMEVENT")
            pass
        
        ###############################################################
        ##                                                       Finger
        ###############################################################
        elif event.type == sdl2.SDL_FINGERDOWN:
            ##print("SDL_FINGERDOWN")
            pass
        elif event.type == sdl2.SDL_FINGERUP:
            ##print("SDL_FINGERUP")
            pass
        elif event.type == sdl2.SDL_FINGERMOTION:
            ##print("SDL_FINGERMOTION")
            pass
        elif event.type == sdl2.SDL_DOLLARGESTURE:
            ##print("SDL_DOLLARGESTURE")
            pass
        elif event.type == sdl2.SDL_DOLLARRECORD:
            ##print("SDL_DOLLARRECORD")
            pass
        elif event.type == sdl2.SDL_MULTIGESTURE:
            ##print("SDL_MULTIGESTURE")
            pass
        
        ###############################################################
        ##                                                    CLIPBOARD
        ###############################################################
        elif event.type == sdl2.SDL_CLIPBOARDUPDATE:
            ##print("SDL_CLIPBOARDUPDATE")
            pass
        
        ###############################################################
        ##                                                  Drag'n Drop
        ###############################################################
        elif event.type == sdl2.SDL_DROPBEGIN:
            ##print("SDL_DROPBEGIN")
            pass
        elif event.type == sdl2.SDL_DROPCOMPLETE:
            ##print("SDL_DROPCOMPLETE")
            pass
        elif event.type == sdl2.SDL_DROPFILE:
            ##print("SDL_DROPFILE")
            pass
        elif event.type == sdl2.SDL_DROPTEXT:
            ##print("SDL_DROPTEXT")
            pass
                        
        ###############################################################
        ##                                                        AUDIO
        ###############################################################
        elif event.type == sdl2.SDL_AUDIODEVICEADDED:
            ##print("SDL_AUDIODEVICEADDED")
            pass
        elif event.type == sdl2.SDL_AUDIODEVICEREMOVED:
            ##print("SDL_AUDIODEVICEREMOVED")
            pass
        
        
        ###############################################################
        ##                                                         MISC
        ###############################################################
        elif event.type == sdl2.SDL_USEREVENT:
            ##print("SDL_USEREVENT")
            pass
        elif event.type == sdl2.SDL_RENDER_TARGETS_RESET:
            ##print("SDL_RENDER_TARGETS_RESET")
            pass
        elif event.type == sdl2.SDL_RENDER_DEVICE_RESET:
            ##print("SDL_RENDER_DEVICE_RESET")
            pass
        elif event.type == sdl2.SDL_LASTEVENT:
            ##print("SDL_LASTEVENT")
            pass
        elif event.type == sdl2.SDL_FIRSTEVENT:
            ##print("SDL_FIRSTEVENT")
            pass
        elif event.type == sdl2.SDL_USEREVENT:
            ##print("")
            pass
        elif event.type == sdl2.SDL_QUIT:
            running = False
            break
        
        ###############################################################
        ##                                                   NO EVENTS?
        ###############################################################
        elif event.type == sdl2.SDL_TEXTEDITINGEVENT_TEXT_SIZE:
            ##print("*SDL_TEXTEDITINGEVENT_TEXT_SIZE")
            pass
        elif event.type == sdl2.SDL_TEXTINPUTEVENT_TEXT_SIZE:
            ##print("*SDL_TEXTINPUTEVENT_TEXT_SIZE")
            pass
        elif event.type == sdl2.SDL_MOUSEWHEEL_NORMAL:
            ##print("*SDL_MOUSEWHEEL_NORMAL")
            pass
        elif event.type == sdl2.SDL_MOUSEWHEEL_FLIPPED:
            ##print("*SDL_MOUSEWHEEL_FLIPPED")
            pass
        elif event.type == sdl2.SDL_MOUSE_TOUCHID:
            ##print("*SDL_MOUSE_TOUCHID")
            pass
        elif event.type == sdl2.SDL_CONTROLLERSENSORUPDATE:
            ##print("*SDL_CONTROLLERSENSORUPDATE")
            pass
        elif event.type == sdl2.SDL_CONTROLLERTOUCHPADDOWN:
            ##print("*SDL_CONTROLLERTOUCHPADDOWN")
            pass
        elif event.type == sdl2.SDL_CONTROLLERTOUCHPADMOTION:
            ##print("*SDL_CONTROLLERTOUCHPADMOTION")
            pass
        elif event.type == sdl2.SDL_CONTROLLERTOUCHPADUP:            
            ##print("*SDL_CONTROLLERTOUCHPADUP")
            pass 
        elif event.type == sdl2.SDL_CommonEvent:
            ##print("")
            pass
        else:
            print("Eventtype not recognized:"+str(event.type))
        
    ###############################################################
    ##                                                  DRAWING GUI
    ###############################################################
    
    ##print("--------------------------------")
    for w in __windows:
        w._redraw()
        
    return len(__windows) > 0


