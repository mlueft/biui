import biui

###
##
##
class Font():
    
    def __init__(self):
        ##
        self._name = "Arial"
        ##
        self._size = 10
        ##
        self.onSizeChanged = biui.EventManager()
        ##
        self.onNameChanged = biui.EventManager()
    
    ### Set/Get the font name.
    ##
    ##
    @property   
    def name(self):
        return self._name
    
    ###
    ##
    ##
    @name.setter
    def name(self,value):
        if value == self._name:
            return
        self._name = value
        self.onNameChanged.provoke(biui.Event)
     
    ### Set/Get the font size.
    ##
    ##
    @property
    def size(self):
        return self._size
    
    ###
    ##
    ##
    @size.setter
    def size(self,value):
        if value == self._size:
            return
        self._size = value
        self.onSizeChanged.provoke(biui.Event)
    
        
        