import biui

##
#
#
class HorizontalSplitter(biui.ContainerWidget.ContainerWidget):
    
    def __init__(self):
        super().__init__()
        #
        self.onJoinUp = biui.EventManager()
        #
        self.onJoinDown = biui.EventManager()
        #
        self.onJoinLeft = biui.EventManager()
        #
        self.onJoinRight = biui.EventManager()
        #
        self.onVerticalSplit = biui.EventManager()
        #
        self.onHorizontalSplit = biui.EventManager()
                
        self._children = []
        self._parent = None
        
        lm = self.getLayoutManager()
        lm.setColumnWidths([0])
        lm.setRowHeights([0])

        self._splitStartPosition = None
        
    def myPaneClick(self,ev):
        lm = self.getLayoutManager()
        index = lm.getPositionOfChild(ev.getEventSource())
        print(self)
        print(index)
        
    def addChild(self,child,x=0,y=0):
        super().addChild(child,x,y)
        child.setAlignment(biui.Alignment.FILL)
        
        child.onHorizontalSplit.add( self.childHorizontalSplit )
        child.onVerticalSplit.add( self.childVerticalSplit )
        child.onJoinRight.add( self.childJoinRight )
        child.onJoinLeft.add( self.childJoinLeft )
        child.onJoinDown.add( self.childJoinDown )
        child.onJoinUp.add( self.childJoinUp )
        
        child.onMouseUp.add( self.myPaneClick )

    def removeChild(self,child):
        super().removeChild(child)
        
        child.onHorizontalSplit.remove( self.childHorizontalSplit )
        child.onVerticalSplit.remove( self.childVerticalSplit )
        child.onJoinRight.remove( self.childJoinRight )
        child.onJoinLeft.remove( self.childJoinLeft )
        child.onJoinDown.remove( self.childJoinDown )
        child.onJoinUp.remove( self.childJoinUp )
         
        child.onMouseUp.remove( self.myPaneClick )
        
    def myMouseUp(self,ev):
        self.onMouseUp.remove(self.myMouseUp)
        self.onMouseMove.remove(self.myMouseMove)
        
    def myMouseMove(self,ev):
        #print(ev.getPosition())
        pass
    ##
    #
    #   
    def childHorizontalSplit(self,ev):
        child = ev.getEventSource()
        lm = self.getLayoutManager()
        index = lm.getPositionOfChild(child)[0]
        self.removeChild(child)
        splitter = biui.VerticalSplitter()
        splitter.addChild(child,0,0)
        splitter.addChild(biui.FlexPane(),0,1)
        lm = splitter.getLayoutManager()
        self.addChild(splitter, index, 0)
    ##
    #
    #
    def childVerticalSplit(self,ev):
        child = ev.getEventSource()
        lm = self.getLayoutManager()
        index = lm.getPositionOfChild(child)[0]
        lm.insertColumnAt(index)
        self.addChild( biui.FlexPane(),index,0 )

    ##
    #
    #
    def childJoinUp(self,ev):
        print("onJoinUp")
    
    ##
    #
    #
    def childJoinRight(self,ev):
        print("onJoinRight")
    
    ##
    #
    #
    def childJoinDown(self,ev):
        print("onJoinDown")
    
    ##
    #
    #
    def childJoinLeft(self,ev):
        print("onJoinLeft")
        
    def _redraw(self, surface):
        #print("FlexPane::_redraw")
        pos = self.getPosition()
        
        # we paint on our own surface
        # not on the parent's surface
        _surface = self._surface
        theme = biui.getTheme()
        theme.drawSplitterBeforeChildren(self,_surface)

        # We draw all Children on our own surface        
        for c in self._children:
            c._redraw(_surface)
                    
        theme.drawSplitterAfterChildren(self,_surface)
        
        # Now we copy the visible area 
        # of our own surface
        # on the parent's surface
        surface.blit(_surface,pos,(0,0,self.getWidth(),self.getHeight()))
        
        
        
        
        