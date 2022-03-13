import biui
from pexpect import expect

## Base class for all container widgets.
#
#
class ContainerWidget(biui.Widget.Widget):
    
    def __init__(self):
        super().__init__()
        #
        self._children = []
        #
        self._surface = biui.createSurface(self.size)
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
     
    def hasChild(self,child):
        for c in self._children:
            if c.hasChild(child):
                return True
            
        return self == child
    
    ##  Removes the given child element.
    #
    #  @param child         A Widget instance.
    #   
    def removeChild(self,child):
        self._layoutManager.removeChild(child)
        if child in self._children:
            self._children.remove(child)
        self.onChildRemoved.provoke(biui.Event(self))
     
    ## Adds a child element to the container.
    #
    #  @param child         A Widget instance.
    #  @param x             Column for layout manager to add the child to. 
    #  @param y             Row for layout manager to add the child to.
    #       
    def addChild(self,child,x=0,y=0):
        child.parent = self
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
        
        if cPos[0]+self.width < pos[0]:
            return None
         
        if cPos[1] > pos[1]:
            return None
        
        if cPos[1]+self.height < pos[1]:
            return None
                
        for i in range(len(self._children)-1,-1,-1):
            c = self._children[i]
            cPos = c.toGlobal((0,0))
            if cPos[0] <= pos[0]:
                if cPos[0]+c.width >= pos[0]: 
                    if cPos[1] <= pos[1]:
                        if cPos[1]+c.height >= pos[1]:
                            if isinstance(c,biui.ContainerWidget.ContainerWidget):
                                return c.getChildAt(pos)
                            else:
                                return c
                    
        return self
    
    def isInvalide(self):
        
        for c in self._children:
            if c.isInvalide():
                return True
    
        return super().isInvalide()
    
        
    ## 
    #
    #  @return            A biui.LayoutManager.
    #
    @property
    def layoutManager(self):
        return self._layoutManager
        
    ## 
    #
    #  @param value       A biui.ayoutManager.
    #  @return            None
    #
    @layoutManager.setter
    def layoutManager(self, value):
        self._layoutManager = value
        
    @property
    def width(self):
        #TODO: call super
        return self._width
    
    @width.setter
    def width(self, value):
        if value > self._width:
            self._recreateSurface = True
        super(biui.Widget.Widget, self.__class__).__thisclass__.width.__set__(self,value)
        #super().width = value
        #self._surface = biui.createSurface(self.getSize())
    
    @property    
    def height(self):
        #TODO: call super
        return self._height
    
    @height.setter
    def height(self, value):
        if value > self._height:
            self._recreateSurface = True
        super(biui.Widget.Widget, self.__class__).__thisclass__.height.__set__(self,value)
        #super().setHeight(value)
        #self._surface = biui.createSurface(self.getSize())
    
    def _getDirtyRectangles(self):
        result = self._dirtyRects.copy()
        for c in self._children:
            result += c._getDirtyRectangles()
        self._dirtyRects.clear()
        return result
    
    def _calculateLayout(self):
        
        mySize = self.size
        
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
    
    def _redraw(self, surface, forceRedraw=False ):

        forceRedraw = self.isInvalide() or forceRedraw
        for c in self._children:
            c._redraw(self._surface,forceRedraw)
                
        self._isInvalide = False
        
    def _onMouseDown(self,ev):
        super()._onMouseDown(ev)
        if ev._stopPropagation:
            return
        for c in self._children:
            if c.hasChild(ev.eventSource):
                c._onMouseDown(ev)
                break
        
    def _onMouseUp(self,ev):
        super()._onMouseUp(ev)
        if ev._stopPropagation:
            return
        for c in self._children:
            if c.hasChild(ev.eventSource):
                c._onMouseUp(ev)
                break
        
    def _onMouseWheel(self,ev):
        super()._onMouseWheel(ev)
        if ev._stopPropagation:
            return
        for c in self._children:
            if c.hasChild(ev.eventSource):
                c._onMouseWheel(ev)
                break
        
    def _onMouseEnter(self,ev):
        super()._onMouseEnter(ev)
        if ev._stopPropagation:
            return
        for c in self._children:
            if c.hasChild(ev.eventSource):
                c._onMouseEnter(ev)
                break
        
    def _onMouseLeave(self,ev):
        super()._onMouseLeave(ev)
        if ev._stopPropagation:
            return
        for c in self._children:
            if c.hasChild(ev.eventSource):
                c._onMouseLeave(ev)
                break
        
    def _onMouseMove(self,ev):
        super()._onMouseMove(ev)
        if ev._stopPropagation:
            return
        for c in self._children:
            if c.hasChild(ev.eventSource):
                c._onMouseMove(ev)
                break
        
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
                
    def _invalidate(self):
        for c in self._children:
            c._invalidate()
        super()._invalidate()
        