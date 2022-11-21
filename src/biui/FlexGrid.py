import biui

### 
##
##
class FlexGrid(biui.ContainerWidget.ContainerWidget):
    
    ##
    _spacerWidth = 10
    
    ##
    _rasterSize = 5
    
    def __init__(self):
        super().__init__()
        theme = biui.getTheme()
        self._themeBackgroundfunction = theme.drawFlexGridBeforeChildren
        self._themeForegroundfunction = theme.drawFlexGridAfterChildren
        self._spacers = []
        self._panes = []
        self._minDragPosition = 0
        self._maxDragPosition = 0
        
        self._draggedSpacer = None
        
        ## stores the last recorded layout.
        self._layout = []
        
        self.onResized.add(self.__onReSized)
        
    def addChild(self):
        pass
    
    def removeChild(self):
        pass
    
    ### Handles a vertical split event of a child FlexPanel.
    ##
    ##   
    def __childVerticalSplit(self,ev:biui.Event)->None:
        
        oldPane = ev.eventSource
        
        ## Area is too small to split
        if oldPane.width <= 2*oldPane.minWidth:
            return
        
        newPane = biui.FlexPane()
        newPane.x = oldPane.x+oldPane.width/2+FlexGrid._spacerWidth/2
        newPane.y = oldPane.y
        newPane.height = oldPane.height
        newPane.width = oldPane.width/2-FlexGrid._spacerWidth/2
        
        oldPane.width = newPane.width
        
        spacer = self._createSpacer(True)
        spacer.x = oldPane.right
        spacer.y = oldPane.y
        spacer.height = oldPane.height
        spacer.addLeftNeighbour(oldPane)
        spacer.addRightNeighbour(newPane)
        
        for s in self._spacers:
            ## the old panel has to be removed from the 
            ## spacer at the right side and the new panel
            ## has to be added.
            if s.isLeftNeighbour(oldPane) and s.isVertical:
                s.removeNeighbour(oldPane)
                s.addLeftNeighbour(newPane)
                
            ## the new panel has to be added where 
            ## the old panel is left or right at
            ## horizontal spacers
            ## The new spacer becomes a neighbour too
            if s.isLeftNeighbour(oldPane) and s.isHorizontal:
                s.addLeftNeighbour(newPane)
                s.addLeftNeighbour(spacer)
            
            if s.isRightNeighbour(oldPane) and s.isHorizontal:
                s.addRightNeighbour(newPane)
                s.addRightNeighbour(spacer)
                
        self.addFlexPane(newPane)
        self.addHorizontalSpacer(spacer)
        self.__saveLayout()
        
        self.__onHorizontalSpacerDown(biui.Event(spacer))
        
    ### Handles a horicontal split event of a child Flexpanel.
    ##
    ##
    def __childHorizontalSplit(self,ev:biui.Event)->None:

        oldPane = ev.eventSource

        ## Area is too small to split
        if oldPane.height <= 2*oldPane.minHeight:
            return
                
        newPane = biui.FlexPane()
        newPane.x = oldPane.x
        newPane.y = oldPane.y+oldPane.height/2+FlexGrid._spacerWidth/2
        newPane.width = oldPane.width
        newPane.height = oldPane.height/2-FlexGrid._spacerWidth/2
        
        oldPane.height = newPane.height
        
        spacer = self._createSpacer(False)
        spacer.x = oldPane.x
        spacer.y = oldPane.bottom
        spacer.width = oldPane.width
        spacer.addLeftNeighbour(oldPane)
        spacer.addRightNeighbour(newPane)
               
        for s in self._spacers:
            ## the old panel has to be removed from the 
            ## spacer below side and the new panel
            ## has to be added.
            if s.isLeftNeighbour(oldPane) and s.isHorizontal:
                s.removeNeighbour(oldPane)
                s.addLeftNeighbour(newPane)
                
            ## the new panel has to be added where 
            ## the old panel is left or right at
            ## vertical spacers
            if s.isLeftNeighbour(oldPane) and s.isVertical:
                s.addLeftNeighbour(newPane)
                s.addLeftNeighbour(spacer)
            
            if s.isRightNeighbour(oldPane) and s.isVertical:
                s.addRightNeighbour(newPane)
                s.addRightNeighbour(spacer)
                
        self.addFlexPane(newPane)
        self.addVerticalSpacer(spacer)
        self.__saveLayout()
        
        self.__onVerticalSpacerDown(biui.Event(spacer))

    ### Returns a new FlexSpacer object.
    ##
    ##
    def _createSpacer(self, isVertical)->biui.FlexSpacer:
        spacer = biui.FlexSpacer(isVertical)
        spacer.height = FlexGrid._spacerWidth
        spacer.width = FlexGrid._spacerWidth
        spacer.alignment = biui.Alignment.ABSOLUTE
        return spacer  
          
    ### Returns the spacer left to the pane.
    ##
    ##
    def __getSpacerLeft(self,widget):
        for s in self._spacers:
            if s.isRightNeighbour(widget) and s.isVertical:
                return s
    
    ### Returns the spacer above the pane.
    ##
    ##
    def __getSpacerTop(self,widget):
        for s in self._spacers:
            if s.isRightNeighbour(widget) and s.isHorizontal:
                return s
    
    ### Return the spacer right to the pane.
    ##
    ##
    def __getSpacerRight(self,widget):
        for s in self._spacers:
            if s.isLeftNeighbour(widget) and s.isVertical:
                return s
    
    ### Returns the spacer below the panee.
    ##
    ##
    def __getSpacerBottom(self,widget):
        for s in self._spacers:
            if s.isLeftNeighbour(widget) and s.isHorizontal:
                return s
    
    ### Removed the spacer above.
    ##
    ##
    def __removeSpacerTop(self,widget):
        spacer = self.__getSpacerTop(widget)
        if not spacer:
            return
        spacer.removeNeighbour(widget)
        
    ### Removed the spacer right.
    ##
    ##
    def __removeSpacerRight(self,widget):
        spacer = self.__getSpacerRight(widget)
        if not spacer:
            return
        spacer.removeNeighbour(widget)
        
    ### Removed the spacer below.
    ##
    ##
    def __removeSpacerBottom(self,widget):
        spacer = self.__getSpacerBottom(widget)
        if not spacer:
            return
        spacer.removeNeighbour(widget)
        
    ### Removed the spacer left.
    ##
    ##
    def __removeSpacerLeft(self,widget):
        spacer = self.__getSpacerLeft(widget)
        if not spacer:
            return
        spacer.removeNeighbour(widget)
            
    ### Removed the spacer above and adds the new spacer.
    ##
    ##
    def __addSpacerTop(self,widget,spacer):
        self.__removeSpacerTop(widget)
        if not spacer:
            return
        spacer.addRightNeighbour(widget)
        
    ### Removed the spacer right and adds the new spacer.
    ##
    ##
    def __addSpacerRight(self,widget,spacer):
        self.__removeSpacerRight(widget)
        if not spacer:
            return
        spacer.addLeftNeighbour(widget)
        
    ### Removed the spacer below and adds the new spacer.
    ##
    ##
    def __addSpacerBottom(self,widget,spacer):
        self.__removeSpacerBottom(widget)
        if not spacer:
            return
        spacer.addLeftNeighbour(widget)
        
    ### Removed the spacer above and adds the new spacer.
    ##
    ##
    def __addSpacerLeft(self,widget,spacer):
        self.__removeSpacerLeft(widget)
        if not spacer:
            return
        spacer.addRightNeighbour(widget)
        
        
    ### 
    ##  
    ##
    def __recreateHorizontalSpacer(self, stayPane,spacer):

        ##
        ## we have to differtiate four cases:
        ##
        if spacer.x == stayPane.x and spacer.width == stayPane.width:
            ##
            ##  The spacer is at the same width of the pane. => remove it
            ##
            self.removeSpacer(spacer)
            
        elif spacer.x == stayPane.x:
            ##
            ## The spacer lays left aligned to the Pane.
            ## => move it and fix width.
            ##

            spacer.left = stayPane.right+FlexGrid._spacerWidth
            
            ## the spacer is removed from the left spacer
            self.__removeSpacerLeft(spacer)
                        
            ## the spacer is becomming a right neighbour
            ## where stayPane is a left neighbour
            s = self.__getSpacerRight(stayPane)
            self.__addSpacerLeft(spacer,s)
            
        elif spacer.right == stayPane.right:
            ##
            ## The spacer lays right aligned to the pane. => fix width
            ##

            spacer.right = stayPane.left-FlexGrid._spacerWidth
            
            ## the spacer is removed where it is a left neighbour
            self.__removeSpacerRight(spacer)
                            
            ## the spacer is becomming a left neighbour
            ## where stayPane is a right neighbour
            s = self.__getSpacerLeft(stayPane)
            self.__addSpacerRight(spacer,s)
            
        else:
            ##
            ## The spacer is wider than the pane. => we need to split the spacer
            ##

            newSpacer = self._createSpacer(False)
            newSpacer.y = spacer.y
            newSpacer.left = stayPane.right+FlexGrid._spacerWidth
            newSpacer.right = spacer.right
            self.addVerticalSpacer(newSpacer)
            
            spacer.right = stayPane.left-FlexGrid._spacerWidth
            
            ## newSpacer becommes a right neighbour where stayPane is a left neighbour
            s = self.__getSpacerRight(stayPane)
            self.__addSpacerLeft(newSpacer,s)
            
            s = self.__getSpacerRight(spacer)
            self.__addSpacerRight(newSpacer,s)
            
            s = self.__getSpacerLeft(stayPane)
            self.__addSpacerRight(spacer,s)
             
            ## neighbours of spacer with left > spacer.right
            ## are moved to newSpacer.
            for n in list(spacer.leftNeighbours):
                if n.left > spacer.right:
                    self.__addSpacerBottom(n,newSpacer)
                
            for n in list(spacer.rightNeighbours):
                if n.left > spacer.right:
                    self.__addSpacerTop(n,newSpacer)
    
    ### 
    ##  
    ##
    def __recreateVerticalSpacer(self, stayPane,spacer):
        
        ##
        ## we have to differtiate four cases:
        ##
        if spacer.y == stayPane.y and spacer.height == stayPane.height:
            ##
            ## The spacer is at the same height of the pane. => remove it
            ##
            self.removeSpacer(spacer)
            
        elif spacer.y == stayPane.y:
            ##
            ## The spacer lays the the lower end(top aligned) of the Pane. => move it and fix height
            ##
            
            spacer.top = stayPane.bottom+FlexGrid._spacerWidth
            
            ## the spacer is removed from the spacer above
            self.__removeSpacerTop(spacer)
            
            ## the spacer is becomming a right neighbour
            ## where stayPane is a left neighbour
            s = self.__getSpacerBottom(stayPane)
            self.__addSpacerTop(spacer,s)
                        
        elif spacer.bottom == stayPane.bottom:
            ##
            ## The spacer lays at the lower end(bottom aligned) of the pane. => fix height
            ##
            
            ##spacer.height = spacer.height-stayPane.height-FlexGrid._spacerWidth
            spacer.bottom = stayPane.top-FlexGrid._spacerWidth
            
            ## the spacer is removed where it is a top neighbour
            self.__removeSpacerBottom(spacer)
            
            ## the spacer is becomming a left neighbour
            ## where stayPane is a right neighbour
            s = self.__getSpacerTop(stayPane)
            self.__addSpacerBottom(spacer,s)
                        
        else:
            ##
            ## The spacer is higher than the pane. => we need to split the spacer
            ##

            newSpacer = self._createSpacer(True)
            newSpacer.x = spacer.x
            newSpacer.top = stayPane.bottom+FlexGrid._spacerWidth
            ##newSpacer.height = spacer.y+ow-newSpacer.y
            newSpacer.bottom = spacer.bottom
            self.addHorizontalSpacer(newSpacer)
            
            spacer.bottom = stayPane.top-FlexGrid._spacerWidth
            
            ## newSpacer becommes a right neighbour where stayPane is a left neighbour
            s = self.__getSpacerBottom(stayPane)
            self.__addSpacerTop(newSpacer,s)
            
            s = self.__getSpacerBottom(spacer)
            self.__addSpacerBottom(newSpacer,s)
            
            s = self.__getSpacerTop(stayPane)
            self.__addSpacerBottom(spacer,s)
            
            ## neighbours of spacer with top > spacer.bottom
            ## are moved to newSpacer.
            for n in list(spacer.leftNeighbours):
                if n.top > spacer.bottom:
                    self.__addSpacerRight(n,newSpacer)
                
            for n in list(spacer.rightNeighbours):
                if n.top > spacer.bottom:
                    self.__addSpacerLeft(n,newSpacer)
                    
    ### Handles a joinUp event of a child FlexPanel.
    ##
    ##
    def __childJoinUp(self,ev:biui.Event)->None:
        self.__simplifySpacer()
        stayPane = ev.eventSource
        
        removePane = None
        ## We are looking for a Pane with the same width
        ## at the same x position
        ## with a distance above of the spacer width
        for p in self._panes:
            if p.x == stayPane.x:
                if p.width == stayPane.width:
                    if stayPane.y-p.bottom == FlexGrid._spacerWidth:
                        removePane = p
                        break
        
        if removePane == None:
            return
        
        spacer = None
        ## we are looking for the spacer where stayPane is the right neighbour
        for s in self._spacers:
            if s.isRightNeighbour(stayPane) and s.isHorizontal:
                spacer = s
                break        
        
        stayPane.top = removePane.top
        
        ## the staypane becomes the right neighbour 
        ## where removePane is the right neighbour
        ## and stayPane is removed from the spaver, where
        ## it is the right neighbour
        for s in self._spacers:
            if s.isRightNeighbour(stayPane) and s.isHorizontal:
                s.removeNeighbour(stayPane)
                
            if s.isRightNeighbour(removePane) and s.isHorizontal:
                s.addRightNeighbour(stayPane)
                s.removeNeighbour(removePane)
                        
        self.removeFlexPane(removePane)
        self.__recreateHorizontalSpacer(stayPane,spacer)
        self.__saveLayout()
        
    ### Handles a joinDown event of a child FlexPanel.
    ##
    ##
    def __childJoinDown(self,ev:biui.Event)->None:
        self.__simplifySpacer()
        stayPane = ev.eventSource
        
        removePane = None
        ## We are looking for a Pane with the same width
        ## at the same x position
        ## with a distance below of the spacer width
        for p in self._panes:
            if p.x == stayPane.x:
                if p.width == stayPane.width:
                    if p.y-stayPane.bottom == FlexGrid._spacerWidth:
                        removePane = p
                        break
        
        if removePane == None:
            return
        
        spacer = None
        ## we are looking for the spacer where stayPane is the left neighbour
        for s in self._spacers:
            if s.isLeftNeighbour(stayPane) and s.isHorizontal:
                spacer = s
                break        

        
        stayPane.bottom = removePane.bottom
        
        ## the staypane becomes the left neighbour 
        ## where removePane is the left neighbour
        ## and stayPane is removed from the spaver, where
        ## it is the left neighbour
        for s in self._spacers:
            if s.isLeftNeighbour(stayPane) and s.isHorizontal:
                s.removeNeighbour(stayPane)
                
            if s.isLeftNeighbour(removePane) and s.isHorizontal:
                s.addLeftNeighbour(stayPane)
                s.removeNeighbour(removePane)
                        
        self.removeFlexPane(removePane)
        self.__recreateHorizontalSpacer(stayPane,spacer)
        self.__saveLayout()
           
    ### Handles a joinLeft event of a child FlexPanel.
    ##
    ##
    def __childJoinLeft(self,ev:biui.Event)->None:
        self.__simplifySpacer()
        stayPane = ev.eventSource
        
        removePane = None
        ## We are looking for a Pane with the same height
        ## at the same y position
        ## with a distance left of the spacer width
        for p in self._panes:
            if p.y == stayPane.y:
                if p.height == stayPane.height:
                    if stayPane.x-p.right == FlexGrid._spacerWidth:
                        removePane = p
                        break
                       
        if removePane == None:
            return
        
        spacer = None
        ## we are looking for the spacer where stayPane is the right neighbour
        for s in self._spacers:
            if s.isRightNeighbour(stayPane) and s.isVertical:
                spacer = s
                break        
        
        stayPane.left = removePane.left
        
        ## the staypane becomes the right neighbour 
        ## where removePane is the right neighbour
        ## and stayPane is removed from the spaver, where
        ## it is the right neighbour
        for s in self._spacers:
            if s.isRightNeighbour(stayPane) and s.isVertical:
                s.removeNeighbour(stayPane)
                
            if s.isRightNeighbour(removePane) and s.isVertical:
                s.addRightNeighbour(stayPane)
                s.removeNeighbour(removePane)
            
        self.removeFlexPane(removePane)
        self.__recreateVerticalSpacer(stayPane,spacer)
        self.__saveLayout()
        
    ### Handles a joinRight event of a child FlexPanel.
    ##
    ##
    def __childJoinRight(self,ev:biui.Event)->None:
        self.__simplifySpacer()
        stayPane = ev.eventSource
        
        removePane = None
        ## We are looking for a Pane with the same height
        ## at the same y position
        ## with a distance left of the spacer width
        for p in self._panes:
            if p.y == stayPane.y:
                if p.height == stayPane.height:
                    if p.x-stayPane.right == FlexGrid._spacerWidth:
                        removePane = p
                        break
        
        if removePane == None:
            return
        
        spacer = None
        ## we are looking for the spacer where stayPane is the left neighbour
        for s in self._spacers:
            if s.isLeftNeighbour(stayPane) and s.isVertical:
                spacer = s
                break        
        
        stayPane.right = removePane.right
        
        ## the staypane becomes the left neighbour 
        ## where removePane is the left neighbour
        ## and stayPane is removed from the spaver, where
        ## it is the left neighbour
        for s in self._spacers:
            if s.isLeftNeighbour(stayPane) and s.isVertical:
                s.removeNeighbour(stayPane)
                
            if s.isLeftNeighbour(removePane) and s.isVertical:
                s.addLeftNeighbour(stayPane)
                s.removeNeighbour(removePane)
                        
        self.removeFlexPane(removePane)
        self.__recreateVerticalSpacer(stayPane,spacer)
        self.__saveLayout()
            
    ### Adds a FlexPane to the Layout.
    ##
    ##
    def addFlexPane(self,child:biui.FlexPane)->None:
        child.alignment = biui.Alignment.ABSOLUTE
        super().addChild(child)
        child.onHorizontalSplit.add( self.__childHorizontalSplit )
        child.onVerticalSplit.add( self.__childVerticalSplit )
        child.onJoinRight.add( self.__childJoinRight )
        child.onJoinLeft.add( self.__childJoinLeft )
        child.onJoinDown.add( self.__childJoinDown )
        child.onJoinUp.add( self.__childJoinUp )
        
        child.onMouseUp.add( self.__myPaneMouseUp )

        self._panes.append(child)
        ##self._invalidate()
        
    ### Just a debug function during development.
    ##
    ##  TODO: just for debug
    def __myPaneMouseUp(self, ev):
        
        s = ev.eventSource
        ##print(s)
        ##print( "{},{},{},{}".format(s.left,s.top,s.right,s.bottom) )
        return 
    
        print( "panes:   "+str(len(self._panes)))
        print( "spacers: "+str(len(self._spacers)))
        print( self._draggedSpacer )
        
        print ("spacers:")
        for s in self._spacers:
            print( "{},{},{},{}".format(s.left,s.top,s.right,s.left) )
            
        print("panes")
        for s in self._panes:
            print( "{},{},{},{}".format(s.left,s.top,s.right,s.left) )
            
    ### Removes a FlexPane object.
    ##
    ##
    def removeFlexPane(self,child:biui.FlexPane)->None:
        super().removeChild(child)
        self._panes.remove(child)
        for s in self._spacers:
            s.removeNeighbour(child)
        child.onHorizontalSplit.remove( self.__childHorizontalSplit )
        child.onVerticalSplit.remove( self.__childVerticalSplit )
        child.onJoinRight.remove( self.__childJoinRight )
        child.onJoinLeft.remove( self.__childJoinLeft )
        child.onJoinDown.remove( self.__childJoinDown )
        child.onJoinUp.remove( self.__childJoinUp )
        
    ### Adds a horizontal spacer object.
    ##
    ##           
    def addHorizontalSpacer(self,child:biui.FlexSpacer)->None:
        child.onMouseDown.add(self.__onHorizontalSpacerDown)
        super().addChild(child)
        self._spacers.append(child)
        
    ### Adds a vertical spacer object.
    ##
    ##           
    def addVerticalSpacer(self,child:biui.FlexSpacer)->None:
        child.onMouseDown.add(self.__onVerticalSpacerDown)
        super().addChild(child)
        self._spacers.append(child)
        
    ### Removes a vertical spacer object.
    ##
    ##
    def removeSpacer(self,child:biui.FlexSpacer)->None:
        child.onMouseDown.remove(self.__onHorizontalSpacerDown)
        child.onMouseDown.remove(self.__onVerticalSpacerDown)
        super().removeChild(child)
        self._spacers.remove(child)
        for s in self._spacers:
            s.removeNeighbour(child)
        
    ### Reduces the number of spacer by "connecting" 
    ##  spacers laying next to each other.
    ##
    ##
    def __simplifySpacer(self)->None:
        
        for s0 in self._spacers:
            for s1 in self._spacers:
                if s0.y == s1.y:
                    if s0.right+FlexGrid._spacerWidth == s1.left:
                        ## horizontally side by side
                        ## s0 is extended, s1 is removed
                        
                        s0.right = s1.right
                        s0.addLeftNeighbours(s1.leftNeighbours)
                        s0.addRightNeighbours(s1.rightNeighbours)
                        if s1 == self._draggedSpacer:
                            self._draggedSpacer  = s0
                        
                        ## s0 is added to the spacer right to s1
                        s = self.__getSpacerRight(s1)
                        self.__addSpacerRight(s0,s)
                                
                        self.removeSpacer(s1)
                        return self.__simplifySpacer()
                elif s0.x == s1.x:
                    if s0.bottom+FlexGrid._spacerWidth == s1.top:
                        ## vertically side by side
                        ## s0 is extended, s1 is removed
                        s0.bottom = s1.bottom
                        s0.addLeftNeighbours(s1.leftNeighbours)
                        s0.addRightNeighbours(s1.rightNeighbours)                        
                        if s1 == self._draggedSpacer:
                            self._draggedSpacer  = s0
                        
                        ## s0 is added to the spacer below to s1
                        s = self.__getSpacerBottom(s1)
                        self.__addSpacerBottom(s0,s)
                        
                                
                        self.removeSpacer(s1)
                        return self.__simplifySpacer()      

    ### Finds panes touching the dragged spacer
    ##  and sorts them to left or right
    ##
    ##
    ## TODO: obsolet
    def __determineAllNeighbours(self):

        for spacer in self._spacers:
            leftPanes = []
            rightPanes = []
            
            sl = spacer.x
            sr = spacer.right
            st = spacer.y
            sb = spacer.bottom
            
            if spacer.width == FlexGrid._spacerWidth:
                ## vertical spacer
                ## we are looking for panes above or below the
                ## spacer
                ## Spacers can be neighbours too.
                for p in self._panes+self._spacers:
                    if p.y >= st:
                        if p.bottom <= sb:
                            if abs(p.x-sr) < FlexGrid._spacerWidth/2:
                                ## pane is right
                                rightPanes.append(p)
                            elif abs(p.right-sl) < FlexGrid._spacerWidth/2:
                                ## pane is left
                                leftPanes.append(p)
            else:
                ## horizontal spacer
                ## we are looking for panes left or 
                ## right the spacer
                ## Spacers can be neighbours too.
                for p in self._panes+self._spacers:
                    if p.x >= sl:
                        if p.right <= sr:
                            if abs(p.y-sb) < FlexGrid._spacerWidth/2:
                                ## pane is below
                                rightPanes.append(p)
                            elif abs(p.bottom-st) < FlexGrid._spacerWidth/2:
                                ## pane is above
                                leftPanes.append(p)
            
            spacer.rightPanes = rightPanes
            spacer.leftPanes = leftPanes

    def __determineDragRegion(self,spacer):
        
        sl = spacer.x
        sr = spacer.right
        st = spacer.y
        sb = spacer.bottom
        
        dragMin = 0
        dragMax = max(self.width,self.height)
        
        if spacer.width == FlexGrid._spacerWidth:
            ## vertical spacer
            ## we are looking for panes above or below the
            ## spacer
            ## Spacers can be neighbours too.
            for p in self._panes+self._spacers:
                if p.y >= st:
                    if p.bottom <= sb:
                        if abs(p.x-sr) < FlexGrid._spacerWidth/2:
                            dragMax = min(dragMax,p.right-p.minWidth-FlexGrid._spacerWidth/2)
                        elif abs(p.right-sl) < FlexGrid._spacerWidth/2:
                            dragMin = max(dragMin,p.x+p.minWidth+FlexGrid._spacerWidth/2)
        else:
            ## horizontal spacer
            ## we are looking for panes left or 
            ## right the spacer
            ## Spacers can be neighbours too.
            for p in self._panes+self._spacers:
                if p.x >= sl:
                    if p.right <= sr:
                        if abs(p.y-sb) < FlexGrid._spacerWidth/2:
                            dragMax = min(dragMax,p.bottom-p.minHeight-FlexGrid._spacerWidth/2)
                        elif abs(p.bottom-st) < FlexGrid._spacerWidth/2:
                            dragMin = max(dragMin,p.y+p.minHeight+FlexGrid._spacerWidth/2)
        
        self._minDragPosition = int(dragMin/self._rasterSize)*self._rasterSize + FlexGrid._rasterSize
        self._maxDragPosition = int(dragMax/self._rasterSize)*self._rasterSize - FlexGrid._rasterSize
        
        
    ### Finds panes touching the dragged spacer
    ##  and sorts them to left or right
    ##
    ##
    ##TODO: obsolet
    def __determineNeighbours(self,spacer):

        leftPanes = []
        rightPanes = []
        
        sl = spacer.x
        sr = spacer.right
        st = spacer.y
        sb = spacer.bottom
        
        dragMin = 0
        dragMax = max(self.width,self.height)
        
        ##if spacer.width == FlexGrid._spacerWidth:
        if spacer.isVertical:
            ## vertical spacer
            ## we are looking for panes above or below the
            ## spacer
            ## Spacers can be neighbours too.
            for p in self._panes+self._spacers:
                if p.y >= st:
                    if p.bottom <= sb:
                        if abs(p.x-sr) < FlexGrid._spacerWidth/2:
                            ## pane is right
                            rightPanes.append(p)
                            dragMax = min(dragMax,p.right-p.minWidth-FlexGrid._spacerWidth/2)
                        elif abs(p.right-sl) < FlexGrid._spacerWidth/2:
                            ## pane is left
                            leftPanes.append(p)
                            dragMin = max(dragMin,p.x+p.minWidth+FlexGrid._spacerWidth/2)
        else:
            ## horizontal spacer
            ## we are looking for panes left or 
            ## right the spacer
            ## Spacers can be neighbours too.
            for p in self._panes+self._spacers:
                if p.x >= sl:
                    if p.right <= sr:
                        if abs(p.y-sb) < FlexGrid._spacerWidth/2:
                            ## pane is below
                            rightPanes.append(p)
                            dragMax = min(dragMax,p.bottom-p.minHeight-FlexGrid._spacerWidth/2)
                        elif abs(p.bottom-st) < FlexGrid._spacerWidth/2:
                            ## pane is above
                            leftPanes.append(p)
                            dragMin = max(dragMin,p.y+p.minHeight+FlexGrid._spacerWidth/2)
        
        spacer.rightPanes = rightPanes
        spacer.leftPanes = leftPanes
        
        self._minDragPosition = int(dragMin/self._rasterSize)*self._rasterSize + FlexGrid._rasterSize
        self._maxDragPosition = int(dragMax/self._rasterSize)*self._rasterSize - FlexGrid._rasterSize
        
    ### Handles a mouse down event of a horizontal spacer.
    ##
    ##
    def __onHorizontalSpacerDown(self,ev:biui.MouseEvent)->None:
        ##print("__onHorizontalSpacerDown")
        
        ## Store dragged spacer.
        self._draggedSpacer = ev.eventSource
        
        ## Determine neighbours.
        ## Determine min and max drag position.
        ##self.__determineAllNeighbours()
        self.__determineDragRegion(self._draggedSpacer)
        
        self.onMouseMove.add(self.__onVerticalMouseMove)
        self.onMouseUp.add(self.__onMouseUp)
        
    ### Handles a mouse down event of a vertical spacer.
    ##
    ##
    def __onVerticalSpacerDown(self,ev:biui.MouseEvent)->None:
        ##print("__onVerticalSpacerDown")
        
        ## Store dragged spacer.
        self._draggedSpacer = ev.eventSource
        
        ## Determine neighbours.
        ## Determine min and max drag position.
        ##self.__determineAllNeighbours()
        self.__determineDragRegion(self._draggedSpacer)
        
        self.onMouseMove.add(self.__onHorizontalMouseMove)
        self.onMouseUp.add(self.__onMouseUp)
        
    ### Handles vertical dragging of a spacer.
    ##
    ##
    def __onVerticalMouseMove(self,ev:biui.MouseEvent)->None:
        
        sh = FlexGrid._spacerWidth/2
        
        pos = self.toLocal(ev.position)[0]
        pos = max(min(pos,self._maxDragPosition),self._minDragPosition)
        pos = int(pos/FlexGrid._rasterSize)*FlexGrid._rasterSize
        
        self._draggedSpacer.x = pos-sh
        
        self._draggedSpacer.alignNeighbours()
        
    ### Handles a horizontal dragging of a spacer.
    ##
    ##
    def __onHorizontalMouseMove(self,ev:biui.MouseEvent)->None:
        
        sh = FlexGrid._spacerWidth/2
        
        pos = self.toLocal(ev.position)[1]
        pos = max(min(pos,self._maxDragPosition),self._minDragPosition)
        pos = int(pos/FlexGrid._rasterSize)*FlexGrid._rasterSize
        
        self._draggedSpacer.y = pos-sh
            
        self._draggedSpacer.alignNeighbours()
            
    ### Handles mouse up event of a spacer. 
    ##
    ##
    def __onMouseUp(self,ev:biui.MouseEvent)->None:
        s = ev.eventSource
        ## each time a spacer was moved, we record the panel layout.
        self.__saveLayout()
        self.onMouseMove.remove(self.__onVerticalMouseMove)
        self.onMouseMove.remove(self.__onHorizontalMouseMove)
        self.onMouseUp.remove(self.__onMouseUp)
        self._draggedSpacer = None
        ev.stopPropagation()
        
        self.__simplifySpacer()
        
    ###
    ##
    ##
    def __saveLayout(self):
        self._layout.clear()
        self._layout.append((self,0,0,self.width,self.height))
        
        for s in self._spacers:
            self._layout.append((s,s.x,s.y,s.width,s.height))
        
    
    ###
    ##
    ##
    def __onReSized(self,ev):
        
        if len(self._layout) == 0:
            return 
        
        sh = FlexGrid._spacerWidth/2
        
        ## old screenwidth
        osw = float(self._layout[0][3])
        ## old screenheight
        osh = float(self._layout[0][4])
        
        ## This ensures all panes at the rim
        ## are filling the fleexGrid. 
        for p in self._panes:
            p.x=0
            p.y=0
            p.width=self.width
            p.height=self.height
            
        
        for i,e in enumerate(self._layout):
            if i > 0:

                ## old elementx
                oex = e[1]
                ## old elementx%
                oexp = oex/osw
                ## old elementy
                oey = e[2]
                ## old elementy%
                oeyp = oey/osh
                ## new elementx
                nex = self.width*oexp
                ## new elemeny
                ney = self.height*oeyp
                
                e[0].x = nex
                e[0].y = ney
                
                if e[0].isVertical:
                    
                    ## old elementheight
                    oeh = e[4]
                    ## old elementheight%
                    oehp = oeh/osh
                    ## new elementheight
                    neh = self.height*oehp
                    
                    e[0].height = neh
                    
                else:
                    
                    ## old elementwidth
                    oew = e[3]
                    ## old elementwidth%
                    oewp = oew/osw
                    ## new elementwidth
                    _new = self.width*oewp
                    
                    e[0].width = _new
                    
        for i,e in enumerate(self._layout):
            if i > 0:
                e[0].alignNeighbours()

            
    def _calculateLayout(self):
        
        if not self.isInvalide():
            print("grid::calculateLayout quit.")
            return 

        print("grid::calculateLayout.")
        ## the first pane is set up to fill the whole grid.
        if len(self._panes) == 1:
            self._panes[0].x = 0
            self._panes[0].y = 0
            self._panes[0].width = self.width
            self._panes[0].height = self.height
            
        super()._calculateLayout()
        