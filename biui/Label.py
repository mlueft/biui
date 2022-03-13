import biui

class Label(biui.Widget.Widget):
    
    def __init__(self):
        super().__init__()
        self.setFont(biui.Font())
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
    def setText(self,value):
        self._text = value
        self._invalidate()
     
    ##
    #
    #   
    def getText(self):
        return self._text
    
    ##
    #
    #
    def setColor(self,value):
        self._color = value
        self._invalidate()
        
    ##
    #
    #
    def getColor(self):
        return self._color
    
    ##
    #
    #
    def setAntialiased(self,value):
        self._antialiased = value
        self._invalidate()
        
    ##
    #
    #
    def getAntialiased(self):
        return self._antialiased
    
    ##
    #
    #
    def setFont(self,value):
        
        if not value.onNameChanged.has(self._onFontChanged): 
            value.onNameChanged.add(self._onFontChanged)
            
        if not value.onSizeChanged.has(self._onFontChanged):
            value.onSizeChanged.add(self._onFontChanged)
            
        self._font = value
        self._invalidate()
     
    ##
    #
    #   
    def getFont(self):
        return self._font