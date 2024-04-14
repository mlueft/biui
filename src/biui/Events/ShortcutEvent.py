import biui
from biui.Events import DOMEvent
from biui.Enum import KeyModifiers
from biui.Enum import Keys

### Represents a KeyEvent. 
##
##
class ShortcutEvent(DOMEvent):
    
    def __init__(self,eventSource,type,keyEvent):
        super().__init__(eventSource)
        self.__type = type
        self.__keyEvent = keyEvent
            
    ###
    ##
    ##
    @property
    def type(self):
        return self.__type
    
    ###
    ##
    ##
    @property
    def keyEvent(self):
        return self.__keyEvent
