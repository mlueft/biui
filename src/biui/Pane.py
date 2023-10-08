#include "pysdl2.inc"
import sdl2 

import biui
from biui.ContainerWidget import ContainerWidget
 
###
##
##
class Pane(ContainerWidget):
    
    ###
    ##
    ##
    def __init__(self):
        
        super().__init__()
        self.__contentPane = biui.ContainerWidget()
        self.__contentPane.alignment = biui.Alignment.FILL
        super().addChild(self.__contentPane,0,0)
        
        ##
        self.__verticalScrollbar = None
        ##
        self.__horizontalScrollbar = None
        
        self.layoutManager.columnWidths = [0,1]
        self.layoutManager.rowHeights = [0,1]
        
        theme = biui.getTheme()
        self._themeBackgroundfunction = theme.drawPaneBeforeChildren
        self._themeForegroundfunction = theme.drawPaneAfterChildren
        
              
    ###
    ##
    ##
    def connectScrollNavigator(self,navigator):
    ##    if navigator.onScrollPositionChanged.has(self.__hndOnScrollPositionChanged):
    ##        return
    ##    
        navigator.connectPane(self.__contentPane)

    ###
    ##
    ##
    def disconnectScrollNavigator(self,navigator):
        navigator.disconnectPane(self.__contentPane)
            
    ###
    ##
    ##
    @property
    def verticalScrollbar(self):
        return self.__verticalScrollbar != None
    
    ###
    ##
    ##
    @verticalScrollbar.setter
    def verticalScrollbar(self,value):
        if value and self.__verticalScrollbar:
            return
        
        if not value:
            ## remove scrollbar
            self.__contentPane.disconnectScrollNavigator(self.__verticalScrollbar)
            super().removeChild(self.__verticalScrollbar)
            super().layoutManager.columnWidths = [0,1]
            self.__verticalScrollbar = None
            return 
        
        ## add scrollbar
        super().layoutManager.columnWidths = [0,20]
        sn = biui.ScrollNavigator()
        sn.alignment = biui.Alignment.FILL
        sn.isVertical = True
        self.__contentPane.connectScrollNavigator(sn)
        super().addChild(sn,1,0)
        self.__verticalScrollbar = sn
        
    ###
    ##
    ##
    @property
    def horizontalScrollbar(self):
        return self.__horizontalScrollbar != None
    
    ###
    ##
    ##
    @horizontalScrollbar.setter
    def horizontalScrollbar(self,value):
        if value and self.__horizontalScrollbar:
            return
        
        if not value:
            ## remove scrollbar
            super().layoutManager.rowHeights = [0,1]
            super().removeChild(self.__horizontalScrollbar)
            self.__contentPane.disconnectScrollNavigator(self.__horizontalScrollbar)
            self.__horizontalScrollbar = None
            return 
        
        ## add scrollbar
        super().layoutManager.rowHeights = [0,20]
        sn = biui.ScrollNavigator()
        sn.alignment = biui.Alignment.FILL
        sn.isHorizontal = True
        self.__contentPane.connectScrollNavigator(sn)
        super().addChild(sn,0,1)
        self.__horizontalScrollbar = sn
        
    ### @see: biui.ContainerWidget.removeChild
    ##
    ##   
    def removeChild(self,child):
        self.__contentPane.removeChild(child)
     
    ### @see: biui.ContainerWidget.addChild
    ##
    ##       
    def addChild(self,child,x=0,y=0):
        self.__contentPane.addChild(child,x,y)
        
    ### Returns the current scroll position.
    ##
    ##  @return            A tuple representing the position.
    ##
    @property
    def scrollPosition(self):
        return self.__contentPane.scrollPosition 
    
    ### Returns the x/y position of the GUI element.
    ##
    ##  @return            A tuple representing the size.
    ##
    @property
    def scrollSize(self):
        return self.__contentPane.scrollSize
            
    ### Returns the maximum scroll position in x direction.
    ##
    ##  @return            
    ##
    @property
    def scrollWidth(self):
        return self.__contentPane.scrollWidth
    
    ### Returns the maximum scroll position in y direction.
    ##
    ##  @return            
    ##
    @property
    def scrollHeight(self):
        return self.__contentPane.scrollHeight
    
    ### Returns the current scroll position in x direction.
    ##
    ##  @return            
    ##
    @property
    def scrollX(self):
        return self.__contentPane.scrollX
    
    ### Sets the current scroll position in x direction. 
    ##
    ##  @param value       An integer value.
    ##  @return            None
    ##
    @scrollX.setter
    def scrollX(self, value):
        self.__contentPane.scrollX = value
        
    ### Returns the current scroll position in y direction.
    ##
    ##  @return            
    ##
    @property
    def scrollY(self):
        return self.__contentPane.scrollY
    
    ### Sets the current scroll position in y direction. 
    ##
    ##  @param value       A integer value.
    ##  @return            None
    ##
    @scrollY.setter
    def scrollY(self, value):
        self.__contentPane.scrollY = value
        
    def _redraw(self, texture, forceRedraw=False ):
        
        if not self.isInvalide():
            if not forceRedraw:
                return
        
        ##print( "redraw:{} {}x{} {}".format(self.name,self.x,self.y,forceRedraw))
 
        wnd = self.window
        sw = self.width
        sh = self.height
        ##for child in self._children:
        ##    sw = max(sw,child.right)
        ##    sh = max(sh,child.bottom)
        self._scrollWidth = sw
        self._scrollHeight = sh
        PYSDL2_CREATETEXTURE(wnd.renderer,sw,sh,self._texture)
              
        pos = self.position
        
        ## we paint on our own surface
        ## not on the parent´s surface
        _texture = self._texture
        theme = biui.getTheme()
        self._themeBackgroundfunction(self.window.renderer,self,_texture)
 
        ## We draw all Children on our own surface        
        for c in self._children:
            forceRedraw = self._isInvalide or forceRedraw
            c._redraw(_texture,forceRedraw)
                    
        self._themeForegroundfunction(self.window.renderer,self,_texture)
        
        ## Now we copy the visible area 
        ## of our own surface
        ## on the parent´s surface
        PYSDL2_RENDER_COPY1(
            self.window.renderer,
            texture,
            _texture,
            (pos[0],pos[1],self.width,self.height),
            (0,0,self.width,self.height)
        )
        
        self._isInvalide = False
