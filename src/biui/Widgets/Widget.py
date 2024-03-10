#include "biui.inc"
#include "pysdl2.inc"

import sdl2
from typing import List,Callable
import biui
from biui.Color import Color

from biui.Events import Event
from biui.Events import KeyEvent
from biui.Events import MouseEvent
from biui.Events import EventManager

from biui.Enum import Alignment
from biui.LayoutManager import LayoutManager



##from biui.Window import Window

### Base class for all GUI elements.
##
##
class Widget():
    
    ###
    ##
    ##
    def __init__(self):
        ## Stores the width of the GUI element.
        self._width:int = 100
        ##Stores the height of the GUI element.
        self._height:int = 100
        ## 
        self._minWidth:int = 0
        ## 
        self._minHeight:int  = 0
        ## 
        self._maxWidth:int  = 10000
        ## 
        self._maxHeight:int  = 10000
        ## stores the x position of the GUI element
        self._x:int  = 0
        ## Stores the y position of the GUI element
        self._y:int  = 0
        ## Stores the collected "dirty rect" for GUI repainting
        self._dirtyRects:List = []
        ## Stores a reference the parent GUI element
        self._parent:ContainerWidget = None
        ##
        self._isInvalide:bool = True
        ##
        self._name:str = ""
        ##
        self._tooltip:str = None
        ##
        self._alignment:int = Alignment.ABSOLUTE
        ## A reference to the theme function which is used to draw the widget.
        ## On Containerwidgets it´s used to draw the widget´s background.
        theme = biui.getTheme()
        self._themeBackgroundfunction:Callable = theme.drawEmpty        
        ##
        self.onTextInput:EventManager = EventManager()
        ##
        self.onKeyUp:EventManager = EventManager()
        ##
        self.onKeyDown:EventManager = EventManager()
        ##
        self.onMouseMove:EventManager = EventManager()
        ##
        self.onMouseLeave:EventManager = EventManager()
        ##
        self.onMouseEnter:EventManager = EventManager()
        ##
        self.onMouseWheel:EventManager = EventManager()
        ##
        self.onMouseUp:EventManager = EventManager()
        ##
        self.onMouseDown:EventManager = EventManager()
        ##
        self.onMouseClick:EventManager = EventManager()
        ##
        self.onBeforeDraw:EventManager = EventManager()
        ##
        self.onAfterDraw:EventManager = EventManager()
        ##
        self.onFocus:EventManager = EventManager()
        ##
        self.onFocusLost:EventManager = EventManager()
        ##
        self._resized:bool = False
        ##
        self.onResized:EventManager = EventManager()
        ## Is triggered when the widget got added to a parent
        self.onGotAdded:EventManager = EventManager()
        ## Is triggered when the widget got removed from a parent
        self.onGotRemoved:EventManager = EventManager()

        ##
        self.__borderColor:Color = None
        self.__backColor:Color = None
        
        self.onMouseDown.add(self.hndMouseDown)
        
    ### Handels the mouse down event to set the focus on the current widget.
    ##
    ##
    def hndMouseDown(self, ev):

        if self.window is None:
            return

        ## The event is going down and up the DOM
        ## We do not process at parents!
        if ev.eventSource != self:
            return 
        
        self.window.setFocus(self)
        
    ### @see Widget._invalidate
    ##
    ##   TODO: hinting return type
    def getChildAt(self, pos:tuple[int,int]):# pylint: disable=unused-argument
        return self
    
    ### Returns the x/y position of the GUI element.
    ##
    ##  @return            A tuple representing the position.
    ##
    @property
    def position(self)->tuple[int,int]:
        return (self._x, self._y)
    
    ### Returns the width/height position of the GUI element.
    ##
    ##  @return            A tuple representing the size.
    ##
    @property
    def size(self)->tuple[int,int]:
        return (self.width, self.height)

    ### 
    ##
    ##  @return            
    ##
    @property
    def backColor(self)->Color:
        return self.__backColor
    
    ### Sets the backcolor for this widget.
    ##
    ##  @param value       
    ##  @return            None
    ##
    @backColor.setter
    def backColor(self, value:Color)->None:
        if self.__backColor == value:
            return
        
        self.__backColor = value
        self._invalidate()
        
    ### 
    ##
    ##  @return            
    ##
    @property
    def borderColor(self)->Color:
        return self.__borderColor
    
    ### Sets the borderColor for this widget.
    ##
    ##  @param value       
    ##  @return            None
    ##
    @borderColor.setter
    def borderColor(self, value:Color)->None:
        if self.__borderColor == value:
            return
        
        self.__borderColor = value
        self._invalidate()
        
    ### 
    ##
    ##  @return            An integer value.
    ##
    @property
    def tooltip(self)->str:
        return self._tooltip
    
    ### Sets the tooltip text for this widget.
    ##
    ##  @param value       The text to show as tooltp
    ##  @return            None
    ##
    @tooltip.setter
    def tooltip(self, value:str)->None:
        self._tooltip = value
        
    ### 
    ##
    ##  @return            An integer value.
    ##
    @property
    def name(self)->str:
        return self._name
    
    ### Sets the x position of the GUI element.
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##
    @name.setter
    def name(self, value:str)->None:
        self._name = value
            
    ### Returns the x position of the GUI element.
    ##
    ##  @return            An integer value.
    ##
    @property
    def x(self)->int:
        return self._x
    
    ### Sets the x position of the GUI element.
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##
    @x.setter
    def x(self, value:int)->None:
        value = int(value)
        if value == self._x:
            return
        ## record old dirty rect for the old position
        self._invalidate()
        self._x = value
        self._invalidate()
    
    ## Returns the y position of the GUI element.
    ##
    ##  @return            An integer value.
    ##
    @property
    def y(self)->int:
        return self._y

    ### Sets the y position of the GUI element.
    ##
    ##  @param value       An integer value.
    ##  @return            None    
    ##
    @y.setter
    def y(self, value:int)->None:
        value = int(value)
        if value == self._y:
            return
        ## record old dirty rect
        self._invalidate()
        self._y = value
        self._invalidate()
    
    ### Set/Get the left border of the widget.
    ##  Is equqalent to x.
    ##
    ##  @return            An integer value.
    ##
    @property
    def left(self)->int:
        return self.x
    
    ### Sets the left border.
    ##  Its the distance of the parent´sleft border to
    ##  the own left border.
    ##
    ##  @param value       An integer value.
    ##
    @left.setter
    def left(self,value:int)->None:
        ##r = self.x+self.width
        ##self.x = value
        ##self.width = r-self.x
        r = self.x+self.width
        self.width = r-value
        self.x = value
    
    ### Set/Get the top border of the widget.
    ##  Setting this value does not change 
    ##  any other border of the widget.
    ##  Incrementing top decreses the height.
    ##  The bottom border stays the same.
    ##
    ##  @return            An integer value.
    ##
    @property
    def top(self)->int:
        return self.y
    
    ### Sets the top border.
    ##  Its the distance of the parents top 
    ##  border to the own top border.
    ##
    ##  @param value       An integer value.
    ##
    @top.setter
    def top(self,value:int)->None:
        ##b = self.y+self.height
        ##self.y = value
        ##self.height = b-self.y
        b = self.y+self.height
        self.height = b-value
        self.y = value
        
    
    ### Set/Get the right border of the widget.
    ##  Setting this value does not change 
    ##  any other border of the widget.
    ##  Incrementing right increments width.
    ##  The left border stays the same.
    ##
    ##  @return            An integer value.
    ##
    @property
    def right(self)->int:
        return self.x+self.width
    
    ### Sets the right border of the widget.
    ##  It is the distance of the parent left border
    ##  to the own right border.
    ##
    ##  @param value       An integer value.
    ##
    @right.setter
    def right(self,value:int)->None:
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
    def bottom(self)->int:
        return self.y+self.height
    
    ### Sets the bottom border of the widget.
    ##  Its value is the distance of the top
    ##  border of the parent widget to the own bottom
    ##  border-
    ##
    ##  @param value       An integer value.
    ##
    @bottom.setter
    def bottom(self,value:int)->None:
        self.height = value-self.y
    
    ### Return the width of the GUI element.
    ##
    ##  @return            An integer value.
    ##
    @property
    def width(self)->int:
        return self._width
    
    ### Sets the width of the GUI element.
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##
    @width.setter     
    def width(self, value:int)->None:
        value = int(value)
        
        if value == self._width:
            return
        
        ## record old dirty rect
        if self._alignment != Alignment.FILL:
            value = min(value, self._maxWidth)
            value = max(value, self._minWidth)
        
        self._invalidate()
        self._width = max(0,value)
        self._invalidate()
        self.onResized.provoke(Event(self))
        self._resized = True
            
    ### Returns the min widt value of the widget.
    ##
    ##  @return            An integer value.
    ##
    @property
    def minWidth(self)->int:
        return self._minWidth
    
    ### Sets the min width value of the widget.
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##    
    @minWidth.setter   
    def minWidth(self, value:int)->None:
        value = int(value)
        self._minWidth = max(0,value)
        if self._minWidth > self._width:
            self.width = self._minWidth

    ### Returns the max width value of the widget.
    ##
    ##  @return            An integer value.
    ##
    @property
    def maxWidth(self)->int:
        return self._maxWidth

    ### Sets the max width value of the widget.
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##    
    @maxWidth.setter   
    def maxWidth(self, value:int)->None:
        value = int(value)
        self._maxWidth = max(0,value)
        if self._maxWidth < self._width:
            self.width = self._maxWidth
    
    ## Returns the y position of the GUI element.
    ##
    ##  @return            An integer value.
    ##
    @property
    def height(self)->int:
        return self._height
            
    ### Sets the height of the GUI element.
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##
    @height.setter
    def height(self, value:int)->None:
        value = int(value)
        
        if value == self._height:
            return
        
        ## record old dirty rect
        if self._alignment != Alignment.FILL:
            value = min(value, self._maxWidth)
            value = max(value, self._minWidth)
            
        self._invalidate()
        self._height = max(1,value)
        self.onResized.provoke(Event(self))
        self._invalidate()
        self._resized = True
            
    ### Returns the min width of the widget.
    ##
    ##  @return            An integer value.
    ##
    @property
    def minHeight(self)->int:
        return self._minHeight
    
    ### Sets the min width of the widget.
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##    
    @minHeight.setter   
    def minHeight(self, value:int)->None:
        value = int(value)
        self._minHeight = max(0,value)
        if self._minHeight > self._height:
            self.height = self._minHeight

    ### Returns the max. height of the widget.
    ##
    ##  @return            An integer value.
    ##
    @property
    def maxHeight(self)->int:
        return self._maxHeight

    ### Sets the max. height of the widget.
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##    
    @maxHeight.setter   
    def maxHeight(self, value:int)->None:
        value = int(value)
        self._maxHeight = max(0,value)
        if self._maxHeight < self._height:
            self.height = self._maxHeight
        
    ###
    ##
    ##
    @property
    def hasChildren(self):
        return False
    
    ### Checks if the given child is a child object or
    ##  if it is the current widget.
    ##
    ## todo: hinting
    def hasChild(self,child)->bool:
        return child == self
    
    ### Returns the alignment setting.
    ##
    ##
    @property
    def alignment(self)->int:
        return self._alignment
            
    ### Serts the alignment setting.
    ##
    ##
    @alignment.setter
    def alignment(self,value:int)->None:
        self._alignment = value
    
    ### Records the current Rect of the GUI element
    ##  in the parent´s coordinate system.
    ##
    ##  @return            None
    ##
    def _recordDirtyRect(self,box:tuple[int,int,int,int])->None:
        if self.parent is None:
            return
        if self.window is None:
            return

        self.parent._recordDirtyRect(box)
        
    ### Checks if the widget is invalide.
    ##  If it is invalide, it has to be redrawn
    ##  at the next refresh.
    ##
    ##
    def isInvalide(self)->bool:
        return self._isInvalide
     
    ### Does some enecassary work if the GUI element
    ##  became invalide. For example after changing its size.
    ##
    ##  @return            None
    ##
    def _invalidate(self)->None:
        ## record new dirty rect
        box = self.position+self.size
        self._recordDirtyRect(box)
        ## set flag to recalculate thif self.window is None:e layout.
        ## set flag to redraw widget
        self._isInvalide = True
    
    ### Returns all dirty rects of the GUI element
    ##  since the last call. Calling this funtion clears
    ##  all recorded rects.
    ##
    ##  @return            A list with tuples.
    ##    
    ## OBSOLET
    def _getDirtyRectangles(self)->list[tuple[int,int,int,int]]:
        result = self._dirtyRects.copy()
        self._dirtyRects.clear()
        return result
    
    ### Returns the parent window of the widget.
    ##
    ## todo: hinting
    @property
    def window(self):#pylint: disable=inconsistent-return-statements
        ##TODO: Any thowbacks from including here?
        from biui.Widgets import Window
        parent = self.parent
        while True:
            if isinstance(parent,Window):#pylint: disable=no-else-return
                return parent
            elif parent == None:
                return
            parent = parent.parent 

    ### Returns the parent GUI element of the GUI element.
    ##  Normally it is the main window or a container element
    ##  that contains the GUI element.
    ##
    ##  @return            A Widget instance.
    ##  todo: hinting
    @property
    def parent(self):
        return self._parent
    
    ### Sets the parent GUI element.
    ##
    ##  @param parent      A Window or ContainerWidget
    ##
    ##  @return            None
    ##  todo: hinting
    @parent.setter
    def parent(self,parent)->None:
        if self._parent is not None:
            self._parent.removeChild(self)
        
        self._parent = parent
        
    ### Returns the drawing texture of the GUI element.
    ##  This is for internal use. Just use the texture
    ##  if you know what you are doing.
    ##
    ##  @return            The drawing texture
    ##  todo: hinting
    def _getTexture(self):
        return self._parent._getTexture()
    
    ### Recalculates the layout of the widget.
    ##
    ##
    def _calculateLayout(self)->None:
        if self._resized:
            self.onResized.provoke(Event(self))
            self._resized = False
            
    ### Is called before the drawing procedure ist starting
    ##  to calculate the layout and before _redraw is called.
    ##
    def _onBeforeDraw(self)->None:
        self.onBeforeDraw.provoke(Event(self))
    
    ### Is called after all redwaing is done.
    ##
    ##
    def _onAfterDraw(self)->None:
        self.onAfterDraw.provoke(Event(self))

    ### Is called when the widget got added to a parent.
    ##
    def _onGotAdded(self)->None:
        self.onGotAdded.provoke(Event(self))
    
    ### Is called when the widget got removed from a parent.
    ##
    ##
    def _onGotRemoved(self)->None:
        self.onGotRemoved.provoke(Event(self))
            
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
    ##  todo: hinting
    def _redraw(self, forceRedraw:bool=False):
        
        if not self.isInvalide():
            if not forceRedraw:
                return None
                
        PYSDL2_CREATETEXTURE(self.window.renderer,self.width,self.height,texture)
        
        self._themeBackgroundfunction(self,texture)
        
        self._isInvalide = False
        
        return texture
        
    ### Is called if a mouse button got pressed and the
    ##  mouse pointer is over the GUI element.
    ##
    ##  @param ev                 A MouseEvent
    ##  @return            None
    ##
    def _onMouseDown(self,ev:MouseEvent)->None:
        self.onMouseDown.provoke(ev)
        
    ### Is called if a mouse button got released and the
    ##  mouse pointer is over the GUI element.
    ##
    ##  @param ev                 A MouseEvent
    ##  @return                   None
    ##
    def _onMouseUp(self,ev:MouseEvent)->None:
        self.onMouseUp.provoke(ev)

    ### Is called if a mouse had a click release and the
    ##  mouse pointer is over the GUI element.
    ##
    ##  @param ev                 A MouseEvent
    ##  @return                   None
    ##
    def _onMouseClick(self,ev:MouseEvent)->None:
        self.onMouseClick.provoke(ev)
             
    ### Is called if a mouse wheel got turned and the
    ##  mouse pointer is over the GUI element.
    ##  @param ev   MouseEvent.MouseEvent
    ##
    ##  @param ev                 A MouseEvent
    ##  @return                   None
    ##
    def _onMouseWheel(self,ev:MouseEvent)->None:
        self.onMouseWheel.provoke(ev)
    
    ### Is called if the mouse pointer enters the GUI element.
    ##
    ##  @param ev                 A MouseEvent
    ##  @return                   None
    ##
    def _onMouseEnter(self,ev:MouseEvent)->None:
        self.onMouseEnter.provoke(ev)
    
    ### Is called if the mouse pointer leaves the GUI element.
    ##
    ##  @param ev                 A MouseEvent
    ##  @return                   None
    ##
    def _onMouseLeave(self,ev:MouseEvent)->None:
        self.onMouseLeave.provoke(ev)
    
    ### Is called if the mouse pointer is over the GUI element
    ##  and moved.
    ##
    ##  @param ev                 A MouseEvent
    ##  @return                   None
    ##
    def _onMouseMove(self,ev:MouseEvent)->None:
        self.onMouseMove.provoke(ev)
    
    ### Is called key got pressed.
    ##  It is necassry to call super().onKeyDown(ev)
    ##  at the end.
    ##
    ##  @param ev                 A KeyEvent.
    ##  @return                   None
    ##
    def _onKeyDown(self,ev:KeyEvent)->None:
        ##print("{} Widget::sdlOnKeyDown".format(self))
        self.onKeyDown.provoke(ev)
    
    ### Is called if a key got released.
    ##  It is necassry to call super().onKeyUp(ev)
    ##  at the end.
    ##
    ##  @param ev                 A KeyEvent.
    ##  @return                   None
    ##
    def _onKeyUp(self,ev:KeyEvent)->None:
        self.onKeyUp.provoke(ev)
    
    ### Is called if a key press ends in a entered character.
    ##  It is necassry to call super().onTextInput(ev)
    ##  at the end.
    ##
    ##  @param ev                 A KeyEvent.
    ##  @return                   None
    ##    
    def _onTextInput(self,ev:KeyEvent)->None:
        self.onTextInput.provoke(ev)

    ### Converts global coordinates to local coordinates
    ##
    ##  @param coordinate         A tuple with x and y coordinates.
    ##  @return                   A tuple.
    ##
    ##
    def toLocal(self, coordinates:tuple[int,int])->tuple[int,int]:
        result = ( coordinates[0]-self._x,coordinates[1]-self._y)
        
        if self._parent is not None:
            result = self._parent.toLocal(result)
        
        return result
    
    ### Converts local coordinates to the top window´s coordinates
    ##
    ##  @param coordinate         A Tuple with x and y coordinates.
    ##  @return                   A tuple. 
    ##
    def toGlobal(self,coordinates:tuple[int,int])->tuple[int,int]:
        result = ( self._x+coordinates[0],self._y+coordinates[1])
        
        if self._parent is not None:
            result = self._parent.toGlobal(result)
        
        return result
    
    ### Sets the focus the the widget.
    ##  @return                    None
    ##
    def focus(self):
        self.window.setFocus(self)
        
        