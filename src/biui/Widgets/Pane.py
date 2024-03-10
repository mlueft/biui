#include "pysdl2.inc"
import sdl2 

import biui
from biui.Widgets import ContainerWidget
from biui.Widgets import ScrollNavigator
from biui.Enum import Alignment

###
##
##
class Pane(ContainerWidget):
    
    ###
    ##
    ##
    def __init__(self):
        
        super().__init__()
        self.__contentPane = ContainerWidget()
        self.__contentPane.alignment = Alignment.FILL
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
        sn = ScrollNavigator()
        sn.alignment = Alignment.FILL
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
        sn = ScrollNavigator()
        sn.alignment = Alignment.FILL
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
        
    def _redraw(self, forceRedraw=False ):
        
        if not self.isInvalide():
            if not forceRedraw:
                return
        
        ##print( "redraw:{} {}x{} {}".format(self.name,self.x,self.y,forceRedraw))
 
        wnd = self.window
        renderer = self.window.renderer        
        sw = self.width
        sh = self.height
        ##for child in self._children:
        ##    sw = max(sw,child.right)
        ##    sh = max(sh,child.bottom)
        self._scrollWidth = sw
        self._scrollHeight = sh
        PYSDL2_CREATETEXTURE(renderer,sw,sh,texture)
              
        pos = self.position
        
        ## we paint on our own surface
        ## not on the parent´s surface
        self._themeBackgroundfunction(self,texture)
 
        ## We draw all Children on our own surface
        forceRedraw = self._isInvalide or forceRedraw
        for c in self._children:
            ## Each child returns a texture where it has drawn itself at (0,0)
            tx = c._redraw(forceRedraw)
            
            ## We copy it at the childs position in the childs size.
            p = c.position
            tgt = (p[0],p[1],c.width,c.height)
            src = (0,0,c.width,c.height)
            PYSDL2_RENDER_COPY1(renderer,texture,tx,tgt,src)
            ## Finally we have to destroy the texture returned by the child
            PYSDL2_DESTROYTEXTURE( tx )
                    
        self._themeForegroundfunction(self,texture)
        
        
        self._isInvalide = False

        return texture