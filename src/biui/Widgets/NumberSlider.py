#include "biui.inc"

import biui
from biui.Widgets import ContainerWidget
from biui.Widgets import Button
from biui.Widgets import Progressbar
from biui.Widgets import TextField
from biui.Enum import Alignment
from biui.Enum import Keys
from pickle import NONE

###
##
##
class NumberSlider(ContainerWidget):
    
    def __init__(self):
        super().__init__()
        ##self.layoutManager._debug = True
        
        ##
        self._allowManualInput = True
        
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
        self._showNavigation = False
        ##
        self._screenDownPosition = None
        ##
        self._decButton = None
        
        ##
        self._incButton = None
        
        ##
        self._bar = self._createBar()
        super().addChild(self._bar,1,0)
        
        ##
        ## TODO: Why is TextField the module and not the class?
        self._textfield = None
        
        lm = self.layoutManager
        lm.columnWidths = [30,0,30]
        
        ##theme = biui.getTheme()
        ##self._themeBackgroundfunction = theme.drawNumberSliderBeforeChildren
        ##self._themeForegroundfunction = theme.drawNumberSliderAfterChildren
        
        self.width = 150
        self.height = 30
        
        self.minValue = -1024
        self.maxValue = 1024
        self.value = 0
        self.step = 0.5
        self.showNavigation = True
    FUNCTIONEND

    ###
    ##
    ##
    def _createBar(self):
        result = Progressbar()
        result.name = "progressbar"
        result.alignment = Alignment.FILL
        ##result.alignment = Alignment.CENTER_CENTER
        result.tooltip = self.tooltip
        result.minValue = self.minValue
        result.maxValue = self.maxValue
        result.onMouseDown.add(self.__hndBarOnMouseDown)
        result.onMouseClick.add(self.__hndBarOnMouseClick)
        return result
    FUNCTIONEND
    
    ###
    ##
    ##
    def _createDecButton(self):
        result = Button()
        result.name = "buttonDec"
        result.minWidth=1
        result.minHeight=1
        result.value = "-"
        result.alignment = Alignment.FILL
        result.tooltip = self.tooltip
        result.onMouseUp.add(self.__hndOnDecMouseUp)
        return result
    FUNCTIONEND
    
    ###
    ##
    ##
    def createIncButton(self):
        result = Button()
        result.name = "buttonInc"
        result.minWidth=1
        result.minHeight=1
        result.value = "+"
        result.alignment = Alignment.FILL
        result.tooltip = self.tooltip
        result.onMouseUp.add(self.__hndIncOnMouseUp)
        return result
    FUNCTIONEND

    ###
    ##
    ##
    def createInputfield(self):
        result = TextField.TextField()
        result.name = "textfield"
        result.alignment = Alignment.FILL
        result.tooltip = self.tooltip
        result.onKeyUp.add(self.__hndTextFieldKeyUp)
        return result
    FUNCTIONEND
        
    ###
    ##
    ##
    def __dir__(self):
        result = super().__dir__()
        result = result + [
            "_decButton", "_incButton", "_bar", "_textfield", 
            "tooltip", "label", "minValue", "maxValue", "value", "step", "microStep", "showNavigation"
        ]
        result.sort()
        return list(set(result))
    FUNCTIONEND
    
    ### @see biui.Widget.tooltip
    ##
    ##
    @property
    def tooltip(self):
        return self._tooltip
    FUNCTIONEND

    ### @see biui.Widget.tooltip
    ##
    ##
    @tooltip.setter
    def tooltip(self, value):
        if self._decButton != None:
            self._decButton.tooltip = value
        if self._incButton != None:
            self._incButton.tooltip = value
        if self._bar != None:
            self._bar.tooltip = value
        self._tooltip = value
    FUNCTIONEND

    ###
    ##
    ##
    def __endManualInput(self):
        ## write back value
        
        if self._textfield == None:
            return 
        
        self._textfield.value = self._textfield.value.strip()
        
        if self._textfield.value != "":
            self.value = float(self._textfield.value)
        
        ## remove textfield
        super().removeChild(self._textfield)
        self._textfield = None
        
        ## add bar
        self._bar = self._createBar()
        self._bar.value = self.value
        super().addChild(self._bar,1,0)
        
        ## restore boxes
        if self.showNavigation:
            ## Force buttons to be added
            self._showNavigation = False
            self.showNavigation = True
        
        self._invalidate()
    FUNCTIONEND
    
    ###
    ##
    ##
    def __hndOnFocusLost(self,ev):
        self.__endManualInput()
    FUNCTIONEND
    
    ###
    ##
    ##
    def __startManualInput(self):
        ## Stop dragging
        self._bar.onMouseMove.remove(self.__hndWndOnMouseMove)
        self._bar.onMouseUp.remove(self.__hndWndOnMouseUp)
        biui.Mouse.show()        
        
        ## Hide bar
        super().removeChild(self._bar)
        self._bar = None
        
        ## hide buttons
        if self._incButton != None:
            super().removeChild(self._incButton)
            self._incButton = None
        if self._decButton != None:
            super().removeChild(self._decButton)
            self._decButton = None
        
        ## Make box full size
        self.layoutManager.columnWidths = [1,0,1]
        
        ## Show Textfield
        self._textfield = self.createInputfield()
        self._textfield.onFocusLost.add(self.__hndOnFocusLost)
        super().addChild(self._textfield,1,0)
        self._textfield.value = str(self.value)
        self._textfield.focus()        
    FUNCTIONEND
     
    ###
    ##
    ##
    def __hndTextFieldKeyUp(self,ev):
        ev.stopPropagation()
        if ev.keyCode in [Keys.K_RETURN,Keys.K_KP_ENTER]:
            self.__endManualInput()
    FUNCTIONEND
    
    ###
    ##
    ##
    def __hndBarOnMouseClick(self,ev):
        if not self._allowManualInput:
            return
        ev.stopPropagation()
        self.__startManualInput()
    FUNCTIONEND
    
    ###
    ##
    ##
    def __hndBarOnMouseDown(self,ev):
        ## if old handler are still there
        self._bar.onMouseMove.remove(self.__hndWndOnMouseMove)
        self._bar.onMouseUp.remove(self.__hndWndOnMouseUp)
        
        self._screenDownPosition = biui.Mouse.position
        self._bar.onMouseMove.add(self.__hndWndOnMouseMove)
        self._bar.onMouseUp.add(self.__hndWndOnMouseUp)
        biui.Mouse.hide()
    FUNCTIONEND
    
    ###
    ##
    ##  
    def __hndWndOnMouseMove(self,ev):
        ev.stopPropagation()
        delta = biui.Mouse.position[0]-self._screenDownPosition[0]
        treshold = 1
        if delta < -treshold:
            self.value -= self.step
        elif delta > treshold:
            self.value += self.step
            
        biui.Mouse.position = self._screenDownPosition
    FUNCTIONEND
    
    ##
    #
    #
    def __hndWndOnMouseUp(self,ev):
        print("mouseUp")
        ev.stopPropagation()
        self._bar.onMouseMove.remove(self.__hndWndOnMouseMove)
        self._bar.onMouseUp.remove(self.__hndWndOnMouseUp)
        biui.Mouse.show()
    FUNCTIONEND
    
    ### Handles the mouse up event of the inc-Button.
    ##
    ##
    def __hndIncOnMouseUp(self,ev):
        self.value += self.microStep
    FUNCTIONEND
    
    ### Handles the up mouse event of the dec-Button.
    ##
    ##
    def __hndOnDecMouseUp(self,ev):
        self.value -= self.microStep
    FUNCTIONEND
    
    ### Get the label object.
    ##
    ##
    @property
    def label(self):
        return self._bar.label
    FUNCTIONEND
    
    ### Returns the minimum value of the slider.
    ##
    ##  @return
    ##
    @property
    def minValue(self):
        return self._minValue
    FUNCTIONEND
    
    ### Sets the minimum value of the number slider.
    ##
    ##  @param value         .
    ##
    @minValue.setter
    def minValue(self,value):
        if value == self.minValue:
            return

        self.maxValue = max(self.maxValue,value)
        self.value = max(self.minValue,value)
        self._minValue = value
        if self._bar != None:
            self._bar.minValue = value
    FUNCTIONEND
    
    ### Returns the maximum value of the number slider.
    ##
    ##  @return    The max value of the slider.
    ##
    @property
    def maxValue(self):
        return self._maxValue
    FUNCTIONEND
    
    ### Sets teh maximum value of the slider.
    ##
    ##  @param value    The max value of the slider.
    ##
    @maxValue.setter
    def maxValue(self,value):
        if value == self._maxValue:
            return

        self.minValue = min(self.minValue,value)
        self.value = min(self.maxValue,value)
        self._maxValue = value
        if self._bar != None:
            self._bar.maxValue = value
    FUNCTIONEND
        
    ### Returns the curent value of the slider.
    ##
    ##  @return    The current value of the slider.
    ##
    @property
    def value(self):
        return self._value
    FUNCTIONEND
    
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
        if self._bar != None:
            self._bar.value = value
        self._invalidate()
    FUNCTIONEND
    
    ### Set/Get the value by which the sliders value is incremented
    ##  or decrimented by dragging with the mouse.
    ##
    ##  @return
    ##
    @property
    def step(self):
        return self._step
    FUNCTIONEND
    
    ### Sets the step value of the slider.
    ##
    ##  @param value  
    ##
    @step.setter
    def step(self,value):
        self._step = value
    FUNCTIONEND
    
    ### Set/Get the value by which the sliders value is incremented
    ##  or decrimented by clicking a the navigation button.
    ##
    ##
    ##
    @property
    def microStep(self):
        return self._microStep
    FUNCTIONEND
    
    ###
    ##
    ##
    @microStep.setter
    def microStep(self,value):
        self._microStep = value
    FUNCTIONEND
    
    ### Returns a bool value indicating if the
    ##  navigation buttons are visible.
    ##
    ##
    @property
    def showNavigation(self):
        return self._showNavigation
    FUNCTIONEND
    
    ### Defines if the navigation buttons are visible.
    ##
    ##  @param value      A boolean value.
    ##
    @showNavigation.setter
    def showNavigation(self,value):
        if self._showNavigation == value:
            return
        
        lm = self.layoutManager
        if value:
            self._incButton = self.createIncButton()
            self._decButton = self._createDecButton()
            super().addChild(self._decButton,0,0)
            super().addChild(self._incButton,2,0)
            lm.columnWidths = [self.height,0,self.height]
        else:
            super().removeChild(self._decButton)
            super().removeChild(self._incButton)
            self._decButton = None
            self._incButton = None
            lm.columnWidths = [1,0,1]
        
        self._showNavigation = value
        self._invalidate()
    FUNCTIONEND  
    
    ###
    ##
    ##
    @property
    def allowManualInput(self):
        return self._allowManualInput  
    FUNCTIONEND
    
    ###
    ##
    ##
    @allowManualInput.setter
    def allowManualInput(self,value):
        ## TODO: stop current input
        self._allowManualInput = value
    FUNCTIONEND
    
    ###
    ##
    ##
    def connectScrollNavigator(self,navigator)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("NumberSlider::connectScrollNavigator():{}".format(self))
        #endif
        pass
    FUNCTIONEND
    
    ###
    ##
    ##
    def disconnectScrollNavigator(self,navigator)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("NumberSlider::disconnectScrollNavigator():{}".format(self))
        #endif
        pass
    FUNCTIONEND
        
    ###
    ##
    ##
    @property
    def hasChildren(self):
        #ifdef SHOW_FUNCTIONNAMES
        print("NumberSlider::hasChildren():{}".format(self))
        #endif
        return False
    FUNCTIONEND
    
    ###  
    ##
    ##   
    def removeChild(self,child)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("NumberSlider::removeChild():{}".format(self))
        #endif
        pass
    FUNCTIONEND
    
    ### 
    ##
    ##       
    def addChild(self,child,x:int=0,y:int=0)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("NumberSlider::addChild():{}".format(self))
        #endif
        pass
    FUNCTIONEND

    