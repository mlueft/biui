import sys
from sdl2.render import SDL_CreateTextureFromSurface
sys.path.append('./../')

import sdl2
import sdl2dll
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

    fontFile0 = "../../fonts/ostrich-sans-regular.ttf"
    fontFile1 = "../../fonts/ostrich-sans-bold.ttf"
    size = 25
    color = (255,255,255,128)
    
    font0 = sdl2.ext.ttf.FontTTF( fontFile0, size, color )
    font1 = sdl2.ext.ttf.FontTTF( fontFile1, size, color )
    
    
    i = 0
    while True:
        
        biui.DL.fill(renderer,texturew,(128,128,128,0))
        
        surface = font0.render_text("Hello world!")
        texture = sdl2.SDL_CreateTextureFromSurface(renderer,surface)
        biui.DL.blit( renderer, texturew, texture,(0,0,100,100),None )
        sdl2.SDL_FreeSurface(surface)
        sdl2.SDL_DestroyTexture(texture)
        
        surface = font1.render_text("Hello world!")
        texture = sdl2.SDL_CreateTextureFromSurface(renderer,surface)
        biui.DL.blit( renderer, texturew, texture,(0,120,100,100),None )
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
        
    font.close()
    
init()
main()
print("fertig")