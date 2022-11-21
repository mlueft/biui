import biui

###
##
##
class FlexPane(biui.ContainerWidget.ContainerWidget):
    
    def __init__(self):
        super().__init__()
        self._minWidth = 40
        self._minHeight = 40
        
        theme = biui.getTheme()
        self._themeBackgroundfunction = theme.drawFlexPaneBeforeChildren
        self._themeForegroundfunction = theme.drawFlexPaneAfterChildren
                
        ##
        self.onJoinUp = biui.EventManager()
        ##
        self.onJoinDown = biui.EventManager()
        ##
        self.onJoinLeft = biui.EventManager()
        ##
        self.onJoinRight = biui.EventManager()
        ##
        self.onVerticalSplit = biui.EventManager()
        ##
        self.onHorizontalSplit = biui.EventManager()
        
        self._acTopLeft = self._createActiveCorner()
        self._acTopLeft.onMouseDown.add(self._onActiveCornerTopLeftMouseDown)
        self._acTopLeft.onMouseUp.add(self._onActiveCornerTopLeftMouseUp)
        self._acTopLeft.alignment = biui.Alignment.TOP_LEFT
        self.addChild(self._acTopLeft)
        
        self._acTopRight = self._createActiveCorner()
        self._acTopRight.onMouseDown.add(self._onActiveCornerTopRightMouseDown)
        self._acTopRight.onMouseUp.add(self._onActiveCornerTopRightMouseUp)
        self._acTopRight.alignment = biui.Alignment.TOP_RIGHT
        self.addChild(self._acTopRight)

        self._acBottomLeft = self._createActiveCorner()
        self._acBottomLeft.onMouseDown.add(self._onActiveCornerBottomLeftMouseDown)
        self._acBottomLeft.onMouseUp.add(self._onActiveCornerBottomLeftMouseUp)
        self._acBottomLeft.alignment = biui.Alignment.BOTTOM_LEFT
        self.addChild(self._acBottomLeft)
        
        self._acBottomRight = self._createActiveCorner()
        self._acBottomRight.onMouseDown.add(self._onActiveCornerBottomRightMouseDown)
        self._acBottomRight.onMouseUp.add(self._onActiveCornerBottomRightMouseUp)
        self._acBottomRight.alignment = biui.Alignment.BOTTOM_RIGHT
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
        
    ### Returns a widget used as a active corner.
    ##
    ##
    def _createActiveCorner(self):
        ## We use a Spacer to get
        ## an invisible corner
        ac = biui.Spacer()
        ac.width = 25
        ac.height = 25
        return ac
        
    ### Handles mouse leave event of the top left active corner.
    ##  It provokes split or join events if necessary.
    ##
    def onActiveCornerTopLeftLeave(self,ev):

        ac = ev.eventSource
        pos = ac.toLocal(ev.position)
        
        if pos[0] <= 0:
            self.onJoinLeft.provoke(biui.Event(self))
        elif pos[1] <= 0:
            self.onJoinUp.provoke(biui.Event(self)) 
        elif pos[0] >= ac.width:
            self.onVerticalSplit.provoke(biui.Event(self))
        else:
            self.onHorizontalSplit.provoke(biui.Event(self))
     
        self._acTopLeft.onMouseLeave.remove(self.onActiveCornerTopLeftLeave)
        
    ### Handles mouse leave event of the top right active corner.
    ##  It provokes split or join events if necessary.
    ##
    def onActiveCornerTopRightLeave(self,ev):

        ac = ev.eventSource
        pos = ac.toLocal(ev.position)
        
        if pos[0] <= 0:
            self.onVerticalSplit.provoke(biui.Event(self))
        elif pos[1] >= ac.height:
            self.onHorizontalSplit.provoke(biui.Event(self))
        elif pos[0] >= ac.width:
            self.onJoinRight.provoke(biui.Event(self)) 
        else:
            self.onJoinUp.provoke(biui.Event(self))

        self._acTopRight.onMouseLeave.remove(self.onActiveCornerTopRightLeave)
        
    ### Handles mouse leave event of the bottom left active corner.
    ##  It provokes split or join events if necessary.
    ##
    def onActiveCornerBottomLeftLeave(self,ev):

        ac = ev.eventSource
        pos = ac.toLocal(ev.position)
        
        if pos[0] <= 0:
            self.onJoinLeft.provoke(biui.Event(self))
        elif pos[1] >= ac.height:
            self.onJoinDown.provoke(biui.Event(self))
        elif pos[0] >= ac.width:
            self.onVerticalSplit.provoke(biui.Event(self)) 
        else:
            self.onHorizontalSplit.provoke(biui.Event(self))
            
        self._acBottomLeft.onMouseLeave.remove(self.onActiveCornerBottomLeftLeave)
        
    ### Handles mouse leave event of the bottom right active corner.
    ##  It provokes split or join events if necessary.
    ##
    def onActiveCornerBottomRightLeave(self,ev):

        ac = ev.eventSource
        pos = ac.toLocal(ev.position)
        
        if pos[0] <= 0:
            self.onVerticalSplit.provoke(biui.Event(self))
        elif pos[1] >= ac.height:
            self.onJoinDown.provoke(biui.Event(self))
        elif pos[0] >= ac.width:
            self.onJoinRight.provoke(biui.Event(self)) 
        else:
            self.onHorizontalSplit.provoke(biui.Event(self))
        
        self._acBottomRight.onMouseLeave.remove(self.onActiveCornerBottomRightLeave)
        
    def _redraw1(self, texture, forceRedraw=False):
        
        if not self.isInvalide():
            if not forceRedraw:
                return 
                
        ##print("FlexPane::_redraw")
        pos = self.position
        
        ## we paint on our own texture
        ## not on the parent's texture
        _texture = self._texture
        theme = biui.getTheme()
        theme.drawFlexPaneBeforeChildren(self.window.renderer,self,_texture)

        forceRedraw = self.isInvalide() or forceRedraw
        ## We draw all Children on our own texture        
        for c in self._children:
            c._redraw(_texture,forceRedraw)
                    
        theme.drawFlexPaneAfterChildren(self.window.renderer,self,_texture)
        
        ## Now we copy the visible area 
        ## of our own texture
        ## on the parent's texture
        ##texture.blit(_texture,pos,(0,0,self.width,self.height))
        biui.DL.blit(
            self.window.renderer,
            texture,
            _texture,
            (pos[0],pos[1],self.width,self.height),
            (0,0,self.width,self.height)
        )
        
        self._isInvalide = False        
                