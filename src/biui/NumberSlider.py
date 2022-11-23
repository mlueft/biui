import biui

###
##
##
class NumberSlider(biui.ContainerWidget.ContainerWidget):
    
    def __init__(self):
        super().__init__()
        ## 
        self._minValue = 0
        ##
        self._maxValue = 0
        ##
        self._value = 0
        ##
        self._step = 5
        ##
        self._microStep = 1
        ##
        self._showNavigation = True
        ##
        self._barDownPosition = None
        ##
        self._decButton = biui.Button()
        self._decButton.name = "buttonDec"
        self._decButton.minWidth=1
        self._decButton.minHeight=1
        self._decButton.value = "-"
        self._decButton.alignment = biui.Alignment.FILL
        self._decButton.onMouseUp.add(self._onDecUp)
        self.addChild(self._decButton,0,0)
        
        ##
        self._incButton = biui.Button()
        self._incButton.name = "buttonInc"
        self._incButton.minWidth=1
        self._incButton.minHeight=1
        self._incButton.value = "+"
        self._incButton.alignment = biui.Alignment.FILL
        self._incButton.onMouseUp.add(self._onIncUp)
        self.addChild(self._incButton,2,0)
        
        ##
        self._bar = biui.Progressbar()
        self._bar.name = "progressbar"
        self._bar.alignment = biui.Alignment.FILL
        self._bar.onMouseDown.add(self._barMouseDown)
        self.addChild(self._bar,1,0)
        
        lm = self.layoutManager
        lm.columnWidths = [30,0,30]
        
        ##theme = biui.getTheme()
        ##self._themeBackgroundfunction = theme.drawNumberSliderBeforeChildren
        ##self._themeForegroundfunction = theme.drawNumberSliderAfterChildren
        
        self.width = 150
        self.height = 50
        
        self.minValue = -1024
        self.maxValue = 1024
        self.value = 0
        self.step = 0.5
        self.showNavigation = True
        
    ###
    ##
    ##
    def _barMouseDown(self,ev):
        self._barDownPosition = ev.position
        self.window.onMouseMove.add(self._wndMouseMove)
        self.window.onMouseUp.add(self._wndMouseUp)
      
    ###
    ##
    ##  
    def _wndMouseMove(self,ev):
        ev.stopPropagation()
        delta = ev.x-self._barDownPosition[0]
        treshold = 1
        if delta < -treshold:
            self.value -= self.step
            self._barDownPosition = ev.position
        elif delta > treshold:
            self.value += self.step
            self._barDownPosition = ev.position
    
    def _wndMouseUp(self,ev):
        ev.stopPropagation()
        self.window.onMouseMove.remove(self._wndMouseMove)
        self.window.onMouseUp.remove(self._wndMouseUp)
    
    ### Handles the mouse up event of the inc-Button.
    ##
    ##
    def _onIncUp(self,ev):
        self.value += self.microStep

    ### Handles the up mouse event of the dec-Button.
    ##
    ##
    def _onDecUp(self,ev):
        self.value -= self.microStep
        
    ### Get the label object.
    ##
    ##
    @property
    def label(self):
        return self._bar.label
    
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
        if value == self.minValue:
            return

        self.maxValue = max(self.maxValue,value)
        self.value = max(self.minValue,value)
        self._minValue = value
        self._bar.minValue = value
    
    ### Set/Get the maximum value.
    ##
    ##  @return    The max value of the slider.
    ##
    @property
    def maxValue(self):
        return self._maxValue
    
    ### Sets teh max value of the slider.
    ##
    ##  @param value    The max value of the slider.
    ##
    @maxValue.setter
    def maxValue(self,value):
        if value == self._maxValue:
            return

        self.minValue = min(self.minValue,value)
        self.value = min(self.value,value)
        self._maxValue = value
        self._bar.maxValue = value

        
    ### Set/Get the current value.
    ##
    ##  @return    The current value of the slider.
    ##
    @property
    def value(self):
        return self._value
    
    ### Sets the current value of the slider.
    ##
    ##  @param value   The value of the slider.
    ##
    @value.setter
    def value(self,value):
        
        if value == self._value:
            return
        value = max(
            min(value,self._maxValue),
            self._minValue
        )
        
        self._value = value
        self._bar.value = value
        self._invalidate()

    ### Set/Get the value by which the sliders value is incremented
    ##  or decrimented by dragging with the mouse.
    ##
    ##  @return
    ##
    @property
    def step(self):
        return self._step
    
    ### Sets the step value of the slider.
    ##
    ##  @param value  
    ##
    @step.setter
    def step(self,value):
        self._step = value
        
    ### Set/Get the value by which the sliders value is incremented
    ##  or decrimented by clicking a the navigation button.
    ##
    ##
    ##
    @property
    def microStep(self):
        return self._microStep
    
    ###
    ##
    ##
    @microStep.setter
    def microStep(self,value):
        self._microStep = value
        
    ### Set/Get if the navigation buttons are visible.
    ##
    ##
    @property
    def showNavigation(self):
        return self._showNavigation
    
    ###
    ##
    ##
    @showNavigation.setter
    def showNavigation(self,value):
        if self._showNavigation == value:
            return
        
        lm = self.layoutManager
        if value:
            self.addChild(self._decButton,0,0)
            self.addChild(self._incButton,2,0)
            lm.columnWidths = [self.height,0,self.height]
        else:
            self.removeChild(self._decButton)
            self.removeChild(self._incButton)
            lm.columnWidths = [1,0,1]
        
        self._showNavigation = value
        self._invalidate()        
        
    def _calculateLayout(self):
        super()._calculateLayout()
