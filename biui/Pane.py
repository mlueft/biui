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
        
    def onMouseDown(self,ev):
        #print("Pane::onMouseDown: "+str(ev))
        pass

    def onMouseUp(self,ev):
        #print("Pane::onMouseUp: "+str(ev))
        pass
    
    def onMouseWheel(self,ev):
        #print("Pane::onMouseWheel: "+str(ev))
        pass
    
    def onMouseEnter(self,ev):
        #print("Pane::onMouseEnter")
        pass
    
    def onMouseLeave(self,ev):
        #print("Pane::onMouseLeave")
        pass
        
    def onKeyDown(self,ev):
        #print("Pane::onKeyDown: "+str(ev))
        # Necassary the the end.
        super().onKeyDown(ev)
        
    def onKeyUp(self,ev):
        #print("Pane::onKeyUp: "+str(ev))
        # Necassary the the end.
        super().onKeyUp(ev)
        
        