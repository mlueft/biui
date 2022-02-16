import biui

##
#
#
class FlexGrid(biui.ContainerWidget.ContainerWidget):
    
    #
    _spacerWidth = 4
    
    #
    _rasterSize = 3
    
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
        
        # TODO: Split is just allowed if the width
        # of the old panel is min. 2.minSize
        
        oldPane = ev.getEventSource()
        
        newPane = biui.FlexPane()
        newPane.setX(oldPane.getX()+oldPane.getWidth()/2+FlexGrid._spacerWidth/2)
        newPane.setY(oldPane.getY())
        newPane.setHeight(oldPane.getHeight())
        newPane.setWidth(oldPane.getWidth()/2-FlexGrid._spacerWidth/2)
        
        oldPane.setWidth(newPane.getWidth())
        
        spacer = self._createSpacer()
        spacer.setX(oldPane.getX()+oldPane.getWidth() )
        spacer.setY(oldPane.getY())
        spacer.setHeight(oldPane.getHeight())
        
        self.addFlexPane(newPane)
        self.addHorizontalSpacer(spacer)
        
        self.__onHorizontalSpacerDown(biui.Event(spacer))
        
    ##
    #
    #
    def childHorizontalSplit(self,ev:biui.Event)->None:
        
        # TODO: Split is just allowed if the width
        # of the old panel is min. 2.minSize
        
        oldPane = ev.getEventSource()
        
        newPane = biui.FlexPane()
        newPane.setX(oldPane.getX())
        newPane.setY(oldPane.getY()+oldPane.getHeight()/2+FlexGrid._spacerWidth/2)
        newPane.setWidth(oldPane.getWidth())
        newPane.setHeight(oldPane.getHeight()/2-FlexGrid._spacerWidth/2)
        
        oldPane.setHeight(newPane.getHeight())
        
        spacer = self._createSpacer()
        spacer.setX(oldPane.getX())
        spacer.setY(oldPane.getY()+oldPane.getHeight())
        spacer.setWidth(oldPane.getWidth())
        
        self.addFlexPane(newPane)
        self.addVerticalSpacer(spacer)
        
        self.__onVerticalSpacerDown(biui.Event(spacer))

    ##
    #
    #
    def _createSpacer(self)->biui.FlexSpacer:
        spacer = biui.Button()
        spacer.setHeight(FlexGrid._spacerWidth)
        spacer.setWidth(FlexGrid._spacerWidth)
        spacer.setAlignment(biui.Alignment.ABSOLUTE)
        return spacer        
    ##
    #
    #
    def childJoinUp(self,ev:biui.Event)->None:
        print("onJoinUp")
    
    ##
    #
    #
    def childJoinRight(self,ev:biui.Event)->None:
        print("onJoinRight")
    
    ##
    #
    #
    def childJoinDown(self,ev:biui.Event)->None:
        print("onJoinDown")
    
    ##
    #
    #
    def childJoinLeft(self,ev:biui.Event)->None:
        print("onJoinLeft")
            
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
        
        child.onMouseUp.add( self.myPaneClick )
        self._panes.append(child)
        
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
         
        child.onMouseUp.remove( self.myPaneClick )
        
    def myPaneClick(self,ev:biui.MouseEvent)->None:
        print("spacers:"+str(len(self._spacers)))
        print("right:"+str(len(self._rightPanes)))
        print("left:"+str(len(self._leftPanes)))
    
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
                    if s0.getX()+s0.getWidth()+FlexGrid._spacerWidth == s1.getX():
                        # horizontally side by side
                        s0.setWidth( s0.getWidth()+s1.getWidth()+FlexGrid._spacerWidth )
                        self.removeHorizontalSpacer(s1)
                        return self.__simplifySpacer()
                elif s0.getX() == s1.getX():
                    if s0.getY()+s0.getHeight()+FlexGrid._spacerWidth == s1.getY():
                        # vertically side by side
                        s0.setHeight( s0.getHeight()+s1.getHeight()+FlexGrid._spacerWidth )
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
        sr = s.getX()+s.getWidth()
        st = s.getY()
        sb = s.getY()+s.getHeight()
        
        dragMin = 0
        dragMax = max(self.getWidth(),self.getHeight())
        
        if s.getWidth() == FlexGrid._spacerWidth:
            # vertical spacer
            # we are looking for panes above or below the
            # spacer
            # Spacers can be neighbours too.
            for p in self._panes+self._spacers:
                if p.getY() >= st:
                    if p.getY()+p.getHeight() <= sb:
                        if abs(p.getX()-sr) < FlexGrid._spacerWidth/2:
                            # pane is right
                            self._rightPanes.append(p)
                            dragMax = min(dragMax,p.getX()+p.getWidth()-p.getMinWidth())
                        elif abs(p.getX()+p.getWidth()-sl) < FlexGrid._spacerWidth/2:
                            # pane is left
                            self._leftPanes.append(p)
                            dragMin = max(dragMin,p.getX()+p.getMinWidth())
        else:
            # horizontal spacer
            # we are looking for panes left or 
            # right the spacer
            # Spacers can be neighbours too.
            for p in self._panes+self._spacers:
                if p.getX() >= sl:
                    if p.getX()+p.getWidth() <= sr:
                        if abs(p.getY()-sb) < FlexGrid._spacerWidth/2:
                            # pane is below
                            self._rightPanes.append(p)
                            dragMax = min(dragMax,p.getY()+p.getHeight()-p.getMinHeight())
                        elif abs(p.getY()+p.getHeight()-st) < FlexGrid._spacerWidth/2:
                            # pane is above
                            self._leftPanes.append(p)
                            dragMin = max(dragMin,p.getY()+p.getMinHeight())
        
        self._minDragPosition = int(dragMin/self._rasterSize)*self._rasterSize + 2*FlexGrid._rasterSize
        self._maxDragPosition = int(dragMax/self._rasterSize)*self._rasterSize - FlexGrid._rasterSize
        
    ##
    #
    #
    def __onHorizontalSpacerDown(self,ev:biui.MouseEvent)->None:
        print("__onHorizontalSpacerDown")
        
        # Store dragged spacer.
        self._draggedSpacer = ev.getEventSource()
        
        # simplify spacers.
        self.__simplifySpacer()
        
        # TODO: The event source could be removed now
        
        # Determine neighbours.
        # Determine min and max drag position.
        self.__determineNeighbours()
        
        self.onMouseMove.add(self.__onVerticalMouseMove)
        self.onMouseUp.add(self.__onMouseUp)
        
    ##
    #
    #
    def __onVerticalSpacerDown(self,ev:biui.MouseEvent)->None:
        print("__onVerticalSpacerDown")
        
        # Store dragged spacer.
        self._draggedSpacer = ev.getEventSource()
        
        # simplify spacers.
        self.__simplifySpacer()
        
        # TODO: The event source could be removed now
        
        # Determine neighbours.
        # Determine min and max drag position.
        self.__determineNeighbours()
        
        self.onMouseMove.add(self.__onHoritontalMouseMove)
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
            x = p.getX()+p.getWidth()
            p.setX( pos+sh )
            p.setWidth( x-pos-sh )
    
        for p in self._leftPanes:
            p.setWidth( pos-p.getX()-sh )
        
    ##
    #
    #
    def __onHoritontalMouseMove(self,ev:biui.MouseEvent)->None:
        
        sh = FlexGrid._spacerWidth/2
        
        pos = self.toLocal(ev.getPosition())[1]
        pos = max(min(pos,self._maxDragPosition),self._minDragPosition)
        pos = int(pos/FlexGrid._rasterSize)*FlexGrid._rasterSize
        
        self._draggedSpacer.setY(pos-sh)
        
        for p in self._rightPanes:
            y = p.getY()+p.getHeight()
            p.setY( pos+sh )
            p.setHeight( y-pos-sh )
    
        for p in self._leftPanes:
            p.setHeight( pos-p.getY()-sh )
            
    
    ##
    #
    #
    def __onMouseUp(self,ev:biui.MouseEvent)->None:
        print("onMouseUp")
        self.onMouseMove.remove(self.__onVerticalMouseMove)
        self.onMouseMove.remove(self.__onHoritontalMouseMove)
        self.onMouseUp.remove(self.__onMouseUp)
        self._draggedSpacer = None
        ev.stopPropagation()

    
    
    def _redraw(self, surface )->None:
        #print("Pane::_redraw")
        pos = self.getPosition()
        
        # we paint on our own surface
        # not on the parent's surface
        _surface = self._surface
        theme = biui.getTheme()
        theme.drawFlexGridBeforeChildren(self,_surface)

        # We draw all Children on our own surface        
        for c in self._children:
            c._redraw(_surface)
                    
        theme.drawFlexGridAfterChildren(self,_surface)
        
        # Now we copy the visible area 
        # of our own surface
        # on the parent's surface
        surface.blit(_surface,pos,(0,0,self.getWidth(),self.getHeight()))
        