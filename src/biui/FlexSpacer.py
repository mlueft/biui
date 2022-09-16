import biui

###
##
##
class FlexSpacer(biui.Widget.Widget):
    
    def __init__(self,isVertical):
        super().__init__()
        self._minWidth = 2
        self._minHeight = 2
        
        self._isVertical = isVertical
        
        ## Panes which are touching with the BOTTOM/RIGHT border.
        self._leftNeibours = []
        
        ## Panes which are touching with the TOP/LEFT border.
        self._rightNeighbours = []
                
        theme = biui.getTheme()
        self._themeBackgroundfunction = theme.drawFlexSpacer
     
    ###
    ##
    ##
    @property
    def isVertical(self):
        return self._isVertical

    ###
    ##
    ##
    @property
    def isHorizontal(self):
        return not self._isVertical
        
    ###
    ##
    ##   
    @property 
    def leftNeighbours(self):
        return self._leftNeibours
    
    ###
    ##
    ##
    @leftNeighbours.setter
    def leftNeighbours(self,value):
        self._leftNeibours = value
    
    ###
    ##
    ##
    @property
    def rightNeighbours(self):
        return self._rightNeighbours
    
    ###
    ##
    ##
    @rightNeighbours.setter
    def rightNeighbours(self,value):
        self._rightNeighbours = value
            
    ###
    ##
    ##
    def addLeftNeighbour(self,pane):
        
        if pane in self._leftNeibours:
            return 
        
        self._leftNeibours.append(pane)
    
    ###
    ##
    ##
    def addRightNeighbour(self,pane):
        
        if pane in self._rightNeighbours:
            return 
        
        self._rightNeighbours.append(pane)
    
    ###
    ##
    ##
    def addLeftNeighbours(self,panes):
        for p in panes:
            self.addLeftNeighbour(p)
    
    ###
    ##
    ##
    def addRightNeighbours(self,panes):
        for p in panes:
            self.addRightNeighbour(p)
            
    ###
    ##
    ##
    def removeNeighbour(self,pane):
        if pane in self._leftNeibours:
            self._leftNeibours.remove(pane)
            
        if pane in self._rightNeighbours:
            self._rightNeighbours.remove(pane)

    ###
    ##
    ##
    def removeNeighbours(self,panes):
        for pane in panes:
            self.removePane(pane)


    ###
    ##
    ##
    def isLeftNeighbour(self,pane):
        return pane in self._leftNeibours
    
    ###
    ##
    ##
    def isRightNeighbour(self,pane):
        return pane in self._rightNeighbours
    
    ###
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
        
        