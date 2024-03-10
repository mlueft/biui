import sys
sys.path.append('./../')

import ctypes
import sdl2
import sdl2dll
import sdl2.sdlttf
from sdl2.render import SDL_CreateTextureFromSurface
from sdl2.pixels import SDL_Color
import biui




def init():
    biui.init()
    biui.setThemeFolder(
        os.path.abspath(
            os.path.join(os.getcwd(),"../themes")
        )
    )

    
    sdl2.SDL_Init( sdl2.SDL_INIT_VIDEO )
    sdl2.ext.init(  )
    sdl2.sdlttf.TTF_Init()
    
def main():
    
    window = sdl2.SDL_CreateWindow( None, 100, 100, 800, 600, sdl2.SDL_WINDOW_RESIZABLE )
    renderer = sdl2.SDL_CreateRenderer(window,-1,sdl2.SDL_RENDERER_ACCELERATED)
    texturew = sdl2.SDL_CreateTexture(
            renderer,
            sdl2.SDL_PIXELFORMAT_RGBA32,
            sdl2.SDL_TEXTUREACCESS_TARGET,
            800,
            600
        )

    fontFile0 = ctypes.c_char_p( b"../../fonts/ostrich-sans-regular.ttf" )
    fontFile1 = ctypes.c_char_p( b"../../fonts/ostrich-sans-bold.ttf" )
    size = ctypes.c_int(50)
    color = SDL_Color(255,255,255,128)
    
    font0 = sdl2.sdlttf.TTF_OpenFont(fontFile0,size)
    font1 = sdl2.sdlttf.TTF_OpenFont(fontFile1,size)
    
    ##sdl2.sdlttf.TTF_SetFontHinting(font0,0)
    ##sdl2.sdlttf.TTF_SetFontKerning(font0,0)
    ##sdl2.sdlttf.TTF_SetFontOutline(font0,0)
    ##sdl2.sdlttf.TTF_SetFontSize(font0,25)
    ##sdl2.sdlttf.TTF_SetFontStyle(font0, 
    ##    sdl2.sdlttf.TTF_STYLE_UNDERLINE | sdl2.sdlttf.TTF_STYLE_ITALIC
    ##)
    
    print( b'TTF_FontFaceFamilyName : '); print( sdl2.sdlttf.TTF_FontFaceFamilyName(font0) )
    print( b'TTF_FontFaces          : '); print( sdl2.sdlttf.TTF_FontFaces(font0) )
    print( b'TTF_FontFaceStyleName  : '); print( sdl2.sdlttf.TTF_FontFaceStyleName(font0) )
    print( b'TTF_GetFontStyle       : '); print( sdl2.sdlttf.TTF_GetFontStyle(font0) )
    print( b'TTF_FontFaceIsFixedWidth       : '); print( sdl2.sdlttf.TTF_FontFaceIsFixedWidth(font0) )
    print( b'TTF_FontHeight       : '); print( sdl2.sdlttf.TTF_FontHeight(font0) )
    print( b'TTF_FontLineSkip       : '); print( sdl2.sdlttf.TTF_FontLineSkip(font0) )
    
    
    
    i = 0
    while True:
        
        biui.DL.fill(renderer,texturew,(128,128,128,0))
        
        text = b'Hello world!'
        
        surface = sdl2.sdlttf.TTF_RenderUTF8_Blended(font0,ctypes.c_char_p( text ),color)
        texture = sdl2.SDL_CreateTextureFromSurface(renderer,surface)
        size0 = biui.DL.getTextureSize(texture)
        biui.DL.blit( renderer, texturew, texture )
        sdl2.SDL_FreeSurface(surface)
        sdl2.SDL_DestroyTexture(texture)
        
        surface = sdl2.sdlttf.TTF_RenderUTF8_Blended(font1,ctypes.c_char_p( text ),color)
        texture = sdl2.SDL_CreateTextureFromSurface(renderer,surface)
        
        size1 = biui.DL.getTextureSize(texture)
        biui.DL.blit( renderer, texturew, texture,(0,size0[3],size1[2],size1[3]) )
        sdl2.SDL_FreeSurface(surface)
        sdl2.SDL_DestroyTexture(texture)
                
        biui.DL.renderCopy(
            renderer,
            texturew,
            (0,0,800,600),
            (0,0,800,600)
        )
        
        biui.DL.present(renderer)
        i += 1
        
    ##sdl2.sdlfft.
    
init()
main()
print("fertig")