#include "pysdl2.inc"
#include "biui.inc"
import biui
import sdl2
import ctypes

### TODO: Does a file based cache make sense?
##        So we do not have to recompose all
##        images at each program start.
##
class ImageLibrary():
    
    def __init__(self):
        ## Stores all loaded or processed images.
        self.__images = {}
        
    ### Returns an I9 of the given width and height.
    ##
    ##  @param renderer
    ##  @param name        Filename as string.
    ##  @param width       Width of the resulting image.
    ##  @param height      Height of the resulting image.
    ## @param convert      Defines if a the returned surface
    ##                     is converted to a texture
    ##
    def getI9(self,renderer,name,width,height,convert=True):

        hashName = str(hash(name))[1:]
        
        ## looking for already stored size
        key = hashName+"_"+str(width)+"x"+str(height)
        if key in self.__images:
            if convert:
                return sdl2.SDL_CreateTextureFromSurface(renderer,self.__images[key])
            return self.__images[key]
        
        names = [
            name + "_tl.png",
            name + "_tc.png",
            name + "_tr.png",
            name + "_cl.png",
            name + "_cc.png",
            name + "_cr.png",
            name + "_bl.png",
            name + "_bc.png",
            name + "_br.png"
        ]
    
        PYSDL2_CREATESURFACE(width,height,tgt)
        
        tl = self.getImage(renderer,names[0],convert=False)
        PYSDL2_GETSURFACESIZE(tl,sizeTL)
        PYSDL2_BLIT(tgt,tl,sizeTL,sizeTL)
        
        tr = self.getImage(renderer,names[2],convert=False)
        PYSDL2_GETSURFACESIZE(tr,sizeTR)
        PYSDL2_BLIT(tgt,tr,(width-sizeTR[2],0,sizeTR[2],sizeTR[3]),sizeTR)
        
        sizeTC = (0,0,width-sizeTL[2]-sizeTR[2],sizeTL[3])
        tc = self.getImage(renderer,names[1],sizeTC[2],sizeTC[3],convert=False)
        PYSDL2_BLIT(tgt,tc,(sizeTL[2],0,sizeTC[2],sizeTC[3]),sizeTC)
        
        bl = self.getImage(renderer,names[6],convert=False)
        PYSDL2_GETSURFACESIZE(bl,sizeBL)
        PYSDL2_BLIT(tgt,bl,(0,height-sizeBL[3],sizeBL[2],sizeBL[3]),sizeBL)
        
        br = self.getImage(renderer,names[8],convert=False)
        PYSDL2_GETSURFACESIZE(br,sizeBR)
        PYSDL2_BLIT(tgt,br,(width-sizeBR[2],height-sizeBR[3],sizeBR[2],sizeBR[3]),sizeBR)
        
        sizeBR = (0,0,width-sizeBL[2]-sizeBR[2],sizeBL[3])
        bc = self.getImage(renderer,names[7],sizeBR[2],sizeBR[3],convert=False)
        PYSDL2_BLIT(tgt,bc,(sizeBL[2],height-sizeBR[3],sizeBR[2],sizeBR[3]),sizeBR)

        sizeCL = (0,0,sizeTL[2],height-sizeTL[3]-sizeBL[3])
        cl = self.getImage(renderer,names[3],sizeCL[2],sizeCL[3],convert=False)
        PYSDL2_BLIT(tgt,cl,(0,sizeTL[3],sizeCL[2],sizeCL[3]),sizeCL)
        
        sizeCR = (0,0,sizeTR[2],height-sizeTR[3]-sizeBR[3])
        cr = self.getImage(renderer,names[5],sizeCR[2],sizeCR[3],convert=False)
        PYSDL2_BLIT(tgt,cr,(width-sizeCR[2],sizeTR[3],sizeCR[2],sizeCR[3]),sizeCR)
        
        sizeCC = (0,0,width-sizeTL[2]-sizeTR[2],height-sizeTL[3]-sizeBL[3])
        cc = self.getImage(renderer,names[4],sizeCC[2],sizeCC[3],convert=False)
        PYSDL2_BLIT(tgt,cc,(sizeTL[2],sizeTL[3],sizeCC[2],sizeCC[3]),sizeCC)
        
        ## store original
        if BIUI_CACHE_IMAGES_I9:
            self.__images[key] = tgt
        
        if convert:
            return sdl2.SDL_CreateTextureFromSurface(renderer,tgt)
            
        return tgt
        
    ### Loades the given image and returns it scaled
    ##  to the given width and height.
    ##  If width and height are not defined.
    ##  the size of the original image is used.
    ##
    ## @param renderer     .
    ## @param fileNAme     .
    ## @param widdth       .
    ## @param height       .
    ## @param convert      Defines if a the returned surface
    ##                     is converted to a texture
    ##
    def getImage(self,renderer,fileName,width=0,height=0,convert=True):
        
        ## we cut off the leading "-"
        ## TODO: We should not use the absolute path.
        ##       the themename and the filename would
        ##       be great.
        hashName = str(hash(fileName))[1:]
        
        ## looking for already stored size
        key = hashName+"_"+str(width)+"x"+str(height)
        if key in self.__images:
            if convert:
                ## convert to texture
                return sdl2.SDL_CreateTextureFromSurface(renderer,self.__images[key])
            return self.__images[key]
        
        ## load original
        imageOriginal = None
        key = hashName+"_0x0"
        if key in self.__images:
            imageOriginal = self.__images[key]
            
        if imageOriginal == None:

            ## load original
            PYSDL2_LOAD_IMG(fileName,renderer,imageOriginal)
            
            ## TODO: We need to convert all images to the right format
            ##imageOriginal = sdl2.SDL_ConvertSurface(imageOriginalTmp, biui._pixelFormat ,0)
            
            if not imageOriginal:
                print(sdl2.SDL_GetError())
            
            ## store original
            if BIUI_CACHE_IMAGES_ORIGINAL:
                self.__images[key] = imageOriginal
            
            ## if size is not given the original is ment.
            if width < 1 and height < 1:
                if convert:
                    return sdl2.SDL_CreateTextureFromSurface(renderer,imageOriginal)
                
                return imageOriginal
            
        ## resize it
        key = hashName+"_"+str(width)+"x"+str(height)
        
        ## resize a copy of  the original
        PYSDL2_CREATESURFACE(width,height,imageScaled)
        r = sdl2.SDL_Rect(0,0,width,height)
        sdl2.SDL_BlitScaled(
            imageOriginal,
            None,
            imageScaled,
            r
        )
        
        ##if error < 0:
        ##    print(sdl2.SDL_GetError())
        ##    quit()
        
        ## store scaled copy
        if BIUI_CACHE_IMAGES_SCALED:
            self.__images[key] = imageScaled
        
        if convert:
            return sdl2.SDL_CreateTextureFromSurface(renderer,imageScaled)
        
        return imageScaled
    
    ### Releases all chached images.
    ##
    ##
    def clearCache(self):
        for i  in self.__images.keys():
            img = self.__images[i]
            PYSDL2_DESTROYIMAGE(img)
        self.__images.clear()
        
    ### Returns the number of cached images.
    ##
    ##
    def getSize(self):
        return len(self.__images)
    
    ### Just a debug funtion for development.
    ##
    ##
    def debug(self):
        print("length:"+str(len(self.__images)))
        for i  in self.__images.keys():
            print(i)
    
    ### Releases all resources.
    ##
    ##
    def quit(self):
        for i  in self.__images.keys():
            img = self.__images[i]
            PYSDL2_DESTROYIMAGE(img)
            