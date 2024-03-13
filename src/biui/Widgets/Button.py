from typing import Callable

import biui

from biui.Widgets import Widget
from biui.Widgets import ContainerWidget
from biui.Widgets import Label

from biui.Enum import ButtonStates
from biui.Color import Color
from biui.Events import Event
from biui.Enum import Alignment


###
##
##
class Button(ContainerWidget):
    
    def __init__(self):
        super().__init__()
        self._state:int = ButtonStates.NORMAL
        ## todo: hinting
        self._icon = None
        self.name:str = "Button"
        
        self.__backColorDown:Color = None
        self.__backColorOver:Color = None
        
        self._label:Label = Label()
        self._label.alignment = Alignment.CENTER_CENTER
       
        theme = biui.getTheme()
        self._themeBackgroundfunction:Callable = theme.drawButtonBeforeChildren
        self._themeForegroundfunction:Callable = theme.drawButtonAfterChildren
        self.width = 150
        self.height = 30
        self.addChild(self._label,1,0)
        
        self._layoutManager.columnWidths = [1,0]
        self._layoutManager.rowHeights = [0]
        
        self.onMouseEnter.add(self.__hndOnMouseEnter)
        self.onMouseLeave.add(self.__hndOnMouseLeave)
        self.onMouseDown.add(self.__hndOnMouseDown)
        self.onMouseUp.add(self.__hndOnMouseUp)
        
    ### 
    ##
    ##  @return            A Color instance.
    ##
    @property
    def backColorOver(self)->Color:
        return self.__backColorOver
    
    ### Sets the backcolor for this widget.
    ##
    ##  @param value       A Color instance.
    ##  @return            None
    ##
    @backColorOver.setter
    def backColorOver(self, value:Color):
        self.__backColorOver = value
                
    ### 
    ##
    ##  @return            A Color instance.
    ##
    @property
    def backColorDown(self)->Color:
        return self.__backColorDown
    
    ### Sets the backcolor for this widget.
    ##
    ##  @param value       A Color instance.
    ##  @return            None
    ##
    @backColorDown.setter
    def backColorDown(self, value:Color):
        self.__backColorDown = value
        
    ### @see ContainerWidget.getChildAt
    ##
    ##   
    def getChildAt(self, pos:tuple[int,int])->Widget:
        ## we do not want to return any child 
        ## objects like labels or icons.
        ## If the position is inside the button,
        ## the button is the last element in the DOM.
        return self

    
    ### Returns the embedded label instance
    ##  to make its properties accessible.
    ##
    ## todo: hinting
    @property
    def label(self):
        return self._label
    
    ### Returns the current state of the button.
    ##  See: ButtonStates
    ##  
    @property
    def state(self)->int:
        return self._state
    
    ### Returns the icon instance of the button
    ##  to make its properties accessible. 
    ##
    ##todo:hinting
    @property
    def icon(self):
        return self._icon
    
    ### Sets the icon instance.
    ##  TODO: Impliment the icon class.
    ##
    ## todo: hinting
    @icon.setter
    def icon(self,icon)->None:
        if icon == self._icon:
            return
        self._icon = icon
        self.addChild(icon,0,0)
        self._invalidate()

    ### Returns the value of the button.
    ##  The value is the shown text.
    ##
    ##
    @property
    def value(self)->str:
        return self._label.value
    
    ### Sets the value of the button.
    ##  The value is the shown text.
    ##
    ##  @param value       The string value of the label.
    ##    
    @value.setter
    def value(self,value:str)->None:
        self._label.value = value

    ###
    ##
    ##
    def __hndOnMouseEnter(self,ev:Event)->None:
        self._invalidate()
        self._state = ButtonStates.OVER
        self._invalidate()
    
    ###
    ##
    ##
    def __hndOnMouseLeave(self,ev:Event)->None:
        self._invalidate()
        self._state = ButtonStates.NORMAL
        self._invalidate()

    ###
    ##
    ##
    def __hndOnMouseDown(self,ev:Event)->None:
        self._invalidate()
        self._state = ButtonStates.DOWN
        self._invalidate()
                
    ###
    ##
    ##
    def __hndOnMouseUp(self,ev:Event)->None:
        self._invalidate()
        self._state = ButtonStates.OVER
        self._invalidate()
                       
        
          
        
