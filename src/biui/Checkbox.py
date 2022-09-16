import biui

###
##
##
class Checkbox(biui.ToggleButton.ToggleButton):
    
    def __init__(self):
        super().__init__()
        
        theme = biui.getTheme()
        self._themeBackgroundfunction = theme.drawCheckboxBeforeChildren
        self._themeForegroundfunction = theme.drawEmpty
         
        