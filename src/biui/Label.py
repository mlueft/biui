import biui

class Label(biui.Widget.Widget):
    
    def __init__(self):
        super().__init__()
        self.name = "label"
        self.value = "label"
        self.color = biui.Color(200,200,200,255)
        self._format = "{}"
        self._font = None
        
        self.font = biui.Font()
        self.font.size = 18
        
        theme = biui.getTheme()
        self._themeBackgroundfunction = theme.drawLabel

        
    def _beforeDraw(self):
        
        theme = biui.getTheme()
        
        size = self.font.getRenderSize(
            self.format.format(self.value)
        )
        
        self.width = size[0]
        self.height = size[1]
        
        super()._calculateLayout()
        
    ### Handles the font change of the font element.
    ##
    ##        
    def _onSizeChanged(self,ev):
        self._invalidate()

    ### Set/Get the format string of the label.
    ##
    ##
    @property   
    def format(self):
        return self._format
    
    ### Sets the label's format.
    ##
    ## @param value  
    ##   
    @format.setter
    def format(self,value):
        self._format = value
        self._invalidate()
             
    ### Set/Get the value of the label.
    ##  The value is the shown text.
    ##
    ##
    @property   
    def value(self):
        return self._value
    
    ###  Sets the shown text.
    ##
    ##   @param value   The text that should be shown.
    ##   
    @value.setter
    def value(self,value):
        self._value = value
        self._invalidate()
        
    ### Set/Get the text color.
    ##
    ##  @return  The color orject.
    ##
    @property
    def color(self):
        return self._color
    
    ### Sets the color of the text.
    ##
    ##  @param value
    ##
    @color.setter
    def color(self,value):
        self._color = value
        self._invalidate()
    
    ### Set/Get the font object.
    ##
    ##  @return
    ##
    @property   
    def font(self):
        return self._font
        
    ### Sets the font object.
    ##
    ##  @param value 
    ##
    @font.setter
    def font(self,value):
        
        if not value.onSizeChanged.has(self._onSizeChanged):
            value.onSizeChanged.add(self._onSizeChanged)
            
        self._font = value
        self._invalidate()
        
        