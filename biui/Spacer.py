import biui

##
#
#
class Spacer(biui.Widget.Widget):
    
    def __init__(self):
        super().__init__()
        
    def _redraw(self, surface):
        #pos = self.toGlobal(self.getPosition())
        pos = self.getPosition()
        theme = biui.getTheme()
        theme.drawSpacer(self,surface)
        super()._redraw(surface)