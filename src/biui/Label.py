import biui

class Label(biui.Widget.Widget):
    
    def __init__(self):
        super().__init__()
        self.font = biui.Font()
        self.font.size = 20
        self.value = "label"
        self.antialiased = True
        self.color = (200,200,200)
        self._format = "{}"
        
        theme = biui.getTheme()
        self._themeBackgroundfunction = theme.drawLabel
         
    def _calculateLayout(self):
        theme = biui.getTheme()
        size = theme.getTextSize(self)
        self.width = size[0]
        self.height = size[1]
        super()._calculateLayout()
        
    ## Handles the font change of the font element.
    #
    #        
    def _onFontChanged(self,ev):
        self._invalidate()

    ## Set/Get the format string of the label.
    #
    #
    @property   
    def format(self):
        return self._format
    
    ##
    #
    #   
    @format.setter
    def format(self,value):
        self._format = value
        self._invalidate()
             
    ## Set/Get the value of the label.
    #  The value is the shown text.
    #
    #
    @property   
    def value(self):
        return self._value
    
    ##
    #
    #   
    @value.setter
    def value(self,value):
        self._value = value
        self._invalidate()
        
    ## Set/Get the text color.
    #
    #
    @property
    def color(self):
        return self._color
    
    ##
    #
    #
    @color.setter
    def color(self,value):
        self._color = value
        self._invalidate()
    
    ## Set/Get the aliased property of the text.
    #
    #
    @property
    def antialiased(self):
        return self._antialiased
    
    ##
    #
    #
    @antialiased.setter
    def antialiased(self,value):
        self._antialiased = value
        self._invalidate()
     
    ## Set/Get the font object.
    #
    #
    @property   
    def font(self):
        return self._font
        
    ##
    #
    #
    @font.setter
    def font(self,value):
        
        if not value.onNameChanged.has(self._onFontChanged): 
            value.onNameChanged.add(self._onFontChanged)
            
        if not value.onSizeChanged.has(self._onFontChanged):
            value.onSizeChanged.add(self._onFontChanged)
            
        self._font = value
        self._invalidate()