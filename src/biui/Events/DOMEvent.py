
from biui.Events import Event
from biui.Events import EventPhase

### Represents a KeyEvent. 
##
##
class DOMEvent(Event):
    
    def __init__(self,eventSource):
        super().__init__(eventSource)
        self._stopPropagation = False
        self._phase = EventPhase.DOWN
            
    ### Stops the handling of the event in the DOM structure.
    ##  So the event is not propagated to the next child
    ##  elements in the DOM.
    ##
    ##
    def stopPropagation(self):
        self._stopPropagation = True

    ###
    ##
    ##
    @property
    def propagationStopped(self)->bool:
        return self._stopPropagation
    
    ### Returns the event phase.
    ##
    ## @return      An integer value representing an
    ##              enum value of biui.EventPhase
    ##
    @property
    def phase(self):
        return self._phase
    
    ### Switches the eventto the P phase.
    ##
    ##
    def _nextPhase(self):
        self._phase = EventPhase.UP
