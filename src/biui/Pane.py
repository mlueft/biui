import biui
###
##
##
class Pane(biui.ContainerWidget.ContainerWidget):
    
    ###
    ##
    ##
    def __init__(self):
        super().__init__()
        theme = biui.getTheme()
        self._themeBackgroundfunction = theme.drawPaneBeforeChildren
        self._themeForegroundfunction = theme.drawPaneAfterChildren
        self.width = 100
        self.height = 100
        