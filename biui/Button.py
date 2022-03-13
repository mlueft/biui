import biui

##
#
#
class Button(biui.ContainerWidget.ContainerWidget):
    
    def __init__(self):
        super().__init__()
        self.width = 50
        self.height = 20
        self._state = biui.ButtonStates.NORMAL
        self._icon = None
        
        self._label = biui.Label()
        self._label.alignment = biui.Alignment.CENTER_CENTER
        self._label.width = 100
        self._label.height = 50
        #self.addChild(self._label,1,0)
        
        self._layoutManager.columnWidths = [1,0,1]
        self._layoutManager.rowHeights = [0]
        
    ## Returns the current state of the button.
    #  See: biui.ButtonStates
    #  
    @property
    def state(self):
        return self._state
    
    ##
    #
    #
    @property
    def icon(self):
        return self._icon
    ##
    #
    #
    @icon.setter
    def icon(self,icon):
        self._icon = icon
        self.addChild(icon,0,0)
        self._invalidate()

    ##
    #
    #
    @property
    def text(self):
        return self._label.text
    
    ##
    #
    #
    @text.setter
    def text(self,value):
        self._label.text = value
                
    def _onMouseEnter(self,ev):
        self._recordDirtyRect()
        self._state = biui.ButtonStates.OVER
        self._invalidate()
        super()._onMouseEnter(ev)
        
    def _onMouseLeave(self,ev):
        self._recordDirtyRect()
        self._state = biui.ButtonStates.NORMAL
        self._invalidate()
        super()._onMouseLeave(ev)
        
    def _onMouseDown(self,ev):
        self._recordDirtyRect()
        self._state = biui.ButtonStates.DOWN
        self._invalidate()
        super()._onMouseDown(ev)
                
    def _onMouseUp(self,ev):
        self._recordDirtyRect()
        self._state = biui.ButtonStates.OVER
        self._invalidate()
        super()._onMouseUp(ev)
        
    def _onMouseMove(self,ev):
        super()._onMouseMove(ev)
        
    def _redraw(self, surface, forceRedraw=False):
        
        if not self.isInvalide():
            if not forceRedraw:
                return
        
        #print("Pane::_redraw")
        pos = self.position
        
        # we paint on our own surface
        # not on the parent's surface
        _surface = self._surface
        theme = biui.getTheme()
        theme.drawButtonBeforeChildren(self,_surface)

        # We draw all Children on our own surface        
        for c in self._children:
            c._redraw(_surface)
                    
        theme.drawButtonAfterChildren(self,_surface)
        
        # Now we copy the visible area 
        # of our own surface
        # on the parent's surface
        surface.blit(_surface,pos,(0,0,self.width,self.height))
        
        self._isInvalide = False
        
