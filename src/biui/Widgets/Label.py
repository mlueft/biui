#include "biui.inc"

import biui

from biui.Widgets import Widget

class Label(Widget):
    
    def __init__(self):
        super().__init__()
        theme = biui.getTheme()
        self._themeBackgroundfunction = theme.drawLabel
        
        self.onBeforeRender.add(self.__hndOnBeforeRender)
        
        self.color = biui.Color(200,200,200,255)
        self._format = "{}"
        self._font = None
        
        self.font = biui.Font()
        self.font.size = 18
        ##
        self._autoSize = True        
        self.name = "label"
        self.value = "label"
    FUNCTIONEND
    
    ###
    ##
    ##
    def __hndOnBeforeRender(self,ev):
        
        if not self._autoSize:
            return
        
        size = self.font.getRenderSize(
            self.format.format(self.value)
        )
        
        self.width = size[0]
        self.height = size[1]
        
        ##super()._calculateLayout()
    FUNCTIONEND
    
    ### Handles the font change of the font element.
    ##
    ##        
    def __hndFontOnSizeChanged(self,ev):
        self._invalidate()
    FUNCTIONEND
    
    ### Set/Get the format string of the label.
    ##
    ##
    @property   
    def format(self):
        return self._format
    FUNCTIONEND
    
    ### Sets the label´s format.
    ##
    ## @param value  
    ##   
    @format.setter
    def format(self,value):
        self._format = value
        self._invalidate()
    FUNCTIONEND
    
    ### Set/Get the value of autoSize.
    ##
    ##
    @property   
    def autoSize(self):
        return self._autoSize
    FUNCTIONEND
    
    ###  Sets autoSize.
    ##
    ##   @param value   Bool value of autoSize..
    ##   
    @autoSize.setter
    def autoSize(self,value):
        self._autoSize = value
        self._invalidate()
    FUNCTIONEND
                     
    ### Set/Get the value of the label.
    ##  The value is the shown text.
    ##
    ##
    @property   
    def value(self):
        return self._value
    FUNCTIONEND
    
    ###  Sets the shown text.
    ##
    ##   @param value   The text that should be shown.
    ##   
    @value.setter
    def value(self,value):
        self._value = value
        self._invalidate()
    FUNCTIONEND
    
    ### Set/Get the text color.
    ##
    ##  @return  The color orject.
    ##
    @property
    def color(self):
        return self._color
    FUNCTIONEND
    
    ### Sets the color of the text.
    ##
    ##  @param value
    ##
    @color.setter
    def color(self,value):
        self._color = value
        self._invalidate()
    FUNCTIONEND
    
    ### Set/Get the font object.
    ##
    ##  @return
    ##
    @property   
    def font(self):
        return self._font
    FUNCTIONEND
    
    ### Sets the font object.
    ##
    ##  @param value 
    ##
    @font.setter
    def font(self,value):
        
        if not value.onSizeChanged.has(self.__hndFontOnSizeChanged):
            value.onSizeChanged.add(self.__hndFontOnSizeChanged)
            
        self._font = value
        self._invalidate()
    FUNCTIONEND
        