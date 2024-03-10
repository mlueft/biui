import biui
from biui.Widgets import Widget

###
##
##
class FlexSpacer(Widget):
    
    def __init__(self,isVertical):
        super().__init__()
        theme = biui.getTheme()
        self._themeBackgroundfunction = theme.drawFlexSpacer
        
        self._minWidth = 2
        self._minHeight = 2
        
        self._isVertical = isVertical
        
        ## Panes which are touching with the BOTTOM/RIGHT border.
        self._leftNeibours = []
        
        ## Panes which are touching with the TOP/LEFT border.
        self._rightNeighbours = []
                
     
    ### Indicates if the spacer is vertical.
    ##
    ##
    @property
    def isVertical(self):
        return self._isVertical

    ### Indicates if the spacer is horizontal.
    ##
    ##
    @property
    def isHorizontal(self):
        return not self._isVertical
        
    ### Returns all right/up neighbours.
    ##
    ##   
    @property 
    def leftNeighbours(self):
        return self._leftNeibours
    
    ### Sets all right/up neighbours.
    ##
    ##
    @leftNeighbours.setter
    def leftNeighbours(self,value):
        self._leftNeibours = value
    
    ### Returns all right/down neighbours.
    ##
    ##
    @property
    def rightNeighbours(self):
        return self._rightNeighbours
    
    ### Sets all right/down neighbours.
    ##
    ##
    @rightNeighbours.setter
    def rightNeighbours(self,value):
        self._rightNeighbours = value
            
    ### Adds a left/up neighbour.
    ##
    ##
    def addLeftNeighbour(self,pane):
        
        if pane in self._leftNeibours:
            return 
        
        self._leftNeibours.append(pane)
    
    ### Adds a right/down neighbour.
    ##
    ##
    def addRightNeighbour(self,pane):
        
        if pane in self._rightNeighbours:
            return 
        
        self._rightNeighbours.append(pane)
    
    ### Adds one or more left/up neighbours.
    ##
    ##
    def addLeftNeighbours(self,panes):
        for p in panes:
            self.addLeftNeighbour(p)
    
    ### Adds one or more right/down neighbours.
    ##
    ##
    def addRightNeighbours(self,panes):
        for p in panes:
            self.addRightNeighbour(p)
            
    ### Removes the neighbour, if it is found as a neighbour.
    ##
    ##
    def removeNeighbour(self,pane):
        if pane in self._leftNeibours:
            self._leftNeibours.remove(pane)
            
        if pane in self._rightNeighbours:
            self._rightNeighbours.remove(pane)

    ### Removes one or more neighbours if they are found as neighbours.
    ##
    ##
    def removeNeighbours(self,panes):
        for pane in panes:
            self.removePane(pane)


    ### Checks if pane is a left/up neighbour.
    ##
    ##
    def isLeftNeighbour(self,pane):
        return pane in self._leftNeibours
    
    ### Checks id pane is a right/down neighbour.
    ##
    ##
    def isRightNeighbour(self,pane):
        return pane in self._rightNeighbours
    
    ### Aligns all neighbour acording to the current left/right borders.
    ##
    ##
    def alignNeighbours(self):
        ##return
        if self.isVertical:
            
            for p in self._leftNeibours:
                p.right = self.left
            
            for p in self._rightNeighbours:
                p.left = self.right
            
        else:
            
            for p in self._leftNeibours:
                p.bottom = self.top
            
            for p in self._rightNeighbours:
                p.top = self.bottom            
        
        