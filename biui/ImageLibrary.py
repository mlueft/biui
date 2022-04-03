import pygame
import biui

## TODO: Does a file based cache make sense?
#        So we don't have to recompose all
#        images at each program start.
#
class ImageLibrary():
    
    def __init__(self):
        self.__images = {}
    
    ## Returns an I9 of the given width and height.
    #
    #
    def getI9(self,name,width,height):

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
    
        tgt = biui.createSurface((width,height))
        
        tl = self.getImage(names[0])
        tgt.blit(tl,(0,0,tl.get_width(),tl.get_height()))
        
        tr = self.getImage(names[2])
        tgt.blit(tr,(width-tr.get_width(),0,tr.get_width(),tr.get_height()))
        
        size = (width-tl.get_width()-tr.get_width(),tl.get_height())
        tc = self.getImage(names[1],size[0],size[1])
        tgt.blit(tc,(tl.get_width(),0,size[0],size[1]))
        
        
        bl = self.getImage(names[6])
        tgt.blit(bl,(0,height-bl.get_height(),bl.get_width(),bl.get_height()))
        
        br = self.getImage(names[8])
        tgt.blit(br,(width-br.get_width(),height-br.get_height(),br.get_width(),br.get_height()))
        
        size = (width-bl.get_width()-br.get_width(),bl.get_height())
        bc = self.getImage(names[7],size[0],size[1])
        tgt.blit(bc,(bl.get_width(),height-bc.get_height(),size[0],size[1]))


        size = (tl.get_width(),height-tl.get_height()-bl.get_height())
        cl = self.getImage(names[3],size[0],size[1])
        tgt.blit(cl,(0,tl.get_height(),size[0],size[1]))
        
        size = (tr.get_width(),height-tr.get_height()-br.get_height())
        cr = self.getImage(names[5],size[0],size[1])
        tgt.blit(cr,(width-cr.get_width(),tr.get_height(),size[0],size[1]))
        
        size = (width-tl.get_width()-tr.get_width(),height-tl.get_height()-bl.get_height())
        cc = self.getImage(names[4],size[0],size[1])
        tgt.blit(cc,(tl.get_width(),tl.get_height(),size[0],size[1]))
        
        return tgt
        
    ## Loades the given image and returns it scaled
    #  to the given width and height.
    #  If width and height are not defined.
    #  the size of the original image is used.
    #
    #
    def getImage(self,fileName,width=0,height=0):
        
        # we cut off the leading "-"
        # TODO: We should not use the absolute path.
        #       the themename and the filename would
        #       be great.
        hashName = str(hash(fileName))[1:]
        
        # looking for already stored size
        key = hashName+"_"+str(width)+"x"+str(height)
        if key in self.__images:
            return self.__images[key]
        
        # load original
        imageOriginal = None
        key = hashName+"_0x0"
        if key in self.__images:
            imageOriginal = self.__images[key]
            
        if imageOriginal == None:
            # load original
            imageOriginal = pygame.image.load(fileName)
            imageOriginal = imageOriginal.convert_alpha()
        
            # store original
            self.__images[key] = imageOriginal
            
            # if size isn't given the original is ment.
            if width < 1 and height < 1:
                return imageOriginal
            
        # resize it
        key = hashName+"_"+str(width)+"x"+str(height)
        
        # resize a copy of  the original
        imageScaled = pygame.transform.scale(imageOriginal, (width,height))
        imageScaled = imageScaled.convert_alpha()
        
        # store scaled copy
        self.__images[key] = imageScaled
        
        return imageScaled
    
    ## Just a debug funtion for development.
    #
    #
    def debug(self):
        print("length:"+str(len(self.__images)))
        for i  in self.__images.keys():
            print(i)
        