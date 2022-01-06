import biui

## Represents a KeyEvent. 
#
#
class KeyEvent(biui.Event.Event):
    
    def __init__(self,char,key=None,scanCode=None, modifiers=None):
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