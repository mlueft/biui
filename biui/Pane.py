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
        self.width = 100
        self.height = 100
        
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
        theme.drawPaneBeforeChildren(self,_surface)

        forceRedraw = self.isInvalide() or forceRedraw
        # We draw all Children on our own surface        
        for c in self._children:
            c._redraw(_surface,forceRedraw)
                    
        theme.drawPaneAfterChildren(self,_surface)
        
        # Now we copy the visible area 
        # of our own surface
        # on the parent's surface
        surface.blit(_surface,pos,(0,0,self.width,self.height))
        
        self._isInvalide = False
        