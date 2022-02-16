import pygame
import math
import biui


def childHorizontalSplit(ev):
    print("childHorizontalSplit")

def childVerticalSplit(ev):
    print("childVerticalSplit")
    
def childJoinUp(ev):
    print("onJoinUp")

def childJoinRight(ev):
    print("onJoinRight")

def childJoinDown(ev):
    print("onJoinDown")

def childJoinLeft(ev):
    print("onJoinLeft")
    
def main():
    
    ##############################################
    #                                       WINDOW
    ##############################################
    wnd = biui.Window()
    wnd.setWidth(1024)
    wnd.setHeight(768)
    
    if True:
        grid = biui.FlexGrid()
        grid.setAlignment(biui.Alignment.FILL)
        
        pane = biui.FlexPane()
        pane.setX(0)
        pane.setY(0)
        pane.setWidth(1024)
        pane.setHeight(768)
          
        grid.addFlexPane(pane)
        
        wnd.addChild(grid)
        
    
    if False:
        fp = biui.FlexPane()
        fp.onJoinUp.add(childJoinUp)
        fp.onJoinRight.add(childJoinRight)
        fp.onJoinDown.add(childJoinDown)
        fp.onJoinLeft.add(childJoinLeft)
        fp.onHorizontalSplit.add(childHorizontalSplit)
        fp.onVerticalSplit.add(childVerticalSplit)
        fp.setX(10)
        fp.setY(10)
        fp.setWidth(500)
        fp.setHeight(500)
        wnd.addChild(fp)
    
    #
    # Temporary main loop
    #
    clock = pygame.time.Clock()
    
    while biui.main():
        pass

if __name__ == "__main__":
    main()