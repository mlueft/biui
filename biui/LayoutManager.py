import biui

##
#
#
class LayoutManager():
    
    def __init__(self,width=1,height=1):
        # Stores the width of the GUI element.
        self._width = width
        #Stores the height of the GUI element.
        self._height = height
        #        
        self._children = [[]]
        #
        self.onChildAdded = biui.EventManager()
        #
        self.onChildRemoved = biui.EventManager()
        #
        self._columnWidths = []
        #
        self._rowHeights = []
        
        self._resizeChildList( width,height)
        
    ##
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
             
        for i in range(max(width,self._width)):
            
            if i >= len(self._children):
                self._children.append([])
                
            tmp = self._children[i]
                
            for j in range(max(height,self._height)):
                if j >= len(tmp):
                    tmp.append(None)
        
    ## 
    #
    #  @param value       An integer value.
    #  @return            None
    #       
    def setWidth(self, value):
        self._width = max(1,value)
    
    ## 
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
    def setHeight(self, value):
        self._height = max(1,value)
        
    # 
    #
    #  @return            An integer value.
    #
    def getHeight(self):
        return self._height
                
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
        self._children[x][y] = child
        self.onChildAdded.provoke(biui.Event(self))
     
    ## Removes the given child element.
    #
    #  @param child         A Widget instance.
    #   
    def removeChild(self,child):
        for i,column in enumerate(self._children):
            self._children[i].remove(child)
        self.onChildRemoved.provoke(biui.Event(self))
    
    ##
    #
    #
    def setColumnWidths(self,values):
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
    def setRowHeights(self,values):
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
        if column > len(self._columnWidths):
            raise Exception( Messages.ERR_COL_INDEX_OUT_OF_RANGE )
        
        self._columnWidths[column] = value
    
    ##
    #
    #
    def setRowHeight(self,row,values):
        self._resizeChildList(0,row)
        if row > len(self._rowHeights):
            raise Exception( Messages.ERR_ROW_INDEX_OUT_OF_RANGE )
        
        self._rowHeights[row] = value
    
    ## Calculates the absolute values of cols
    #  in relation to size.
    #  TODO: A column width of 0 on purpose isn't possible.
    #        It will be interpretes as a filler.
    #  TODO: If abolute values are in sum bigger than size
    #        filler will be negative. :-(
    #        Could turn into a problem!?
    #
    #  @param cols        An array with widths definition
    #                     floats - percent values
    #                     int    - absolut values
    #                     0      - fill the rest
    #  @param size        The complete size
    #  @return            An array with absolute values.
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
        # TODO: calculate position and size
        #       for each child.
        cellX = 0
        widths  = self.__calculatePixelWidths(self._columnWidths,size[0])
        heights = self.__calculatePixelWidths(self._rowHeights,size[1])
        for i,cellWidth in enumerate(widths):
            cellY = 0
            for j,cellHeight in enumerate(heights):
                child = self._children[i][j]
                if child != None:
                    alignment = child.getAlignment()
                    if alignment == biui.Alignment.FILL:
                        child.setX(cellX)
                        child.setY(cellY)
                        child.setWidth(cellWidth)
                        child.setHeight(cellHeight)
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
                            childY = cellHeight/2-child.getHeight()/2
                        
                        
                        # BOTTOM
                        #elif    alignment == biui.Alignment.BOTTOM_LEFT \
                        #   or alignment == biui.Alignment.BOTTOM_CENTER \
                        #   or alignment == biui.Alignment.BOTTOM_RIGHT:
                        elif alignment in [8,9,10]:
                            childY = cellHeight-child.getHeight()
                            
                        
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
                            childX = cellWidth/2-child.getWidth()/2
                        
                        # RIGHT
                        #elif    alignment == biui.Alignment.TOP_RIGHT  \
                        #   or alignment == biui.Alignment.CENTER_RIGHT \
                        #   or alignment == biui.Alignment.BOTTOM_RIGHT:
                        elif alignment in [4,7,10]:
                            childX = cellWidth-child.getWidth()
                        
                        child.setX(cellX+childX)
                        child.setY(cellY+childY)
                        #child.setWidth(cellWidth)
                        #child.setHeight(cellHeight)
                        
                cellY = cellY + cellHeight
            cellX = cellX + cellWidth
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    