import pygame

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
from pygame import surface

EventsEvent = biui.Event.Event
MouseEvent = biui.MouseEvent.MouseEvent
KeyEvent = biui.KeyEvent.KeyEvent
EventTypes = biui.EventTypes.EventTypes
EventManager = biui.EventManager.EventManager
Window = biui.Window.Window
Pane = biui.Pane.Pane
KeyModifiers = biui.KeyModifiers.KeyMofifiers
Keys = biui.Keys.Keys
Button = biui.Button.Button

# Defines if all directy rects are drawn on screen.
# For debug use. This makes everything slower.
__SHOWUPDATEBOXES = False

# Stores if pygame is initialized.
__pygame_initialized__ = False

## Initializes pygame. Can be called more than once.
#  It takes care about multiple calls.
#
def initPyGame():
    global __pygame_initialized__
    if __pygame_initialized__ == True:
        return 
    pygame.init()
    __pygame_initialized__ = True
 
 ## Stores all window objects.
 #  Pygame allows just one window.
 #
__windowSurfaces = []

## Creates a pygame window object and returns it.
#  It for internal use only. Don't call it.
#
#  @param window        A biui.Window.
#  @return              a pygame window surface.
#
def createWindow(window):
    global __windowSurfaces
    biui.initPyGame()
    sf = pygame.display.set_mode( window.getSize(), pygame.RESIZABLE, vsync=1 )
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
    return sf

def _addWindow(window):
    __windowSurfaces.append(window)

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

## Stored a reference to the Widget the mouse is over.
#
#
__hoverWidget = None

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

## Stores the Instance of Theme.
#
#
__theme = None

## Returns the Theme instance. If necassary it is created.
#
#  @return             A Theme object.
#
def getTheme():
    global __theme
    if __theme == None:
        __theme = biui.Theme.Theme()
        
    return __theme

 
## The biui main loop.
#  Cares about event distribution and drawing of the GUI.
#
def main():
    global __windowSurfaces, __hoverWidget
        
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
            bStates = pygame.mouse.get_pressed(num_buttons=5)
            ev = biui.MouseEvent(bStates,event.pos,0,0)
            receiver = biui.__getChildAt(event.pos)
            if receiver != __hoverWidget:
                if __hoverWidget != None:
                    __hoverWidget.onMouseLeave(ev)
                __hoverWidget = receiver
                __hoverWidget.onMouseEnter(ev)
            else:
                receiver.onMouseMove(ev)

            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Filter wheel action.
            if event.button not in [4,5]:
                bStates = pygame.mouse.get_pressed(num_buttons=5)
                ev = biui.MouseEvent(bStates,event.pos,0,0)
                receiver = biui.__getChildAt(event.pos)
                receiver.onMouseDown(ev)
            
        elif event.type == pygame.MOUSEBUTTONUP:
            # Filter wheel action.
            if event.button not in [4,5]:
                bStates = pygame.mouse.get_pressed(num_buttons=5)
                ev = biui.MouseEvent(bStates,event.pos,0,0)
                receiver = biui.__getChildAt(event.pos)
                receiver.onMouseUp(ev)
            
        elif event.type == pygame.MOUSEWHEEL:
            mpos = pygame.mouse.get_pos()
            bStates = pygame.mouse.get_pressed(num_buttons=5)
            ev = biui.MouseEvent(bStates,mpos,event.x,event.y)
            receiver = biui.__getChildAt(mpos)
            receiver.onMouseWheel(ev)
            
            
        #
        # Keyboard events
        #
        # Keyboard events are send throw the DOM structure.
        #
        elif event.type == pygame.KEYDOWN:
            #print( "keydown: "+ str(event) )
            ev = biui.KeyEvent(
                event.unicode,
                event.key,
                event.scancode,
                event.mod
            )
            for w in __windowSurfaces:
                w.onKeyDown(ev)
        elif event.type == pygame.KEYUP:
            #print( "keyup: "+ str(event) )
            ev = biui.KeyEvent(
                event.unicode,
                event.key,
                event.scancode,
                event.mod
            )        
            for w in __windowSurfaces:
                w.onKeyUp(ev)
        elif event.type == pygame.TEXTINPUT:
            #print( "textinput: "+ str(event) )
            ev = biui.KeyEvent(
                event.text
            )            
            for w in __windowSurfaces:
                w.onTextInput(ev)
            
            
        #
        # Window events
        # We have to find the focused window.
        # Currently we have just one!
        #
        # Window events are send directly to the window.
        #
        elif event.type == pygame.WINDOWLEAVE:
            for w in __windowSurfaces:
                w.onWindowLeave()
        elif event.type == pygame.WINDOWENTER:
            for w in __windowSurfaces:
                w.onWindowEnter()
        elif event.type == pygame.ACTIVEEVENT:
            for w in __windowSurfaces:
                w.onWindowFocus()
        elif event.type == pygame.WINDOWFOCUSLOST:
            for w in __windowSurfaces:
                w.onWindowFocusLost()
        elif event.type == pygame.WINDOWHIDDEN:
            for w in __windowSurfaces:
                w.onWindowHidden()
        elif event.type == pygame.WINDOWMINIMIZED:
            for w in __windowSurfaces:
                w.onWindowMinimized()
        elif event.type == pygame.WINDOWRESTORED:
            for w in __windowSurfaces:
                w.onWindowRestored()
        elif event.type == pygame.WINDOWSHOWN:
            for w in __windowSurfaces:
                w.onWindowShown()
        elif event.type == pygame.WINDOWFOCUSGAINED:
            for w in __windowSurfaces:
                w.onWindowFocusGained()
        elif event.type == pygame.WINDOWTAKEFOCUS:
            for w in __windowSurfaces:
                w.onWindowTakeFocus()
        elif event.type == pygame.WINDOWCLOSE:
            for w in __windowSurfaces:
                w.onWindowClose()
        elif event.type == pygame.WINDOWMAXIMIZED:
            for w in __windowSurfaces:
                w.onWindowMaximized()
        elif event.type == pygame.WINDOWMOVED:
            for w in __windowSurfaces:
                w.onWindowMoved()
        elif event.type == pygame.WINDOWSIZECHANGED:
            for w in __windowSurfaces:
                w.setWidth(event.x)
                w.setHeight(event.y)
                w.onWindowSizeChanged()
        elif event.type == pygame.WINDOWRESIZED:
            for w in __windowSurfaces:
                w.setWidth(event.x)
                w.setHeight(event.y)
                w.onWindowResized()
        elif event.type == pygame.WINDOWEXPOSED:
            for w in __windowSurfaces:
                w.onWindowExposed()
        elif event.type == pygame.VIDEORESIZE:
            pass
        elif event.type == pygame.VIDEOEXPOSE:
            pass
              
              
        #
        # MISC
        #
        elif event.type == pygame.QUIT:
            for w in __windowSurfaces:
                w.onWindowExposed()
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
                pygame.display.update()
                
    pygame.display.update(dr)
    
    return True