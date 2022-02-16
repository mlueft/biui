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

        #
        self.onWindowEnter = biui.EventManager()
        #
        self.onWindowLeave = biui.EventManager()
        #
        self.onWindowFocus = biui.EventManager()
        #
        self.onWindowFocusLost = biui.EventManager()
        #
        self.onWindowHidden = biui.EventManager()
        #
        self.onWindowMinimized = biui.EventManager()
        #
        self.onWindowRestored = biui.EventManager()
        #
        self.onWindowShown = biui.EventManager()
        #
        self.onWindowShown = biui.EventManager()
        #
        self.onWindowFocusGained = biui.EventManager()
        #
        self.onWindowFocusTaken = biui.EventManager()
        #
        self.onWindowClose = biui.EventManager()
        #
        self.onWindowMaximized = biui.EventManager()
        #
        self.onWindowMoved = biui.EventManager()
        #
        self.onWindowMSizeChanged = biui.EventManager()
        #
        self.onWindowSizeChanged = biui.EventManager()
        #
        self.onWindowResized = biui.EventManager()
        #
        self.onWindowExposed = biui.EventManager()
        
    ##
    #
    #
    def _onWindowEnter(self,ev):
        self.onWindowEnter.provoke(ev)
    
    ##
    #
    #
    def _onWindowLeave(self,ev):
        self.onWindowLeave.provoke(ev)

    ##
    #
    #
    def _onWindowFocus(self,ev):
        self.onWindowFocus.provoke(ev)
        self._invalidate()
    
    ##
    #
    #
    def _onWindowFocusLost(self,ev):
        self.onWindowFocusLost.provoke(ev)
    
    ##
    #
    #
    def _onWindowHidden(self,ev):
        self.onWindowHidden.provoke(ev)
    
    ##
    #
    #
    def _onWindowMinimized(self,ev):
        self.onWindowMinimized.provoke(ev)
    
    ##
    #
    #
    def _onWindowRestored(self,ev):
        self.onWindowRestored.provoke(ev)
        self._invalidate()
    
    ##
    #
    #
    def _onWindowShown(self,ev):
        self.onWindowShown.provoke(ev)
        self._invalidate()
    
    ##
    #
    #
    def _onWindowFocusGained(self,ev):
        self.onWindowFocusGained.provoke(ev)
    
    ##
    #
    #
    def _onWindowTakeFocus(self,ev):
        self.onWindowFocusTaken.provoke(ev)
    
    ##
    #
    #
    def _onWindowClose(self,ev):
        self.onWindowClose.provoke(ev)
    
    ##
    #
    #
    def _onWindowMaximized(self,ev):
        self.onWindowMaximized.provoke(ev)
    
    ##
    #
    #
    def _onWindowMoved(self,ev):
        self.onWindowMoved.provoke(ev)
    
    ##
    #
    #
    def _onWindowSizeChanged(self,ev):
        self.onWindowSizeChanged.provoke(ev)
        self._invalidate()
    
    ##
    #
    #
    def _onWindowResized(self,ev):
        self.onWindowResized.provoke(ev)
        self._invalidate()
    
    ##
    #
    #
    def _onWindowExposed(self,ev):
        self.onWindowExposed.provoke(ev)
        pass
    
    ##
    #
    #
    def getMousePosition(self):
        return biui.getMousePosition()
    
    ##
    #
    #
    def _onQuit(self):
        pass

    def setX(self, value):
        self._x = value
            
    def setY(self, value):
        self._y = value
    
    def _getSurface(self):
        return self._surface
        
    def _redraw(self):
        self._calculateLayout()
        #print("Window::_redraw")
        theme = biui.getTheme()
        theme.drawWindowBeforeChildren(self,self._surface)
        super()._redraw(self._surface)
        theme.drawWindowAfterChildren(self,self._surface)
        
    def setWidth(self, value):
        self._width = max(1,value)
        #self._surface = biui.createSurface(self.getSize())
        
    def setHeight(self, value):
        self._height = max(1,value)
        #self._surface = biui.createSurface(self.getSize())
        
    def getChildAt(self, pos):
        for i in range(len(self._children)-1,-1,-1):
            c = self._children[i]
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