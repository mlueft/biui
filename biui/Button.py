import biui

##
#
#
class Button(biui.Widget.Widget):
    
    def __init__(self):
        super().__init__()
        self.setWidth(50)
        self.setHeight(20)
        self._state = biui.ButtonStates.NORMAL
    
    ## Returns the current state of the button.
    #  See: biui.ButtonStates
    #  
    def getState(self):
        return self._state
    
    def _onMouseEnter(self,ev):
        self._recordDirtyRect()
        self._state = biui.ButtonStates.OVER
        self._invalidate()
        super()._onMouseEnter(ev)
        
    def _onMouseLeave(self,ev):
        self._recordDirtyRect()
        self._state = biui.ButtonStates.NORMAL
        self._invalidate()
        super()._onMouseLeave(ev)
        
    def _onMouseDown(self,ev):
        self._recordDirtyRect()
        self._state = biui.ButtonStates.DOWN
        self._invalidate()
        super()._onMouseDown(ev)
                
    def _onMouseUp(self,ev):
        self._recordDirtyRect()
        self._state = biui.ButtonStates.OVER
        self._invalidate()
        super()._onMouseUp(ev)
        
    def _onMouseMove(self,ev):
        super()._onMouseMove(ev)
        
    def _redraw(self, surface):
        #pos = self.toGlobal(self.getPosition())
        pos = self.getPosition()
        theme = biui.getTheme()
        theme.drawButton(self,surface)
        super()._redraw(surface)
        
