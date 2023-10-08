#include "biui.inc"

###
##
##
class EventPhase():
    
    def __init__(self):
        raise Exception( BIUI_ERR_CLASS_NOT_INIT )
    
    DOWN = 0      ## In the down phase the event is walking down the DOM.
    UP   = 1      ## In the up phase the event is walking back up to the root(window).