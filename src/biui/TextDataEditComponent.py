##from  biui.Widgets import Widget
from biui.DataEditComponent import DataEditComponent
from biui.Events import Event, EventManager

class TextDataEditComponent(DataEditComponent): ##Widget):
    
    def __init__(self):
        super().__init__()
        
        self.__data = ""
        self._cursorPosition = 0
        
        self.onCursorpositionChanged:EventManager = EventManager()
        self.onSelectionChanged:EventManager = EventManager()
        
        
    ###
    ##
    ##
    @property
    def data(self):
        return self.__data;
    
    ###
    ##
    ##
    @data.setter
    def data(self,value):
        self.__data = value
        self.cursorPosition = len(value)
        self.onDataChanged.provoke(Event(self))
        
    ###
    ##
    ##
    @property
    def selection(self):
        return None
    
    ###
    ##
    ##
    @selection.setter
    def selection(self,value):
        self.onSelectionChanged.provoke(Event(self))
        return None
    
    ###
    ##
    ##
    @property
    def cursorPosition(self):
        return self._cursorPosition
    
    ###
    ##
    ##
    @cursorPosition.setter
    def cursorPosition(self,value):
        value = max(0,value)
        value = min(value,len(self.__data))
        self._cursorPosition = value
        self.onCursorpositionChanged.provoke(Event(self))
    
    ###
    ##
    ##
    def delete(self):
        value = self.__data
        
        self.__data = value[:self._cursorPosition-1]+value[self._cursorPosition:]
        self.cursorPosition = self.cursorPosition-1
    
    ###
    ##
    ##
    def insert(self,text):
        value = self.__data
        
        self.__data = value[:self._cursorPosition]+text+value[self._cursorPosition:]
        self.cursorPosition = self.cursorPosition+len(text)
        
        self.onDataChanged.provoke(Event(self))
        
    