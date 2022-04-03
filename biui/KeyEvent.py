import biui

## Represents a KeyEvent. 
#
#
class KeyEvent(biui.Event.Event):
    
    def __init__(self,eventSource,char,key=None,scanCode=None, modifiers=None):
        super().__init__(eventSource)
        self.__char = char
        self.__key = key
        self.__scanCode = scanCode
        self.__modifiers = modifiers
        self._stopPropagation = False
            
    ## Stops the handling of the event in the DOM structure.
    #  So the event is not propagated to the next child
    #  elements in the DOM.
    #
    #
    def stopPropagation(self):
        self._stopPropagation = True
            
    def __str__(self):
        p = (
            biui.default(self.__char,""),
            biui.default(self.__key,""),
            biui.default(self.__scanCode,""),
            biui.default(self.__modifiers,"")    
        )
        result = "KeyEvent: char: '%s' key: %s scancode: %s mod: %s" % p
        return result