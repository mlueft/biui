from typing import Callable

import biui
from biui.ToggleButton import ToggleButton
from biui.Color import Color
###
##
##
class Checkbox(ToggleButton):
    
    def __init__(self):
        super().__init__()
        
        self.__checkboxBackColorCheckedNormal:Color = None 
        self.__checkboxBackColorCheckedOver:Color = None
        self.__checkboxBackColorCheckedDown:Color = None
        self.__checkboxBackColorCheckedChecked:Color = None
        self.__checkboxBorderColor:Color = None
        
        
        theme = biui.getTheme()
        self._themeBackgroundfunction:Callable = theme.drawCheckboxBeforeChildren
        self._themeForegroundfunction:Callable = theme.drawCheckboxAfterChildren

        
    ### Returns the background color of the checkbox itself in normal state.
    ##
    ##  @return            A Color instance.
    ##
    @property
    def checkboxBackColorCheckedNormal(self)->Color:
        return self.__checkboxBackColorCheckedNormal
    
    ### Sets the background color of the checkbox itself in normal state.
    ##
    ##  @param value       A Color instance.
    ##  @return            None
    ##
    @checkboxBackColorCheckedNormal.setter
    def checkboxBackColorCheckedNormal(self, value:Color)->None:
        self.__checkboxBackColorCheckedNormal = value
        
    ### Returns the background color of the checkbox itself in over state.
    ##
    ##  @return            A Color instance.
    ##
    @property
    def checkboxBackColorCheckedOver(self)->Color:
        return self.__checkboxBackColorCheckedOver
    
    ### Sets the background color of the checkbox itself in over state.
    ##
    ##  @param value       A Color instance.
    ##  @return            None
    ##
    @checkboxBackColorCheckedOver.setter
    def checkboxBackColorCheckedOver(self, value:Color)->None:
        self.__checkboxBackColorCheckedOver = value
        
    ### Returns the background color of the checkbox itself in down state.
    ##
    ##  @return            A Color instance.
    ##
    @property
    def checkboxBackColorCheckedDown(self)->Color:
        return self.__checkboxBackColorCheckedDown
    
    ### Sets the background color of the checkbox itself in down state.
    ##
    ##  @param value       A Color instance.
    ##  @return            None
    ##
    @checkboxBackColorCheckedDown.setter
    def checkboxBackColorCheckedDown(self, value:Color)->None:
        self.__checkboxBackColorCheckedDown = value
        
    ### Returns the background color of the checkbox itself in checked state.
    ##
    ##  @return            A Color instance.
    ##
    @property
    def checkboxBackColorCheckedChecked(self)->Color:
        return self.__checkboxBackColorCheckedChecked
    
    ### Sets the background color of the checkbox itself in checked state.
    ##
    ##  @param value       A Color instance.
    ##  @return            None
    ##
    @checkboxBackColorCheckedChecked.setter
    def checkboxBackColorCheckedChecked(self, value:Color)->None:
        self.__checkboxBackColorCheckedChecked = value
        
    ### Sets the border color of the checkbox itself.
    ##
    ##  @return            A Color instance.
    ##
    @property
    def checkboxBorderColor(self)->Color:
        return self.__checkboxBorderColor
    
    ### Returns the border color of the checkbox itself.
    ##
    ##  @param value       A Color instance.
    ##  @return            None
    ##
    @checkboxBorderColor.setter
    def checkboxBorderColor(self, value:Color)->None:
        self.__checkboxBorderColor = value
        