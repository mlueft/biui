import biui

##
#
#
class ContainerWidget(biui.Widget.Widget):
    
    def __init__(self):
        super().__init__()
        self._children = []
        self._surface = biui.createSurface(self.getSize())
        #
        self.onChildAdded = biui.EventManager()
        #
        self.onChildRemoved = biui.EventManager()
        
    ## Returns all child elements.
    #
    #  @return               A list with Widgets.
    #
    def getChildren(self):
        return self._children
     
    ##  Removes the given child element.
    #
    #  @param child         A Widget instance.
    #   
    def removeChild(self,child):
        self._children.remove(child)
        self.onChildRemoved.provoke(biui.Event(self))
     
    ## Adds a child element to the container.
    #
    #  @param child         A Widget instance.
    #       
    def addChild(self, child):
        child.setParent(self)
        self._children.append(child)
        self._invalidate()
        self.onChildAdded.provoke(biui.Event(self))
    
    ## Returns the child element at the given position, itself or None.
    #
    #  @param pos             A tuple representing a position in the
    #                         element's coordinate system.
    #  @return                None or a Widget
    #
    def getChildAt(self, pos):
        #print( "ContainerWidget::getChildAt" )
        
        cPos = self.toGlobal((0,0))
        if cPos[0] > pos[0]:
            return None
        
        if cPos[0]+self.getWidth() < pos[0]:
            return None
         
        if cPos[1] > pos[1]:
            return None
        
        if cPos[1]+self.getHeight() < pos[1]:
            return None
                
        for c in self._children:
            cPos = c.toGlobal((0,0))
            if cPos[0] <= pos[0]:
                if cPos[0]+c.getWidth() >= pos[0]: 
                    if cPos[1] <= pos[1]:
                        if cPos[1]+c.getHeight() >= pos[1]:
                            if isinstance(c,biui.ContainerWidget.ContainerWidget):
                                return c.getChildAt(pos)
                            else:
                                return c
                    
        return self
    
    def setWidth(self, value):
        super().setWidth(value)
        self._surface = biui.createSurface(self.getSize())
        
    def setHeight(self, value):
        super().setHeight(value)
        self._surface = biui.createSurface(self.getSize())
    
    def _getDirtyRectangles(self):
        result = self._dirtyRects.copy()
        for c in self._children:
            result += c._getDirtyRectangles()
        self._dirtyRects.clear()
        return result
    
    def _redraw(self, surface ):
        #print("ContainerWidget::_redraw")
        for c in self._children:
            c._redraw(self._surface)
                
    def _onKeyDown(self,ev):
        super()._onKeyDown(ev)
        for c in self._children:
            c._onKeyDown(ev)
            
    def _onKeyUp(self,ev):
        super()._onKeyUp(ev)
        for c in self._children:
            c._onKeyUp(ev)
    
    def _onTextInput(self,ev):
        super()._onTextInput(ev)
        for c in self._children:
            c._onTextInput(ev)
                