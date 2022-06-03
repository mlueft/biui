import biui

## Base class for all container widgets.
#
#
class ContainerWidget(biui.Widget.Widget):
    
    def __init__(self,doSurface=True):
        super().__init__()
        #
        self._children = []
        #
        self._layoutManager = biui.LayoutManager()
        #
        self.onChildAdded = biui.EventManager()
        #
        self.onChildRemoved = biui.EventManager()
        #
        self._recreateSurface = False
        #
        if doSurface:
            self._surface = biui.createSurface(self.size)
        # A reference to the theme function which is used to draw the widget forground.
        theme = biui.getTheme()
        self._themeForegroundfunction = theme.drawEmpty
        
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
                
        for c in reversed(self._children):
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
    
        
    ## Returns the layout manager.
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
        super()._calculateLayout()
        mySize = self.size
        
        # If necassary create a new surface.
        # TODO: Is it cheaper to hold a big
        # temporary surfacee in biui than
        # create a new one continously?
        if self._recreateSurface:
            self._surface = biui.createSurface(mySize)
            self._recreateSurface = False
            
        for c in self._children:
            c._calculateLayout()
        
        self._layoutManager._calculateLayout(mySize)

    ## This version doesn't work yet, because the subsurface
    #  must be completely inside the surface.
    #
    #
    def _redrawSub(self, surface, forceRedraw=False ):

        if not self.isInvalide():
            if not forceRedraw:
                return
        
        # we paint on a subsurface to
        # get sure no child paints over the container edges.
        _surface = surface.subsurface((self.x,self.y,self.width,self.height))

        theme = biui.getTheme()
        self._themeBackgroundfunction(self,_surface)

        forceRedraw = self.isInvalide() or forceRedraw
        # We draw all Children on our own surface        
        for c in self._children:
            c._redraw(_surface,forceRedraw)
                    
        self._themeForegroundfunction(self,_surface)
        
        self._isInvalide = False
            
    def _redraw(self, surface, forceRedraw=False ):

        if not self.isInvalide():
            if not forceRedraw:
                return
        
        #print("Pane::_redraw")
        pos = self.position
        
        # we paint on our own surface
        # not on the parent's surface
        _surface = self._surface
        theme = biui.getTheme()
        self._themeBackgroundfunction(self,_surface)

        forceRedraw = self.isInvalide() or forceRedraw
        # We draw all Children on our own surface        
        for c in self._children:
            c._redraw(_surface,forceRedraw)
                    
        self._themeForegroundfunction(self,_surface)
        
        # Now we copy the visible area 
        # of our own surface
        # on the parent's surface
        surface.blit(_surface,pos,(0,0,self.width,self.height))
        
        self._isInvalide = False
        
    def _onMouseDown(self,ev):
        
        # phase down
        super()._onMouseDown(ev)
        if ev._stopPropagation:
            return
        
        childFound = False
        for c in self._children:
            if c.hasChild(ev.eventSource):
                c._onMouseDown(ev)
                childFound = True
                if c == ev.eventSource:
                    # we set event phase to up!
                    # This is the case if c is not a ContainerWidget.
                    ev._nextPhase()
                break
        
        # if no child has got the event.
        # the event has reached the deepest level.
        if not childFound:
            # we set event phase to up!
            ev._nextPhase()
        else:
            # pahse up
            if ev._stopPropagation:
                return
            super()._onMouseDown(ev)
        
    def _onMouseUp(self,ev):
        
        # phase down
        super()._onMouseUp(ev)
        if ev._stopPropagation:
            return
        
        childFound = False
        for c in self._children:
            if c.hasChild(ev.eventSource):
                c._onMouseUp(ev)
                childFound = True
                if c == ev.eventSource:
                    # we set event phase to up!
                    # This is the case if c is not a ContainerWidget.
                    ev._nextPhase()
                break

        # if no child has got the event.
        # the event has reached the deepest level.
        if not childFound:
            # we set event phase to up!
            ev._nextPhase()
        else:
            # pahse up
            if ev._stopPropagation:
                return
            super()._onMouseUp(ev)
            
    def _onMouseClick(self,ev):
        # phase down
        super()._onMouseClick(ev)
        if ev._stopPropagation:
            return
        
        childFound = False
        for c in self._children:
            if c.hasChild(ev.eventSource):
                c._onMouseClick(ev)
                childFound = True
                if c == ev.eventSource:
                    # we set event phase to up!
                    # This is the case if c is not a ContainerWidget.
                    ev._nextPhase()
                break
                    
        # if no child has got the event.
        # the event has reached the deepest level.
        if not childFound:
            # we set event phase to up!
            ev._nextPhase()
        else:
            # pahse up
            if ev._stopPropagation:
                return
            super()._onMouseClick(ev)
                    
    def _onMouseWheel(self,ev):
        
        # phase down
        super()._onMouseWheel(ev)
        if ev._stopPropagation:
            return
        
        childFound = False
        for c in self._children:
            if c.hasChild(ev.eventSource):
                c._onMouseWheel(ev)
                childFound = True
                if c == ev.eventSource:
                    # we set event phase to up!
                    # This is the case if c is not a ContainerWidget.
                    ev._nextPhase()
                break
        
        # if no child has got the event.
        # the event has reached the deepest level.
        if not childFound:
            # we set event phase to up!
            ev._nextPhase()
        else:
            # pahse up
            if ev._stopPropagation:
                return
            super()._onMouseWheel(ev)
            
    def _onMouseEnter(self,ev):
        
        # phase down
        super()._onMouseEnter(ev)
        if ev._stopPropagation:
            return
        
        childFound = False
        for c in self._children:
            if c.hasChild(ev.eventSource):
                c._onMouseEnter(ev)
                childFound = True
                if c == ev.eventSource:
                    # we set event phase to up!
                    # This is the case if c is not a ContainerWidget.
                    ev._nextPhase()
                break
        
        # if no child has got the event.
        # the event has reached the deepest level.
        if not childFound:
            # we set event phase to up!
            ev._nextPhase()
        else:
            # pahse up
            if ev._stopPropagation:
                return
            super()._onMouseEnter(ev)
            
    def _onMouseLeave(self,ev):
        
        # phase down
        super()._onMouseLeave(ev)
        if ev._stopPropagation:
            return
        
        childFound = False
        for c in self._children:
            if c.hasChild(ev.eventSource):
                c._onMouseLeave(ev)
                childFound = True
                if c == ev.eventSource:
                    # we set event phase to up!
                    # This is the case if c is not a ContainerWidget.
                    ev._nextPhase()
                break
        
        # if no child has got the event.
        # the event has reached the deepest level.
        if not childFound:
            # we set event phase to up!
            ev._nextPhase()
        else:
            # pahse up
            if ev._stopPropagation:
                return
            super()._onMouseLeave(ev)
            
    def _onMouseMove(self,ev):
        
        # phase down
        super()._onMouseMove(ev)
        if ev._stopPropagation:
            return
        
        childFound = False
        for c in self._children:
            if c.hasChild(ev.eventSource):
                c._onMouseMove(ev)
                childFound = True
                if c == ev.eventSource:
                    # we set event phase to up!
                    # This is the case if c is not a ContainerWidget.
                    ev._nextPhase()
                break
        
        # if no child has got the event.
        # the event has reached the deepest level.
        if not childFound:
            # we set event phase to up!
            ev._nextPhase()
        else:
            # pahse up
            if ev._stopPropagation:
                return
            super()._onMouseMove(ev)
                    
    def _onKeyDown(self,ev):
        
        #phase down
        super()._onKeyDown(ev)
        if ev._stopPropagation:
            return
        
        childFound = False
        for c in self._children:
            if c.hasChild(ev.eventSource):
                c._onKeyDown(ev)
                childFound = True
                if c == ev.eventSource:
                    # we set event phase to up!
                    # This is the case if c is not a ContainerWidget.
                    ev._nextPhase()
                break
            
        # if no child has got the event.
        # the event has reached the deepest level.
        if not childFound:
            # we set event phase to up!
            ev._nextPhase()
        else:
            # pahse up
            if ev._stopPropagation:
                return
            super()._onKeyDown(ev)
            
    def _onKeyUp(self,ev):
        
        #phase down
        super()._onKeyUp(ev)
        if ev._stopPropagation:
            return
        
        childFound = False
        for c in self._children:
            if c.hasChild(ev.eventSource):
                c._onKeyUp(ev)
                childFound = True
                if c == ev.eventSource:
                    # we set event phase to up!
                    # This is the case if c is not a ContainerWidget.
                    ev._nextPhase()
                break
        
        # if no child has got the event.
        # the event has reached the deepest level.
        if not childFound:
            # we set event phase to up!
            ev._nextPhase()
        else:
            # pahse up
            if ev._stopPropagation:
                return
            super()._onKeyUp(ev)
    
    def _onTextInput(self,ev):
        
        #phase down
        super()._onTextInput(ev)
        if ev._stopPropagation:
            return
        
        childFound = False
        for c in self._children:
            if c.hasChild(ev.eventSource):
                c._onTextInput(ev)
                childFound = True
                if c == ev.eventSource:
                    # we set event phase to up!
                    # This is the case if c is not a ContainerWidget.
                    ev._nextPhase()
                break
                
        # if no child has got the event.
        # the event has reached the deepest level.
        if not childFound:
            # we set event phase to up!
            ev._nextPhase()
        else:
            # pahse up
            if ev._stopPropagation:
                return
            super()._onTextInput(ev)
                            
    def _invalidate(self):
        for c in self._children:
            c._invalidate()
        super()._invalidate()
        