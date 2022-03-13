import biui

##
#
#
class FlexPane(biui.ContainerWidget.ContainerWidget):
    
    def __init__(self):
        super().__init__()
        self._minWidth = 40
        self._minHeight = 40
        
        #
        self.onJoinUp = biui.EventManager()
        #
        self.onJoinDown = biui.EventManager()
        #
        self.onJoinLeft = biui.EventManager()
        #
        self.onJoinRight = biui.EventManager()
        #
        self.onVerticalSplit = biui.EventManager()
        #
        self.onHorizontalSplit = biui.EventManager()
        
        self._acTopLeft = self._createActiveCorner()
        self._acTopLeft.onMouseDown.add(self._onActiveCornerTopLeftMouseDown)
        self._acTopLeft.onMouseUp.add(self._onActiveCornerTopLeftMouseUp)
        self._acTopLeft.setAlignment(biui.Alignment.TOP_LEFT)
        self.addChild(self._acTopLeft)
        
        self._acTopRight = self._createActiveCorner()
        self._acTopRight.onMouseDown.add(self._onActiveCornerTopRightMouseDown)
        self._acTopRight.onMouseUp.add(self._onActiveCornerTopRightMouseUp)
        self._acTopRight.setAlignment(biui.Alignment.TOP_RIGHT)
        self.addChild(self._acTopRight)

        self._acBottomLeft = self._createActiveCorner()
        self._acBottomLeft.onMouseDown.add(self._onActiveCornerBottomLeftMouseDown)
        self._acBottomLeft.onMouseUp.add(self._onActiveCornerBottomLeftMouseUp)
        self._acBottomLeft.setAlignment(biui.Alignment.BOTTOM_LEFT)
        self.addChild(self._acBottomLeft)
        
        self._acBottomRight = self._createActiveCorner()
        self._acBottomRight.onMouseDown.add(self._onActiveCornerBottomRightMouseDown)
        self._acBottomRight.onMouseUp.add(self._onActiveCornerBottomRightMouseUp)
        self._acBottomRight.setAlignment(biui.Alignment.BOTTOM_RIGHT)
        self.addChild(self._acBottomRight)
        
        
    def _onActiveCornerTopLeftMouseDown(self,ev):
        self._acTopLeft.onMouseLeave.add(self.onActiveCornerTopLeftLeave)
    
    def _onActiveCornerTopRightMouseDown(self,ev):
        self._acTopRight.onMouseLeave.add(self.onActiveCornerTopRightLeave)
    
    def _onActiveCornerBottomLeftMouseDown(self,ev):
        self._acBottomLeft.onMouseLeave.add(self.onActiveCornerBottomLeftLeave)
    
    def _onActiveCornerBottomRightMouseDown(self,ev):
        self._acBottomRight.onMouseLeave.add(self.onActiveCornerBottomRightLeave)


    def _onActiveCornerTopLeftMouseUp(self,ev):
        self._acTopLeft.onMouseLeave.remove(self.onActiveCornerTopLeftLeave)
    
    def _onActiveCornerTopRightMouseUp(self,ev):
        self._acTopRight.onMouseLeave.remove(self.onActiveCornerTopRightLeave)
    
    def _onActiveCornerBottomLeftMouseUp(self,ev):
        self._acBottomLeft.onMouseLeave.remove(self.onActiveCornerBottomLeftLeave)
    
    def _onActiveCornerBottomRightMouseUp(self,ev):
        self._acBottomRight.onMouseLeave.remove(self.onActiveCornerBottomRightLeave)
        
    ##
    #
    #
    def _createActiveCorner(self):
        ac = biui.Pane()
        ac.setWidth(25)
        ac.setHeight(25)
        return ac
        
    ##
    #
    #
    def onActiveCornerTopLeftLeave(self,ev):

        ac = ev.getEventSource()
        pos = ac.toLocal(ev.getPosition())
        
        if pos[0] <= 0:
            self.onJoinLeft.provoke(biui.Event(self))
        elif pos[1] <= 0:
            self.onJoinUp.provoke(biui.Event(self)) 
        elif pos[0] >= ac.getWidth():
            self.onVerticalSplit.provoke(biui.Event(self))
        else:
            self.onHorizontalSplit.provoke(biui.Event(self))
     
        self._acTopLeft.onMouseLeave.remove(self.onActiveCornerTopLeftLeave)
        
    ##
    #
    #
    def onActiveCornerTopRightLeave(self,ev):

        ac = ev.getEventSource()
        pos = ac.toLocal(ev.getPosition())
        
        if pos[0] <= 0:
            self.onVerticalSplit.provoke(biui.Event(self))
        elif pos[1] >= ac.getHeight():
            self.onHorizontalSplit.provoke(biui.Event(self))
        elif pos[0] >= ac.getWidth():
            self.onJoinRight.provoke(biui.Event(self)) 
        else:
            self.onJoinUp.provoke(biui.Event(self))

        self._acTopRight.onMouseLeave.remove(self.onActiveCornerTopRightLeave)
        
    ##
    #
    #
    def onActiveCornerBottomLeftLeave(self,ev):

        ac = ev.getEventSource()
        pos = ac.toLocal(ev.getPosition())
        
        if pos[0] <= 0:
            self.onJoinLeft.provoke(biui.Event(self))
        elif pos[1] >= ac.getHeight():
            self.onJoinDown.provoke(biui.Event(self))
        elif pos[0] >= ac.getWidth():
            self.onVerticalSplit.provoke(biui.Event(self)) 
        else:
            self.onHorizontalSplit.provoke(biui.Event(self))
            
        self._acBottomLeft.onMouseLeave.remove(self.onActiveCornerBottomLeftLeave)
        
    ##
    #
    #
    def onActiveCornerBottomRightLeave(self,ev):

        ac = ev.getEventSource()
        pos = ac.toLocal(ev.getPosition())
        
        if pos[0] <= 0:
            self.onVerticalSplit.provoke(biui.Event(self))
        elif pos[1] >= ac.getHeight():
            self.onJoinDown.provoke(biui.Event(self))
        elif pos[0] >= ac.getWidth():
            self.onJoinRight.provoke(biui.Event(self)) 
        else:
            self.onHorizontalSplit.provoke(biui.Event(self))
        
        self._acBottomRight.onMouseLeave.remove(self.onActiveCornerBottomRightLeave)
        
    def _redraw(self, surface, forceRedraw=False):
        
        if not self.isInvalide():
            if not forceRedraw:
                return 
                
        #print("FlexPane::_redraw")
        pos = self.getPosition()
        
        # we paint on our own surface
        # not on the parent's surface
        _surface = self._surface
        theme = biui.getTheme()
        theme.drawFlexPaneBeforeChildren(self,_surface)

        forceRedraw = self.isInvalide() or forceRedraw
        # We draw all Children on our own surface        
        for c in self._children:
            c._redraw(_surface,forceRedraw)
                    
        theme.drawFlexPaneAfterChildren(self,_surface)
        
        # Now we copy the visible area 
        # of our own surface
        # on the parent's surface
        surface.blit(_surface,pos,(0,0,self.getWidth(),self.getHeight()))
        
        self._isInvalide = False        
                