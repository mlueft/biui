#include "pysdl2.inc"
import sdl2
import ctypes
import biui
from biui.Widgets import Widget
 

### Base class for all container widgets.
##
##
class Image(Widget):
    
    def __init__(self):
        super().__init__()
        theme = biui.getTheme()
        self._themeBackgroundfunction = theme.drawImage
        
        self.__file = None
        self.__lockRatio = True
        self.__originalSize = None
        
        
    ### Returns the file path.
    ##
    ##  @return            A string value.
    ##
    @property
    def file(self):
        return self.__file
    
    ### Sets the file path of the image to show.
    ##  TODO: At the time file is set the img has already to be added to the window.
    ##
    ##  @param value       An string value.
    ##  @return            None
    ##
    @file.setter
    def file(self, value):
        
        if value == self.__file:
            return

        self.__file = value
        self._invalidate()
        
        ## We load the image and set width and height to 
        ## the original image size 
        theme = biui.getTheme()
        img = theme.getImageLibrary().getImage(self.window.renderer,value,0,0)
        
        PYSDL2_GETTEXTURESIZE(img,size)
        
        self.__originalSize = size
        self.width = size[2]
        self.height = size[3]
                
    ### 
    ##
    ##  @return            A boolean value.
    ##
    @property
    def lockRatio(self):
        return self.__lockRatio
    
    ### 
    ##
    ##  @param value       An boolean value.
    ##  @return            None
    ##
    @lockRatio.setter
    def lockRatio(self, value):
        
        if value == self.__lockRatio:
            return

        self.__lockRatio = value
        self._invalidate()
        
    ### @see: biui.Widget.width
    ##
    ##
    @property
    def width(self):
        return super().width
    
    ### @see: biui.Widget.width
    ##
    @width.setter     
    def width(self, value):
        if value == super().width:
            return
        super(Image,self.__class__).width.fset(self,value)
        if self.__lockRatio:
            ratio = self.__originalSize[2]/self.__originalSize[3]
            value = value*ratio
            super(Image,self.__class__).height.fset(self,value)

    ## @see: biui.Widget.height
    ##
    ##
    @property
    def height(self):
        return super().height
            
    ### @see: biui.Widget.height
    ##
    ##
    @height.setter
    def height(self, value):
        if value == super().height:
            return
        super(Image,self.__class__).height.fset(self,value)
        if self.__lockRatio:
            ratio = self.__originalSize[2]/self.__originalSize[3]
            value = value*ratio
            super(Image,self.__class__).width.fset(self,value)
            
    ###
    ##
    ##
    @property
    def renderRect(self):
        return (0,0,self._width,self._height)
    
    