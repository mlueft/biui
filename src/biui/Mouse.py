import ctypes
import sdl2
from sdl2.events import SDL_DISABLE, SDL_ENABLE

class SingletonMouse(object):
    
    ###
    ##
    ##
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonMouse, cls).__new__(cls)
        return cls.instance

    ### Returns the mouse position on screen.
    ##
    ##
    @property
    def position(self):
        x = ctypes.c_int()
        y = ctypes.c_int()
        sdl2.SDL_GetGlobalMouseState(ctypes.byref(x),ctypes.byref(y));
        return (x.value,y.value)
    
    ###
    ##
    ##
    @position.setter
    def position(self,position):
        sdl2.SDL_WarpMouseGlobal(position[0],position[1])

    ###
    ##
    ##
    def hide(self):
        sdl2.SDL_ShowCursor(SDL_DISABLE)
    ###
    ##
    ##
    def show(self):
        sdl2.SDL_ShowCursor(SDL_ENABLE)
        
        
        
        