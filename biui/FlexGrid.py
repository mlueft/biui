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
    
    ##
    #
    #   
    def childVerticalSplit(self,ev:biui.Event)->None:
        
        #print("childVerticalSplit")
        oldPane = ev.getEventSource()
        
        if oldPane.getWidth() <= 2*oldPane.getMinWidth():
            return
        
        newPane = biui.FlexPane()
        newPane.setX(oldPane.getX()+oldPane.getWidth()/2+FlexGrid._spacerWidth/2)
        newPane.setY(oldPane.getY())
        newPane.setHeight(oldPane.getHeight())
        newPane.setWidth(oldPane.getWidth()/2-FlexGrid._spacerWidth/2)
        
        oldPane.setWidth(newPane.getWidth())
        
        spacer = self._createSpacer()
        spacer.setX(oldPane.getRight() )
        spacer.setY(oldPane.getY())
        spacer.setHeight(oldPane.getHeight())
        
        self.addFlexPane(newPane)
        self.addHorizontalSpacer(spacer)
        
        self.__onHorizontalSpacerDown(biui.Event(spacer))
        
    ##
    #
    #
    def childHorizontalSplit(self,ev:biui.Event)->None:
        #print("childHorizontalSplit")
        oldPane = ev.getEventSource()

        if oldPane.getHeight() <= 2*oldPane.getMinHeight():
            return
                
        newPane = biui.FlexPane()
        newPane.setX(oldPane.getX())
        newPane.setY(oldPane.getY()+oldPane.getHeight()/2+FlexGrid._spacerWidth/2)
        newPane.setWidth(oldPane.getWidth())
        newPane.setHeight(oldPane.getHeight()/2-FlexGrid._spacerWidth/2)
        
        oldPane.setHeight(newPane.getHeight())
        
        spacer = self._createSpacer()
        spacer.setX(oldPane.getX())
        spacer.setY(oldPane.getBottom())
        spacer.setWidth(oldPane.getWidth())
        
        self.addFlexPane(newPane)
        self.addVerticalSpacer(spacer)
        
        self.__onVerticalSpacerDown(biui.Event(spacer))

    ##
    #
    #
    def _createSpacer(self)->biui.FlexSpacer:
        spacer = biui.FlexSpacer()
        spacer.setHeight(FlexGrid._spacerWidth)
        spacer.setWidth(FlexGrid._spacerWidth)
        spacer.setAlignment(biui.Alignment.ABSOLUTE)
        return spacer  
          
    ##
    #
    #
    def __recreateVerticalSpacer(self, stayPane,spacer):
        #print("__recreateVerticalSpacer")
        # we have to differtiate four cases:
        # 1. The spacer is at the same width of the pane. => remove it
        # 2. The spacer is wider than the pane. => we need to split the spacer
        # 3. The spacer lays at the right end of the pane. => fix width
        # 4. The spacer lays the the left end of the Pane. => move it and fix width
        if spacer.getX() == stayPane.getX() and spacer.getWidth() == stayPane.getWidth():
            # Case 1
            self.removeHorizontalSpacer(spacer)
        elif spacer.getX() == stayPane.getX():
            # Case 4
            spacer.setX( stayPane.getRight()+FlexGrid._spacerWidth )
            spacer.setWidth(spacer.getWidth()-stayPane.getWidth()-FlexGrid._spacerWidth)
            
        elif spacer.getRight() == stayPane.getRight():
            # case 3
            spacer.setWidth(spacer.getWidth()-stayPane.getWidth()-FlexGrid._spacerWidth)
            
        else:
            # case 2
            ow = spacer.getWidth()

            spacer.setWidth( stayPane.getX()-FlexGrid._spacerWidth-spacer.getX())
            
            newSplitter = self._createSpacer()
            newSplitter.setY(spacer.getY())
            newSplitter.setX(stayPane.getRight()+FlexGrid._spacerWidth)
            w = spacer.getX()+ow-newSplitter.getX()

            newSplitter.setWidth(w)
            self.addVerticalSpacer(newSplitter)
                
    ##
    #
    #
    def __recreateHorizontalSpacer(self, stayPane,spacer):
        #print("__recreateVerticalSpacer")
        # we have to differtiate four cases:
        # 1. The spacer is at the same height of the pane. => remove it
        # 2. The spacer is higher than the pane. => we need to split the spacer
        # 3. The spacer lays at the lower end of the pane. => fix height
        # 4. The spacer lays the the lower end of the Pane. => move it and fix height
        if spacer.getY() == stayPane.getY() and spacer.getHeight() == stayPane.getHeight():
            #print("1")
            # Case 1
            self.removeVerticalSpacer(spacer)
        elif spacer.getY() == stayPane.getY():
            #print("4")
            # Case 4
            spacer.setY( stayPane.getBottom()+FlexGrid._spacerWidth )
            w = spacer.getHeight()-stayPane.getHeight()-FlexGrid._spacerWidth
            spacer.setHeight(w)
            
        elif spacer.getBottom() == stayPane.getBottom():
            #print("3")
            # case 3
            w = spacer.getHeight()-stayPane.getHeight()-FlexGrid._spacerWidth
            spacer.setHeight(w)
            
        else:
            #print("2")
            # case 2
            ow = spacer.getHeight()

            spacer.setHeight( stayPane.getY()-FlexGrid._spacerWidth-spacer.getY())
            
            newSpacer = self._createSpacer()
            newSpacer.setX(spacer.getX())
            newSpacer.setY(stayPane.getBottom()+FlexGrid._spacerWidth)
            w = spacer.getY()+ow-newSpacer.getY()
            newSpacer.setHeight(w)
            self.addHorizontalSpacer(newSpacer)
            
    ##
    #
    #
    def childJoinUp(self,ev:biui.Event)->None:
        self.__simplifySpacer()
        stayPane = ev.getEventSource()
        
        removePane = None
        # We are looking for a Pane with the same width
        # at the same x position
        # with a distance above of the spacer width
        for p in self._panes:
            if p.getX() == stayPane.getX():
                if p.getWidth() == stayPane.getWidth():
                    if stayPane.getY()-p.getY()-p.getHeight() == FlexGrid._spacerWidth:
                        removePane = p
                        break
        
        if removePane == None:
            return
        
        spacer = None
        # we are looking for the spacer above the stayPane
        for s in self._spacers:
            if stayPane.getX() >= s.getX():
                if stayPane.getX() <= s.getLeft():
                    if s.getBottom() == stayPane.getY():
                        spacer = s
                        break

        self.__recreateVerticalSpacer(stayPane,spacer)
        
        stayPane.setY(removePane.getY())
        stayPane.setHeight(stayPane.getHeight()+removePane.getHeight()+FlexGrid._spacerWidth)
        
        self.removeFlexPane(removePane)
                
    ##
    #
    #
    def childJoinDown(self,ev:biui.Event)->None:
        self.__simplifySpacer()
        stayPane = ev.getEventSource()
        
        removePane = None
        # We are looking for a Pane with the same width
        # at the same x position
        # with a distance below of the spacer width
        for p in self._panes:
            if p.getX() == stayPane.getX():
                if p.getWidth() == stayPane.getWidth():
                    if p.getY()-stayPane.getBottom() == FlexGrid._spacerWidth:
                        removePane = p
                        break
        
        if removePane == None:
            return
        
        spacer = None
        # we are looking for the spacer below the stayPane
        for s in self._spacers:
            if stayPane.getX() >= s.getX():
                if stayPane.getX() <= s.getRight():
                    if s.getBottom() == removePane.getY():
                        spacer = s
                        break


        self.__recreateVerticalSpacer(stayPane,spacer)
        
        stayPane.setHeight(stayPane.getHeight()+removePane.getHeight()+FlexGrid._spacerWidth)
        
        self.removeFlexPane(removePane)
                
    ##
    #
    #
    def childJoinLeft(self,ev:biui.Event)->None:
        self.__simplifySpacer()
        stayPane = ev.getEventSource()
        
        removePane = None
        # We are looking for a Pane with the same height
        # at the same y position
        # with a distance left of the spacer width
        for p in self._panes:
            if p.getY() == stayPane.getY():
                if p.getHeight() == stayPane.getHeight():
                    if stayPane.getX()-p.getX()-p.getWidth() == FlexGrid._spacerWidth:
                        removePane = p
                        break
                       
        if removePane == None:
            return
        
        spacer = None
        # we are looking for the left above the stayPane
        for s in self._spacers:
            if stayPane.getY() >= s.getY():
                if stayPane.getY() <= s.getBottom():
                    if s.getX()+s.getWidth() == stayPane.getX():
                        spacer = s
                        break
                    
        self.__recreateHorizontalSpacer(stayPane,spacer)
        
        stayPane.setX(removePane.getX())
        stayPane.setWidth(stayPane.getWidth()+removePane.getWidth()+FlexGrid._spacerWidth)
        
        self.removeFlexPane(removePane)
                
    ##
    #
    #
    def childJoinRight(self,ev:biui.Event)->None:
        self.__simplifySpacer()
        stayPane = ev.getEventSource()
        
        removePane = None
        # We are looking for a Pane with the same height
        # at the same y position
        # with a distance left of the spacer width
        for p in self._panes:
            if p.getY() == stayPane.getY():
                if p.getHeight() == stayPane.getHeight():
                    if p.getX()-stayPane.getRight() == FlexGrid._spacerWidth:
                        removePane = p
                        break
        
        if removePane == None:
            return
        
        spacer = None
        # we are looking for the spacer right the stayPane
        for s in self._spacers:
            if stayPane.getY() >= s.getY():
                if stayPane.getY() <= s.getBottom():
                    if s.getX()+s.getWidth() == removePane.getX():
                        spacer = s
                        break


        self.__recreateHorizontalSpacer(stayPane,spacer)
        
        stayPane.setWidth(stayPane.getWidth()+removePane.getWidth()+FlexGrid._spacerWidth)
        
        self.removeFlexPane(removePane)
        
            
    ##
    #
    #
    def addFlexPane(self,child:biui.FlexPane)->None:
        child.setAlignment(biui.Alignment.ABSOLUTE)
        super().addChild(child)
        child.onHorizontalSplit.add( self.childHorizontalSplit )
        child.onVerticalSplit.add( self.childVerticalSplit )
        child.onJoinRight.add( self.childJoinRight )
        child.onJoinLeft.add( self.childJoinLeft )
        child.onJoinDown.add( self.childJoinDown )
        child.onJoinUp.add( self.childJoinUp )
        
        child.onMouseUp.add( self.myPaneMouseeUp )

        self._panes.append(child)
        
    def myPaneMouseeUp(self, ev):
        print( "panes:   "+str(len(self._panes)))
        print( "spacers: "+str(len(self._spacers)))
        print( self._draggedSpacer )
    ##
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
        
    ##
    #
    #           
    def addHorizontalSpacer(self,child:biui.FlexSpacer)->None:
        child.onMouseDown.add(self.__onHorizontalSpacerDown)
        super().addChild(child)
        self._spacers.append(child)
        
    ##
    #
    #
    def removeHorizontalSpacer(self,child:biui.FlexSpacer)->None:
        child.onMouseDown.remove(self.__onHorizontalSpacerDown)
        super().removeChild(child)
        self._spacers.remove(child)

    ##
    #
    #           
    def addVerticalSpacer(self,child:biui.FlexSpacer)->None:
        child.onMouseDown.add(self.__onVerticalSpacerDown)
        super().addChild(child)
        self._spacers.append(child)
        
    ##
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
                if s0.getY() == s1.getY():
                    if s0.getRight()+FlexGrid._spacerWidth == s1.getX():
                        # horizontally side by side
                        s0.setWidth( s0.getWidth()+s1.getWidth()+FlexGrid._spacerWidth )
                        if s1 == self._draggedSpacer:
                            self._draggedSpacer  = s0
                        self.removeHorizontalSpacer(s1)
                        return self.__simplifySpacer()
                elif s0.getX() == s1.getX():
                    if s0.getBottom()+FlexGrid._spacerWidth == s1.getY():
                        # vertically side by side
                        s0.setHeight( s0.getHeight()+s1.getHeight()+FlexGrid._spacerWidth )
                        if s1 == self._draggedSpacer:
                            self._draggedSpacer  = s0
                        self.removeHorizontalSpacer(s1)
                        return self.__simplifySpacer()      
                  
    ## Finds panes touching the dragged spacer
    # and sorts them to left or right
    #
    #
    def __determineNeighbours(self):
        self._leftPanes = []
        self._rightPanes = []
        
        s = self._draggedSpacer
        sl = s.getX()
        sr = s.getRight()
        st = s.getY()
        sb = s.getBottom()
        
        dragMin = 0
        dragMax = max(self.getWidth(),self.getHeight())
        
        if s.getWidth() == FlexGrid._spacerWidth:
            # vertical spacer
            # we are looking for panes above or below the
            # spacer
            # Spacers can be neighbours too.
            for p in self._panes+self._spacers:
                if p.getY() >= st:
                    if p.getBottom() <= sb:
                        if abs(p.getX()-sr) < FlexGrid._spacerWidth/2:
                            # pane is right
                            self._rightPanes.append(p)
                            dragMax = min(dragMax,p.getRight()-p.getMinWidth()-FlexGrid._spacerWidth/2)
                        elif abs(p.getRight()-sl) < FlexGrid._spacerWidth/2:
                            # pane is left
                            self._leftPanes.append(p)
                            dragMin = max(dragMin,p.getX()+p.getMinWidth()+FlexGrid._spacerWidth/2)
        else:
            # horizontal spacer
            # we are looking for panes left or 
            # right the spacer
            # Spacers can be neighbours too.
            for p in self._panes+self._spacers:
                if p.getX() >= sl:
                    if p.getRight() <= sr:
                        if abs(p.getY()-sb) < FlexGrid._spacerWidth/2:
                            # pane is below
                            self._rightPanes.append(p)
                            dragMax = min(dragMax,p.getBottom()-p.getMinHeight()-FlexGrid._spacerWidth/2)
                        elif abs(p.getBottom()-st) < FlexGrid._spacerWidth/2:
                            # pane is above
                            self._leftPanes.append(p)
                            dragMin = max(dragMin,p.getY()+p.getMinHeight()+FlexGrid._spacerWidth/2)
        
        self._minDragPosition = int(dragMin/self._rasterSize)*self._rasterSize + FlexGrid._rasterSize
        self._maxDragPosition = int(dragMax/self._rasterSize)*self._rasterSize - FlexGrid._rasterSize
        
    ##
    #
    #
    def __onHorizontalSpacerDown(self,ev:biui.MouseEvent)->None:
        #print("__onHorizontalSpacerDown")
        
        # Store dragged spacer.
        self._draggedSpacer = ev.getEventSource()
        
        # simplify spacers.
        self.__simplifySpacer()
        
        # Determine neighbours.
        # Determine min and max drag position.
        self.__determineNeighbours()
        
        self.onMouseMove.add(self.__onVerticalMouseMove)
        self.onMouseUp.add(self.__onMouseUp)
        
    ##
    #
    #
    def __onVerticalSpacerDown(self,ev:biui.MouseEvent)->None:
        #print("__onVerticalSpacerDown")
        
        # Store dragged spacer.
        self._draggedSpacer = ev.getEventSource()
        
        # simplify spacers.
        self.__simplifySpacer()
        
        # Determine neighbours.
        # Determine min and max drag position.
        self.__determineNeighbours()
        
        self.onMouseMove.add(self.__onHorizontalMouseMove)
        self.onMouseUp.add(self.__onMouseUp)
        
    ##
    #
    #
    def __onVerticalMouseMove(self,ev:biui.MouseEvent)->None:
        sh = FlexGrid._spacerWidth/2
        
        pos = self.toLocal(ev.getPosition())[0]
        pos = max(min(pos,self._maxDragPosition),self._minDragPosition)
        pos = int(pos/FlexGrid._rasterSize)*FlexGrid._rasterSize
        
        self._draggedSpacer.setX(pos-sh)
        
        for p in self._rightPanes:
            x = p.getRight()
            p.setX( pos+sh )
            p.setWidth( x-pos-sh )
    
        for p in self._leftPanes:
            p.setWidth( pos-p.getX()-sh )
        
    ##
    #
    #
    def __onHorizontalMouseMove(self,ev:biui.MouseEvent)->None:
        
        sh = FlexGrid._spacerWidth/2
        
        pos = self.toLocal(ev.getPosition())[1]
        pos = max(min(pos,self._maxDragPosition),self._minDragPosition)
        pos = int(pos/FlexGrid._rasterSize)*FlexGrid._rasterSize
        
        self._draggedSpacer.setY(pos-sh)
        
        for p in self._rightPanes:
            y = p.getBottom()
            p.setY( pos+sh )
            p.setHeight( y-pos-sh )
    
        for p in self._leftPanes:
            p.setHeight( pos-p.getY()-sh )
            
    ##
    #
    #
    def __onMouseUp(self,ev:biui.MouseEvent)->None:
        print("FlexGrid::onMouseUp")
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
        pos = self.getPosition()
        
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
        surface.blit(_surface,pos,(0,0,self.getWidth(),self.getHeight()))
        
    def _calculateLayout(self):
        
        if not self.isInvalide():
            return 
        
        #print("resize")
                
        super()._calculateLayout()
        
        self._isInvalide = False
        