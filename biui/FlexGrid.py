import biui

## TODO: Simplify alghorithmen by using new setter for left,top,right and bottom.
#
#
class FlexGrid(biui.ContainerWidget.ContainerWidget):
    
    #
    _spacerWidth = 4
    
    #
    _rasterSize = 5
    
    def __init__(self):
        super().__init__()
        self._spacers = []
        self._panes = []
        self._minDragPosition = 0
        self._maxDragPosition = 0
        
        # Panes which are touching with the BOTTOM/RIGHT border.
        self._leftPanes = []
        
        # Panes which are touching with the TOP/LEFT border.
        self._rightPanes = []
    
        self._draggedSpacer = None
        
    def addChild(self):
        pass
    
    def removeChild(self):
        pass
    
    ## Handles a vertical split event of a child FlexPanel.
    #
    #   
    def childVerticalSplit(self,ev:biui.Event)->None:
        
        #print("childVerticalSplit")
        oldPane = ev.eventSource
        
        if oldPane.width <= 2*oldPane.minWidth:
            return
        
        newPane = biui.FlexPane()
        newPane.x = oldPane.x+oldPane.width/2+FlexGrid._spacerWidth/2
        newPane.y = oldPane.y
        newPane.height = oldPane.height
        newPane.width = oldPane.width/2-FlexGrid._spacerWidth/2
        
        oldPane.width = newPane.width
        
        spacer = self._createSpacer()
        spacer.x = oldPane.right
        spacer.y = oldPane.y
        spacer.height = oldPane.height
        
        self.addFlexPane(newPane)
        self.addHorizontalSpacer(spacer)
        
        self.__onHorizontalSpacerDown(biui.Event(spacer))
        
    ## Handles a horicontal split event of a child Flexpanel.
    #
    #
    def childHorizontalSplit(self,ev:biui.Event)->None:
        #print("childHorizontalSplit")
        oldPane = ev.eventSource

        if oldPane.height <= 2*oldPane.minHeight:
            return
                
        newPane = biui.FlexPane()
        newPane.x = oldPane.x
        newPane.y = oldPane.y+oldPane.height/2+FlexGrid._spacerWidth/2
        newPane.width = oldPane.width
        newPane.height = oldPane.height/2-FlexGrid._spacerWidth/2
        
        oldPane.height = newPane.height
        
        spacer = self._createSpacer()
        spacer.x = oldPane.x
        spacer.y = oldPane.bottom
        spacer.width = oldPane.width
        
        self.addFlexPane(newPane)
        self.addVerticalSpacer(spacer)
        
        self.__onVerticalSpacerDown(biui.Event(spacer))

    ## Returns a new FlexSpacer object.
    #
    #
    def _createSpacer(self)->biui.FlexSpacer:
        spacer = biui.FlexSpacer()
        spacer.height = FlexGrid._spacerWidth
        spacer.width = FlexGrid._spacerWidth
        spacer.alignment = biui.Alignment.ABSOLUTE
        return spacer  
          
    ## Tries to reduce the number of vertical spacer objects
    #  by joining them.
    #
    #
    def __recreateVerticalSpacer(self, stayPane,spacer):
        #print("__recreateVerticalSpacer")
        # we have to differtiate four cases:
        # 1. The spacer is at the same width of the pane. => remove it
        # 2. The spacer is wider than the pane. => we need to split the spacer
        # 3. The spacer lays at the right end of the pane. => fix width
        # 4. The spacer lays the the left end of the Pane. => move it and fix width
        if spacer.x == stayPane.x and spacer.width == stayPane.width:
            # Case 1
            self.removeHorizontalSpacer(spacer)
        elif spacer.x == stayPane.x:
            # Case 4
            spacer.x = stayPane.right+FlexGrid._spacerWidth
            spacer.width = spacer.width-stayPane.width-FlexGrid._spacerWidth
            
        elif spacer.right == stayPane.right:
            # case 3
            spacer.width = spacer.width-stayPane.width-FlexGrid._spacerWidth
            
        else:
            # case 2
            ow = spacer.width

            spacer.width = stayPane.x-FlexGrid._spacerWidth-spacer.x
            
            newSplitter = self._createSpacer()
            newSplitter.y = spacer.y
            newSplitter.x = stayPane.right+FlexGrid._spacerWidth
            w = spacer.x+ow-newSplitter.x

            newSplitter.width = w
            self.addVerticalSpacer(newSplitter)
                
    ## Tries to reduce the number of horicontal spacer objects
    #  by joining them.

    #
    def __recreateHorizontalSpacer(self, stayPane,spacer):
        #print("__recreateVerticalSpacer")
        # we have to differtiate four cases:
        # 1. The spacer is at the same height of the pane. => remove it
        # 2. The spacer is higher than the pane. => we need to split the spacer
        # 3. The spacer lays at the lower end of the pane. => fix height
        # 4. The spacer lays the the lower end of the Pane. => move it and fix height
        if spacer.y == stayPane.y and spacer.height == stayPane.height:
            #print("1")
            # Case 1
            self.removeVerticalSpacer(spacer)
        elif spacer.y == stayPane.y:
            #print("4")
            # Case 4
            spacer.y = stayPane.bottom+FlexGrid._spacerWidth 
            w = spacer.height-stayPane.height-FlexGrid._spacerWidth
            spacer.height = w
            
        elif spacer.bottom == stayPane.bottom:
            #print("3")
            # case 3
            w = spacer.height-stayPane.height-FlexGrid._spacerWidth
            spacer.height = w
            
        else:
            #print("2")
            # case 2
            ow = spacer.height

            spacer.height = stayPane.y-FlexGrid._spacerWidth-spacer.y
            
            newSpacer = self._createSpacer()
            newSpacer.x = spacer.x
            newSpacer.y = stayPane.bottom+FlexGrid._spacerWidth
            w = spacer.y+ow-newSpacer.y
            newSpacer.height = w
            self.addHorizontalSpacer(newSpacer)
            
    ## Handles a joinUp event of a child FlexPanel.
    #
    #
    def childJoinUp(self,ev:biui.Event)->None:
        self.__simplifySpacer()
        stayPane = ev.eventSource
        
        removePane = None
        # We are looking for a Pane with the same width
        # at the same x position
        # with a distance above of the spacer width
        for p in self._panes:
            if p.x == stayPane.x:
                if p.width == stayPane.width:
                    if stayPane.y-p.y-p.height == FlexGrid._spacerWidth:
                        removePane = p
                        break
        
        if removePane == None:
            return
        
        spacer = None
        # we are looking for the spacer above the stayPane
        for s in self._spacers:
            if stayPane.x >= s.x:
                if stayPane.x <= s.left:
                    if s.bottom == stayPane.y:
                        spacer = s
                        break

        self.__recreateVerticalSpacer(stayPane,spacer)
        
        stayPane.y = removePane.y
        stayPane.height = stayPane.height+removePane.height+FlexGrid._spacerWidth
        
        self.removeFlexPane(removePane)
                
    ## Handles a joinDown event of a child FlexPanel.
    #
    #
    def childJoinDown(self,ev:biui.Event)->None:
        self.__simplifySpacer()
        stayPane = ev.eventSource
        
        removePane = None
        # We are looking for a Pane with the same width
        # at the same x position
        # with a distance below of the spacer width
        for p in self._panes:
            if p.x == stayPane.x:
                if p.width == stayPane.width:
                    if p.y-stayPane.bottom == FlexGrid._spacerWidth:
                        removePane = p
                        break
        
        if removePane == None:
            return
        
        spacer = None
        # we are looking for the spacer below the stayPane
        for s in self._spacers:
            if stayPane.x >= s.x:
                if stayPane.x <= s.right:
                    if s.bottom == removePane.y:
                        spacer = s
                        break


        self.__recreateVerticalSpacer(stayPane,spacer)
        
        stayPane.height = stayPane.height+removePane.height+FlexGrid._spacerWidth
        
        self.removeFlexPane(removePane)
                
    ## Handles a joinLeft event of a child FlexPanel.
    #
    #
    def childJoinLeft(self,ev:biui.Event)->None:
        self.__simplifySpacer()
        stayPane = ev.eventSource
        
        removePane = None
        # We are looking for a Pane with the same height
        # at the same y position
        # with a distance left of the spacer width
        for p in self._panes:
            if p.y == stayPane.y:
                if p.height == stayPane.height:
                    if stayPane.x-p.x-p.width == FlexGrid._spacerWidth:
                        removePane = p
                        break
                       
        if removePane == None:
            return
        
        spacer = None
        # we are looking for the left above the stayPane
        for s in self._spacers:
            if stayPane.y >= s.y:
                if stayPane.y <= s.bottom:
                    if s.x+s.width == stayPane.x:
                        spacer = s
                        break
                    
        self.__recreateHorizontalSpacer(stayPane,spacer)
        
        stayPane.x = removePane.x
        stayPane.width = stayPane.width+removePane.width+FlexGrid._spacerWidth
        
        self.removeFlexPane(removePane)
                
    ## Handles a joinRight event of a child FlexPanel.
    #
    #
    def childJoinRight(self,ev:biui.Event)->None:
        self.__simplifySpacer()
        stayPane = ev.eventSource
        
        removePane = None
        # We are looking for a Pane with the same height
        # at the same y position
        # with a distance left of the spacer width
        for p in self._panes:
            if p.y == stayPane.y:
                if p.height == stayPane.height:
                    if p.x-stayPane.right == FlexGrid._spacerWidth:
                        removePane = p
                        break
        
        if removePane == None:
            return
        
        spacer = None
        # we are looking for the spacer right the stayPane
        for s in self._spacers:
            if stayPane.y >= s.y:
                if stayPane.y <= s.bottom:
                    if s.x+s.width == removePane.x:
                        spacer = s
                        break


        self.__recreateHorizontalSpacer(stayPane,spacer)
        
        stayPane.width = stayPane.width+removePane.width+FlexGrid._spacerWidth
        
        self.removeFlexPane(removePane)
        
            
    ## Adds a FlexPane to the Layout.
    #
    #
    def addFlexPane(self,child:biui.FlexPane)->None:
        child.alignment = biui.Alignment.ABSOLUTE
        super().addChild(child)
        child.onHorizontalSplit.add( self.childHorizontalSplit )
        child.onVerticalSplit.add( self.childVerticalSplit )
        child.onJoinRight.add( self.childJoinRight )
        child.onJoinLeft.add( self.childJoinLeft )
        child.onJoinDown.add( self.childJoinDown )
        child.onJoinUp.add( self.childJoinUp )
        
        child.onMouseUp.add( self.myPaneMouseeUp )

        self._panes.append(child)
        
    ## Just a debug function during development.
    #
    #
    def myPaneMouseeUp(self, ev):
        print( "panes:   "+str(len(self._panes)))
        print( "spacers: "+str(len(self._spacers)))
        print( self._draggedSpacer )
        
    ## Removes a FlexPane object.
    #
    #
    def removeFlexPane(self,child:biui.FlexPane)->None:
        super().removeChild(child)
        self._panes.remove(child)
        child.onHorizontalSplit.remove( self.childHorizontalSplit )
        child.onVerticalSplit.remove( self.childVerticalSplit )
        child.onJoinRight.remove( self.childJoinRight )
        child.onJoinLeft.remove( self.childJoinLeft )
        child.onJoinDown.remove( self.childJoinDown )
        child.onJoinUp.remove( self.childJoinUp )
        
    ## Adds a horizontal spacer object.
    #
    #           
    def addHorizontalSpacer(self,child:biui.FlexSpacer)->None:
        child.onMouseDown.add(self.__onHorizontalSpacerDown)
        super().addChild(child)
        self._spacers.append(child)
        
    ## Removes a horizontal spacer object.
    #
    #
    def removeHorizontalSpacer(self,child:biui.FlexSpacer)->None:
        child.onMouseDown.remove(self.__onHorizontalSpacerDown)
        super().removeChild(child)
        self._spacers.remove(child)

    ## Adds a vertical spacer object.
    #
    #           
    def addVerticalSpacer(self,child:biui.FlexSpacer)->None:
        child.onMouseDown.add(self.__onVerticalSpacerDown)
        super().addChild(child)
        self._spacers.append(child)
        
    ## Removes a vertical spacer object.
    #
    #
    def removeVerticalSpacer(self,child:biui.FlexSpacer)->None:
        child.onMouseDown.remove(self.__onVerticalSpacerDown)
        super().removeChild(child)
        self._spacers.remove(child)
        
    ## Reduces the number of spacer by "connecting" 
    #  spacers laying next to each other.
    #
    #
    def __simplifySpacer(self)->None:
        for s0 in self._spacers:
            for s1 in self._spacers:
                if s0.y == s1.y:
                    if s0.right+FlexGrid._spacerWidth == s1.x:
                        # horizontally side by side
                        s0.width = s0.width+s1.width+FlexGrid._spacerWidth
                        if s1 == self._draggedSpacer:
                            self._draggedSpacer  = s0
                        self.removeHorizontalSpacer(s1)
                        return self.__simplifySpacer()
                elif s0.x == s1.x:
                    if s0.bottom+FlexGrid._spacerWidth == s1.y:
                        # vertically side by side
                        s0.height = s0.height+s1.height+FlexGrid._spacerWidth
                        if s1 == self._draggedSpacer:
                            self._draggedSpacer  = s0
                        self.removeHorizontalSpacer(s1)
                        return self.__simplifySpacer()      
                  
    ## Finds panes touching the dragged spacer
    #  and sorts them to left or right
    #
    #
    def __determineNeighbours(self):
        self._leftPanes = []
        self._rightPanes = []
        
        s = self._draggedSpacer
        sl = s.x
        sr = s.right
        st = s.y
        sb = s.bottom
        
        dragMin = 0
        dragMax = max(self.width,self.height)
        
        if s.width == FlexGrid._spacerWidth:
            # vertical spacer
            # we are looking for panes above or below the
            # spacer
            # Spacers can be neighbours too.
            for p in self._panes+self._spacers:
                if p.y >= st:
                    if p.bottom <= sb:
                        if abs(p.x-sr) < FlexGrid._spacerWidth/2:
                            # pane is right
                            self._rightPanes.append(p)
                            dragMax = min(dragMax,p.right-p.minWidth-FlexGrid._spacerWidth/2)
                        elif abs(p.right-sl) < FlexGrid._spacerWidth/2:
                            # pane is left
                            self._leftPanes.append(p)
                            dragMin = max(dragMin,p.x+p.minWidth+FlexGrid._spacerWidth/2)
        else:
            # horizontal spacer
            # we are looking for panes left or 
            # right the spacer
            # Spacers can be neighbours too.
            for p in self._panes+self._spacers:
                if p.x >= sl:
                    if p.right <= sr:
                        if abs(p.y-sb) < FlexGrid._spacerWidth/2:
                            # pane is below
                            self._rightPanes.append(p)
                            dragMax = min(dragMax,p.bottom-p.minHeight-FlexGrid._spacerWidth/2)
                        elif abs(p.bottom-st) < FlexGrid._spacerWidth/2:
                            # pane is above
                            self._leftPanes.append(p)
                            dragMin = max(dragMin,p.y+p.minHeight+FlexGrid._spacerWidth/2)
        
        self._minDragPosition = int(dragMin/self._rasterSize)*self._rasterSize + FlexGrid._rasterSize
        self._maxDragPosition = int(dragMax/self._rasterSize)*self._rasterSize - FlexGrid._rasterSize
        
    ## Handles a mouse down event of a horizontal spacer.
    #
    #
    def __onHorizontalSpacerDown(self,ev:biui.MouseEvent)->None:
        #print("__onHorizontalSpacerDown")
        
        # Store dragged spacer.
        self._draggedSpacer = ev.eventSource
        
        # simplify spacers.
        self.__simplifySpacer()
        
        # Determine neighbours.
        # Determine min and max drag position.
        self.__determineNeighbours()
        
        self.onMouseMove.add(self.__onVerticalMouseMove)
        self.onMouseUp.add(self.__onMouseUp)
        
    ## Handles a mouse down event of a vertical spacer.
    #
    #
    def __onVerticalSpacerDown(self,ev:biui.MouseEvent)->None:
        #print("__onVerticalSpacerDown")
        
        # Store dragged spacer.
        self._draggedSpacer = ev.eventSource
        
        # simplify spacers.
        self.__simplifySpacer()
        
        # Determine neighbours.
        # Determine min and max drag position.
        self.__determineNeighbours()
        
        self.onMouseMove.add(self.__onHorizontalMouseMove)
        self.onMouseUp.add(self.__onMouseUp)
        
    ## Handles vertical dragging of a spacer.
    #
    #
    def __onVerticalMouseMove(self,ev:biui.MouseEvent)->None:
        sh = FlexGrid._spacerWidth/2
        
        pos = self.toLocal(ev.position)[0]
        pos = max(min(pos,self._maxDragPosition),self._minDragPosition)
        pos = int(pos/FlexGrid._rasterSize)*FlexGrid._rasterSize
        
        self._draggedSpacer.x = pos-sh
        
        for p in self._rightPanes:
            x = p.right
            p.x = pos+sh
            p.width = x-pos-sh
    
        for p in self._leftPanes:
            p.width = pos-p.x-sh
        
    ## Handles a horizontal dragging of a spacer.
    #
    #
    def __onHorizontalMouseMove(self,ev:biui.MouseEvent)->None:
        
        sh = FlexGrid._spacerWidth/2
        
        pos = self.toLocal(ev.position)[1]
        pos = max(min(pos,self._maxDragPosition),self._minDragPosition)
        pos = int(pos/FlexGrid._rasterSize)*FlexGrid._rasterSize
        
        self._draggedSpacer.y = pos-sh
        
        for p in self._rightPanes:
            y = p.bottom
            p.y = pos+sh
            p.height = y-pos-sh
    
        for p in self._leftPanes:
            p.height = pos-p.y-sh
            
    ## Handles mouse up event of a spacer. 
    #
    #
    def __onMouseUp(self,ev:biui.MouseEvent)->None:
        self.onMouseMove.remove(self.__onVerticalMouseMove)
        self.onMouseMove.remove(self.__onHorizontalMouseMove)
        self.onMouseUp.remove(self.__onMouseUp)
        self._draggedSpacer = None
        ev.stopPropagation()
    
    def _redraw(self, surface, forceRedraw=False)->None:
        
        if not self.isInvalide():
            if not forceRedraw:
                return
                    
        #print("Pane::_redraw")
        pos = self.position
        
        # we paint on our own surface
        # not on the parent's surface
        _surface = self._surface
        theme = biui.getTheme()
        theme.drawFlexGridBeforeChildren(self,_surface)

        forceRedraw = self.isInvalide() or forceRedraw
        
        # We draw all Children on our own surface        
        for c in self._children:
            c._redraw(_surface,forceRedraw)
                    
        theme.drawFlexGridAfterChildren(self,_surface)
        
        # Now we copy the visible area 
        # of our own surface
        # on the parent's surface
        surface.blit(_surface,pos,(0,0,self.width,self.height))
        
    def _calculateLayout(self):
        
        if not self.isInvalide():
            return 

        super()._calculateLayout()
        
        self._isInvalide = False
        