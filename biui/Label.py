import biui

class Label(biui.Widget.Widget):
    
    def __init__(self):
        super().__init__()
        self.font = biui.Font()
        self._text = "Label"
        self._antialiased = True
        self._color = (100,100,100)
        
    def _redraw(self, surface, forceRedraw=False):
        if not self.isInvalide():
            if not forceRedraw:
                return 
        
        print("Label::_redraw()")
        theme = biui.getTheme()
        theme.drawLabel(self,surface)
        
        self._isInvalide = False

    ##
    #
    #        
    def _onFontChanged(self,ev):
        self._invalidate()
     
    ##
    #
    #
    @property   
    def text(self):
        return self._text
    
    ##
    #
    #   
    @text.setter
    def text(self,value):
        self._text = value
        self._invalidate()
        
    ##
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
    
    ##
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
     
    ##
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