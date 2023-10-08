import ctypes
import sdl2
from sdl2.events import SDL_DISABLE, SDL_ENABLE

### A singleton class to handle properties of the mouse pointer.
##
##
class Mouse(object):
    
    ###
    ##
    ##
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Mouse, cls).__new__(cls)
        return cls.instance

    ### Returns the mouse position on screen.
    ##
    ##  @return     A tuple with x and y position.
    ##
    @property
    def position(self):
        x = ctypes.c_int()
        y = ctypes.c_int()
        sdl2.SDL_GetGlobalMouseState(ctypes.byref(x),ctypes.byref(y));
        return (x.value,y.value)
    
    ### Sets the mouse pointer to a position on the screen.
    ##
    ##  @param position       A tuple with x and y position.
    ##
    @position.setter
    def position(self,position):
        sdl2.SDL_WarpMouseGlobal(position[0],position[1])

    ### Sets the mouse pointer invisible.
    ##
    ##
    def hide(self):
        sdl2.SDL_ShowCursor(SDL_DISABLE)
        
    ### Makes the mouse pointer visible
    ##
    ##
    def show(self):
        sdl2.SDL_ShowCursor(SDL_ENABLE)
        
        
        
        