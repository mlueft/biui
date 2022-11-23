import biui

### TODO: Does a file based cache make sense?
##        So we do not have to recompose all
##        images at each program start.
##
class ImageLibrary():
    
    def __init__(self):
        ## Stores all loaded or processed images.
        self.__images = {}
        ## Controls if resized images are cached.
        self.cacheImagesScaled = True
        ## Controls if original images are cached.
        self.cacheImagesOriginal = True
        ## Controls if I9 images are cached.
        self.cacheImagesI9 = True
        
    ### Returns an I9 of the given width and height.
    ##
    ##  @param renderer
    ##  @param name        Filename as string.
    ##  @param width       Width of the resulting image.
    ##  @param height      Height of the resulting image.
    ##
    def getI9(self,renderer,name,width,height):

        hashName = str(hash(name))[1:]
        
        ## looking for already stored size
        key = hashName+"_"+str(width)+"x"+str(height)
        if key in self.__images:
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
    
        tgt = biui.DL.createTexture(renderer,width,height)
        
        tl = self.getImage(renderer,names[0])
        sizeTL = biui.DL.getTextureSize(tl)
        biui.DL.blit(
            renderer,
            tgt,
            tl,
            sizeTL,
            sizeTL         
        )
        
        tr = self.getImage(renderer,names[2])
        sizeTR = biui.DL.getTextureSize(tr)
        biui.DL.blit(
            renderer,
            tgt,
            tr,
            (width-sizeTR[2],0,sizeTR[2],sizeTR[3])
        )
        
        sizeTC = (0,0,width-sizeTL[2]-sizeTR[2],sizeTL[3])
        tc = self.getImage(renderer,names[1],sizeTC[2],sizeTC[3])
        biui.DL.blit(
            renderer,
            tgt,
            tc,
            (sizeTL[2],0,sizeTC[2],sizeTC[3]),
            sizeTC
        )
        
        bl = self.getImage(renderer,names[6])
        sizeBL = biui.DL.getTextureSize(bl)
        biui.DL.blit(
            renderer,
            tgt,
            bl,
            (0,height-sizeBL[3],sizeBL[2],sizeBL[3]),
            sizeBL
        )
        
        br = self.getImage(renderer,names[8])
        sizeBR = biui.DL.getTextureSize(br)
        biui.DL.blit(
            renderer,
            tgt,
            br,
            (width-sizeBR[2],height-sizeBR[3],sizeBR[2],sizeBR[3]),
            sizeBR
            
        )
        
        sizeBR = (0,0,width-sizeBL[2]-sizeBR[2],sizeBL[3])
        bc = self.getImage(renderer,names[7],sizeBR[2],sizeBR[3])
        biui.DL.blit(
            renderer,
            tgt,
            bc,
            (sizeBL[2],height-sizeBR[3],sizeBR[2],sizeBR[3]),
            sizeBR
        )

        sizeCL = (0,0,sizeTL[2],height-sizeTL[3]-sizeBL[3])
        cl = self.getImage(renderer,names[3],sizeCL[2],sizeCL[3])
        biui.DL.blit(
            renderer,
            tgt,
            cl,
            (0,sizeTL[3],sizeCL[2],sizeCL[3]),
            sizeCL
        )
        
        sizeCR = (0,0,sizeTR[2],height-sizeTR[3]-sizeBR[3])
        cr = self.getImage(renderer,names[5],sizeCR[2],sizeCR[3])
        biui.DL.blit(
            renderer,
            tgt,
            cr,
            (width-sizeCR[2],sizeTR[3],sizeCR[2],sizeCR[3]),
            sizeCR
        )
        
        sizeCC = (0,0,width-sizeTL[2]-sizeTR[2],height-sizeTL[3]-sizeBL[3])
        cc = self.getImage(renderer,names[4],sizeCC[2],sizeCC[3])
        biui.DL.blit(
            renderer,
            tgt,
            cc,
            (sizeTL[2],sizeTL[3],sizeCC[2],sizeCC[3]),
            sizeCC
        )
        
        ## store original
        if self.cacheImagesI9:
            self.__images[key] = tgt
                
        return tgt
        
    ### Loades the given image and returns it scaled
    ##  to the given width and height.
    ##  If width and height are not defined.
    ##  the size of the original image is used.
    ##
    ##
    def getImage(self,renderer,fileName,width=0,height=0):
        
        ## we cut off the leading "-"
        ## TODO: We should not use the absolute path.
        ##       the themename and the filename would
        ##       be great.
        hashName = str(hash(fileName))[1:]
        
        ## looking for already stored size
        key = hashName+"_"+str(width)+"x"+str(height)
        if key in self.__images:
            return self.__images[key]
        
        ## load original
        imageOriginal = None
        key = hashName+"_0x0"
        if key in self.__images:
            imageOriginal = self.__images[key]
            
        if imageOriginal == None:

            ## load original
            imageOriginal = biui.DL.loadImage(fileName,renderer)
            
            ## TODO: We need to convert all images to the right format
            ##imageOriginal = sdl2.SDL_ConvertSurface(imageOriginalTmp, biui._pixelFormat ,0)
            
            if not imageOriginal:
                print(sdl2.SDL_GetError())
            
            ## store original
            if self.cacheImagesOriginal:
                self.__images[key] = imageOriginal
            
            ## if size is not given the original is ment.
            if width < 1 and height < 1:
                return imageOriginal
            
        ## resize it
        key = hashName+"_"+str(width)+"x"+str(height)
        
        ## resize a copy of  the original
        imageScaled = biui.DL.createTexture(renderer,width,height)
        
        biui.DL.blit(
            renderer,
            imageScaled,
            imageOriginal,
            (0,0,width,height)
        )
        
        ##if error < 0:
        ##    print(sdl2.SDL_GetError())
        ##    quit()
        
        ## store scaled copy
        if self.cacheImagesScaled:
            self.__images[key] = imageScaled
        
        return imageScaled
    
    ### Releases all chached images.
    ##
    ##
    def clearCache(self):
        for i  in self.__images.keys():
            img = self.__images[i]
            biui.DL.free(img)
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
            biui.DL.free(img)
            