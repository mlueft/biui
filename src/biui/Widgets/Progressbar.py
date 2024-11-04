#include "biui.inc"

import biui
from biui.Widgets import ContainerWidget
from biui.Widgets import Label
from biui.Enum import Alignment

class Progressbar(ContainerWidget):
    
    def __init__(self):
        super().__init__()
        theme = biui.getTheme()
        self._themeBackgroundfunction = theme.drawProgressbarBeforeChildren
        self._themeForegroundfunction = theme.drawProgressbarAfterChildren
        
        ## 
        self._minValue = -1024
        ##
        self._maxValue = 1024
        ##
        self._value = 0
        ##
        self._showValue = True
        ##
        self._label = self._createLabel()
        self.addChild(self._label,0,0)
    FUNCTIONEND
    
    ###
    ##
    ##
    def _createLabel(self):
        result = Label()
        result.name = "label"
        result.alignment = Alignment.CENTER_CENTER
        result.value = ""
        return result
    FUNCTIONEND
    
    ### Get the label object.
    ##
    ##
    @property
    def showValue(self):
        return self._showValue
    FUNCTIONEND
    
    ###
    ##
    ##
    @showValue.setter
    def showValue(self,value):
        if value == self._showValue:
            return

        if not value:
            self.label.value = ""
        else:
            self.label.value = value
            
        self._showValue = value
        
        self._invalidate()
    FUNCTIONEND
            
    ### Get the label object.
    ##
    ##
    @property
    def label(self):
        return self._label
    FUNCTIONEND
    
    ### Set/Get the minimum value.
    ##
    ##
    @property
    def minValue(self):
        return self._minValue
    FUNCTIONEND
    
    ###
    ##
    ##
    @minValue.setter
    def minValue(self,value):
        if self.value < value:
            self.value = max(self.value,value)
        self._minValue = value
    FUNCTIONEND
    
    ### Set/Get the maximum value.
    ##
    ##
    @property
    def maxValue(self):
        return self._maxValue
    FUNCTIONEND
    
    ###
    ##
    ##
    @maxValue.setter
    def maxValue(self,value):
        if self.value > value:
            self.value = min(self.value,value)
        self._maxValue = value
    FUNCTIONEND
        
    ### Set/Get the current value.
    ##
    ##
    @property
    def value(self):
        return self._value
    FUNCTIONEND
    
    ###
    ##
    ##
    @value.setter
    def value(self,value):
        if value == self._value:
            return
        value = max(min(value,self.maxValue),self.minValue)
        self._invalidate()
        self._value = value
        if self._showValue:
            self._label.value = value
    FUNCTIONEND
    
    ### @see biui.ContainerWidget.getChildAt
    ##
    ##    
    def getChildAt(self, pos):
        
        ## we do not want to return any child 
        ## objects like labels or icons.
        ## If the position is inside the widget,
        ## the widget is the last element in the DOM.
        
        cPos = self.toGlobal((0,0))
        if cPos[0] > pos[0]:
            return None
        
        if cPos[0]+self.width < pos[0]:
            return None
         
        if cPos[1] > pos[1]:
            return None
        
        if cPos[1]+self.height < pos[1]:
            return None
                
        return self
    FUNCTIONEND
    
    