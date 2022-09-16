import biui

class Progressbar(biui.ContainerWidget.ContainerWidget):
    
    def __init__(self):
        super().__init__()
        theme = biui.getTheme()
        self._themeBackgroundfunction = theme.drawProgressbarBeforeChildren
        self._themeForegroundfunction = theme.drawProgressbarChildren
        ## 
        self._minValue = -1024
        ##
        self._maxValue = 1024
        ##
        self._value = 0
        ##
        self._showValue = True
        ##
        self._label = biui.Label()
        self._label.alignment = biui.Alignment.CENTER_CENTER
        self._label.value = ""
        self.addChild(self._label,0,0)

    ### Get the label object.
    ##
    ##
    @property
    def showValue(self):
        return self._showValue
    
    ###
    ##
    ##
    @showValue.setter
    def showValue(self,value):
        if self._showValue != value:
            self._invalidate()
        if not value:
            self.label.value = ""
        else:
            self.label.value = value
        self._showValue = value
            
    ### Get the label object.
    ##
    ##
    @property
    def label(self):
        return self._label
    
    ### Set/Get the minimum value.
    ##
    ##
    @property
    def minValue(self):
        return self._minValue
    
    ###
    ##
    ##
    @minValue.setter
    def minValue(self,value):
        if self.value < value:
            self.value = max(self.value,value)
        self._minValue = value
    
    ### Set/Get the maximum value.
    ##
    ##
    @property
    def maxValue(self):
        return self._maxValue
    
    ###
    ##
    ##
    @maxValue.setter
    def maxValue(self,value):
        if self.value > value:
            self.value = min(self.value,value)
        self._maxValue = value

        
    ### Set/Get the current value.
    ##
    ##
    @property
    def value(self):
        return self._value
    
    ###
    ##
    ##
    @value.setter
    def value(self,value):
        value = max(min(value,self._maxValue),self._minValue)
        if self.value != value:
            self._invalidate()
        self._value = value
        if self._showValue:
            self._label.value = value

