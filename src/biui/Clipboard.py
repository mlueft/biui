import pyperclip

### A singleton class to handle properties of the mouse pointer.
##
##
class Clipboard(object):
    
    ###
    ##
    ##
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Clipboard, cls).__new__(cls)
        return cls.instance

    ###
    ##
    ##
    def set(self,value):
        pyperclip.copy(value)
    
    ###
    ##
    ##
    def get(self):
        return pyperclip.paste()
    
    ###
    ##
    ##
    def has(self):
        pass
    