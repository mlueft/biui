import biui

class FlexSpacer(biui.Pane.Pane):
    
    def __init__(self):
        super().__init__()
        self._minWidth = 10
        self._minHeight = 10
        