import biui

##
#
#
class ToggleButton(biui.Button.Button):
    
    def __init__(self):
        super().__init__()
        self._state = biui.ButtonStates.NORMAL
        self._checked = False
    
    ##
    #
    #    
    @property
    def checked(self):
        return self._checked
    
    ##
    #
    #
    @checked.setter
    def checked(self,value):
        # Prevents unnacassary _draw-calls
        if self._checked == value:
            return
        
        self._recordDirtyRect()
        self._checked = value
        self._invalidate()
        
    @property
    def state(self):
        if self._checked:
            return biui.ButtonStates.CHECKED
        
        return self._state
            
    def _onMouseUp(self,ev):
        self._recordDirtyRect()
        self._checked = not self._checked
        self._invalidate()
        super()._onMouseUp(ev)
        
        