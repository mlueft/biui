import sdl2
import ctypes

###
##
##
class DL:
    
    ##_pixelFormat = sdl2.SDL_AllocFormat( sdl2.SDL_PIXELFORMAT_RGBA32 )
    _pixelFormat = sdl2.SDL_PIXELFORMAT_RGBA32
    
    def __init__(self):
        pass

    def init():
        sdl2.ext.init()
    
    def quit():
        pass
    
    def getWindowId(window):
        return sdl2.SDL_GetWindowID(window)
    
    def renderCopy(renderer,texture,srect,trect):
            src = sdl2.SDL_Rect(int(srect[0]),int(srect[1]),int(srect[2]),int(srect[3]))
            tgt = sdl2.SDL_Rect(int(trect[0]),int(trect[1]),int(trect[2]),int(trect[3]))
            sdl2.render.SDL_RenderCopy(renderer,texture,src,tgt)
    
    def createWindow(title = "", size=(800,600), flags = None):
        if flags == None:
            flags = sdl2.SDL_WINDOW_RESIZABLE
            
        res = sdl2.SDL_CreateWindow( None, 100, 100, size[0], size[1], flags )
        return res
    
    def drawRect(renderer,texture,color,rect,fill=0):
        
        tmpT = sdl2.SDL_GetRenderTarget(renderer)

        sdl2.SDL_SetRenderTarget(renderer,texture)
        sdl2.render.SDL_SetRenderDrawColor(renderer, color[0], color[1], color[2], color[3])
        
        _rect = sdl2.SDL_Rect(
            int(rect[0]),
            int(rect[1]),
            int(rect[2]),
            int(rect[3])
        )
        if fill == 0:
            sdl2.SDL_RenderDrawRect(renderer,_rect)
        else:
            sdl2.SDL_RenderFillRect(renderer,_rect)
    
        sdl2.SDL_SetRenderTarget(renderer,tmpT)
        
    def fill(renderer,texture,color):
        tmpT = sdl2.SDL_GetRenderTarget(renderer)
        sdl2.SDL_SetRenderTarget(renderer,texture)
        sdl2.render.SDL_SetRenderDrawColor(renderer, color[0], color[1], color[2], color[3])
        sdl2.render.SDL_RenderClear(renderer)
        sdl2.SDL_SetRenderTarget(renderer,tmpT)
        
    def present(renderer):
        sdl2.SDL_RenderPresent(renderer)
        
    def createRenderer(window,index=-1,flags=sdl2.SDL_RENDERER_ACCELERATED):
    ##def createRenderer(window,index=-1,flags=sdl2.SDL_RENDERER_SOFTWARE):
        result = sdl2.SDL_CreateRenderer(window,index,flags)
        sdl2.SDL_SetRenderDrawBlendMode(result, sdl2.SDL_BLENDMODE_BLEND)
        return result
    
    def setRenderColor(renderer,r,g,b,a):
        return sdl2.render.SDL_SetRenderDrawColor(renderer, r, g, b, a)
    
    def clear(renderer):
        return sdl2.render.SDL_RenderClear(renderer);
    
    def renderPresent(renderer):
        return sdl2.SDL_RenderPresent(renderer)
    
    def createTexture(renderer,w,h):
        res = sdl2.SDL_CreateTexture(
            renderer,
            DL._pixelFormat,
            sdl2.SDL_TEXTUREACCESS_TARGET,
            int(w),
            int(h)
        )
        sdl2.SDL_SetTextureBlendMode(res,sdl2.SDL_BLENDMODE_BLEND)
        DL.fill(renderer,res,(0,0,0,0))
        return res
    
    def getTextureSize(texture):
        oWidth = ctypes.c_int()
        oHeight = ctypes.c_int()
        sdl2.SDL_QueryTexture(texture,None,None,oWidth,oHeight)
        return (0,0,oWidth.value,oHeight.value)
                
    def getWindowBorderSize(window):
        top = ctypes.c_int()
        left = ctypes.c_int()
        bottom = ctypes.c_int()
        right = ctypes.c_int()
        sdl2.SDL_GetWindowBordersSize(
            window,
            ctypes.byref(top),
            ctypes.byref(left),
            ctypes.byref(bottom),
            ctypes.byref(right)
        )
        return top.value,left.value,bottom.value,right.value
    
    def getWindowPos(window):
        x = ctypes.c_int()
        y = ctypes.c_int()
        sdl2.SDL_GetWindowPosition(
            window,
            ctypes.byref(x),
            ctypes.byref(y)
        )
        return x.value,y.value
    
    def setWindowPos(window,x,y):
        sdl2.SDL_SetWindowPosition(window,x,y)

    def getWindowSize(window):
        width = ctypes.c_int()
        height = ctypes.c_int()
        sdl2.SDL_GetWindowSize(
            window,
            ctypes.byref(width),
            ctypes.byref(height)
        )
        return width.value,height.value
    
    def setWindowSize(window,width,height):
        sdl2.SDL_SetWindowSize(
            window,
            width,
            height
        )
            
    def blit(renderer,tTgt,tSrc,tgtRect=None,srcRect=None):

        if srcRect == None:
            srcRect = DL.getTextureSize(tSrc)
        
        if tgtRect == None:
            tgtRect = srcRect
                
        tmpT = sdl2.SDL_GetRenderTarget(renderer)
        src = sdl2.SDL_Rect(
            int(srcRect[0]),
            int(srcRect[1]),
            int(srcRect[2]),
            int(srcRect[3])
        )
        
        tgt = sdl2.SDL_Rect(
            int(tgtRect[0]),
            int(tgtRect[1]),
            int(tgtRect[2]),
            int(tgtRect[3])
        )
        
        ##print( srcRect )
        ##print( tgtRect )
        sdl2.SDL_SetRenderTarget(renderer,tTgt)
        sdl2.render.SDL_RenderCopy(renderer,tSrc,src,tgt)
        sdl2.SDL_SetRenderTarget(renderer,tmpT)
    
    def setWindowTitle(window,title):
        bTitle = title.encode('utf-8')
        sdl2.SDL_SetWindowTitle(window,bTitle)
        
    def loadImage(fileName,renderer):
        img = sdl2.ext.load_img(fileName)
        texture = sdl2.SDL_CreateTextureFromSurface(renderer,img)
        sdl2.SDL_SetTextureBlendMode(texture,sdl2.SDL_BLENDMODE_BLEND)
        sdl2.SDL_FreeSurface(img)
        return texture
    
    def free(obj):
        if obj == None:
            return
        elif type(obj.contents) == sdl2.SDL_Renderer:
            sdl2.SDL_DestroyRenderer(obj)
            return 
        elif type(obj.contents) == sdl2.SDL_Window:
            sdl2.SDL_DestroyWindow(obj)
            return 
        elif type(obj.contents) == sdl2.SDL_Texture:
            sdl2.SDL_DestroyTexture(obj)
            return 
        else:
            print( "Objekttype in free() nicht erkannt:"+str(type(obj)))
    