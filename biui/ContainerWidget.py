import biui

##
#
#
class ContainerWidget(biui.Widget.Widget):
    
    def __init__(self):
        super().__init__()
        #
        self._children = []
        #
        self._surface = biui.createSurface(self.getSize())
        #
        self._layoutManager = biui.LayoutManager()
        #
        self.onChildAdded = biui.EventManager()
        #
        self.onChildRemoved = biui.EventManager()
        #
        self._recreateSurface = False
        
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
        self._layoutManager.removeChild(child)
        self._children.remove(child)
        self.onChildRemoved.provoke(biui.Event(self))
     
    ## Adds a child element to the container.
    #
    #  @param child         A Widget instance.
    #  @param x             Column for layout manager to add the child to. 
    #  @param y             Row for layout manager to add the child to.
    #       
    def addChild(self,child,x=0,y=0):
        child.setParent(self)
        #self._children.insert(0,child)
        self._children.append(child)
        self._layoutManager.addChild(child,x,y)
        self._invalidate()
        self.onChildAdded.provoke(biui.Event(self))
    
    ## Returns the child element at the given position, itself or None.
    #
    #  @param pos             A tuple representing a position in the
    #                         element's coordinate system.
    #  @return                None or a Widget
    #
    def getChildAt(self, pos):
        cPos = self.toGlobal((0,0))
        if cPos[0] > pos[0]:
            return None
        
        if cPos[0]+self.getWidth() < pos[0]:
            return None
         
        if cPos[1] > pos[1]:
            return None
        
        if cPos[1]+self.getHeight() < pos[1]:
            return None
                
        for i in range(len(self._children)-1,-1,-1):
            c = self._children[i]
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
    
    ## 
    #
    #  @param value       A biui.ayoutManager.
    #  @return            None
    #
    def setLayoutManager(self, value):
        self._layoutManager = value
    
    ## 
    #
    #  @return            A biui.LayoutManager.
    #
    def getLayoutManager(self):
        return self._layoutManager
        
    def setWidth(self, value):
        if value > self._width:
            self._recreateSurface = True
        super().setWidth(value)
        #self._surface = biui.createSurface(self.getSize())
        
    def setHeight(self, value):
        if value > self._height:
            self._recreateSurface = True
        super().setHeight(value)
        #self._surface = biui.createSurface(self.getSize())
    
    def _getDirtyRectangles(self):
        result = self._dirtyRects.copy()
        for c in self._children:
            result += c._getDirtyRectangles()
        self._dirtyRects.clear()
        return result
    
    def _calculateLayout(self):
        
        if not self._runLayoutManager:
            # If we don't have to recalculate, prob. a child has to.
            for c in self._children:
                c._calculateLayout()            
            return
        
        mySize = self.getSize()
        
        # If necassary create a new surface.
        # TODO: Is it cheaper to hold a big
        # temporary surfacee in biui than
        # create a new one continously?
        if self._recreateSurface:
            self._surface = biui.createSurface(mySize)
            self._recreateSurface = False
            
        self._layoutManager._calculateLayout(mySize)
        for c in self._children:
            c._calculateLayout()
        self._runLayoutManager = False
    
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
                