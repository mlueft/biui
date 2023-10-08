import biui
from biui.ContainerWidget import ContainerWidget

###
##
##
class ButtonGroup(ContainerWidget):
    
    def __init__(self):
        super().__init__()
        theme = biui.getTheme()
        self._themeBackgroundfunction = theme.drawButtonGroupBeforeChildren
        self._themeForegroundfunction = theme.drawButtonGroupAfterChildren
        
    ### @see biui.ContainerWidget.addChild
    ##
    ##        
    def addChild(self, child:biui.Widget,x:int=0,y:int=0)->None:
        super().addChild(child,x,y)
        child.onMouseUp.add(self.__hndOnMouseUp)

    ### @see biui.ContainerWidget.removeChild
    ##
    ##    
    def removeChild(self, child:biui.Widget)->None:
        super().removeChild(child)
        child.onMouseUp.remove(self.__hndOnMouseUp)
    
    ###
    ##
    ##
    def __hndOnMouseUp(self,ev:biui.Event)->None:
        source = ev.eventSource
        for c in self._children:
            c.checked = c == source
