import biui

##
#
#
class Button(biui.ContainerWidget.ContainerWidget):
    
    def __init__(self):
        super().__init__()
        theme = biui.getTheme()
        self._themeBackgroundfunction = theme.drawButtonBeforeChildren
        self._themeForegroundfunction = theme.drawButtonAfterChildren
        self.width = 150
        self.height = 30
        self._state = biui.ButtonStates.NORMAL
        self._icon = None
        
        self._label = biui.Label()
        self._label.alignment = biui.Alignment.CENTER_CENTER
        self.addChild(self._label,1,0)
        
        self._layoutManager.columnWidths = [1,0,1]
        self._layoutManager.rowHeights = [0]
        
        self.onMouseEnter.add(self.__onMouseEnter)
        self.onMouseLeave.add(self.__onMouseLeave)
        self.onMouseDown.add(self.__onMouseDown)
        self.onMouseUp.add(self.__onMouseUp)
        
    def getChildAt(self, pos):
        
        # we don't want to return any child 
        # objects like labels or icons.
        # If the position is inside the button,
        # the button is the last element in the DOM.
        
        cPos = self.toGlobal((0,0))
        if cPos[0] > pos[0]:
            return None
        
        if cPos[0]+self.width < pos[0]:
            return None
         
        if cPos[1] > pos[1]:
            return None
        
        if cPos[1]+self.height < pos[1]:
            return None
                
        return self
    
    ## Returns the embedded label instance
    #  to make it's properties accessible.
    #
    #
    @property
    def label(self):
        return self._label
    
    ## Returns the current state of the button.
    #  See: biui.ButtonStates
    #  
    @property
    def state(self):
        return self._state
    
    ## Returns the icon instance of the button
    #  to make it's properties accessible. 
    #
    #
    @property
    def icon(self):
        return self._icon
    
    ## Sets the icon instance.
    #  TODO: Impliment the icon class.
    #
    #
    @icon.setter
    def icon(self,icon):
        self._icon = icon
        self.addChild(icon,0,0)
        self._invalidate()

    ## Returns the value of the button.
    #  The value is the shown text.
    #
    #
    @property
    def value(self):
        return self._label.value
    
    ## Sets the value of the button.
    #  The value is the shown text.
    #
    @value.setter
    def value(self,value):
        self._label.value = value

    def __onMouseEnter(self,ev):
        self._recordDirtyRect()
        self._state = biui.ButtonStates.OVER
        self._invalidate()
        
    def __onMouseLeave(self,ev):
        self._recordDirtyRect()
        self._state = biui.ButtonStates.NORMAL
        self._invalidate()
        
    def __onMouseDown(self,ev):
        self._recordDirtyRect()
        self._state = biui.ButtonStates.DOWN
        self._invalidate()
                
    def __onMouseUp(self,ev):
        self._recordDirtyRect()
        self._state = biui.ButtonStates.OVER
        self._invalidate()
               
