import biui
from biui.ContainerWidget import ContainerWidget

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
        self.onItemClick = biui.EventManager()
        

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
        super().addChild(child)
        
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