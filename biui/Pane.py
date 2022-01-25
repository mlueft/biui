import biui

##
#
#
class Pane(biui.ContainerWidget.ContainerWidget):
    
    ##
    #
    #
    def __init__(self):
        super().__init__()
        self.setWidth(100)
        self.setHeight(100)
        
    def _redraw(self, surface):
        #print("Pane::_redraw")
        pos = self.getPosition()
        
        # we paint on our own surface
        # not on the parent's surface
        _surface = self._surface
        theme = biui.getTheme()
        theme.drawPaneBeforeChildren(self,_surface)

        # We draw all Children on our own surface        
        for c in self._children:
            c._redraw(_surface)
                    
        theme.drawPaneAfterChildren(self,_surface)
        
        # Now we copy the visible area 
        # of our own surface
        # on the parent's surface
        surface.blit(_surface,pos,(0,0,self.getWidth(),self.getHeight()))
        