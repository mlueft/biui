import biui

##
#
#
class NumberSlider(biui.ContainerWidget.ContainerWidget):
    
    def __init__(self):
        super().__init__()
        self.width = 150
        self.height = 50
        # 
        self._minValue = -1024
        #
        self._maxValue = 1024
        #
        self._value = 0
        #
        self._step = 0.5
        #
        self._showNavigation = True
        #
        self._decButton = biui.Button()
        self._decButton.minWidth=1
        self._decButton.minHeight=1
        self._decButton.value = "-"
        self._decButton.alignment = biui.Alignment.FILL
        self._decButton.onMouseUp.add(self._onDecUp)
        self.addChild(self._decButton,0,0)
        
        #
        self._incButton = biui.Button()
        self._incButton.minWidth=1
        self._incButton.minHeight=1
        self._incButton.value = "+"
        self._incButton.alignment = biui.Alignment.FILL
        self._incButton.onMouseUp.add(self._onIncUp)
        self.addChild(self._incButton,2,0)
        
        #
        self._label = biui.Label()
        self._label.alignment = biui.Alignment.CENTER_CENTER
        self.addChild(self._label,1,0)
        
        lm = self.layoutManager
        lm.columnWidths = [30,0,30]
        
    ## Handles the mouse up event of the inc-Button.
    #
    #
    def _onIncUp(self,ev):
        self.value=self.value+self.step

    ## Handles the up mouse event of the dec-Button.
    #
    #
    def _onDecUp(self,ev):
        self.value=self.value-self.step
        
    ## Set/Get the label object.
    #
    #
    @property
    def label(self):
        return self._label
    
    ## Set/Get the minimum value.
    #
    #
    @property
    def minValue(self):
        return self._minValue
    
    ##
    #
    #
    @minValue.setter
    def minValue(self,value):
        if self.value < value:
            self.value = max(self.value,value)
        self._minValue = value
    
    ## Set/Get the maximum value.
    #
    #
    @property
    def maxValue(self):
        return self._maxValue
    
    ##
    #
    #
    @maxValue.setter
    def maxValue(self,value):
        if self.value > value:
            self.value = min(self.value,value)
        self._maxValue = value

        
    ## Set/Get the current value.
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
        value = max(min(value,self._maxValue),self._minValue)
        if self.value != value:
            self._invalidate()
        self._value = value
        self._label.value = value

    ## Set/Get the value by which the sliders value is incremented
    #  or decrimented by clicking a the navigation button.
    #
    #
    @property
    def step(self):
        return self._step
    
    ##
    #
    #
    @step.setter
    def step(self,value):
        self._step = value
        
    ## Set/Get if the navigation buttons are visible.
    #
    #
    @property
    def showNavigation(self):
        return self._showNavigation
    
    ##
    #
    #
    @showNavigation.setter
    def showNavigation(self,value):
        
        if self._showNavigation != value:
            lm = self.layoutManager
            if value:
                self.addChild(self._decButton,0,0)
                self.addChild(self._incButton,2,0)
                lm.columnsWidths = [self.height,0,self.height]
            else:
                self.removeChild(self._decButton)
                self.removeChild(self._incButton)
                lm.columnsWidths = [1,0,1]                
            self._invalidate()
        
        self._showNavigation = value
        
        
    def _redraw(self, surface, forceRedraw=False):
        
        if not self.isInvalide():
            if not forceRedraw:
                return
        
        #print("Pane::_redraw")
        pos = self.position
        
        # we paint on our own surface
        # not on the parent's surface
        _surface = self._surface
        theme = biui.getTheme()
        theme.drawNumberSliderBeforeChildren(self,_surface)

        forceRedraw = self.isInvalide() or forceRedraw
        # We draw all Children on our own surface        
        for c in self._children:
            c._redraw(_surface,forceRedraw)
                    
        theme.drawNumberSliderAfterChildren(self,_surface)
        
        # Now we copy the visible area 
        # of our own surface
        # on the parent's surface
        surface.blit(_surface,pos,(0,0,self.width,self.height))
        
        self._isInvalide = False
        