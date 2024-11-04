#include "biui.inc"

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
        
        self._minWidth = 1
        self._minHeight = 1
        
        self._isVertical = isVertical
        
        ## Panes which are touching with the BOTTOM/RIGHT border.
        self._leftNeibours = []
        
        ## Panes which are touching with the TOP/LEFT border.
        self._rightNeighbours = []
        self.backColor = biui.Color(255,0,0)
    FUNCTIONEND
     
    ### Indicates if the spacer is vertical.
    ##
    ##
    @property
    def isVertical(self):
        return self._isVertical
    FUNCTIONEND
    
    ### Indicates if the spacer is horizontal.
    ##
    ##
    @property
    def isHorizontal(self):
        return not self._isVertical
    FUNCTIONEND
        
    ### Returns all right/up neighbours.
    ##
    ##   
    @property 
    def leftNeighbours(self):
        return self._leftNeibours
    FUNCTIONEND
    
    ### Sets all right/up neighbours.
    ##
    ##
    @leftNeighbours.setter
    def leftNeighbours(self,value):
        self._leftNeibours = value
    FUNCTIONEND
    
    ### Returns all right/down neighbours.
    ##
    ##
    @property
    def rightNeighbours(self):
        return self._rightNeighbours
    FUNCTIONEND
    
    ### Sets all right/down neighbours.
    ##
    ##
    @rightNeighbours.setter
    def rightNeighbours(self,value):
        self._rightNeighbours = value
    FUNCTIONEND
            
    ### Adds a left/up neighbour.
    ##
    ##
    def addLeftNeighbour(self,pane):
        
        if pane in self._leftNeibours:
            return 
        
        self._leftNeibours.append(pane)
    FUNCTIONEND
    
    ### Adds a right/down neighbour.
    ##
    ##
    def addRightNeighbour(self,pane):
        
        if pane in self._rightNeighbours:
            return 
        
        self._rightNeighbours.append(pane)
    FUNCTIONEND
    
    ### Adds one or more left/up neighbours.
    ##
    ##
    def addLeftNeighbours(self,panes):
        for p in panes:
            self.addLeftNeighbour(p)
    FUNCTIONEND
    
    ### Adds one or more right/down neighbours.
    ##
    ##
    def addRightNeighbours(self,panes):
        for p in panes:
            self.addRightNeighbour(p)
    FUNCTIONEND
            
    ### Removes the neighbour, if it is found as a neighbour.
    ##
    ##
    def removeNeighbour(self,pane):
        if pane in self._leftNeibours:
            self._leftNeibours.remove(pane)
            
        if pane in self._rightNeighbours:
            self._rightNeighbours.remove(pane)
    FUNCTIONEND
    
    ### Removes one or more neighbours if they are found as neighbours.
    ##
    ##
    def removeNeighbours(self,panes):
        for pane in panes:
            self.removePane(pane)
    FUNCTIONEND

    ### Checks if pane is a left/up neighbour.
    ##
    ##
    def isLeftNeighbour(self,pane):
        return pane in self._leftNeibours
    FUNCTIONEND
    
    ### Checks id pane is a right/down neighbour.
    ##
    ##
    def isRightNeighbour(self,pane):
        return pane in self._rightNeighbours
    FUNCTIONEND
    
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
    FUNCTIONEND
        