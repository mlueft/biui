import biui

### Represents a KeyEvent. 
##
##
class DOMEvent(biui.Event.Event):
    
    def __init__(self,eventSource):
        super().__init__(eventSource)
        self._stopPropagation = False
        self._phase = biui.EventPhase.DOWN
            
    ### Stops the handling of the event in the DOM structure.
    ##  So the event is not propagated to the next child
    ##  elements in the DOM.
    ##
    ##
    def stopPropagation(self):
        self._stopPropagation = True

    @property
    def phase(self):
        return self._phase
    
    def _nextPhase(self):
        self._phase = biui.EventPhase.UP
