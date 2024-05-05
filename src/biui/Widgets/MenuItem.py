
import biui
from biui.Widgets import Button,MenuItem,MenuPane,Menubar
from biui.Events import EventManager
from biui.Events import Event
from biui.Enum import Alignment

###
##
##
class MenuItem(Button):
    
    ###
    ##
    ##
    def __init__(self):
        super().__init__()
        
        ## Is provoked when the item is cklicked.
        self.onItemClick = EventManager()
        
        ## Is provoked when a child has to show a submenu.
        self.onShowSubmenu = EventManager()
                
        theme = biui.getTheme()
        self._themeBackgroundfunction = theme.drawMenubuttonBeforeChildren
        self._themeForegroundfunction = theme.drawMenubuttonAfterChildren
        self.alignment = Alignment.FILL
        self.value = "Menupoint"
        self.label.color = biui.Color(0,0,0,0)
        self.label.alignment = Alignment.CENTER_LEFT
        self.layoutManager.columnWidths = [5,0,5]
        

        self._items = []
        
        self.__showSubmenuIndicator = True
        
        self.__subMenuWidget = None
        
        self.onBeforeDraw.add(self.__hndOnBeforeDraw)
        self.onMouseClick.add(self.__hndOnMouseClick)
        self.onMouseEnter.add(self.__hndOnMouseEnter)
        
    ### Returns a boolean value indicating if the sub 
    ##  menu indicator is shown or not.
    ##
    ##
    @property
    def showSubmenuIndicator(self):
        return self.__showSubmenuIndicator
    
    ### Sets the x position of the GUI element.
    ##
    ##  @param value       (bool) Defines if the sub
    ##  menu indicator is shown.
    ##
    @showSubmenuIndicator.setter
    def showSubmenuIndicator(self, value):
        self.__showSubmenuIndicator = value

    ### Returns the number of items in the submenu.
    ##
    ##
    @property
    def menuLength(self):
        return len(self._items)
    
    ### Returns a boolean value indicating if the item
    ##  has a sub menu.
    ##
    ##
    @property
    def hasSubmenu(self):
        return len(self._items) > 0
                    
    ###
    ##
    ##
    def __hndOnBeforeDraw(self,ev):
        margin = 10
        self.width = self.label.width+margin
        
    ### Adds a item to the sub menu.
    ##
    ##  @param child    (biui.MenuItem) The menu item to be added.
    ##
    def addItem(self,child):
        child.onShowSubmenu.add(self.__hndChildSubmenu)
        self._items.append(child)
        if type(self.parent) != Menubar:
            self.label.format = "{} >"
        
    ### Removes an item from the sub menu.
    ##
    ##  @param child    (biui.MenuItem) The menu item to be removed.
    ##
    def removeItem(self,child):
        child.onShowSubmenu.remove(self.__hndChildSubmenu)
        self._items.remove(child)
        if len(self._children) == 0:
            self.label.format = "{}"
        
    ###
    ##
    ##
    def __hndOnMouseClick(self,ev):
        self.onItemClick.provoke(ev)

    ### Creates the showSubmenu event.
    ##
    ##
    def __hndOnMouseEnter(self,ev):
        ##print("MenuItem::__hndOnMouseEnter")
        ##if self.hasSubmenu:
        self.onShowSubmenu.provoke(Event(self))
        
    ### Forwards the event of subitems, so it reaches the menubar
    ##  The menubar handles displaying submenues
    ##
    def __hndChildSubmenu(self,ev):
        self.onShowSubmenu.provoke(ev)
        
    ### Returns the Widget of the sub menu.
    ##
    ##  @return
    ##
    def getMenuWidget(self):
        if self.__subMenuWidget != None:
            return self.__subMenuWidget
        
        container = MenuPane()
        
        height = 0
        for item in self._items:
            item.alignment = Alignment.DOCK_TOP
            height += item.height
            container.addItem(item)
        
        container.height = height
        container.alignment = Alignment.ABSOLUTE
        self.__subMenuWidget = container
        return container