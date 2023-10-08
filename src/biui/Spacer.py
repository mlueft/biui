import biui
from biui.Widget import Widget

### General spacer object.
##  It can be used in the layoutmanager
##  to get visual seperation between
##  elements.
##
class Spacer(Widget):
    
    def __init__(self):
        super().__init__()
        
        theme = biui.getTheme()
        self._themeBackgroundfunction = theme.drawSpacer
        