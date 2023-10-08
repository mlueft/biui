
from biui.ButtonStates import ButtonStates
from biui.Button import Button

###
##
##
class ToggleButton(Button):
    
    def __init__(self):
        super().__init__()
        self._state = ButtonStates.NORMAL
        self._checked = False
        self.__backColorChecked = None

        self.onMouseUp.add(self.__hndOnMouseUp)
        
    ### Sets the background color in checked state.
    ##
    ##  @return            
    ##
    @property
    def backColorChecked(self):
        return self.__backColorChecked
    
    ### Sets the background color in checked state..
    ##
    ##  @param value       
    ##  @return            None
    ##
    @backColorChecked.setter
    def backColorChecked(self, value):
        self.__backColorChecked = value
            
    ### Set/Get the checked value of the ToggleButton.
    ##
    ##    
    @property
    def checked(self):
        return self._checked
    
    ###
    ##
    ##
    @checked.setter
    def checked(self,value):
        ## Prevents unnacassary _draw-calls
        if self._checked == value:
            return
        
        self._invalidate()
        self._checked = value
        self._invalidate()
        
    ### Returns the current button state.
    ##  @see ButtonStates
    ##
    ##
    @property
    def state(self):
        if self._checked:
            return ButtonStates.CHECKED
        
        return self._state
            
    def __hndOnMouseUp(self,ev):
        self._invalidate()
        self._checked = not self._checked
        self._invalidate()
        ##super()._onMouseUp(ev)
        
        