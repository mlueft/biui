import biui

## Base class for event objects
#
#
class Event():

    ##
    #
    #
    def __init__(self, eventSource):
        self._eventSource = eventSource
        
    ##
    #
    #
    def getEventSource(self):
        return self._eventSource