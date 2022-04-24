import os
from time import time
import pygame
from pygame import surface

import biui.Event
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

Event = biui.Event.Event
MouseEvent = biui.MouseEvent.MouseEvent
KeyEvent = biui.KeyEvent.KeyEvent
EventTypes = biui.EventTypes.EventTypes
EventManager = biui.EventManager.EventManager
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

#
__clickTime = 0.25
#
__themeFolder = "themes"

# Stores the Instance of Theme.
__theme = None

# Defines if all directy rects are drawn on screen.
# For debug use. This makes everything slower.
__SHOWUPDATEBOXES = False

# Stores if pygame is initialized.
__pygame_initialized__ = False

# Stores the last known mouse position
__lastMousePos = None

## Stored a reference to the Widget the mouse is over.
__hoverWidget = None

## Stores all window objects.
#  Pygame allows just one window.
__windowSurfaces = []

# Stores the time of the mouseDown event.
__mouseDownTime = None

## Initializes pygame. Can be called more than once.
#  It takes care about multiple calls.
#
def initPyGame():
    global __pygame_initialized__
    if __pygame_initialized__ == True:
        return 
    pygame.init()
    __pygame_initialized__ = True
 
## Creates a pygame window object and returns it.
#  It for internal use only. Don't call it.
#
#  @param window        A biui.Window.
#  @return              a pygame window surface.
#
def createWindow(window):
    global __windowSurfaces
    biui.initPyGame()
    sf = pygame.display.set_mode( window.size, pygame.RESIZABLE, vsync=1 )
    return sf

## Creates a pygame surface and returns it.
#  It is for internal use only. Don't call it.
#
#  @param size          A tuple representing the size ofthe surface.
#  @return              A pygame surface
#
def createSurface(size):
    biui.initPyGame()
    sf = pygame.surface.Surface(size)
    sf = sf.convert_alpha()
    sf.fill( pygame.Color(0, 0, 0, 0) )
    return sf

def _addWindow(window):
    __windowSurfaces.insert(0,window)

## Returns the Widget at the given position.
#  Currently the function doesn't care about
#  the window, beecause there is just one.
#
#  @param pos               A tuple representing a position.
#  @return                  A Widget object
#
def __getChildAt(pos):
    global __windowSurfaces
    
    for w in __windowSurfaces:
        return w.getChildAt(pos)

## Returns a defaault value if value is None
#  If value is not None value is returned.
#  Otherwise default is returned.
#
#  @param value      A python literal.
#  @param default    A default value.
#  @return           vValue or default.
#
def default(value,default):
    if value != None:
        return value
    return default

##
#
#
def getMousePosition():
    return biui.__lastMousePos

##
#
#
def selectTheme(name="default"):
    theme = getTheme()
    theme.selectTheme(name)

## Returns the Theme instance. If necassary it is created.
#
#  @return             A Theme object.
#
def getTheme():
    global __theme
    if __theme == None:
        __theme = biui.Theme.Theme( os.path.join(os.getcwd(),__themeFolder) )
        selectTheme()
    return __theme

 
## The biui main loop.
#  Cares about event distribution and drawing of the GUI.
#
def main():
    global __windowSurfaces, __hoverWidget, __mouseDownTime, __clickTime
        
    # ++++++++++++++++++++++++++++++++++++++++++++++
    #                                 Event handling
    # ++++++++++++++++++++++++++++++++++++++++++++++
    events =  pygame.event.get()

    for event in events:
        
        #
        # Mouse events
        #
        # Mouse events are send directly to the widget.
        #
        if event.type == pygame.MOUSEMOTION:
            biui.__lastMousePos = event.pos
            bStates = pygame.mouse.get_pressed(num_buttons=5)
            receiver = biui.__getChildAt(event.pos)
            ev = biui.MouseEvent(receiver,bStates,event.pos,0,0)
            if receiver != __hoverWidget:
                if __hoverWidget != None:
                    evLeave = biui.MouseEvent(__hoverWidget,bStates,event.pos,0,0)
                    for w in __windowSurfaces:
                        w._onMouseLeave(evLeave)
                __hoverWidget = receiver
                __hoverWidget._onMouseEnter(ev)
            else:
                for w in __windowSurfaces:
                    w._onMouseMove(ev)

            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Filter wheel action.
            if event.button not in [4,5]:
                __mouseDownTime = time()
                bStates = pygame.mouse.get_pressed(num_buttons=5)
                receiver = biui.__getChildAt(event.pos)
                ev = biui.MouseEvent(receiver,bStates,event.pos,0,0)
                for w in __windowSurfaces:
                    w._onMouseDown(ev)
                    
        elif event.type == pygame.MOUSEBUTTONUP:
            # Filter wheel action.
            if event.button not in [4,5]:
                #print(time()-__mouseDownTime)                
                bStates = pygame.mouse.get_pressed(num_buttons=5)
                receiver = biui.__getChildAt(event.pos)
                ev = biui.MouseEvent(receiver,bStates,event.pos,0,0)
                if time()-__mouseDownTime < __clickTime:
                    for w in __windowSurfaces:
                        w._onMouseClick(ev)

                for w in __windowSurfaces:
                    w._onMouseUp(ev)
                        
        elif event.type == pygame.MOUSEWHEEL:
            mpos = pygame.mouse.get_pos()
            bStates = pygame.mouse.get_pressed(num_buttons=5)
            receiver = biui.__getChildAt(mpos)
            ev = biui.MouseEvent(receiver,bStates,mpos,event.x,event.y)
            for w in __windowSurfaces:
                w._onMouseWheel(ev)
            
            
        #
        # Keyboard events
        #
        # Keyboard events are send throw the DOM structure.
        #
        elif event.type == pygame.KEYDOWN:
            #print( "keydown: "+ str(event) )
            for w in __windowSurfaces:
                ev = biui.KeyEvent(
                    w,
                    event.unicode,
                    event.key,
                    event.scancode,
                    event.mod
                )
                w._onKeyDown(ev)
        elif event.type == pygame.KEYUP:
            #print( "keyup: "+ str(event) )
            for w in __windowSurfaces:
                ev = biui.KeyEvent(
                    w,
                    event.unicode,
                    event.key,
                    event.scancode,
                    event.mod
                )        
                w._onKeyUp(ev)
        elif event.type == pygame.TEXTINPUT:
            #print( "textinput: "+ str(event) )
            for w in __windowSurfaces:
                ev = biui.KeyEvent(
                    w,
                    event.text
                )            
                w._onTextInput(ev)
            
            
        #
        # Window events
        # We have to find the focused window.
        # Currently we have just one!
        #
        # Window events are send directly to the window.
        #
        elif event.type == pygame.WINDOWLEAVE:
            for w in __windowSurfaces:
                w._onWindowLeave(biui.Event(w))
        elif event.type == pygame.WINDOWENTER:
            for w in __windowSurfaces:
                w._onWindowEnter(biui.Event(w))
        elif event.type == pygame.ACTIVEEVENT:
            for w in __windowSurfaces:
                w._onWindowFocus(biui.Event(w))
        elif event.type == pygame.WINDOWFOCUSLOST:
            for w in __windowSurfaces:
                w._onWindowFocusLost(biui.Event(w))
        elif event.type == pygame.WINDOWHIDDEN:
            for w in __windowSurfaces:
                w._onWindowHidden(biui.Event(w))
        elif event.type == pygame.WINDOWMINIMIZED:
            for w in __windowSurfaces:
                w._onWindowMinimized(biui.Event(w))
        elif event.type == pygame.WINDOWRESTORED:
            for w in __windowSurfaces:
                w._onWindowRestored(biui.Event(w))
        elif event.type == pygame.WINDOWSHOWN:
            for w in __windowSurfaces:
                w._onWindowShown(biui.Event(w))
        elif event.type == pygame.WINDOWFOCUSGAINED:
            for w in __windowSurfaces:
                w._onWindowFocusGained(biui.Event(w))
        elif event.type == pygame.WINDOWTAKEFOCUS:
            for w in __windowSurfaces:
                w._onWindowTakeFocus(biui.Event(w))
        elif event.type == pygame.WINDOWCLOSE:
            for w in __windowSurfaces:
                w._onWindowClose(biui.Event(w))
        elif event.type == pygame.WINDOWMAXIMIZED:
            for w in __windowSurfaces:
                w._onWindowMaximized(biui.Event(w))
        elif event.type == pygame.WINDOWMOVED:
            for w in __windowSurfaces:
                w._onWindowMoved(biui.Event(w))
        elif event.type == pygame.WINDOWSIZECHANGED:
            for w in __windowSurfaces:
                w.width = event.x
                w.height = event.y
                w._onWindowSizeChanged(biui.Event(w))
        elif event.type == pygame.WINDOWRESIZED:
            for w in __windowSurfaces:
                w.width = event.x
                w.height = event.y
                w._onWindowResized(biui.Event(w))
        elif event.type == pygame.WINDOWEXPOSED:
            for w in __windowSurfaces:
                w._onWindowExposed(biui.Event(w))
        elif event.type == pygame.VIDEORESIZE:
            pass
        elif event.type == pygame.VIDEOEXPOSE:
            pass
              
              
        #
        # MISC
        #
        elif event.type == pygame.QUIT:
            for w in __windowSurfaces:
                w._onWindowExposed(biui.Event(w))
            return False
        
        
        #
        # Else
        #
        else:
            #print("Event: "+ str(pygame.event.event_name(event.type)))
            pass
            
            
    # ++++++++++++++++++++++++++++++++++++++++++++++
    #                                     Redraw GUI
    # ++++++++++++++++++++++++++++++++++++++++++++++
    dr = []
    for w in __windowSurfaces:
        w._redraw()
        dr += w._getDirtyRectangles()
        
        if __SHOWUPDATEBOXES:
            for r in dr:
                pygame.draw.rect(w._getSurface(),(255,0,0),r,1)
                #pygame.display.update()
    
    if len(dr) >0:            
        pygame.display.update(dr)
    
    return True