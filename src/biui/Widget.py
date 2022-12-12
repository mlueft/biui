import biui


### Base class for all GUI elements.
##
##
class Widget:
    
    ###
    ##
    ##
    def __init__(self):
        ## Stores the width of the GUI element.
        self._width = 100
        ##Stores the height of the GUI element.
        self._height = 100
        ## 
        self._minWidth = 0
        ## 
        self._minHeight = 0
        ## 
        self._maxWidth = 10000
        ## 
        self._maxHeight = 10000
        ## stores the x position of the GUI element
        self._x = 0
        ## Stores the y position of the GUI element
        self._y = 0
        ## Stores the collected "dirty rect" for GUI repainting
        self._dirtyRects = []
        ## Stores a reference the parent GUI element
        self._parent = None
        ##
        self._isInvalide = True
        ##
        self._name = ""
        ##
        self._alignment = biui.Alignment.ABSOLUTE
        ## A reference to the theme function which is used to draw the widget.
        ## On Containerwidgets it's used to draw the widget's background.
        theme = biui.getTheme()
        self._themeBackgroundfunction = theme.drawEmpty        
        ##
        self.onMouseUp = biui.EventManager()
        ##
        self.onTextInput = biui.EventManager()
        ##
        self.onKeyUp = biui.EventManager()
        ##
        self.onKeyDown = biui.EventManager()
        ##
        self.onMouseMove = biui.EventManager()
        ##
        self.onMouseLeave = biui.EventManager()
        ##
        self.onMouseEnter = biui.EventManager()
        ##
        self.onMouseWheel = biui.EventManager()
        ##
        self.onMouseUp = biui.EventManager()
        ##
        self.onMouseDown = biui.EventManager()
        ##
        self.onMouseClick = biui.EventManager()
        ##
        self._resized = False
        ##
        self.onResized = biui.EventManager()

        
    ### Sets the x/y position of the GUI element.
    ##
    ##  @return            A tuple representing the position.
    ##
    @property
    def position(self):
        return (self._x, self._y)
    
    ### Returns the x/y position of the GUI element.
    ##
    ##  @return            A tuple representing the size.
    ##
    @property
    def size(self):
        return (self.width, self.height)

    ### 
    ##
    ##  @return            An integer value.
    ##
    @property
    def name(self):
        return self._name
    
    ### Sets the x position of the GUI element.
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##
    @name.setter
    def name(self, value):
        self._name = value
            
    ### Returns the x position of the GUI element.
    ##
    ##  @return            An integer value.
    ##
    @property
    def x(self):
        return self._x
    
    ### Sets the x position of the GUI element.
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##
    @x.setter
    def x(self, value):
        value = int(value)
        if value == self._x:
            return
        ## record old dirty rect for the old position
        self._recordDirtyRect()
        self._x = value
        self._invalidate()
    
    ## Returns the y position of the GUI element.
    ##
    ##  @return            An integer value.
    ##
    @property
    def y(self):
        return self._y

    ### Sets the y position of the GUI element.
    ##
    ##  @param value       An integer value.
    ##  @return            None    
    ##
    @y.setter
    def y(self, value):
        value = int(value)
        if value == self._y:
            return
        ## record old dirty rect
        self._recordDirtyRect()
        self._y = value
        self._invalidate()
    
    ### Set/Get the left border of the widget.
    ##  Is equqalent to x.
    ##
    ##  @return            An integer value.
    ##
    @property
    def left(self):
        return self.x
    
    ### Sets the left border.
    ##  Its the distance of the parent'sleft border to
    ##  the own left border.
    ##
    ##  @param value       An integer value.
    ##
    @left.setter
    def left(self,value):
        r = self.x+self.width
        self.x = value
        self.width = r-self.x
    
    ### Set/Get the top border of the widget.
    ##  Setting this value does not change 
    ##  any other border of the widget.
    ##  Incrementing top decreses the height.
    ##  The bottom border stays the same.
    ##
    ##  @return            An integer value.
    ##
    @property
    def top(self):
        return self.y
    
    ### Sets the top border.
    ##  Its the distance of the parents top 
    ##  border to the own top border.
    ##
    ##  @param value       An integer value.
    ##
    @top.setter
    def top(self,value):
        b = self.y+self.height
        self.y = value
        self.height = b-self.y
    
    ### Set/Get the right border of the widget.
    ##  Setting this value does not change 
    ##  any other border of the widget.
    ##  Incrementing right increments width.
    ##  The left border stays the same.
    ##
    ##  @return            An integer value.
    ##
    @property
    def right(self):
        return self.x+self.width
    
    ### Sets the right border of the widget.
    ##  It is the distance of the parent left border
    ##  to the own right border.
    ##
    ##  @param value       An integer value.
    ##
    @right.setter
    def right(self,value):
        self.width = value-self.x
    
    ### Set/Get the bottom border of the widget.
    ##  Setting this value does not change 
    ##  any other border of the widget.
    ##  Incrementing bottom increments height.
    ##  top stays the same.
    ##
    ##  @return            An integer value.
    ##
    @property
    def bottom(self):
        return self.y+self.height
    
    ### Sets the bottom border of the widget.
    ##  Its value is the distance of the top
    ##  border of the parent widget to the own bottom
    ##  border-
    ##
    ##  @param value       An integer value.
    ##
    @bottom.setter
    def bottom(self,value):
        self.height = value-self.y
    
    ### Return the width of the GUI element.
    ##
    ##  @return            An integer value.
    ##
    @property
    def width(self):
        return self._width
    
    ### Sets the width of the GUI element.
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##
    @width.setter     
    def width(self, value):
        value = int(value)
        
        if value == self._width:
            return
        
        ## record old dirty rect
        if self._alignment != biui.Alignment.FILL:
            value = min(value, self._maxWidth)
            value = max(value, self._minWidth)
        
        self._recordDirtyRect()
        self._width = max(0,value)
        self._invalidate()
        self.onResized.provoke(biui.Event(self))
        self._resized = True
            
    ### Returns the min widt value of the widget.
    ##
    ##  @return            An integer value.
    ##
    @property
    def minWidth(self):
        return self._minWidth
    
    ### Sets the min width value of the widget.
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##    
    @minWidth.setter   
    def minWidth(self, value):
        value = int(value)
        self._minWidth = max(0,value)
        if self._minWidth > self._width:
            self.width = self._minWidth

    ### Returns the max width value of the widget.
    ##
    ##  @return            An integer value.
    ##
    @property
    def maxWidth(self):
        return self._maxWidth

    ### Sets the max width value of the widget.
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##    
    @maxWidth.setter   
    def maxWidth(self, value):
        value = int(value)
        self._maxWidth = max(0,value)
        if self._maxWidth < self._width:
            self.width = self._maxWidth
    
    ## Returns the y position of the GUI element.
    ##
    ##  @return            An integer value.
    ##
    @property
    def height(self):
        return self._height
            
    ### Sets the height of the GUI element.
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##
    @height.setter
    def height(self, value):
        value = int(value)
        
        if value == self._height:
            return
        
        ## record old dirty rect
        if self._alignment != biui.Alignment.FILL:
            value = min(value, self._maxWidth)
            value = max(value, self._minWidth)
            
        self._recordDirtyRect()
        self._height = max(1,value)
        self.onResized.provoke(biui.Event(self))
        self._invalidate()
        self._resized = True
            
    ### Returns the min width of the widget.
    ##
    ##  @return            An integer value.
    ##
    @property
    def minHeight(self):
        return self._minHeight
    
    ### Sets the min width of the widget.
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##    
    @minHeight.setter   
    def minHeight(self, value):
        value = int(value)
        self._minHeight = max(0,value)
        if self._minHeight > self._height:
            self.height = self._minHeight

    ### Returns the max. height of the widget.
    ##
    ##  @return            An integer value.
    ##
    @property
    def maxHeight(self):
        return self._maxHeight

    ### Sets the max. height of the widget.
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##    
    @maxHeight.setter   
    def maxHeight(self, value):
        value = int(value)
        self._maxHeight = max(0,value)
        if self._maxHeight < self._height:
            self.height = self._maxHeight
        
    ### Checks if the given child is a child object or
    ##  if it is the current widget.
    ##
    ##
    def hasChild(self,child):
        return child == self
    
    ### Returns the alignment setting.
    ##
    ##
    @property
    def alignment(self):
        return self._alignment
            
    ### Serts the alignment setting.
    ##
    ##
    @alignment.setter
    def alignment(self,value):
        self._alignment = value
    
    ### Records the current Rect of the GUI element
    ##  in the parent's coordinate system.
    ##
    ##  @return            None
    ##
    def _recordDirtyRect(self):
        if self.parent == None:
            return
        if self.window == None:
            return
        pos = self.toGlobal((0,0))
        self.window.recortDirtyRectangle((
            pos[0],
            pos[1],
            self._width,
            self._height
        ))
        
    ### Checks if the widget is invalide.
    ##  If it is invalide, it has to bee redrawn
    ##  at the next refresh.
    ##
    ##
    def isInvalide(self):
        return self._isInvalide
     
    ### Does some enecassary work if the GUI element
    ##  became invalide. For example after changing its size.
    ##
    ##  @return            None
    ##
    def _invalidate(self):
        ## record new dirty rect
        self._recordDirtyRect()
        ## set flag to recalculate the layout.
        ## set flag to redraw widget
        self._isInvalide = True
    
    ### Returns all dirty rects of the GUI element
    ##  since the last call. Calling this funtion clears
    ##  all recorded rects.
    ##
    ##  @return            A list with tuples.
    ##    
    def _getDirtyRectangles(self):
        result = self._dirtyRects.copy()
        self._dirtyRects.clear()
        return result
    
    ### Returns the parent window of the widget.
    ##
    ##
    @property
    def window(self):
        parent = self.parent
        while True:
            if type(parent) == biui.Window:
                return parent
            if parent == None:
                return
            parent = parent.parent 

    ### Returns the parent GUI element of the GUI element.
    ##  Normally it is the main window or a container element
    ##  that contains the GUI element.
    ##
    ##  @return            A Widget instance.
    ##
    @property
    def parent(self):
        return self._parent
    
    ### Sets the parent GUI element.
    ##
    ##  @param parent      A Window or ContainerWidget
    ##
    ##  @return            None
    ##
    @parent.setter
    def parent(self,parent):
        if self._parent != None:
            self._parent.removeChild(self)
        
        self._parent = parent
     
    ### Returns the drawing texture of the GUI element.
    ##  This is for internal use. Just use the texture
    ##  if you know what you are doing.
    ##
    ##  @return            The drawing texture
    ##
    def _getTexture(self):
        return self._parent._getTexture()
    
    ### Recalculates the layout of the widget.
    ##
    ##
    def _calculateLayout(self):
        if self._resized:
            self.onResized.provoke(biui.Event(self))
            self._resized = False
            
    ### Is called before the drawing procedure ist starting
    ##  to calculate the layout and before _redraw is called.
    ##
    def _beforeDraw(self):
        pass
    
    ### Is called after all redwaing is done.
    ##
    ##
    def _afterDraw(self):
        pass
    
    ### Redraws the GUI element. This is for internal use.
    ##  Just use this function if you know what you are doing.
    ##  Do not call super()._redraw().
    ##  Copy the guard to your _redraw()-version
    ##  and set _isInvalide to False at the end!
    ##  If you derive from a widget and call super(),
    ##  The parent would overdraw your widget.
    ##  @param surface            The drawing surface.
    ##
    ##  @return            None
    ##
    def _redraw(self, texture, forceRedraw=False):
        
        if not self.isInvalide():
            if not forceRedraw:
                return 
                
        theme = biui.getTheme()
        self._themeBackgroundfunction(self.window.renderer,self,texture)
        
        self._isInvalide = False
        
        
    ### Is called if a mouse button got pressed and the
    ##  mouse pointer is over the GUI element.
    ##
    ##  @param ev                 A MouseEvent
    ##  @return            None
    ##
    def _onMouseDown(self,ev):
        self.onMouseDown.provoke(ev)
        
    ### Is called if a mouse button got released and the
    ##  mouse pointer is over the GUI element.
    ##
    ##  @param ev                 A MouseEvent
    ##  @return                   None
    ##
    def _onMouseUp(self,ev):
        self.onMouseUp.provoke(ev)

    ### Is called if a mouse had a click release and the
    ##  mouse pointer is over the GUI element.
    ##
    ##  @param ev                 A MouseEvent
    ##  @return                   None
    ##
    def _onMouseClick(self,ev):
        self.onMouseClick.provoke(ev)
             
    ### Is called if a mouse wheel got turned and the
    ##  mouse pointer is over the GUI element.
    ##  @param ev   biui.MouseEvent.MouseEvent
    ##
    ##  @param ev                 A MouseEvent
    ##  @return                   None
    ##
    def _onMouseWheel(self,ev):
        self.onMouseWheel.provoke(ev)
    
    ### Is called if the mouse pointer enters the GUI element.
    ##
    ##  @param ev                 A MouseEvent
    ##  @return                   None
    ##
    def _onMouseEnter(self,ev):
        self.onMouseEnter.provoke(ev)
    
    ### Is called if the mouse pointer leaves the GUI element.
    ##
    ##  @param ev                 A MouseEvent
    ##  @return                   None
    ##
    def _onMouseLeave(self,ev):
        self.onMouseLeave.provoke(ev)
    
    ### Is called if the mouse pointer is over the GUI element
    ##  and moved.
    ##
    ##  @param ev                 A MouseEvent
    ##  @return                   None
    ##
    def _onMouseMove(self,ev):
        self.onMouseMove.provoke(ev)
    
    ### Is called key got pressed.
    ##  It is necassry to call super().onKeyDown(ev)
    ##  at the end.
    ##
    ##  @param ev                 A KeyEvent.
    ##  @return                   None
    ##
    def _onKeyDown(self,ev):
        self.onKeyDown.provoke(ev)
    
    ### Is called if a key got released.
    ##  It is necassry to call super().onKeyUp(ev)
    ##  at the end.
    ##
    ##  @param ev                 A KeyEvent.
    ##  @return                   None
    ##
    def _onKeyUp(self,ev):
        self.onKeyUp.provoke(ev)
    
    ### Is called if a key press ends in a entered character.
    ##  It is necassry to call super().onTextInput(ev)
    ##  at the end.
    ##
    ##  @param ev                 A KeyEvent.
    ##  @return                   None
    ##    
    def _onTextInput(self,ev):
        self.onTextInput.provoke(ev)

    ### Converts global coordinates to local coordinates
    ##
    ##  @param coordinate         A tuple with x and y coordinates.
    ##  @return                   A tuple.
    ##
    ##
    def toLocal(self, coordinates):
        result = ( coordinates[0]-self._x,coordinates[1]-self._y)
        
        if self._parent != None:
            result = self._parent.toLocal(result)
        
        return result
    
    ### Converts local coordinates to the top window's coordinates
    ##
    ##  @param coordinate         A Tuple with x and y coordinates.
    ##  @return                   A tuple. 
    ##
    def toGlobal(self,coordinates):
        result = ( self._x+coordinates[0],self._y+coordinates[1])
        
        if self._parent != None:
            result = self._parent.toGlobal(result)
        
        return result