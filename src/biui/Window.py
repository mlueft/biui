import biui
import sdl2

###
##
##
class Window(biui.ContainerWidget.ContainerWidget):
    
    ###
    ##
    ##
    def __init__(self,width,height):
        super().__init__()
        self._window = biui.DL.createWindow( "",(width,height))
        self._id = biui.DL.getWindowId(self._window)
        self._title = ""
        self._renderer = biui.DL.createRenderer(self._window)

        ##
        self.onWindowClose = biui.EventManager()
        ##
        self.onWindowShown = biui.EventManager()
        ##
        self.onWindowHidden = biui.EventManager()
        ##
        self.onWindowExposed = biui.EventManager()
        ##
        self.onWindowMoved = biui.EventManager()
        ##
        self.onWindowResized = biui.EventManager()
        ##
        self.onWindowSizeChanged = biui.EventManager()
        ##
        self.onWindowMinimized = biui.EventManager()
        ##
        self.onWindowMaximized = biui.EventManager()
        ##
        self.onWindowRestored = biui.EventManager()
        ##
        self.onWindowEnter = biui.EventManager()
        ##
        self.onWindowLeave = biui.EventManager()
        ##
        self.onWindowFocusGained = biui.EventManager()
        ##
        self.onWindowFocusLost = biui.EventManager()
        ##
        self.onWindowFocus = biui.EventManager()
        ##
        self._SHOWUPDATEBOXES = True
        ##
        self.__guiTexture = None
        ##
        self.__dr = biui.DirtyRectangleManager()
        
        ##print(dir(self._window))
        ## '__bool__', '__class__', '__ctypes_from_outparam__',
        ## '__delattr__', '__delitem__', '__dict__', '__dir__',
        ## '__doc__', '__eq__', '__format__', '__ge__',
        ## '__getattribute__', '__getitem__', '__gt__',
        ## '__hash__', '__init__', '__init_subclass__', '__le__',
        ## '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
        ## '__reduce_ex__', '__repr__', '__setattr__', '__setitem__',
        ## '__setstate__', '__sizeof__', '__str__', '__subclasshook__',
        ## '__weakref__', '_b_base_', '_b_needsfree_', '_objects',
        ## '_type_', 'contents']
        ##print(dir(self._window.contents))
        ## '__bool__', '__class__', '__ctypes_from_outparam__',
        ## '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
        ## '__format__', '__ge__', '__getattribute__', '__gt__',
        ## '__hash__', '__init__', '__init_subclass__', '__le__',
        ## '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
        ## '__reduce_ex__', '__repr__', '__setattr__', '__setstate__',
        ## '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
        ## '_b_base_', '_b_needsfree_', '_objects', '_type_', 'from_param',
        ## 'value']
        
        self.onWindowClose.add(self.__onClose)
        
        biui._addWindow(self)
        
        
    
    ## SDL_GetWindowPosition
    ## SDL_SetWindowPosition
    
    ## SDL_GetWindowSize
    ## SDL_SetWindowSize

    ## SDL_GetWindowMaximumSize
    ## SDL_SetWindowMaximumSize

    ## SDL_GetWindowMinimumSize
    ## SDL_SetWindowMinimumSize
    
    ## SDL_ShowWindow
    ## SDL_HideWindow
    ## SDL_MaximizeWindow
    ## SDL_MinimizeWindow
    ## SDL_RaiseWindow
    ## SDL_RestoreWindow
    
    ###
    ##
    ##
    def recortDirtyRectangle(self,rect):
        self.__dr.add(rect)
        
    @property
    def x(self):
        x,y = biui.DL.getWindowPos(self._window)
        return x
    
    @x.setter
    def x(self, value):
        if value == self.x:
            return
        biui.DL.setWindowPos(self._window,value,self.y)
    
    @property
    def y(self):
        x,y = biui.DL.getWindowPos(self._window)
        return y

    @y.setter
    def y(self, value):
        if value == self.y:
            return
        biui.DL.setWindowPos(self._window,self.x,value)

    @property
    def width(self):
        w,h = biui.DL.getWindowSize(self._window)
        return w
    
    @width.setter
    def width(self, value):
        if value == self.width:
            return
        if value > self.width:
            self._invalidate()
        biui.DL.setWindowSize(self._window,value,self.height)
    
    @property    
    def height(self):
        w,h = biui.DL.getWindowSize(self._window)
        return h
    
    @height.setter
    def height(self, value):
        if value == self.height:
            return
        if value > self.height:
            self._invalidate()
        biui.DL.setWindowSize(self._window,self.width,value)


    ## Returns the title of the window.
    ##
    ##  @return            An string value.
    ##
    @property
    def title(self):
        return self._title

    ### Sets the title of the window.
    ##
    ##  @param value       An string value.
    ##  @return            None    
    ##
    @title.setter
    def title(self, value):
        biui.DL.setWindowTitle(self._window,value)
        self._title = value
    
    ###
    ##
    ##
    def __onClose(self,ev):
        ## TODO: clean up all eventmanagers
        
        biui.DL.free(self._window)
        biui._removeWindow(self)
    
    ###
    ##
    ##
    def _onWindowEvent(self,event):
        ev = biui.Event(self)
        
        if event.window.event == sdl2.SDL_WINDOWEVENT_CLOSE:
            print("SDL_WINDOWEVENT_CLOSE")
            self.onWindowClose.provoke(ev)
        elif event.window.event == sdl2.SDL_WINDOWEVENT_SHOWN:
            print("SDL_WINDOWEVENT_SHOWN")
            self.onWindowShown.provoke(ev)
            self._invalidate()
        elif event.window.event == sdl2.SDL_WINDOWEVENT_HIDDEN:
            print("SDL_WINDOWEVENT_HIDDEN")
            self.onWindowHidden.provoke(ev)
        elif event.window.event == sdl2.SDL_WINDOWEVENT_EXPOSED:
            print("SDL_WINDOWEVENT_EXPOSED")
            self.onWindowExposed.provoke(ev)
            self._invalidate()
        elif event.window.event == sdl2.SDL_WINDOWEVENT_MOVED:
            ##print("SDL_WINDOWEVENT_MOVED")
            if self.x != event.window.data1 or self.y != event.window.data2:
                biui.DL.setWindowSize(
                    self._window,
                    event.window.data1,
                    event.window.data2
                )
                self.onWindowMoved.provoke(ev)
        elif event.window.event == sdl2.SDL_WINDOWEVENT_RESIZED:
            ##print("SDL_WINDOWEVENT_RESIZED")
            if self.width != event.window.data1 or self.height != event.window.data2:
                biui.DL.setWindowSize(
                    self._window,
                    event.window.data1,
                    event.window.data2
                )
                self.onWindowResized.provoke(ev)
                self._invalidate()
        elif event.window.event == sdl2.SDL_WINDOWEVENT_SIZE_CHANGED:
            ##print("SDL_WINDOWEVENT_SIZE_CHANGED(%s,%s)",event.window.data1,event.window.data2)
            if self.width != event.window.data1 or self.height != event.window.data2:
                biui.DL.setWindowSize(
                    self._window,
                    event.window.data1,
                    event.window.data2
                )
                self.onWindowSizeChanged.provoke(ev)
                self._invalidate()
        elif event.window.event == sdl2.SDL_WINDOWEVENT_MINIMIZED:
            print("SDL_WINDOWEVENT_MINIMIZED")
            self.onWindowMinimized.provoke(ev)
        elif event.window.event == sdl2.SDL_WINDOWEVENT_MAXIMIZED:
            print("SDL_WINDOWEVENT_MAXIMIZED")
            self.onWindowMaximized.provoke(ev)
        elif event.window.event == sdl2.SDL_WINDOWEVENT_RESTORED:
            print("SDL_WINDOWEVENT_RESTORED")
            self.onWindowRestored.provoke(ev)
            self._invalidate()
        elif event.window.event == sdl2.SDL_WINDOWEVENT_ENTER:
            print("SDL_WINDOWEVENT_ENTER")
            self.onWindowEnter.provoke(ev)
        elif event.window.event == sdl2.SDL_WINDOWEVENT_LEAVE:
            print("SDL_WINDOWEVENT_LEAVE")
            self.onWindowLeave.provoke(ev)
        elif event.window.event == sdl2.SDL_WINDOWEVENT_FOCUS_GAINED:
            print("SDL_WINDOWEVENT_FOCUS_GAINED")
            self.onWindowFocusGained.provoke(ev)
        elif event.window.event == sdl2.SDL_WINDOWEVENT_FOCUS_LOST:
            print("SDL_WINDOWEVENT_FOCUS_LOST")
            self.onWindowFocusLost.provoke(ev)
        elif event.window.event == sdl2.SDL_WINDOWEVENT_TAKE_FOCUS:
            #print("SDL_WINDOWEVENT_TAKE_FOCUS")
            #self.onWindowFocus.provoke(ev)
            #self._invalidate()
            pass
        else:
            print("*Unknown Windowevent.")
            pass

    ### Returns the current mouse position on the window.
    ##
    ##  @return         A tuple with x andy position of the
    ##                  mouse pointer.
    ##
    def getMousePosition(self):
        return biui.getMousePosition()
    
    ### Returns the windows internal id.
    ##
    ##
    @property
    def id(self):
        return self._id 
                
    ###
    ##
    ##
    def _onQuit(self):
        pass

    ### Returns the window's renderer.
    ##
    ##
    @property
    def renderer(self):
        return self._renderer


    def _redraw(self, forceRedraw=False):
        if self._SHOWUPDATEBOXES:
            if self.__guiTexture != None:
                ##print("cleargreen")
                r = (0,0,self.width,self.height)
                biui.DL.renderCopy(self.renderer,self.__guiTexture,r,r)
                biui.DL.free(self.__guiTexture)
                self.__guiTexture = None
                biui.DL.present(self.renderer)
                return 
        
        if not self.isInvalide():
            if not forceRedraw:
                return
        
        ##print("window::redraw----------------------------------------",forceRedraw)
        
        for c in self._children:
            c._beforeDraw()
        
        self._calculateLayout()
        
        theme = biui.getTheme()
        
        if self._texture == None:
            ##print("windows new texture")
            self._texture = biui.DL.createTexture(self.renderer,self.width,self.height)
            self.__guiTexture = self._texture
            forceRedraw = True
        
        if self._SHOWUPDATEBOXES:
            self.__guiTexture = biui.DL.createTexture(self.renderer,self.width,self.height)
            forceRedraw = True
            
        theme.drawWindowBeforeChildren(self.renderer,self,self.__guiTexture)
        
        for c in self._children:
            c._redraw(self.__guiTexture,forceRedraw)
                    
        theme.drawWindowAfterChildren(self.renderer,self,self.__guiTexture)
        
        dr = self.__dr.getRectangles()
        ## remove double rects
        ##dr = set(dr)
        
        ## Draw update boxes
        if self._SHOWUPDATEBOXES:
            boxTexture = biui.DL.createTexture(self.renderer,self.width,self.height)
            for r in dr:
                _r = [r[0],r[1],r[2]-r[0],r[3]-r[1]]
                biui.DL.drawRect(self.renderer,boxTexture,(0,255,0,255),_r,0)
                
            r = (0,0,self.width,self.height)
            biui.DL.renderCopy(self.renderer,self.__guiTexture,r,r)
            biui.DL.renderCopy(self.renderer,boxTexture,r,r)
            biui.DL.free(boxTexture)
            ##print("render boxes")
        else:
            ## just render dirty rectangles
            for r in dr:
                r = list(r)
                ## r must not reach over the widow's texture
                r[0] = max(0,r[0])
                r[1] = max(0,r[1])
                r[2] = min(r[2],self.width-r[0])
                r[3] = min(r[3],self.height-r[1])
                
                biui.DL.renderCopy(self.renderer,self._texture,r,r)
            
        biui.DL.present(self.renderer)
        
        self._isInvalide = False
        
        for c in self._children:
            c._afterDraw()
                    
    def getChildAt(self, pos):
        for c in reversed(self._children):
            cPos = c.toGlobal((0,0))
            if cPos[0] <= pos[0]:
                if cPos[0]+c.width >= pos[0]: 
                    if cPos[1] <= pos[1]:
                        if cPos[1]+c.height >= pos[1]:
                            if isinstance(c,biui.ContainerWidget.ContainerWidget):
                                return c.getChildAt(pos)
                            else:
                                return c
        return self
    
    def _recordDirtyRect(self):
        self.recortDirtyRectangle((
            0,
            0,
            self.width,
            self.height
        ))
            