import biui

##
#
#
class VerticalSplitter(biui.HorizontalSplitter.HorizontalSplitter):
    
    def __init__(self):
        super().__init__()
        

    def childVerticalSplit(self,ev):
        child = ev.getEventSource()
        lm = self.getLayoutManager()
        index = lm.getPositionOfChild(child)[1]
        self.removeChild(child)
        splitter = biui.HorizontalSplitter()
        splitter.addChild(child,0,0)
        splitter.addChild(biui.FlexPane(),1,0)
        lm = splitter.getLayoutManager()
        self.addChild(splitter, 0,index)
        
    def childHorizontalSplit(self,ev):
        wnd = self.getWindow()
        self._splitStartPosition = wnd.getMousePosition()
        self.onMouseUp.add(self.myMouseUp)
        self.onMouseMove.add(self.myMouseMove)
        child = ev.getEventSource()
        lm = self.getLayoutManager()
        index = lm.getPositionOfChild(child)[1]        
        lm.insertRowAt(index)
        pane = biui.FlexPane()
        self.addChild( pane,0,index )
