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

### Base class for all GUI elements.
##
##
class Widget():
    
    
    ###
    ##
    ##
    def __init__(self):
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::__init__():{}".format(self))
        #endif
        
        ## Stores the width of the GUI element.
        self._width:int = 100
        ##Stores the height of the GUI element.
        self._height:int = 40
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
          
        ###
        ##
        self.onTextInput:EventManager = EventManager()
        
        ###
        ##
        self.onKeyUp:EventManager = EventManager()
        
        ###
        ##
        self.onKeyDown:EventManager = EventManager()
        
        ###
        ##
        self.onMouseMove:EventManager = EventManager()
        
        ###
        ##
        self.onMouseLeave:EventManager = EventManager()
        
        ###
        ##
        self.onMouseEnter:EventManager = EventManager()
        
        ###
        ##
        self.onMouseWheel:EventManager = EventManager()
        
        ###
        ##
        self.onMouseUp:EventManager = EventManager()
        
        ###
        ##
        self.onMouseDown:EventManager = EventManager()
        
        ###
        ##
        self.onMouseClick:EventManager = EventManager()
        
        ###
        ##
        self.onBeforeRender:EventManager = EventManager()
        
        ###
        ##
        self.onAfterRender:EventManager = EventManager()
        
        ###
        ##
        self.onFocus:EventManager = EventManager()
        
        ###
        ##
        self.onFocusLost:EventManager = EventManager()
        
        ### Is provoked if a keyboard short cut occured.
        ##
        self.onShortcut:EventManager = EventManager()
        
        ###
        ##
        self.onResized:EventManager = EventManager()
        
        ### Is provoked when the widget got added to a parent
        ##  If a parent was added, this event is not provoked.
        ##
        self.onGotAdded:EventManager = EventManager()
        
        ### Is provoked when the widget got removed from a parent
        ##  If a parent was removed, this event is not provoked.
        ##
        self.onGotRemoved:EventManager = EventManager()

        ##
        self._resized:bool = False
        ##
        self.__borderColor:Color = None
        self.__backColor:Color = None
        
        self.onMouseDown.add(self.__hndMouseDown)
    FUNCTIONEND
    
    ###
    ##
    ##
    def __dir__(self):
        result = [
             "onTextInput",  "onKeyUp",      "onKeyDown",    "onMouseMove",
             "onMouseLeave", "onMouseEnter", "onMouseWheel", "onMouseUp",
             "onMouseDown",  "onMouseClick", "onBeforeDraw", "onAfterDraw",
             "onFocus",      "onFocusLost",  "onShortcut",   "onGotAdded",
             "onResized",    "onGotRemoved",
             
             "position",     "size",         "backColor",    "borderColor",
             "tooltip",      "name",         "x",            "y",
             "left",         "top",          "right",        "bottom",
             "width",        "minWidth",     "maxWidth",     "height",
             "minHeight",    "maxHeight",    "window",       "parent",
             "renderRect",   "isInvalide",   "alignment",
             
             "getChildAt",   "hasChildren",  "hasChild",     "toLocal",
             "toGlobal",     "focus",
              
             "_recordDirtyRect", "_invalidate", "_getDirtyRectangles",
             "_calculateLayout", "_getTexture", "_render",
             
            "_onBeforeRender", "_onAfterRender",  "_onGotAdded",   "_onGotRemoved",
            "_onMouseDown",  "_onMouseUp",    "_onMouseClick", "_onMouseWheel",
            "_onMouseEnter", "_onMouseLeave", "_onMouseMove",  "_onKeyDown",
            "_onKeyUp",      "_onTextInput",  "_onShortcut",   "_onResized",
            "_onFocus",      "_onFocusLost"
        ]
        result.sort()
        return result
    FUNCTIONEND
    
    ###
    ##
    ##
    def __delattr__(self, name):
        raise AttributeError(BIUI_ERR_DEL_ATTR_NOT_ALLOWED)
    FUNCTIONEND
    
    ###
    ##
    ##
    def debug(self,prefix=""):
        print("{}* {} ({})".format(prefix,self, self.name))
        for i in dir(self):
            print("{}  {} : {}".format( prefix,i, getattr(self,i,"") ))
    FUNCTIONEND
    
    ### Handels the mouse down event to set the focus on the current widget.
    ##
    ##
    def __hndMouseDown(self, ev):
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::__hndMouseDown():{}".format(self))
        #endif
        if self.window is None:
            return

        ## The event is going down and up the DOM
        ## We do not process at parents!
        if ev.eventSource != self:
            return 
        
        self.window.setFocus(self)
    FUNCTIONEND

    ### 
    ##
    ##   TODO: hinting return type
    def getChildAt(self, pos:tuple[int,int]):# pylint: disable=unused-argument
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::getChildAt():{}".format(self))
        #endif
        return self
    FUNCTIONEND

    ### Returns the x/y position of the GUI element.
    ##
    ##  @return            A tuple representing the position.
    ##
    @property
    def position(self)->tuple[int,int]:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::position_get():{}".format(self))
        #endif
        return (self._x, self._y)
    FUNCTIONEND

    ### Returns the width/height position of the GUI element.
    ##
    ##  @return            A tuple representing the size.
    ##
    @property
    def size(self)->tuple[int,int]:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::size_get():{}".format(self))
        #endif
        return (self.width, self.height)
    FUNCTIONEND

    ### 
    ##
    ##  @return            
    ##
    @property
    def backColor(self)->Color:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::backColor_get():{}".format(self))
        #endif
        return self.__backColor
    FUNCTIONEND

    ### Sets the backcolor for this widget.
    ##
    ##  @param value       
    ##  @return            None
    ##
    @backColor.setter
    def backColor(self, value:Color)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::backColor_set():{}".format(self))
        #endif
        if self.__backColor == value:
            return
        
        self.__backColor = value
        self._invalidate()
    FUNCTIONEND

    ### 
    ##
    ##  @return            
    ##
    @property
    def borderColor(self)->Color:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::brderColor_get():{}".format(self))
        #endif
        return self.__borderColor
    FUNCTIONEND

    ### Sets the borderColor for this widget.
    ##
    ##  @param value       
    ##  @return            None
    ##
    @borderColor.setter
    def borderColor(self, value:Color)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::borderColor_set():{}".format(self))
        #endif
        if self.__borderColor == value:
            return
        
        self.__borderColor = value
        self._invalidate()
    FUNCTIONEND

    ### 
    ##
    ##  @return            An integer value.
    ##
    @property
    def tooltip(self)->str:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::tooltip_get():{}".format(self))
        #endif
        return self._tooltip
    FUNCTIONEND

    ### Sets the tooltip text for this widget.
    ##
    ##  @param value       The text to show as tooltp
    ##  @return            None
    ##
    @tooltip.setter
    def tooltip(self, value:str)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::tooltip_set():{}".format(self))
        #endif
        self._tooltip = value
    FUNCTIONEND

    ### 
    ##
    ##  @return            An integer value.
    ##
    @property
    def name(self)->str:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::name_get():{}".format(self))
        #endif
        return self._name
    FUNCTIONEND

    ### Sets the x position of the GUI element.
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##
    @name.setter
    def name(self, value:str)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::name_set():{}".format(self))
        #endif
        self._name = value
    FUNCTIONEND

    ### Returns the x position of the GUI element.
    ##
    ##  @return            An integer value.
    ##
    @property
    def x(self)->int:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::x_get():{}".format(self))
        #endif
        return self._x
    FUNCTIONEND

    ### Sets the x position of the GUI element.
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##
    @x.setter
    def x(self, value:int)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::x_set():{}".format(self))
        #endif
        value = int(value)
        if value == self._x:
            return
        self._x = value
        self._invalidate()
    FUNCTIONEND

    ## Returns the y position of the GUI element.
    ##
    ##  @return            An integer value.
    ##
    @property
    def y(self)->int:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::y_get():{}".format(self))
        #endif
        return self._y
    FUNCTIONEND

    ### Sets the y position of the GUI element.
    ##
    ##  @param value       An integer value.
    ##  @return            None    
    ##
    @y.setter
    def y(self, value:int)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::y_set():{}".format(self))
        #endif
        value = int(value)
        if value == self._y:
            return
        self._y = value
        self._invalidate()
    FUNCTIONEND

    ### Set/Get the left border of the widget.
    ##  Is equqalent to x.
    ##
    ##  @return            An integer value.
    ##
    @property
    def left(self)->int:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::left_get():{}".format(self))
        #endif
        return self.x
    FUNCTIONEND

    ### Sets the left border.
    ##  Its the distance of the parent´sleft border to
    ##  the own left border.
    ##
    ##  @param value       An integer value.
    ##
    @left.setter
    def left(self,value:int)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::left_set():{}".format(self))
        #endif
        ##r = self.x+self.width
        ##self.x = value
        ##self.width = r-self.x
        r = self.x+self.width
        self.width = r-value
        self.x = value
    FUNCTIONEND

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
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::top_get():{}".format(self))
        #endif
        return self.y
    FUNCTIONEND

    ### Sets the top border.
    ##  Its the distance of the parents top 
    ##  border to the own top border.
    ##
    ##  @param value       An integer value.
    ##
    @top.setter
    def top(self,value:int)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::top_set():{}".format(self))
        #endif
        ##b = self.y+self.height
        ##self.y = value
        ##self.height = b-self.y
        b = self.y+self.height
        self.height = b-value
        self.y = value
    FUNCTIONEND
    
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
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::right_get():{}".format(self))
        #endif
        return self.x+self.width
    FUNCTIONEND

    ### Sets the right border of the widget.
    ##  It is the distance of the parent left border
    ##  to the own right border.
    ##
    ##  @param value       An integer value.
    ##
    @right.setter
    def right(self,value:int)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::right_set():{}".format(self))
        #endif
        self.width = value-self.x
    FUNCTIONEND

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
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::bottom_get():{}".format(self))
        #endif
        return self.y+self.height
    FUNCTIONEND

    ### Sets the bottom border of the widget.
    ##  Its value is the distance of the top
    ##  border of the parent widget to the own bottom
    ##  border-
    ##
    ##  @param value       An integer value.
    ##
    @bottom.setter
    def bottom(self,value:int)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::bottom_set():{}".format(self))
        #endif
        self.height = value-self.y
    FUNCTIONEND

    ### Return the width of the GUI element.
    ##
    ##  @return            An integer value.
    ##
    @property
    def width(self)->int:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::width_get():{}".format(self))
        #endif
        return self._width
    FUNCTIONEND

    ### Sets the width of the GUI element.
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##
    @width.setter     
    def width(self, value:int)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::width_set():{}".format(self))
        #endif
        value = int(value)
        
        if value == self._width:
            return
        
        if self._alignment != Alignment.FILL:
            value = min(value, self._maxWidth)
            value = max(value, self._minWidth)
        
        ##self._invalidate()
        self._width = max(0,value)
        self._invalidate()
        ##self._onResized(Event(self))
        self._resized = True
    FUNCTIONEND

    ### Returns the min widt value of the widget.
    ##
    ##  @return            An integer value.
    ##
    @property
    def minWidth(self)->int:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::minWidth_get():{}".format(self))
        #endif
        return self._minWidth
    FUNCTIONEND

    ### Sets the min width value of the widget.
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##    
    @minWidth.setter   
    def minWidth(self, value:int)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::minWidth_set():{}".format(self))
        #endif
        value = int(value)
        self._minWidth = max(0,value)
        if self._minWidth > self._width:
            self.width = self._minWidth
    FUNCTIONEND

    ### Returns the max width value of the widget.
    ##
    ##  @return            An integer value.
    ##
    @property
    def maxWidth(self)->int:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::maxWidth_get():{}".format(self))
        #endif
        return self._maxWidth
    FUNCTIONEND

    ### Sets the max width value of the widget.
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##    
    @maxWidth.setter   
    def maxWidth(self, value:int)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::maxWidth_set():{}".format(self))
        #endif
        value = int(value)
        self._maxWidth = max(0,value)
        if self._maxWidth < self._width:
            self.width = self._maxWidth
    FUNCTIONEND

    ## Returns the y position of the GUI element.
    ##
    ##  @return            An integer value.
    ##
    @property
    def height(self)->int:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::height_get():{}".format(self))
        #endif
        return self._height
    FUNCTIONEND

    ### Sets the height of the GUI element.
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##
    @height.setter
    def height(self, value:int)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::height_set():{}".format(self))
        #endif
        value = int(value)
        
        if value == self._height:
            return
        
        if self._alignment != Alignment.FILL:
            value = min(value, self._maxWidth)
            value = max(value, self._minWidth)
            
        self._height = max(1,value)
        ##self._onResized(Event(self))
        self._invalidate()
        self._resized = True
    FUNCTIONEND

    ### Returns the min width of the widget.
    ##
    ##  @return            An integer value.
    ##
    @property
    def minHeight(self)->int:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::minHeight_get():{}".format(self))
        #endif
        return self._minHeight
    FUNCTIONEND

    ### Sets the min width of the widget.
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##    
    @minHeight.setter   
    def minHeight(self, value:int)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::minHeight_set():{}".format(self))
        #endif
        value = int(value)
        self._minHeight = max(0,value)
        if self._minHeight > self._height:
            self.height = self._minHeight
    FUNCTIONEND

    ### Returns the max. height of the widget.
    ##
    ##  @return            An integer value.
    ##
    @property
    def maxHeight(self)->int:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::maxHeight_get():{}".format(self))
        #endif
        return self._maxHeight
    FUNCTIONEND

    ### Sets the max. height of the widget.
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##    
    @maxHeight.setter   
    def maxHeight(self, value:int)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::maxHeight_set():{}".format(self))
        #endif
        value = int(value)
        self._maxHeight = max(0,value)
        if self._maxHeight < self._height:
            self.height = self._maxHeight
    FUNCTIONEND

    ###
    ##
    ##
    @property
    def hasChildren(self):
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::hasChildren():{}".format(self))
        #endif
        return False
    FUNCTIONEND

    ### Checks if the given child is a child object or
    ##  if it is the current widget.
    ##
    ## todo: hinting
    def hasChild(self,child)->bool:
        #ifdef SHOW_FUNCTIONNAMES
        ##print("Widget::hasChild():{}".format(self))
        #endif
        return child == self
    FUNCTIONEND

    ### Returns the alignment setting.
    ##
    ##
    @property
    def alignment(self)->int:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::alignment():{}".format(self))
        #endif
        return self._alignment
    FUNCTIONEND

    ### Serts the alignment setting.
    ##
    ##
    @alignment.setter
    def alignment(self,value:int)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::alignment():{}".format(self))
        #endif
        self._alignment = value
    FUNCTIONEND

    ### Records the current Rect of the GUI element
    ##  in the parent´s coordinate system.
    ##
    ##  @return            None
    ##
    def _recordDirtyRect(self,box:tuple[int,int,int,int])->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::_recordDirtyRect():{}".format(self))
        #endif
        
        if self.parent is None:
            return
        
        if self.window is None:
            return

        self.parent._recordDirtyRect(box)
    FUNCTIONEND

    ### Checks if the widget is invalide.
    ##  If it is invalide, it has to be redrawn
    ##  at the next refresh.
    ##
    ##
    def isInvalide(self)->bool:
        #ifdef SHOW_FUNCTIONNAMES
        ##print("Widget::isInvalide():{}".format(self))
        #endif
        return self._isInvalide
    FUNCTIONEND

    ### Does some enecassary work if the GUI element
    ##  became invalide. For example after changing its size.
    ##
    ##  @return            None
    ##
    def _invalidate(self)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::invalidate():{}".format(self))
        #endif
        
        ## set flag to recalculate the layout.
        ## set flag to redraw widget
        self._isInvalide = True
    FUNCTIONEND

    ### Returns all dirty rects of the GUI element
    ##  since the last call. Calling this funtion clears
    ##  all recorded rects.
    ##
    ##  @return            A list with tuples.
    ##    
    ## OBSOLET
    def _getDirtyRectangles(self)->list[tuple[int,int,int,int]]:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::_getDirtyRectangles():{}".format(self))
        #endif
        result = self._dirtyRects.copy()
        self._dirtyRects.clear()
        return result
    FUNCTIONEND

    ### Returns the parent window of the widget.
    ##
    ## todo: hinting
    @property
    def window(self):#pylint: disable=inconsistent-return-statements
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::window_get():{}".format(self))
        #endif
        ##TODO: Any thowbacks from including here?
        from biui.Widgets import Window
        parent = self.parent
        while True:
            if isinstance(parent,Window):#pylint: disable=no-else-return
                return parent
            elif parent == None:
                return
            parent = parent.parent 
    FUNCTIONEND

    ### Returns the parent GUI element of the GUI element.
    ##  Normally it is the main window or a container element
    ##  that contains the GUI element.
    ##
    ##  @return            A Widget instance.
    ##  todo: hinting
    @property
    def parent(self):
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::parent_get():{}".format(self))
        #endif
        return self._parent
    FUNCTIONEND

    ### Sets the parent GUI element.
    ##
    ##  @param parent      A Window or ContainerWidget
    ##
    ##  @return            None
    ##  todo: hinting
    @parent.setter
    def parent(self,parent)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::parent_set():{}".format(self))
        #endif
        if self._parent is not None:
            self._parent.removeChild(self)
        
        self._parent = parent
    FUNCTIONEND

    ### Returns the drawing texture of the GUI element.
    ##  This is for internal use. Just use the texture
    ##  if you know what you are doing.
    ##
    ##  @return            The drawing texture
    ##  todo: hinting
    def _getTexture(self):
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::_getTexture():{}".format(self))
        #endif
        return self._parent._getTexture()
    FUNCTIONEND

    ### Recalculates the layout of the widget.
    ##
    ##
    def _calculateLayout(self)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::_calculateLayout():{}".format(self))
        #endif
        
        if self._isInvalide:
            self.recordDirtyRect()
    FUNCTIONEND

    ### Records the dirty recangle
    ##
    ##
    def recordDirtyRect(self):
        box = self.position+self.size
        self._recordDirtyRect(box)
    FUNCTIONEND
    
    ### Returns the region of the texture to be rendered on screen.
    ##  The texture is returned by _render().
    ##
    @property
    def renderRect(self):
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::renderRect_get():{}".format(self))
        #endif
        return (0,0,self._width,self._height)
    FUNCTIONEND
    
    ###
    ##
    ##
    def _main(self):
        if self._resized:
            self._onResized(Event(self))
            self._resized = False
    FUNCTIONEND
        
    ### Redraws the GUI element. This is for internal use.
    ##  Just use this function if you know what you are doing.
    ##  Do not call super()._render().
    ##  Copy the guard to your _render()-version
    ##  and set _isInvalide to False at the end!
    ##  If you derive from a widget and call super(),
    ##  The parent would overdraw your widget.
    ##  @param surface            The drawing surface.
    ##
    ##  @return            None
    ##  todo: hinting
    def _render(self, forceRedraw:bool=False):
        #ifdef SHOW_FUNCTIONNAMES
        ##print("Widget::_render():{}".format(self))
        #endif
        
        if not self.isInvalide():
            if not forceRedraw:
                return None
                
        PYSDL2_CREATETEXTURE(self.window.renderer,self.width,self.height,texture)
        
        self._themeBackgroundfunction(self,texture)
        
        self._isInvalide = False
        
        return texture
    FUNCTIONEND

    ### Converts global coordinates to local coordinates
    ##
    ##  @param coordinate         A tuple with x and y coordinates.
    ##  @return                   A tuple.
    ##
    ##
    def toLocal(self, coordinates:tuple[int,int])->tuple[int,int]:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::toLocal():{}".format(self))
        #endif
        result = ( coordinates[0]-self._x,coordinates[1]-self._y)
        
        if self._parent is not None:
            result = self._parent.toLocal(result)
        
        return result
    FUNCTIONEND

    ### Converts local coordinates to the top window´s coordinates
    ##
    ##  @param coordinate         A Tuple with x and y coordinates.
    ##  @return                   A tuple. 
    ##
    def toGlobal(self,coordinates:tuple[int,int])->tuple[int,int]:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::toGlobal():{}".format(self))
        #endif
        result = ( self._x+coordinates[0],self._y+coordinates[1])
        
        if self._parent is not None:
            result = self._parent.toGlobal(result)
        
        return result
    FUNCTIONEND

    ### Sets the focus the the widget.
    ##  @return                    None
    ##
    def focus(self):
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::focus():{}".format(self))
        #endif
        self.window.setFocus(self)
    FUNCTIONEND

    ### Is called before the drawing procedure ist starting
    ##  to calculate the layout and before _redraw is called.
    ##
    def _onBeforeRender(self)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::_onBeforeRender():{}".format(self))
        #endif
        ##self._onBeforeRender(Event(self))
        self.onBeforeRender.provoke(Event(self))
    FUNCTIONEND

    ### Is called after all redwaing is done.
    ##
    ##
    def _onAfterRender(self)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::_onAfterRender():{}".format(self))
        #endif
        ##self._onAfterDraw(Event(self))
        self.onAfterRender.provoke(Event(self))
    FUNCTIONEND

    ### Is called when the widget got added to a parent.
    ##
    def _onGotAdded(self)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::_onGotAdded():{}".format(self))
        #endif
        ##self._onGotAdded(Event(self))
        self.onGotAdded.provoke(Event(self))
    FUNCTIONEND

    ### Is called when the widget got removed from a parent.
    ##
    ##
    def _onGotRemoved(self)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::_onGotRemoved():{}".format(self))
        #endif
        ##self._onGotRemoved(Event(self))
        self.onGotRemoved.provoke(Event(self))
    FUNCTIONEND

    ### Is called if a mouse button got pressed and the
    ##  mouse pointer is over the GUI element.
    ##
    ##  @param ev                 A MouseEvent
    ##  @return            None
    ##
    def _onMouseDown(self,ev:MouseEvent)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::_onMouseDown():{}".format(self))
        #endif
        self.onMouseDown.provoke(ev)
    FUNCTIONEND

    ### Is called if a mouse button got released and the
    ##  mouse pointer is over the GUI element.
    ##
    ##  @param ev                 A MouseEvent
    ##  @return                   None
    ##
    def _onMouseUp(self,ev:MouseEvent)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::_onMouseUp():{}".format(self))
        #endif
        self.onMouseUp.provoke(ev)
    FUNCTIONEND

    ### Is called if a mouse had a click release and the
    ##  mouse pointer is over the GUI element.
    ##
    ##  @param ev                 A MouseEvent
    ##  @return                   None
    ##
    def _onMouseClick(self,ev:MouseEvent)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::_onMouseClick():{}".format(self))
        #endif
        self.onMouseClick.provoke(ev)
    FUNCTIONEND

    ### Is called if a mouse wheel got turned and the
    ##  mouse pointer is over the GUI element.
    ##  @param ev   MouseEvent.MouseEvent
    ##
    ##  @param ev                 A MouseEvent
    ##  @return                   None
    ##
    def _onMouseWheel(self,ev:MouseEvent)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::_onMouseWheel():{}".format(self))
        #endif
        self.onMouseWheel.provoke(ev)
    FUNCTIONEND

    ### Is called if the mouse pointer enters the GUI element.
    ##
    ##  @param ev                 A MouseEvent
    ##  @return                   None
    ##
    def _onMouseEnter(self,ev:MouseEvent)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::_onMouseEnter():{}".format(self))
        #endif
        self.onMouseEnter.provoke(ev)
    FUNCTIONEND

    ### Is called if the mouse pointer leaves the GUI element.
    ##
    ##  @param ev                 A MouseEvent
    ##  @return                   None
    ##
    def _onMouseLeave(self,ev:MouseEvent)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::_onMouseLeave():{}".format(self))
        #endif
        self.onMouseLeave.provoke(ev)
    FUNCTIONEND

    ### Is called if the mouse pointer is over the GUI element
    ##  and moved.
    ##
    ##  @param ev                 A MouseEvent
    ##  @return                   None
    ##
    def _onMouseMove(self,ev:MouseEvent)->None:
        #ifdef SHOW_FUNCTIONNAMES
        ##print("Widget::_onMouseMove():{}".format(self))
        #endif
        self.onMouseMove.provoke(ev)
    FUNCTIONEND

    ### Is called key got pressed.
    ##  It is necassry to call super().onKeyDown(ev)
    ##  at the end.
    ##
    ##  @param ev                 A KeyEvent.
    ##  @return                   None
    ##
    def _onKeyDown(self,ev:KeyEvent)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::_onKeyDown():{}".format(self))
        #endif
        ##print("{} Widget::sdlOnKeyDown".format(self))
        self.onKeyDown.provoke(ev)
    FUNCTIONEND

    ### Is called if a key got released.
    ##  It is necassry to call super().onKeyUp(ev)
    ##  at the end.
    ##
    ##  @param ev                 A KeyEvent.
    ##  @return                   None
    ##
    def _onKeyUp(self,ev:KeyEvent)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::_onKeyUp():{}".format(self))
        #endif
        self.onKeyUp.provoke(ev)
    FUNCTIONEND

    ### Is called if a key press ends in a entered character.
    ##  It is necassry to call super().onTextInput(ev)
    ##  at the end.
    ##
    ##  @param ev                 A KeyEvent.
    ##  @return                   None
    ##    
    def _onTextInput(self,ev:KeyEvent)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::_onTextInput():{}".format(self))
        #endif
        self.onTextInput.provoke(ev)
    FUNCTIONEND

    ### 
    ##
    ##
    def _onShortcut(self,ev:Event)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::_onShortcut():{}".format(self))
        #endif
        ##print("Widget::_onShortcut ({})".format(self.name))
        self.onShortcut.provoke(ev)
    FUNCTIONEND

    ### 
    ##
    ##
    def _onResized(self,ev:Event)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::_onResized():{}".format(self))
        #endif
        self.onResized.provoke(ev)
    FUNCTIONEND

    def _onFocus(self,ev:Event)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::_onFocus():{}".format(self))
        #endif
        self.onFocus.provoke(ev)          
    FUNCTIONEND

    def _onFocusLost(self,ev:Event)->None:
        #ifdef SHOW_FUNCTIONNAMES
        print("Widget::_onFocusLost():{}".format(self))
        #endif
        self.onFocusLost.provoke(ev)         
    FUNCTIONEND
        
        
        
        
        
        