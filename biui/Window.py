import biui

##
#
#
class Window(biui.ContainerWidget.ContainerWidget):
    
    ##
    #
    #
    def __init__(self):
        super().__init__()
        self.setWidth(1024)
        self.setHeight(768)
        self._surface = biui.createWindow(self)
        biui._addWindow(self)
        
    ##
    #
    #
    def onWindowEnter(self):
        pass
    
    ##
    #
    #
    def onWindowLeave(self):
        pass

    ##
    #
    #
    def onWindowFocus(self):
        self._invalidate()
    
    ##
    #
    #
    def onWindowFocusLost(self):
        pass
    
    ##
    #
    #
    def onWindowHidden(self):
        pass
    
    ##
    #
    #
    def onWindowMinimized(self):
        pass
    
    ##
    #
    #
    def onWindowRestored(self):
        self._invalidate()
    
    ##
    #
    #
    def onWindowShown(self):
        self._invalidate()
    
    ##
    #
    #
    def onWindowFocusGained(self):
        pass
    
    ##
    #
    #
    def onWindowTakeFocus(self):
        pass
    
    ##
    #
    #
    def onWindowClose(self):
        pass
    
    ##
    #
    #
    def onWindowMaximized(self):
        pass
    
    ##
    #
    #
    def onWindowMoved(self):
        pass
    
    ##
    #
    #
    def onWindowSizeChanged(self):
        self._invalidate()
    
    ##
    #
    #
    def onWindowResized(self):
        self._invalidate()
    
    ##
    #
    #
    def onWindowExposed(self):
        pass
    
    ##
    #
    #
    def onQuit(self):
        pass

    def setX(self, value):
        self._x = value
            
    def setY(self, value):
        self._y = value
    
    def _getSurface(self):
        return self._surface
        
    def _redraw(self):
        #print("Window::_redraw")
        theme = biui.getTheme()
        theme.drawWindowBeforeChildren(self,self._surface)
        super()._redraw(self._surface)
        theme.drawWindowAfterChildren(self,self._surface)
        
    def setWidth(self, value):
        self._width = value
        #self._surface = biui.createSurface(self.getSize())
        
    def setHeight(self, value):
        self._height = value
        #self._surface = biui.createSurface(self.getSize())
        
    def getChildAt(self, pos):
        for c in self._children:
            cPos = c.toGlobal((0,0))
            if cPos[0] <= pos[0]:
                if cPos[0]+c.getWidth() >= pos[0]: 
                    if cPos[1] <= pos[1]:
                        if cPos[1]+c.getHeight() >= pos[1]:
                            if isinstance(c,biui.ContainerWidget.ContainerWidget):
                                return c.getChildAt(pos)
                            else:
                                return c
                   
        return self
    
    def _recordDirtyRect(self):
        #print("Window::_recordDirtyRect")
        self._dirtyRects = [(
            0,
            0,
            self._width,
            self._height
        )]