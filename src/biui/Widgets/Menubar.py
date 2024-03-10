import biui
from biui.Widgets import ContainerWidget
from biui.Events import EventManager
from biui.Enum import Alignment


###
##
##
class Menubar(ContainerWidget):

    ###
    ##
    ##
    def __init__(self):
        self.alignment = Alignment.DOCK_TOP
        self._menuAlignment = Alignment.DOCK_LEFT
        self.__currentMenu = []
        self.onItemClick = EventManager()
        self.__menuOn = False
        
        super().__init__()
        self.layoutManager.columnWidths = [0]
        self.layoutManager.rowHeights = [0]
        self.height = 30
        theme = biui.getTheme()
        self._themeBackgroundfunction = theme.drawMenubarBeforeChildren
        self._themeForegroundfunction = theme.drawMenubarAfterChildren

    ### @see biui.ContainerWidget.addChild
    ##
    ##
    def addChild(self,child,x=0,y=0):
        raise Exception(BIUI_ERR_MENUBAR_ADDCHILD)
    
    ### @see biui.ContainerWidget.removeChild
    ##
    ##
    def removeChild(self):
        raise Exception(BIUI_ERR_MENUBAR_REMOVECHILD)
    
    ### Returns the menu alignment value.
    ##  Alignment of the menuitems inside the menubar.
    ##
    ##
    @property
    def menuAlignment(self):
        return self._menuAlignment

    ### Sets the menu alignment value.
    ##
    ##
    @menuAlignment.setter
    def menuAlignment(self,value):
        for child in self._children:
            child.alignment = value

        self._menuAlignment = value
        self._invalidate()

    ### Adds a menu item.
    ##
    ##  @param child    (biui.MenuItem) 
    ##
    def addItem(self,child):
        child.alignment = self._menuAlignment
        child.onShowSubmenu.add(self.__hndOnShowSubmenu)
        child.onMouseDown.add(self.__hndOnMouseDown)
        child.onItemClick.add(self.__hndMenuOnItemClick)
        super().addChild(child,0,0)

    ### removes a menu item.
    ##
    ##  @param child    (biui.MenuItem)
    ##
    def removeItem(self,child):
        child.onShowSubmenu.remove(self.__hndOnShowSubmenu)
        child.onMouseDown.remove(self.__hndOnMouseDown)
        super().removeChild(child)

    ###
    ##
    ##
    def __hndOnMouseDown(self,ev):
        if self.__menuOn:
            self.__closeMenu()
            self.__menuOn = False
            return

        self.__menuOn = True
        self.__showSubMenu(ev.eventSource)
        
        ## now the menu bar is attached to a window.
        ## we have to listen to a mouseDown on the window to
        ## register an outside click to close the menu
        ## but we must add this just once.
        self.window.onMouseDown.add(self.__hndWindowMouseDown)
        self.window.onWindowFocusLost.add(self.__hndWindowFocusLost)
                    
    ###
    ##
    ##
    def __hndWindowMouseDown(self,ev):
        item = ev.eventSource
        if self.hasChild(item):
            return
        for menu in self.__currentMenu:
            if menu.hasChild(item):
                return        
        self.__closeMenu()
        
    ###
    ##
    ##
    def __hndWindowFocusLost(self,ev):
        self.__closeMenu()
        
    ###
    ##
    ##
    def __hndOnShowSubmenu(self,ev):
        item = ev.eventSource
        self.__showSubMenu(item)

    ###
    ##
    ##
    def __closeMenu(self):
        self.window.onMouseDown.remove(self.__hndWindowMouseDown)
        self.window.onWindowFocusLost.remove(self.__hndWindowFocusLost)
                
        for child in self.__currentMenu:
            self.__removeSubMenu(child)
        self.__menuOn = False
        self.__currentMenu = []


    ###
    ##
    ##
    def __removeSubMenu(self,menu):
        menu.onItemClick.remove(self.__hndMenuOnItemClick)
        menu.onGotRemoved.remove(self.__hndMenuOnGotRemoved)
        self.window.removeChild(menu)

    ###
    ##
    ##
    def __showSubMenu(self,item):

        if not self.__menuOn:
            return

        ## it we show a sub menu
        ## there could be menues open
        ## which should be removed
        ## because they are are on a
        ## different branch and on a lower
        ## level than the new one
        ## we go backwards throuu the menues
        ## if item isn´t in the menu
        ## it has to bwe removed.
        for i in range(len(self.__currentMenu)-1,-1,-1):
            menu = self.__currentMenu[i]
            if not menu.hasChild(item):
                self.__removeSubMenu(menu)
                self.__currentMenu.remove(menu)
            else:
                ## we have reached the current leven.
                ## we are finished
                break

        ## if the current item has no submenu
        ## we don´t have to do anything
        if not item.hasSubmenu:
            return

        menu = item.getMenuWidget()

        firstLevel = self.hasChild(item)
        if firstLevel:
            ## we place the menu below the item
            pos = item.toGlobal((0,0))
            if self.alignment == Alignment.DOCK_TOP:
                menu.x = pos[0]
                menu.y = pos[1]+item.height
            elif self.alignment == Alignment.DOCK_LEFT:
                menu.x = pos[0]+item.width
                menu.y = pos[1]
            elif self.alignment == Alignment.DOCK_BOTTOM:
                menu.x = pos[0]
                menu.y = pos[1]-menu.height
            else:
                menu.x = pos[0]-menu.width
                menu.y = pos[1]
        else:
            ## we place the menu next to the item
            ## we place the menu below the item
            ## -10 for overlapping
            pos = item.toGlobal((0,0))
            menu.x = pos[0]+item.width-10
            menu.y = pos[1]

        if menu.right > self.window.width:
            menu.x = self.window.width-menu.width

        if menu.x <0:
            menu.x = 0

        if menu.bottom > self.window.height:
            menu.y = self.window.height-menu.height

        if menu.bottom < 0:
            menu.y = 0

        menu.onItemClick.add(self.__hndMenuOnItemClick)
        menu.onGotRemoved.add(self.__hndMenuOnGotRemoved)
        if firstLevel:
            self.window.showOverlay(menu,"menu")
        else:
            self.window.addOverlay(menu,"menu")

        self.__currentMenu.append(menu)


    ###
    ##
    ##
    def __hndMenuOnGotRemoved(self,ev):
        self.__closeMenu()

    ###
    ##
    ##
    def __hndMenuOnItemClick(self,ev):
        if ev.eventSource.hasSubmenu:
            return
        
        self.__closeMenu()
        self.onItemClick.provoke(ev)
