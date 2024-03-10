import biui
from biui.Widgets import ContainerWidget
from biui.Events import EventManager,Event
from biui.Widgets import Spacer
from biui.Enum import Alignment

###
##
##
class FlexPane(ContainerWidget):
    
    def __init__(self):
        super().__init__()
        theme = biui.getTheme()
        self._themeBackgroundfunction = theme.drawFlexPaneBeforeChildren
        self._themeForegroundfunction = theme.drawFlexPaneAfterChildren
        
        self._minWidth = 40
        self._minHeight = 40
        
                
        ##
        self.onJoinUp = EventManager()
        ##
        self.onJoinDown = EventManager()
        ##
        self.onJoinLeft = EventManager()
        ##
        self.onJoinRight = EventManager()
        ##
        self.onVerticalSplit = EventManager()
        ##
        self.onHorizontalSplit = EventManager()
        
        self._acTopLeft = self._createActiveCorner()
        self._acTopLeft.onMouseDown.add(self.__hndOnActiveCornerTopLeftMouseDown)
        self._acTopLeft.onMouseUp.add(self.__hndOnActiveCornerTopLeftMouseUp)
        self._acTopLeft.alignment = Alignment.TOP_LEFT
        self.addChild(self._acTopLeft)
        
        self._acTopRight = self._createActiveCorner()
        self._acTopRight.onMouseDown.add(self.__hndOnActiveCornerTopRightMouseDown)
        self._acTopRight.onMouseUp.add(self.__hndOnActiveCornerTopRightMouseUp)
        self._acTopRight.alignment = Alignment.TOP_RIGHT
        self.addChild(self._acTopRight)

        self._acBottomLeft = self._createActiveCorner()
        self._acBottomLeft.onMouseDown.add(self.__hndOnActiveCornerBottomLeftMouseDown)
        self._acBottomLeft.onMouseUp.add(self.__hndOnActiveCornerBottomLeftMouseUp)
        self._acBottomLeft.alignment = Alignment.BOTTOM_LEFT
        self.addChild(self._acBottomLeft)
        
        self._acBottomRight = self._createActiveCorner()
        self._acBottomRight.onMouseDown.add(self.__hndOnActiveCornerBottomRightMouseDown)
        self._acBottomRight.onMouseUp.add(self.__hndOnActiveCornerBottomRightMouseUp)
        self._acBottomRight.alignment = Alignment.BOTTOM_RIGHT
        self.addChild(self._acBottomRight)
        
        
    ## TODO: Those four functions could be removed?
    def __hndOnActiveCornerTopLeftMouseDown(self,ev):
        self._acTopLeft.onMouseLeave.add(self.__hndOnActiveCornerTopLeftLeave)
    
    def __hndOnActiveCornerTopRightMouseDown(self,ev):
        self._acTopRight.onMouseLeave.add(self.__hndOnActiveCornerTopRightLeave)
    
    def __hndOnActiveCornerBottomLeftMouseDown(self,ev):
        self._acBottomLeft.onMouseLeave.add(self.__hndOnActiveCornerBottomLeftLeave)
    
    def __hndOnActiveCornerBottomRightMouseDown(self,ev):
        self._acBottomRight.onMouseLeave.add(self.__hndOnActiveCornerBottomRightLeave)


    def __hndOnActiveCornerTopLeftMouseUp(self,ev):
        self._acTopLeft.onMouseLeave.remove(self.__hndOnActiveCornerTopLeftLeave)
    
    def __hndOnActiveCornerTopRightMouseUp(self,ev):
        self._acTopRight.onMouseLeave.remove(self.__hndOnActiveCornerTopRightLeave)
    
    def __hndOnActiveCornerBottomLeftMouseUp(self,ev):
        self._acBottomLeft.onMouseLeave.remove(self.__hndOnActiveCornerBottomLeftLeave)
    
    def __hndOnActiveCornerBottomRightMouseUp(self,ev):
        self._acBottomRight.onMouseLeave.remove(self.__hndOnActiveCornerBottomRightLeave)
        
    ### Returns a widget used as a active corner.
    ##
    ##
    def _createActiveCorner(self):
        ## We use a Spacer to get
        ## an invisible corner
        ac = Spacer()
        ac.width = 15
        ac.height = 15
        return ac
        
    ### Handles mouse leave event of the top left active corner.
    ##  It provokes split or join events if necessary.
    ##
    def __hndOnActiveCornerTopLeftLeave(self,ev):

        ac = ev.eventSource
        pos = ac.toLocal(ev.position)
        
        if pos[0] <= 0:
            self.onJoinLeft.provoke(Event(self))
        elif pos[1] <= 0:
            self.onJoinUp.provoke(Event(self)) 
        elif pos[0] >= ac.width:
            self.onVerticalSplit.provoke(Event(self))
        else:
            self.onHorizontalSplit.provoke(Event(self))
     
        self._acTopLeft.onMouseLeave.remove(self.__hndOnActiveCornerTopLeftLeave)
        
    ### Handles mouse leave event of the top right active corner.
    ##  It provokes split or join events if necessary.
    ##
    def __hndOnActiveCornerTopRightLeave(self,ev):

        ac = ev.eventSource
        pos = ac.toLocal(ev.position)
        
        if pos[0] <= 0:
            self.onVerticalSplit.provoke(Event(self))
        elif pos[1] >= ac.height:
            self.onHorizontalSplit.provoke(Event(self))
        elif pos[0] >= ac.width:
            self.onJoinRight.provoke(Event(self)) 
        else:
            self.onJoinUp.provoke(Event(self))

        self._acTopRight.onMouseLeave.remove(self.__hndOnActiveCornerTopRightLeave)
        
    ### Handles mouse leave event of the bottom left active corner.
    ##  It provokes split or join events if necessary.
    ##
    def __hndOnActiveCornerBottomLeftLeave(self,ev):

        ac = ev.eventSource
        pos = ac.toLocal(ev.position)
        
        if pos[0] <= 0:
            self.onJoinLeft.provoke(Event(self))
        elif pos[1] >= ac.height:
            self.onJoinDown.provoke(Event(self))
        elif pos[0] >= ac.width:
            self.onVerticalSplit.provoke(Event(self)) 
        else:
            self.onHorizontalSplit.provoke(Event(self))
            
        self._acBottomLeft.onMouseLeave.remove(self.__hndOnActiveCornerBottomLeftLeave)
        
    ### Handles mouse leave event of the bottom right active corner.
    ##  It provokes split or join events if necessary.
    ##
    def __hndOnActiveCornerBottomRightLeave(self,ev):

        ac = ev.eventSource
        pos = ac.toLocal(ev.position)
        
        if pos[0] <= 0:
            self.onVerticalSplit.provoke(Event(self))
        elif pos[1] >= ac.height:
            self.onJoinDown.provoke(Event(self))
        elif pos[0] >= ac.width:
            self.onJoinRight.provoke(Event(self)) 
        else:
            self.onHorizontalSplit.provoke(Event(self))
        
        self._acBottomRight.onMouseLeave.remove(self.__hndOnActiveCornerBottomRightLeave)
        
    def _redraw1(self, texture, forceRedraw=False):
        
        if not self.isInvalide():
            if not forceRedraw:
                return 
                
        ##print("FlexPane::_redraw")
        pos = self.position
        
        ## we paint on our own texture
        ## not on the parent´s texture
        _texture = self._texture
        theme = biui.getTheme()
        theme.drawFlexPaneBeforeChildren(self.window.renderer,self,_texture)

        forceRedraw = self.isInvalide() or forceRedraw
        ## We draw all Children on our own texture        
        for c in self._children:
            c._redraw(_texture,forceRedraw)
                    
        theme.drawFlexPaneAfterChildren(self.window.renderer,self,_texture)
        
        ## Now we copy the visible area 
        ## of our own texture
        ## on the parent´s texture
        ##texture.blit(_texture,pos,(0,0,self.width,self.height))
        PYSDL2_RENDER_COPY1(self.window.renderer,texture,_texture,(pos[0],pos[1],self.width,self.height),(0,0,self.width,self.height))
        
        self._isInvalide = False        
                