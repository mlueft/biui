
##
#
#
class Widget:
    
    ## Base class for all GUI elements.
    #
    #
    def __init__(self):
        # Stores the width of the GUI element.
        self._width = 100
        #Stores the height of the GUI element.
        self._height = 100
        # stores the x position of the GUI element
        self._x = 0
        # Stores the y position of the GUI element
        self._y = 0
        # Stores the collected "dirty rect" for GUI repainting
        self._dirtyRects = []
        # Stores a reference the parent GUI element
        self._parent = None
        
    ## Sets the x/y position of the GUI element.
    #
    #  @return            A tuple representing the position.
    #
    def getPosition(self):
        return (self._x, self._y)
    
    ## Returns the x/y position of the GUI element.
    #
    #  @return            A tuple representing the size.
    #
    def getSize(self):
        return (self._width, self._height)
    
    ## Sets the x position of the GUI element.
    #
    #  @param value       An integer value.
    #  @return            None
    #
    def setX(self, value):
        # record old dirty rect for the old position
        self._recordDirtyRect()
        self._x = value
        self._invalidate()
    
    ## Returns the x position of the GUI element.
    #
    #  @return            An integer value.
    #
    def getX(self):
        return self._x

    ## Sets the y position of the GUI element.
    #
    #  @param value       An integer value.
    #  @return            None    
    #
    def setY(self, value):
        # record old dirty rect
        self._recordDirtyRect()
        self._y = value
        self._invalidate()
    
    # Returns the y position of the GUI element.
    #
    #  @return            An integer value.
    #
    def getY(self):
        return self._y
    
    ## Sets the width of the GUI element.
    #
    #  @param value       An integer value.
    #  @return            None
    #       
    def setWidth(self, value):
        # record old dirty rect
        self._recordDirtyRect()
        self._width = value
        self._invalidate()
    
    ## Return the width of the GUI element.
    #
    #  @return            An integer value.
    #
    def getWidth(self):
        return self._width
    
    ## Sets the height of the GUI element.
    #
    #  @param value       An integer value.
    #  @return            None
    #
    def setHeight(self, value):
        # record old dirty rect
        self._recordDirtyRect()
        self._height = value
        self._invalidate()
    
    # Returns the y position of the GUI element.
    #
    #  @return            An integer value.
    #
    def getHeight(self):
        return self._height
    
    ## Records the current Rect of the GUI element
    #  in the parent's coordinate system.
    #
    #  @return            None
    #
    def _recordDirtyRect(self):
        pos = self.toGlobal((0,0))
        self._dirtyRects.append((
            pos[0],
            pos[1],
            self._width,
            self._height
        ))
        
    ## Does some enecassary work if the GUI element
    #  became invalide. For example after changing it's size.
    #
    #  @return            None
    #
    def _invalidate(self):
        # record new dirty rect
        self._recordDirtyRect()
    
    ## Returns all dirty rects of the GUI element
    #  since the last call. Calling this funtion clears
    #  all recorded rects.
    #
    #  @return            A list with tuples.
    #    
    def _getDirtyRectangles(self):
        result = self._dirtyRects.copy()
        self._dirtyRects.clear()
        return result
    
    ## Returns the parent GUI element of the GUI element.
    #  Normally it is the main window or a container element
    #  that contains the GUI element.
    #
    #  @return            A Widget instance.
    #
    def getParent(self):
        return self._parent
    
    ## Sets the parent GUI element.
    #
    #  @param parent      A Window or ContainerWidget
    #
    #  @return            None
    #
    def setParent(self,parent):
        if self._parent != None:
            self._parent.removeChild(self)
        
        self._parent = parent
     
    ## Returns the drawing surface of the GUI element.
    #  This is for internal use. Just use the surface
    #  if you know what you are doing.
    #
    #  @return            The drawing surface
    #
    def _getSurface(self):
        return self._parent._getSurface()
    
    ## Redraws the GUI element. This is for internal use.
    #  Just usr this function if you know what you are doing.
    #
    #  @param surface            The drawing surface.
    #
    #  @return            None
    #
    def _redraw(self,surface):
        #print("Widget::_redraw")
        pass

    ## Is called if a mouse button got pressed and the
    #  mouse pointer is over the GUI element.
    #
    #  @param ev                 A MouseEvent
    #  @return            None
    #
    def onMouseDown(self,ev):
        pass

    ## Is called if a mouse button got released and the
    #  mouse pointer is over the GUI element.
    #
    #  @param ev                 A MouseEvent
    #  @return                   None
    #
    def onMouseUp(self,ev):
        pass
     
    ## Is called if a mouse wheel got turned and the
    #  mouse pointer is over the GUI element.
    #  @param ev   biui.MouseEvent.MouseEvent
    #
    #  @param ev                 A MouseEvent
    #  @return                   None
    #
    def onMouseWheel(self,ev):
        pass
    
    ## Is called if the mouse pointer enters the GUI element.
    #
    #  @param ev                 A MouseEvent
    #  @return                   None
    #
    def onMouseEnter(self,ev):
        pass
    
    ## Is called if the mouse pointer leaves the GUI element.
    #
    #  @param ev                 A MouseEvent
    #  @return                   None
    #
    def onMouseLeave(self,ev):
        pass
    
    ## Is called if the mouse pointer is over the GUI element
    #  and moved.
    #
    #  @param ev                 A MouseEvent
    #  @return                   None
    #
    def onMouseMove(self,ev):
        pass
    
    ## Is called key got pressed.
    #  It's necassry to call super().onKeyDown(ev)
    #  at the end.
    #
    #  @param ev                 A KeyEvent.
    #  @return                   None
    #
    def onKeyDown(self,ev):
        #print( "Widget::onKeyDown  : " +str(ev) )
        pass
    
    ## Is called if a key got released.
    #  It's necassry to call super().onKeyUp(ev)
    #  at the end.
    #
    #  @param ev                 A KeyEvent.
    #  @return                   None
    #
    def onKeyUp(self,ev):
        #print( "Widget::onKeyUp    : " +str(ev) )
        pass
    
    ## Is called if a key press ends in a entered character.
    #  It's necassry to call super().onTextInput(ev)
    #  at the end.
    #
    #  @param ev                 A KeyEvent.
    #  @return                   None
    #    
    def onTextInput(self,ev):
        #print( "Widget::onTextInput: " +str(ev) )
        pass

    ## Converts global coordinates to local coordinates
    #
    #  @param coordinate         A tuple with x and y coordinates.
    #  @return                   A tuple.
    #
    #
    def toLocal(self, coordinates):
        result = ( coordinates[0]-self._x,coordinates[1]-self._y)
        
        if self._parent != None:
            result = self._parent.toLocal(result)
        
        return result
    
    ## Converts local coordinates to global coordinates
    #
    #  @param coordinate         A Tuple with x and y coordinates.
    #  @return                   A tuple. 
    #
    def toGlobal(self,coordinates):
        result = ( self._x+coordinates[0],self._y+coordinates[1])
        
        if self._parent != None:
            result = self._parent.toGlobal(result)
        
        return result