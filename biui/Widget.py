import biui

## Base class for all GUI elements.
#
#
class Widget:
    
    ##
    #
    #
    def __init__(self):
        # Stores the width of the GUI element.
        self._width = 100
        #Stores the height of the GUI element.
        self._height = 100
        # 
        self._minWidth = 1
        # 
        self._minHeight = 1
        # 
        self._maxWidth = 10000
        # 
        self._maxHeight = 10000
        # stores the x position of the GUI element
        self._x = 0
        # Stores the y position of the GUI element
        self._y = 0
        # Stores the collected "dirty rect" for GUI repainting
        self._dirtyRects = []
        # Stores a reference the parent GUI element
        self._parent = None
        #
        self._runLayoutManager = True
        #
        self._alignment = biui.Alignment.ABSOLUTE
        #
        self.onMouseUp = biui.EventManager()
        #
        self.onTextInput = biui.EventManager()
        #
        self.onKeyUp = biui.EventManager()
        #
        self.onKeyDown = biui.EventManager()
        #
        self.onMouseMove = biui.EventManager()
        #
        self.onMouseLeave = biui.EventManager()
        #
        self.onMouseEnter = biui.EventManager()
        #
        self.onMouseWheel = biui.EventManager()
        #
        self.onMouseUp = biui.EventManager()
        #
        self.onMouseDown = biui.EventManager()
        
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
        if self._alignment != biui.Alignment.FILL:
            value = min(value, self._maxWidth)
            value = max(value, self._minWidth)
        
        if value != self._width:
            self._recordDirtyRect()
            self._width = max(1,value)
            self._invalidate()
    
    ## Return the width of the GUI element.
    #
    #  @return            An integer value.
    #
    def getWidth(self):
        return self._width
    
    ## 
    #
    #  @param value       An integer value.
    #  @return            None
    #       
    def setMinWidth(self, value):
        self._minWidth = max(1,value)
        if self._minWidth > self._width:
            self.setWidth( self._minWidth )
            
    ## 
    #
    #  @return            An integer value.
    #
    def getMinWidth(self):
        return self._minWidth

    ## 
    #
    #  @param value       An integer value.
    #  @return            None
    #       
    def setMaxWidth(self, value):
        self._maxWidth = max(1,value)
        if self._maxWidth < self._width:
            self.setWidth( self._maxWidth )

    ## 
    #
    #  @return            An integer value.
    #
    def getMaxWidth(self):
        return self._maxWidth
            
    ## Sets the height of the GUI element.
    #
    #  @param value       An integer value.
    #  @return            None
    #
    def setHeight(self, value):
        # record old dirty rect
        if self._alignment != biui.Alignment.FILL:
            value = min(value, self._maxWidth)
            value = max(value, self._minWidth)
            
        if value != self._height:
            self._recordDirtyRect()
            self._height = max(1,value)
            self._invalidate()
    
    # Returns the y position of the GUI element.
    #
    #  @return            An integer value.
    #
    def getHeight(self):
        return self._height
    
    ## 
    #
    #  @param value       An integer value.
    #  @return            None
    #       
    def setMinHeight(self, value):
        self._minHeight = max(1,value)
        if self._minHeight > self._height:
            self.setHeight( self._minHeight )
            
    ## 
    #
    #  @return            An integer value.
    #
    def getMinHeight(self):
        return self._minHeight

    ## 
    #
    #  @param value       An integer value.
    #  @return            None
    #       
    def setMaxHeight(self, value):
        self._maxHeight = max(1,value)
        if self._maxHeight < self._height:
            self.setHeight( self._maxHeight )

    ## 
    #
    #  @return            An integer value.
    #
    def getMaxHeight(self):
        return self._maxHeight
        
    ##
    #
    #
    def setAlignment(self,value):
        self._alignment = value
    
    ##
    #
    #
    def getAlignment(self):
        return self._alignment
    
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
        # set flag to recalculate the layout.
        self._runLayoutManager = True
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
    
    def getWindow(self):
        parent = self.getParent()
        while True:
            newParent = parent.getParent()
            if newParent == None:
                return parent
            parent = newParent 
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
    
    ##
    #
    #
    def _calculateLayout(self):
        if not self._runLayoutManager:
            return
        self._layoutManager._calculateLayout()
        self._runLayoutManager = False
    
    ## Redraws the GUI element. This is for internal use.
    #  Just usr this function if you know what you are doing.
    #
    #  @param surface            The drawing surface.
    #
    #  @return            None
    #
    def _redraw(self,surface):
        pass

    ## Is called if a mouse button got pressed and the
    #  mouse pointer is over the GUI element.
    #
    #  @param ev                 A MouseEvent
    #  @return            None
    #
    def _onMouseDown(self,ev):
        self.onMouseDown.provoke(ev)

    ## Is called if a mouse button got released and the
    #  mouse pointer is over the GUI element.
    #
    #  @param ev                 A MouseEvent
    #  @return                   None
    #
    def _onMouseUp(self,ev):
        self.onMouseUp.provoke(ev)
     
    ## Is called if a mouse wheel got turned and the
    #  mouse pointer is over the GUI element.
    #  @param ev   biui.MouseEvent.MouseEvent
    #
    #  @param ev                 A MouseEvent
    #  @return                   None
    #
    def _onMouseWheel(self,ev):
        self.onMouseWheel.provoke(ev)
    
    ## Is called if the mouse pointer enters the GUI element.
    #
    #  @param ev                 A MouseEvent
    #  @return                   None
    #
    def _onMouseEnter(self,ev):
        self.onMouseEnter.provoke(ev)
    
    ## Is called if the mouse pointer leaves the GUI element.
    #
    #  @param ev                 A MouseEvent
    #  @return                   None
    #
    def _onMouseLeave(self,ev):
        self.onMouseLeave.provoke(ev)
    
    ## Is called if the mouse pointer is over the GUI element
    #  and moved.
    #
    #  @param ev                 A MouseEvent
    #  @return                   None
    #
    def _onMouseMove(self,ev):
        self.onMouseMove.provoke(ev)
    
    ## Is called key got pressed.
    #  It's necassry to call super().onKeyDown(ev)
    #  at the end.
    #
    #  @param ev                 A KeyEvent.
    #  @return                   None
    #
    def _onKeyDown(self,ev):
        self.onKeyDown.provoke(ev)
    
    ## Is called if a key got released.
    #  It's necassry to call super().onKeyUp(ev)
    #  at the end.
    #
    #  @param ev                 A KeyEvent.
    #  @return                   None
    #
    def _onKeyUp(self,ev):
        self.onKeyUp.provoke(ev)
    
    ## Is called if a key press ends in a entered character.
    #  It's necassry to call super().onTextInput(ev)
    #  at the end.
    #
    #  @param ev                 A KeyEvent.
    #  @return                   None
    #    
    def _onTextInput(self,ev):
        self.onTextInput.provoke(ev)

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