import biui

## Manages a virtual grid of cells containing children. 
#  Each child has to be a biui.Widget.
#
class LayoutManager():
    
    def __init__(self,width=1,height=1):
        #        
        self._children = [[[]]]
        #
        self._columnWidths = [0]
        #
        self._rowHeights = [0]
        #
        self.onChildAdded = biui.EventManager()
        #
        self.onChildRemoved = biui.EventManager()
        
        self._resizeChildList(width,height)
        
    ## Just adds columns or Rows at the end
    #
    #
    def _resizeChildList(self,width,height):
        if width == 0:
            width = len(self._children)
            
        if height == 0:
            _max = 0
            for i in self._children:
                _max = max(_max,len(i))
            height = _max
             
        for i in range(width):
        
            # add column    
            if i >= len(self._children):
                self._children.append([])
                
            row = self._children[i]
                
            for j in range(height):
                if j >= len(row):
                    row.append([])
        
        # columnWidths
        for i in range(len(self._columnWidths),len(self._children)):
            self._columnWidths.append(0)
            
        # rowHeights
        for i in range(len(self._rowHeights),len(self._children[0])):
            self._rowHeights.append(0)        
        
    ## Adds a child element to the Layout.
    #
    #  @param child         A Widget instance.
    #  @param x             Column for the child. 
    #  @param y             Row for the child.    
    #       
    def addChild(self, child,x,y):
        self._resizeChildList(x+1,y+1)
        self._width = len(self._children)
        self._height = len(self._children[0])
        self._children[x][y].append(child)
        self.onChildAdded.provoke(biui.Event(self))
     
    ## Removes the given child element.
    #
    #  @param child         A Widget instance.
    #   
    def removeChild(self,child):
        for i,column in enumerate(self._children):
            for j,row in enumerate(column):
                if child in self._children[i][j]:
                    self._children[i][j].remove(child)
        self.onChildRemoved.provoke(biui.Event(self))
    
    ##
    #
    #
    @property
    def columnWidths(self):
        return self._columnWidths
        
    ##
    #
    #
    @columnWidths.setter
    def columnWidths(self,values):
        self._resizeChildList(len(values),0)
        self._columnWidths.clear()
        for i in range(max(len(self._children),len(values))):
            if i < len(values):
                self._columnWidths.append(values[i])
            else:
                self._columnWidths.append(0)
    
    ##
    #
    #
    @property
    def rowHeights(self):
        return self._rowHeights
    
    ##
    #
    #
    @rowHeights.setter
    def rowHeights(self,values):
        self._resizeChildList(0,len(values))
        self._rowHeights.clear()
        for i in range(max(len(self._children[0]),len(values))):
            if i < len(values):
                self._rowHeights.append(values[i])
            else:
                self._rowHeights.append(0)
    
    ##
    #
    #
    def setColumnWidth(self,column,value):
        self._resizeChildList(column,0)
        for i in range(len(self._columnWidths),column+1):
            self._columnWidths.append(0.0)
            
        self._columnWidths[column] = value
            
    ##
    #
    #
    def setRowHeight(self,row,values):
        self._resizeChildList(0,row)
        for i in range(len(self._rowHeights),row+1):
            self._rowHeights.append(0.0)
                    
        self._rowHeights[row] = value
    

    
    ##
    #
    #
    def getPositionOfChild(self,child):
        for i,column in enumerate(self._children):
            for j,row in enumerate(column):
                for c in row:
                    if c==child:
                        return (i,j)
        return None
    
    ##
    #
    #
    def insertColumnAt(self,index,width = 0):
        self._children.insert(index,[])
        self._columnWidths.insert(index,width)
        
        for i in self._rowHeights:
            self._children[index].append([])

    ##
    #
    #
    def insertRowAt(self,index,height=0):

        for i,child in enumerate(self._children):
            self._children[i].insert(index,[])
            
        self._rowHeights.insert(index,height)
        
    ##
    #
    #
    def getColumnWidth(self,index):
        return self._columnWidths[index]
    
    ## Calculates the absolute values of cols
    #  in relation to size.
    #  TODO: A column width of 0 on purpose isn't possible.
    #        It will be interpretes as a filler.
    #  TODO: If abolute values are in sum bigger than size
    #        filler will be negative. :-(
    #        Could turn into a problem!?
    #
    #  @param cols        A list with widths definition.
    #                     floats - percent values
    #                     int    - absolut values
    #                     0      - fill the rest
    #  @param size        The complete size
    #  @return            An array with absolute values.
    #
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
    
    ##  Calculate size and position of all children
    #   in the grid defines by children, widths and heights
    #   of Columns and rows.
    #
    #   @param            The parent's size.
    #
    def _calculateLayout(self, size):
        widths  = self.__calculatePixelWidths(self._columnWidths,size[0])
        heights = self.__calculatePixelWidths(self._rowHeights,size[1])
        cellX = 0
        for i,cellWidth in enumerate(widths):
            cellY = 0
            for j,cellHeight in enumerate(heights):
                for child in self._children[i][j]:
                    if child != None:
                        alignment = child.alignment
                        if alignment == biui.Alignment.ABSOLUTE:
                            pass
                        
                        elif alignment == biui.Alignment.FILL:
                            child.x = cellX
                            child.y = cellY
                            child.width = cellWidth
                            child.height = cellHeight
                        else:
                            
                            childX = 0
                            childY = 0
                            
                            #
                            # Y
                            #
                            
                            # TOP
                            #if    alignment == biui.Alignment.TOP_LEFT   \
                            #   or alignment == biui.Alignment.TOP_CENTER \
                            #   or alignment == biui.Alignment.TOP_RIGHT:
                            #    childY = 0
                               
                             
                            # CENTER
                            #if    alignment == biui.Alignment.CENTER_LEFT   \
                            #   or alignment == biui.Alignment.CENTER_CENTER \
                            #   or alignment == biui.Alignment.CENTER_RIGHT:
                            if alignment in [5,6,7]:
                                childY = cellHeight/2-child.height/2
                            
                            
                            # BOTTOM
                            #elif    alignment == biui.Alignment.BOTTOM_LEFT \
                            #   or alignment == biui.Alignment.BOTTOM_CENTER \
                            #   or alignment == biui.Alignment.BOTTOM_RIGHT:
                            elif alignment in [8,9,10]:
                                childY = cellHeight-child.height
                                
                            
                            #
                            # X
                            #  
                              
                            # LEFT
                            #if    alignment == biui.Alignment.TOP_LEFT    \
                            #   or alignment == biui.Alignment.CENTER_LEFT \
                            #   or alignment == biui.Alignment.BOTTOM_LEFT:
                            #    pass
                            
                            # CENTER
                            #if    alignment == biui.Alignment.TOP_CENTER    \
                            #   or alignment == biui.Alignment.CENTER_CENTER \
                            #   or alignment == biui.Alignment.BOTTOM_CENTER:
                            if alignment in [3,6,9]:
                                childX = cellWidth/2-child.width/2
                            
                            # RIGHT
                            #elif    alignment == biui.Alignment.TOP_RIGHT  \
                            #   or alignment == biui.Alignment.CENTER_RIGHT \
                            #   or alignment == biui.Alignment.BOTTOM_RIGHT:
                            elif alignment in [4,7,10]:
                                childX = cellWidth-child.width
                            
                            child.x = cellX+childX
                            child.y = cellY+childY
                            #child.setWidth(cellWidth)
                            #child.setHeight(cellHeight)
                            
                cellY = cellY + cellHeight
            cellX = cellX + cellWidth
    