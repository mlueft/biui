#include "pysdl2.inc"
#include "biui.inc"
from typing import TypeAlias

import os
from time import time

import sdl2
import sdl2.ext
import json

from biui.EventPhase import EventPhase
from biui.Event import Event
from biui.DOMEvent import DOMEvent
from biui.MouseEvent import MouseEvent
from biui.KeyEvent import KeyEvent
from biui.EventTypes import EventTypes
from biui.EventManager import EventManager
from biui.Theme import Theme
from biui.ThemeImg import ThemeImg
from biui.Keys import Keys
from biui.KeyModifiers import KeyModifiers
from biui.Widget import Widget
from biui.ContainerWidget import ContainerWidget
from biui.Window import Window
from biui.Pane import Pane
from biui.Button import Button
from biui.ButtonStates import ButtonStates
from biui.ToggleButton import ToggleButton
from biui.ButtonGroup import ButtonGroup
from biui.LayoutManager import LayoutManager
from biui.Alignment import Alignment
from biui.FlexPane import FlexPane
from biui.FlexSpacer import FlexSpacer
from biui.FlexGrid import FlexGrid
from biui.Label import Label
from biui.Font import Font
from biui.NumberSlider import NumberSlider
from biui.ImageLibrary import ImageLibrary
from biui.Spacer import Spacer
from biui.Progressbar import Progressbar
from biui.Checkbox import Checkbox
from biui.Hinting import Hinting
from biui.Style import Style
from biui.Direction import Direction
from biui.DirtyRectangleManager import DirtyRectangleManager
from biui.Mouse import Mouse
from biui.Menubar import Menubar
from biui.MenuItem import MenuItem
from biui.MenuPane import MenuPane
from biui.ScrollNavigator import ScrollNavigator
from biui.Image import Image
from biui.Color import Color


from sdl2.surface import SDL_CreateRGBSurface
from sdl2.mouse import SDL_BUTTON_LMASK, SDL_BUTTON_MIDDLE, SDL_BUTTON_RIGHT, SDL_BUTTON_LEFT, SDL_BUTTON_X1, SDL_BUTTON_X2

Mouse = Mouse()
##
__themeFolder = BIUI_THEMEFOLDER

## Stores the Instance of Theme.
__theme = None

## Stores if pygame is initialized.
__initialized__ = False

### Stores all window objects.
__windows:list[Window] = []

## Folders in which biui is  looking for font files
__fontFolders = []

##
__fonts:list[list[str]] = []

def profile(fnc):
    import cProfile, pstats
    profiler = cProfile.Profile()
    profiler.enable()
    fnc()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('tottime')
    stats.print_stats()
    
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

### Initializes biui and sub systems. Can be called more than once.
##  It takes care about multiple calls.
##
def init():
    global __initialized__
    if __initialized__:
        return 
    
    PYSDL2_INIT()
    __fillFontFolders()
    scanFonts()
    __initialized__ = True
    
    ##
    ## TODO: Look for platform specific font folders
    ##       and add them to __fontFolders.
    ##
 
###
##
##
def quit():
    global __theme,__initialized__
    __theme.quit()
    PYSDL2_QUIT()
    __initialized__ = False

###
##
##
def addFontFolder(path):
    global __fontFolders
    if not os.path.exists(path):
        return False
    
    if path not in __fontFolders:
        __fontFolders.append(path)
    
    return True

###
##
##
def getFontFolders():
    global __fontFolders
    return __fontFolders

###
##
##
def getFonts():
    global __fonts
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
    global __fonts
    for f  in __fonts:
        if f[0] == fontName:
            return f[1]

    ## TODO: react if no font is found.
    pass
    
###
##
##
def getDefaultFont():
    return getFontPath("padmaa.ttf")
    return getFontPath("GlacialIndifference-Regular.ttf")

###
##
##
def __fillFontFolders():
    
    ## DEFAULT
    addFontFolder( os.path.abspath("./../../fonts") )
    
    ## UBUNTU
    base = "/usr/share/fonts/truetype"
    for path in os.listdir(base):
        subject = os.path.join(base,path)
        if os.path.isdir(subject):
            addFontFolder( subject )
    
    ## WINDOWS
    addFontFolder( "c:\windows\fonts" )
    
    ## MACOS
    
###
##
##
def _removeWindow(window):
    global __windows
    __windows.remove(window)
    
###
##
##
def _addWindow(window):
    global __windows
    __windows.insert(0,window)
    
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
    global __themeFolder, __theme
    themeFile = os.path.join(__themeFolder,name, "theme.json")
    with open( themeFile) as sFile:
        themaData = sFile.read()
    themeData = json.loads(themaData)
    __theme == None
    theme = getTheme(themeData)
    theme.selectTheme(name)

### Returns the Theme instance. If necassary it is created.
##
##  @return             A Theme object.
##
def getTheme(themeData = None):
    global __theme,__themeFolder
    if __theme == None:
        if themeData["class"] == "biui.ThemeImg":
            print("1")
            __theme = ThemeImg( __themeFolder )
        elif themeData["class"] == "biui.Theme":
            print("2")
            __theme = Theme( __themeFolder )
    return __theme

### The biui main loop.
##  Cares about event distribution and drawing of the GUI.
##
##  @return        True as long as a window is open.
##
def main():
    global __windows
    
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
        elif event.type == sdl2.SDL_MOUSEBUTTONDOWN:
            ##print("SDL_MOUSEBUTTONDOWN")
            for w in __windows:
                if w.id ==  event.window.windowID:
                    w.sdlOnMouseDown(event)
                    break

        elif event.type == sdl2.SDL_MOUSEBUTTONUP:
            ##print("SDL_MOUSEBUTTONUP")
            for w in __windows:
                if w.id ==  event.window.windowID:
                    w.sdlOnMouseUp(event)
                    break
                                
        elif event.type == sdl2.SDL_MOUSEWHEEL:
            ##print("SDL_MOUSEWHEEL")
            for w in __windows:
                if w.id ==  event.window.windowID:
                    w.sdlOnMouseWheel(event)
                    break

        elif event.type == sdl2.SDL_MOUSEMOTION:
            ##print("SDL_MOUSEMOTION")
            for w in __windows:
                if w.id ==  event.window.windowID:
                    w.sdlOnMouseMotion(event)
                    break

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
            for w in __windows:
                if w.id ==  event.window.windowID:
                    w._onKeyDown(event)
                    break
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
            
            ##print("windowEvent::"+str(event.window.windowID))
            for w in __windows:
                if w.id ==  event.window.windowID:
                    w.sdlOnWindowEvent(event)
                    break
            
            
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
        ##                                                  Drag´n Drop
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
    
    for w in __windows:
        w._redraw()
        
    return len(__windows) > 0


