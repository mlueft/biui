import biui

##
#
#
class ButtonGroup(biui.ContainerWidget.ContainerWidget):
    
    def __init__(self):
        super().__init__()
        
    def addChild(self, child):
        super().addChild(child)
        child.onMouseUp.add(self.upHandler)
    
    def upHandler(self,ev):
        source = ev.getEventSource()
        for c in self._children:
            c.setChecked(c == source)
        
    def _redraw(self, surface):
        #print("Pane::_redraw")
        pos = self.getPosition()
        
        # we paint on our own surface
        # not on the parent's surface
        _surface = self._surface
        theme = biui.getTheme()
        theme.drawButtonGroupBeforeChildren(self,_surface)

        # We draw all Children on our own surface        
        for c in self._children:
            c._redraw(_surface)
                    
        theme.drawButtonGroupChildren(self,_surface)
        
        # Now we copy the visible area 
        # of our own surface
        # on the parent's surface
        surface.blit(_surface,pos,(0,0,self.getWidth(),self.getHeight()))