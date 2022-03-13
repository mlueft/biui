import pygame
import math
import biui
import time

def milli():
    return round(time.time() * 1000)

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
    wnd.width = 1024
    wnd.height = 768
    
    if False:
        lbl = biui.Label()
        lbl.x = 10
        lbl.y = 10
        lbl.font.size = 25
        lbl.font.name = "Courier"
        lbl.color = (200,200,200)
        lbl.anialiased = True
        
        wnd.addChild(lbl)
        
        btn = biui.Button()
        btn.x = 19
        btn.y = 100
        btn.width = 300
        btn.height = 100
        
        wnd.addChild(btn)
        
    if False:
        start = milli()
        print( "start           : "+str(milli()-start))
        
        
        all_fonts = pygame.font.get_fonts()
        print("fonts:"+str(len(all_fonts)))
        
        
        start = milli()
        print( "all_fonts           : "+str(milli()-start))
        
        
        sf = wnd._getSurface()
    
    
        start = milli()
        print( "surface           : "+str(milli()-start))
        
        
        font = pygame.font.SysFont("Arial",72)
        print("====================")
        for i in dir(font):
            print(str(i))
            
            
        start = milli()
        print( "font           : "+str(milli()-start))
        
        
        text = font.render("hello world!", True,(0,128,0))
        print("====================")
        for i in dir(text):
            print(str(i))        
        
        
        start = milli()
        print( "font           : "+str(milli()-start))
        
        
    if True:
        grid = biui.FlexGrid()
        grid.alignment = biui.Alignment.FILL
        
        pane = biui.FlexPane()
        pane.x = 0
        pane.y = 0
        pane.width = 1024
        pane.height = 768
          
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
        fp.x = 10
        fp.y = 10
        fp.width = 500
        fp.height = 500
        wnd.addChild(fp)
    
    #
    # Temporary main loop
    #
    clock = pygame.time.Clock()
    
    while biui.main():
        #sf.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))
        pygame.display.flip()

if __name__ == "__main__":
    main()