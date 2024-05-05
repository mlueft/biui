import biui
import ctypes

import sdl2
import sdl2dll
import sdl2.sdlttf
from sdl2.pixels import SDL_Color

from biui.Events import EventManager
from biui.Events import Event
from biui.Enum import Direction

###
##
##
class Font():
    
    ###
    ##
    ##
    def __init__(self,fileName = None, size = 20 ):
        
        if fileName == None:
            fileName = biui.getDefaultFont()
        
        ##
        self._font = sdl2.sdlttf.TTF_OpenFont(
            ctypes.c_char_p(bytes(fileName, 'utf-8')),
            ctypes.c_int(size)
        )
        self._direction = None
        self.direction = Direction.LTR
        ##
        self.onSizeChanged = EventManager()
        
    ### Closes the loadedFont.
    ##
    ##    
    def close(self):
        sdl2.sdlttf.TTF_CloseFont(self._font)
    
    ### Get the font family name.
    ##
    ##
    @property   
    def familyName(self):
        result = sdl2.sdlttf.TTF_FontFaceFamilyName(self._font)
        return result.decode('utf-8')
    
    ### Get the font style name.
    ##
    ##
    @property   
    def styleName(self):
        result = sdl2.sdlttf.TTF_FontFaceStyleName(self._font)
        return result.decode('utf-8')

    ### Get the font ascent.
    ##
    ##
    @property   
    def ascent(self):
        return sdl2.sdlttf.TTF_FontAscent(self._font)  
        
    ### Get the font descent.
    ##
    ##
    @property   
    def descent(self):
        return sdl2.sdlttf.TTF_FontDescent(self._font)
    
    ### gets the font size.
    ##
    @property
    def size(self):
        return sdl2.sdlttf.TTF_FontHeight(self._font)
         
    ### Set the font size.
    ##
    ##   @param  value   (float)
    ##
    @size.setter   
    def size(self, value):
        sdl2.sdlttf.TTF_SetFontSize(
            self._font,
            ctypes.c_int(value)
        )
        self.onSizeChanged.provoke(Event(self))
    
    
    ### Get the font line spacing.
    ##
    ##
    @property   
    def lineSpacing(self):
        return sdl2.sdlttf.TTF_FontLineSkip(self._font)
    
    ### Returns the font hinting.
    ##
    ##
    @property
    def hinting(self):
        return sdl2.sdlttf.TTF_GetFontHinting(self._font)
    
    ### Sets the font hinting.
    ##
    ##  @param value       An integer value.
    ##
    @hinting.setter
    def hinting(self, value):
        sdl2.sdlttf.TTF_SetFontHinting(
            self._font,
            ctypes.c_int(value)
        )
        
    ### Returns the font hinting.
    ##
    ##
    @property
    def kerning(self):
        return sdl2.sdlttf.TTF_GetFontKerning(self._font)==1
    
    ### Sets the font kerning.
    ##
    ##   @param  value   (bool)
    ##
    @kerning.setter
    def kerning(self, value):
        sdl2.sdlttf.TTF_SetFontKerning(
            self._font,
            ctypes.c_int(value)
        )
    

    ### Returns the font style.
    ##
    ##
    @property
    def style(self):
        return sdl2.sdlttf.TTF_GetFontStyle(self._font)
    
    ### Sets the font style.
    ##
    ##   @param  value   (int)
    ##
    @style.setter
    def style(self, value):
        sdl2.sdlttf.TTF_SetFontStyle(
            self._font,
            ctypes.c_int(value)
        )
    
    ### Gets the font outline.
    ##
    ##
    ##
    @property
    def outline(self):
        return sdl2.sdlttf.TTF_GetFontOutline(self._font)
    
    ### Sets the font outline.
    ##
    ##   @param  value   (int)
    ##
    @outline.setter
    def outline(self, value):
        sdl2.sdlttf.TTF_SetFontOutline(
            self._font,
            ctypes.c_int(value)
        )

    ### Gets the font alignment.
    ##
    ##
    ##
    @property
    def alignment(self):
        return sdl2.sdlttf.TTF_GetFontWrappedAlign(self._font)
    
    ### Sets the font alignment.
    ##  TODO: Build ENUM-Class
    ##
    ##   @param  value
    ##
    @alignment.setter
    def alignment(self, value):
        sdl2.sdlttf.TTF_SetFontWrappedAlign(
            self._font,        ##TODO: UseENUM-Class
            ctypes.c_int(value)
        )
            
    ### Gets the font direction.
    ##  
    @property
    def direction(self):
        return self._direction
        
    ### Sets the font direction.
    ##
    ##   @param  value   (int)
    ##
    @direction.setter
    def direction(self, value):
        self._direction = value
        sdl2.sdlttf.TTF_SetFontDirection(
            self._font,
            ctypes.c_int(value)
        )

    ### Gets width and height of the given text
    ##  in pixels.
    ##
    ##   @param text
    ##
    def getRenderSize(self,text):
        
        w = ctypes.c_int()
        h = ctypes.c_int()
        sdl2.sdlttf.TTF_SizeUTF8(
            self._font,
            ctypes.c_char_p(bytes(str(text), 'utf-8')),
            ctypes.byref(w),
            ctypes.byref(h)
        )
        return (w.value,h.value)
    
    ### Measures how much of the given text
    ##  fits in the given width 
    ##
    ##   @param text
    ##   @param width
    ##   @return       count of characters and extent
    ##
    def measure(self,text,width):
        extent = ctypes.c_int()
        count = ctypes.c_int()
        sdl2.sdlttf.TTF_MeasureUTF8(
            self._font,
            ctypes.c_char_p(bytes(text, 'utf-8')),
            ctypes.c_int(width),
            ctypes.byref(extent),
            ctypes.byref(count)
        )
        return (count.value,extent.value)
        
    ### Renders the given text and returns a new texture
    ##  width the rendered text.
    ##
    ##   @param renderer
    ##   @param text
    ##   @param color
    ##   @param wrapLength
    ##
    def render(self,renderer,text,color,wrapLength=0):
        
        color = SDL_Color(
            color.r,
            color.g,
            color.b,
            color.a
        )
        
        surface = sdl2.sdlttf.TTF_RenderUTF8_Blended_Wrapped(
            self._font,
            ctypes.c_char_p(bytes(text, 'utf-8')),
            color,
            wrapLength
        )
        texture = sdl2.SDL_CreateTextureFromSurface(renderer,surface)
        sdl2.SDL_FreeSurface(surface)
        return texture
        