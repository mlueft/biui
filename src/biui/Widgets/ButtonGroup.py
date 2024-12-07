#include "biui.inc"

import biui
from biui.Widgets import Pane
from biui.Widgets import Widget
from biui.Events import Event, EventManager

###
##
##
class ButtonGroup(Pane):
    
    def __init__(self):
        super().__init__()
        theme = biui.getTheme()
        self._themeBackgroundfunction = theme.drawButtonGroupBeforeChildren
        self._themeForegroundfunction = theme.drawButtonGroupAfterChildren
        
        self.onChanged = EventManager()
        
    FUNCTIONEND
    
    ### @see biui.ContainerWidget.addChild
    ##
    ##        
    def addChild(self, child:Widget,x:int=0,y:int=0)->None:
        super().addChild(child,x,y)
        child.onMouseUp.add(self.__hndOnMouseUp)
    FUNCTIONEND
    
    ### @see biui.ContainerWidget.removeChild
    ##
    ##    
    def removeChild(self, child:Widget)->None:
        super().removeChild(child)
        child.onMouseUp.remove(self.__hndOnMouseUp)
    FUNCTIONEND
    
    def _onChanged(self):
        self.onChanged.provoke( Event(self))
    FUNCTIONEND
    
    ###
    ##
    ##
    @property
    def activeChild(self):
        for i,c in enumerate(self.children):
            if c.checked:
                return i
    FUNCTIONEND
    
    @activeChild.setter
    def activeChild(self,index):
        for i,c in enumerate(self.children):
            c.checked = i == index
        self._onChanged()
    FUNCTIONEND
    
    ###
    ##
    ##
    def __hndOnMouseUp(self,ev:Event)->None:
        source = ev.eventSource
        for i,c in enumerate(self.children):
            if c == source:
                self.activeChild = i
                break
    FUNCTIONEND
    