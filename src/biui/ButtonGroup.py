import biui

###
##
##
class ButtonGroup(biui.ContainerWidget.ContainerWidget):
    
    def __init__(self):
        super().__init__()
        theme = biui.getTheme()
        self._themeBackgroundfunction = theme.drawButtonGroupBeforeChildren
        self._themeForegroundfunction = theme.drawButtonGroupAfterChildren
        
    def addChild(self, child):
        super().addChild(child)
        child.onMouseUp.add(self.upHandler)

    def removeChild(self, child):
        super().removeChild(child)
        child.onMouseUp.remove(self.upHandler)
            
    def upHandler(self,ev):
        source = ev.eventSource
        for c in self._children:
            c.checked = c == source
