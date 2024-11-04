import biui
from biui.Widgets import ContainerWidget
from biui.Events import EventManager
from biui.Enum import Alignment

###
##
##
class MenuPane(ContainerWidget):
    
    def __init__(self):
        super().__init__()
        theme = biui.getTheme()
        self._themeBackgroundfunction = theme.drawMenuPaneBeforeChildren
        self._themeForegroundfunction = theme.drawMenuPaneAfterChildren        
        
        ##
        self.onItemClick = EventManager()
        
        self.onBeforeRender.add(self.__hndOnBeforeRender)
        
    ###
    ##
    ##
    def __hndOnBeforeRender(self,ev):
        ## We have to find the size of the biggest item
        ## the pane. Items are resized by layout manager.
        margin = 10
        maxWidth = 0
        for child in self._children:
            maxWidth = max( maxWidth, child.label.width)
            
        self.width = maxWidth+margin


    ### @see biui.ContainerWidget.addChild
    ##
    ##
    def addChild(self,child,x=0,y=0):
        raise Exception(BIUI_ERR_MENUPANE_ADDCHILD)
    
    ### @see biui.ContainerWidget.removeChild
    ##
    ##
    def removeChild(self):
        raise Exception(BIUI_ERR_MENUPANE_REMOVECHILD)
    
    ### Adds a menu item to the Menupane.
    ##
    ## @param child       (biui.Menuitem) The menu item to be added.
    ##
    def addItem(self,child):
        child.onItemClick.add(self.__hndItemOnItemClick)
        super().addChild(child,0,len(self._children))
        
    ### Removes a menu item from the menu pane.
    ##
    ## @param child       (biui.Menuitem) The menu item to be removed.
    ##
    def removeItem(self,child):
        child.onItemClick.remove(self.__hndItemOnItemClick)
        super().removeChild(child)
        
    ###
    ##
    ##
    def __hndItemOnItemClick(self,ev):
        self.onItemClick.provoke(ev)