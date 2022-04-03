import biui

##
#
#
class FlexSpacer(biui.Widget.Widget):
    
    def __init__(self):
        super().__init__()
        self._minWidth = 2
        self._minHeight = 2
        
    def _redraw(self, surface, forceRedraw=False):
        
        if not self.isInvalide():
            if not forceRedraw:
                return
                    
        pos = self.position
        theme = biui.getTheme()
        theme.drawFlexSpacer(self,surface)
        self._isInvalide = False
        
        