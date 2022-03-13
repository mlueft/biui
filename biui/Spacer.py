import biui

##
#
#
class Spacer(biui.Widget.Widget):
    
    def __init__(self):
        super().__init__()
        
    def _redraw(self, surface, forceRedraw=False):
        #pos = self.toGlobal(self.getPosition())
        pos = self.getPosition()
        theme = biui.getTheme()
        theme.drawSpacer(self,surface)
        self._isInvalide = False
        
