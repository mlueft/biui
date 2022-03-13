import pygame
import math
import biui
import time

   
def upHandler(ev):
    print("up")

def main():
    
    ##############################################
    #                                       WINDOW
    ##############################################
    wnd = biui.Window()
    wnd.setWidth(1024)
    wnd.setHeight(768)
    
    if True:

        for i in range(1):
            button0 = biui.Button()
            button0.onMouseUp.add(upHandler)
            button0.setX(10)
            button0.setY(10+i*25)
            wnd.addChild(button0)

        for i in range(1):
            button0 = biui.FlexSpacer()
            button0.onMouseUp.add(upHandler)
            button0.setX(100)
            button0.setY(10+i*25)
            button0.setWidth(100)
            button0.setHeight(20)
            wnd.addChild(button0)
    if False:
        grid = biui.FlexGrid()
        grid.setAlignment(biui.Alignment.FILL)
        
        pane = biui.FlexPane()
        pane.setX(0)
        pane.setY(0)
        pane.setWidth(1024)
        pane.setHeight(768)
          
        grid.addFlexPane(pane)
        
        wnd.addChild(grid)
        
 
    #
    # Temporary main loop
    #
    clock = pygame.time.Clock()
    
    while biui.main():
        #sf.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))
        pygame.display.flip()

if __name__ == "__main__":
    main()