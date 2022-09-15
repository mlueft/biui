
import sdl2
import ctypes
from sdl2.error import SDL_GetError


sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)

dMode = sdl2.SDL_DisplayMode()
if sdl2.SDL_GetDesktopDisplayMode(0,dMode) != 0:
    print( SDL_GetError() )
print( dMode.w,dMode.h)