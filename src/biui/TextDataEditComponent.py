##from  biui.Widgets import Widget
from biui.DataEditComponent import DataEditComponent
from biui.Events import Event, EventManager
from biui.Enum import EditingMode

class TextDataEditComponent(DataEditComponent):
    
    def __init__(self):
        super().__init__()
        
        self.__data = ""
        self._cursorPosition = 0
        
        self.onCursorpositionChanged:EventManager = EventManager()
        self.onSelectionChanged:EventManager = EventManager()
        self._selectionBox = None
        self.__editingMode = EditingMode.INSERT
        
    ###
    ##
    ##
    @property
    def editingMode(self):
        return self.__editingMode
    
    ###
    ##
    ##
    @editingMode.setter
    def editingMode(self,value):
        self.__editingMode = value
    
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
    def selectionBox(self):
        return self._selectionBox
    
    ###
    ##
    ##
    def selectAll(self):
        self.cursorPosition = 0;
        self.extendSelection(999999999)
             
    ###
    ##
    ##
    def moveSelection(self,x=0,y=0):
        
        if self._selectionBox == None:
            return
        
        if x == 0:
            return
        
        sb = self._selectionBox
        
        ## selection is at the beginning
        if sb[0][0]==0 and x < 0:
            return
        
        data = self.__data

        ## selection is at the end
        if sb[1][0] == len(data) and x > 0:
            return
        
        cp = self._cursorPosition
                
        ## rs - startposition of the text to be replaced
        ## re - end position of the text to be replaced
        
        ## p0 - part previews the replacement/selection
        ## p1 - part to be replaced
        ## p2 - part after the replacement/selection
        ## s  - selected part        
        if x>0:
            ## x characters right to the selection
            rs = sb[1][0]
            re = rs+x
            
            p0 = data[:sb[0][0]]
            p1 = data[rs:re]
            p2 = data[re:]
            s = data[sb[0][0]:sb[1][0]]
            
            data = p0+p1+s+p2
             
        else:
            ## x characters left to the selection
            rs = sb[0][0]+x
            re = sb[0][0]
            
            p0 = data[:rs]
            p1 = data[rs:re]
            p2 = data[sb[1][0]:]
            s = data[sb[0][0]:sb[1][0]]
            
            data = p0+s+p1+p2
        
        self.__data = data
        
        ##self.cursorPosition = len(text0+text)
        sb[0][0]+= x
        sb[1][0]+= x
        self._selectionBox = sb 
        cp += x
        self._cursorPosition = cp
        
        self.onCursorpositionChanged.provoke(Event(self))
        self.onSelectionChanged.provoke(Event(self))
        self.onDataChanged.provoke(Event(self))
        
    
    ###
    ##
    ##
    def moveCursor(self,x=0,y=0):
        
        if x != 0:
            self.cursorPosition += x
       
    ### Extends the selection in x and y direction
    ##  x > 0 => right
    ##  x < 0 => left
    ##  y > 0 => down
    ##  y < 0 => up
    ##
    def extendSelection(self,x=0,y=0):
        x = int(x)
        y = int(y)
        
        sb = self._selectionBox
        cp = self.cursorPosition
            
        if sb == None:
            sb = [
                [cp,0],
                [cp+x,0]
            ]
            cp = cp + x
        else:
            if cp > sb[0][0]:
                ## cursor is right
                ## right border mooves
                sb[1][0] = sb[1][0]+x
                cp = sb[1][0]
            else:
                ## corsur is left
                ## left border mooves
                sb[0][0] = sb[0][0]+x
                cp = sb[0][0]
                
        if sb[0][0] > sb[1][0]:
            sb = [sb[1],sb[0]]
 
        sb[0][0] = max(0,sb[0][0])
        sb[0][0] = min(len(self.__data),sb[0][0])
        
        sb[1][0] = max(0,sb[1][0])
        sb[1][0] = min(len(self.__data),sb[1][0])
         
        cp = max(0,cp)
        cp = min(len(self.__data),cp)
        
        self._selectionBox = sb
        self._cursorPosition = cp
        self.onSelectionChanged.provoke(Event(self))
        self.onCursorpositionChanged.provoke(Event(self))
    
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
        self._selectionBox = None
        self.onSelectionChanged.provoke(Event(self))
        self.onCursorpositionChanged.provoke(Event(self))
    
    ### Removes the selection or the charakter left to the cursor.
    ##
    ##
    def delete(self):
        
        if self._selectionBox:
            self.insert("")
            return
                
        value = self.__data
        
        cp = max(0,self._cursorPosition-1)
        self.__data = value[:cp]+value[self._cursorPosition:]
        self.cursorPosition = cp

    ### Removes the selection or the character right to the cursor.
    ##
    ##
    def remove(self):
        
        if self._selectionBox:
            self.insert("")
            return
        
        value = self.__data
        
        cp = max(0,self._cursorPosition)
        self.__data = value[:cp]+value[self._cursorPosition+1:]
        self.cursorPosition = cp
            
    ###
    ##
    ##
    def insert(self,text):
        value = self.__data
        if self._selectionBox:
            sb = self._selectionBox
            x0 = sb[0][0]
            x1 = sb[1][0]
        else:
            x0 = self._cursorPosition
            x1 = self._cursorPosition
            if self.__editingMode == EditingMode.REPLACE:
                x1 = self._cursorPosition+1
            
        text0 = value[:x0]
        text1 = value[x1:]
            
        self.__data = text0+text+text1
        self.cursorPosition = len(text0+text)
        
        self.onDataChanged.provoke(Event(self))
        
    