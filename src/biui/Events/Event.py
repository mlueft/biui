import biui

### Base class for event objects
##
##
class Event():

    ###
    ##
    ##
    def __init__(self, eventSource):
        self._eventSource = eventSource
        
    ### Returns the event source object.
    ##
    ##
    @property
    def eventSource(self):
        return self._eventSource