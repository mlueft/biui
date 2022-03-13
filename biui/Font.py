import biui

class Font():
    
    def __init__(self):
        self._name = "Arial"
        self._size = 10
        self.onSizeChanged = biui.EventManager()
        self.onNameChanged = biui.EventManager()
    
    ##
    #
    #
    def setName(self,value):
        if value == self._name:
            return
        self._name = value
        self.onNameChanged.provoke(biui.Event)
    
    ##
    #
    #   
    def getName(self):
        return self._name
    
    ##
    #
    #
    def setSize(self,value):
        if value == self._size:
            return
        self._size = value
        self.onSizeChanged.provoke(biui.Event)
     
    ##
    #
    #   
    def getSize(self):
        return self._size
    
        
        