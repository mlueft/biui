import biui
from biui.DOMEvent import DOMEvent

### Represents a KeyEvent. 
##
##
class KeyEvent(DOMEvent):
    
    def __init__(self,eventSource,char,key=None,scanCode=None, modifiers=None):
        super().__init__(eventSource)
        self.__char = char
        self.__key = key
        self.__scanCode = scanCode
        self.__modifiers = modifiers
            
    def __str__(self):
        p = (
            biui.default(self.__char,""),
            biui.default(self.__key,""),
            biui.default(self.__scanCode,""),
            biui.default(self.__modifiers,"")    
        )
        result = "KeyEvent: char: '%s' key: %s scancode: %s mod: %s" % p
        return result