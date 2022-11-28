import ctypes
import sdl2
from sdl2.events import SDL_DISABLE, SDL_ENABLE

class Mouse:
    
    def __init__(self):
        pass
    
    ### Returns the mouse position on screen.
    ##
    ##
    def getPosition():
        x = ctypes.c_int()
        y = ctypes.c_int()
        sdl2.SDL_GetGlobalMouseState(ctypes.byref(x),ctypes.byref(y));
        return (x.value,y.value)
    
    ###
    ##
    ##
    def setPosition(x,y):
        sdl2.SDL_WarpMouseGlobal(x,y)

    ###
    ##
    ##
    def hide():
        sdl2.SDL_ShowCursor(SDL_DISABLE)
    ###
    ##
    ##
    def show():
        sdl2.SDL_ShowCursor(SDL_ENABLE)
        
        
        
        