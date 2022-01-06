import biui

##
#
#
class Button(biui.Widget.Widget):
    
    def __init__(self):
        super().__init__()
        self.setWidth(50)
        self.setHeight(20)
        
    def onMouseMove(self,ev):
        print("Pane::mouseMove: "+str(ev))
        
    def _redraw(self, surface):
        #pos = self.toGlobal(self.getPosition())
        pos = self.getPosition()
        theme = biui.getTheme()
        theme.drawButton(self,surface)
        super()._redraw(surface)
        
