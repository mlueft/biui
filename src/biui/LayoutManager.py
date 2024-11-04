#include "biui.inc"

##import biui
from biui.Events import EventManager
from biui.Events import Event
from biui.Enum import Alignment


### Manages a virtual grid of cells containing children. 
##  Each child has to be a biui.Widget.
##
class LayoutManager():
    
    def __init__(self,x=0,y=0):
        self._debug = False
        ##        
        self._children = [[[]]]
        ##
        self._columnWidths = [0]
        ##
        self._rowHeights = [0]
        ## Files when a child is added
        self.onChildAdded = EventManager()
        ## Fires when a child is removed
        self.onChildRemoved = EventManager()
        
        self._resizeChildList(x+1,y+1)
    FUNCTIONEND
    
    ### Just adds columns or Rows at the end
    ##
    ##  @param width
    ##  @param height
    ##
    def _resizeChildList(self,width,height):
        if False:
            if width == 0:
                width = len(self._children)
                
            if height == 0:
                height = max(_max,len(self._children[0]))
        
        width = max(width,len(self._children))
        height = max(height,len(self._children[0]))
        
        for i in range(width):
        
            ## add column
            if i >= len(self._children):
                self._children.append([])
                
            row = self._children[i]
                
            for j in range(height):
                if j >= len(row):
                    row.append([])
        
        ## columnWidths
        for i in range(len(self._columnWidths),len(self._children)):
            self._columnWidths.append(0)
            
        ## rowHeights
        for i in range(len(self._rowHeights),len(self._children[0])):
            self._rowHeights.append(0)        
    FUNCTIONEND
        
    ### Adds a child element to the Layout.
    ##
    ##  @param child         A Widget instance.
    ##  @param x             Column for the child. 
    ##  @param y             Row for the child.    
    ##       
    def addChild(self, child,x,y):
        self._resizeChildList(x+1,y+1)
        self._width = len(self._children)
        self._height = len(self._children[0])
        self._children[x][y].append(child)
        self.onChildAdded.provoke(Event(child))
    FUNCTIONEND
     
    ### Removes the given child element.
    ##
    ##  @param child         A Widget instance.
    ##   
    def removeChild(self,child):
        for i,column in enumerate(self._children):
            for j,row in enumerate(column):
                if child in self._children[i][j]:
                    self._children[i][j].remove(child)
                    self.onChildRemoved.provoke(Event(child))
    FUNCTIONEND
    
    ### Set/Get all column widths.
    ##
    ##  @return      A List with the column widths.
    ##
    @property
    def columnWidths(self):
        return self._columnWidths
    FUNCTIONEND
        
    ### Sets the column widths.
    ##
    ##  @param values    A list with column. 
    ##                   Integer values are are absolut values.
    ##                   Float values are procentual values. 
    ##
    @columnWidths.setter
    def columnWidths(self,values):
        self._resizeChildList(len(values),0)
        self._columnWidths.clear()
        for i in range(max(len(self._children),len(values))):
            if i < len(values):
                self._columnWidths.append(values[i])
            else:
                self._columnWidths.append(0)
    FUNCTIONEND
    
    ### Set/Get all row heights.
    ##
    ##  @return      A List with the row heights.
    ##
    @property
    def rowHeights(self):
        return self._rowHeights
    FUNCTIONEND
    
    ### Sets the row heights.
    ##
    ##  @param values    A list row heights. 
    ##                   Integer values are are absolut values.
    ##                   Float values are procentual values. 
    ##
    @rowHeights.setter
    def rowHeights(self,values):
        self._resizeChildList(0,len(values))
        self._rowHeights.clear()
        for i in range(max(len(self._children[0]),len(values))):
            if i < len(values):
                self._rowHeights.append(values[i])
            else:
                self._rowHeights.append(0)
    FUNCTIONEND
    
    ### Sets the width of the given column.
    ##
    ##  @param column   The index of the column.
    ##  @param value    The width of the column.
    ##
    def setColumnWidth(self,column,value):
        self._resizeChildList(column,0)
        for i in range(len(self._columnWidths),column+1):
            self._columnWidths.append(0.0)
            
        self._columnWidths[column] = value
    FUNCTIONEND
            
    ### Sets the height of the given row.
    ##
    ##  @param row      The index of the row.
    ##  @param values   The height of the row
    ##
    def setRowHeight(self,row,values):
        self._resizeChildList(0,row)
        for i in range(len(self._rowHeights),row+1):
            self._rowHeights.append(0.0)
                    
        self._rowHeights[row] = value
    FUNCTIONEND
    
    ### Returns the (column,row) of the given child.
    ##
    ##  @param child      A wifget instance.
    ##
    def getPositionOfChild(self,child):
        for i,column in enumerate(self._children):
            for j,row in enumerate(column):
                for c in row:
                    if c==child:
                        return (i,j)
        return None
    FUNCTIONEND
    
    ### Adds a column at the given position.
    ##  Columns are moved to right.
    ##
    ##  @param index    The index of the column after that the column is inserted.
    ##  @param width    The width of the inserted column.
    ##
    def insertColumnAt(self,index,width = 0):
        self._children.insert(index,[])
        self._columnWidths.insert(index,width)
        
        for i in self._rowHeights:
            self._children[index].append([])
    FUNCTIONEND
    
    ### Adds a Row at the given position.
    ##  Rows are moved down.
    ##
    ##  @param index   The indexof the row after that the row is inserted.
    ##  @param height  The height of the inserted row.
    ##
    def insertRowAt(self,index,height=0):

        for i,child in enumerate(self._children):
            self._children[i].insert(index,[])
            
        self._rowHeights.insert(index,height)
    FUNCTIONEND
        
    ### Returns the width value of the given column.
    ##
    ##  @param index     The index of the column.
    ##
    def getColumnWidth(self,index):
        return self._columnWidths[index]
    FUNCTIONEND
    
    def debug(self,prefix=""):
        print( "{}Layoutmanager".format(prefix) )
        print( "{}    columns : {}".format(prefix,self._columnWidths) )
        print( "{}    rows    : {}".format(prefix,self.rowHeights) )
        print( "{}    children: {}".format(prefix,self._children) )
    FUNCTIONEND
        
    ### Calculates the absolute values of cols
    ##  in relation to size.
    ##  TODO: A column width of 0 on purpose is not possible.
    ##        It will be interpretes as a filler.
    ##  TODO: If abolute values are in sum bigger than size
    ##        filler will be negative. :-(
    ##        Could turn into a problem!?
    ##
    ##  @param cols        A list with widths definition.
    ##                     floats - percent values
    ##                     int    - absolut values
    ##                     0      - fill the rest
    ##  @param size        The complete size
    ##  @return            An array with absolute values.
    ##
    def __calculatePixelWidths(self, cols, size):
        
        result = []
        qty0 = 0
        for width in cols:
            if width == 0:
                cellWidth = 0
                qty0=qty0+1
            elif type(width) == float:
                cellWidth = size*width/100
            else:
                cellWidth = width
            result.append(cellWidth)
            
        spaceLeft = size
        for i in result:
            spaceLeft = spaceLeft - i
            
        for i,w in enumerate(result):
            if w == 0:
                result[i] = spaceLeft/qty0
    
        return result
    FUNCTIONEND
    
    ###  Calculate size and position of all children
    ##   in the grid defines by children, widths and heights
    ##   of Columns and rows.
    ##
    ##   @param            The parent´s size.
    ##
    def _calculateLayout(self, size):
        size = [0,0,size[0],size[1]]
        ## Calculate docked children
        ## and apat size for cell calculation
        for i,tmp in enumerate(self._columnWidths):
            for j,tmp in enumerate(self._rowHeights):
                ##print(i,j)
                ##print(self._children[i])
                ##print(self._children[i][j])
                for child in self._children[i][j]:
                    alignment = child.alignment
                    if alignment == Alignment.DOCK_TOP:
                        child.x = size[0]
                        child.y = size[1]
                        child.width = size[2]
                        size[1] += child.height 
                        size[3] -= child.height
                    elif alignment == Alignment.DOCK_LEFT:
                        child.x = size[0]
                        child.y = size[1]
                        child.height = size[3]
                        size[0] += child.width
                        size[2] -= child.width
                    elif alignment == Alignment.DOCK_BOTTOM:
                        child.x = size[0]
                        child.y = size[1]+size[3]-child.height
                        child.width = size[2]
                        size[3] -= child.height
                    elif alignment == Alignment.DOCK_RIGHT:
                        child.x = size[0]+size[2]-child.width
                        child.y = size[1]
                        child.height = size[3]
                        size[2]-= child.width

        widths  = self.__calculatePixelWidths(self._columnWidths,size[2])
        heights = self.__calculatePixelWidths(self._rowHeights,size[3])
        cellX = size[0]
        for i,cellWidth in enumerate(widths):
            cellY = size[1]
            for j,cellHeight in enumerate(heights):
                for child in self._children[i][j]:
                    if child != None:
                        alignment = child.alignment
                        if alignment == Alignment.ABSOLUTE:
                            pass
                            ## TODO: How to we get the child
                            ##       to the new origin of size?
                        
                        elif alignment == Alignment.FILL:
                            child.x = cellX
                            child.y = cellY
                            child.width = cellWidth
                            child.height = cellHeight
                            if self._debug:
                                print("set child:{} {}x{} {}x{}".format(child.name,cellX,cellY,cellWidth,cellHeight) )
                        ## exclude dockings
                        elif alignment not in (11,12,13,14):
                            
                            childX = 0
                            childY = 0
                            
                            ##
                            ## Y
                            ##
                            
                            ## TOP
                            ##if    alignment == Alignment.TOP_LEFT   \
                            ##   or alignment == Alignment.TOP_CENTER \
                            ##   or alignment == Alignment.TOP_RIGHT:
                            ##    childY = 0
                               
                             
                            ## CENTER
                            ##if    alignment == Alignment.CENTER_LEFT   \
                            ##   or alignment == Alignment.CENTER_CENTER \
                            ##   or alignment == Alignment.CENTER_RIGHT:
                            if alignment in [5,6,7]:
                                childY = cellHeight/2-child.height/2
                            
                            
                            ## BOTTOM
                            ##elif    alignment == Alignment.BOTTOM_LEFT \
                            ##   or alignment == Alignment.BOTTOM_CENTER \
                            ##   or alignment == Alignment.BOTTOM_RIGHT:
                            elif alignment in [8,9,10]:
                                childY = cellHeight-child.height
                                
                            
                            ##
                            ## X
                            ##  
                              
                            ## LEFT
                            ##if    alignment == Alignment.TOP_LEFT    \
                            ##   or alignment == Alignment.CENTER_LEFT \
                            ##   or alignment == Alignment.BOTTOM_LEFT:
                            ##    pass
                            
                            ## CENTER
                            ##if    alignment == Alignment.TOP_CENTER    \
                            ##   or alignment == Alignment.CENTER_CENTER \
                            ##   or alignment == Alignment.BOTTOM_CENTER:
                            if alignment in [3,6,9]:
                                childX = cellWidth/2-child.width/2
                            
                            ## RIGHT
                            ##elif    alignment == Alignment.TOP_RIGHT  \
                            ##   or alignment == Alignment.CENTER_RIGHT \
                            ##   or alignment == Alignment.BOTTOM_RIGHT:
                            elif alignment in [4,7,10]:
                                childX = cellWidth-child.width
                            
                            child.x = cellX+childX
                            child.y = cellY+childY
                            ##child.setWidth(cellWidth)
                            ##child.setHeight(cellHeight)
                            
                cellY = cellY + cellHeight
            cellX = cellX + cellWidth
    FUNCTIONEND
    
    