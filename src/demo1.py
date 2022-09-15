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
    wnd.width = 1024
    wnd.height = 768
    
    if True:

        for i in range(1):
            button0 = biui.Button()
            button0.onMouseUp.add(upHandler)
            button0.x = 10
            button0.y = 10+i*25
            wnd.addChild(button0)

        for i in range(1):
            button0 = biui.FlexSpacer()
            button0.onMouseUp.add(upHandler)
            button0.x = 100
            button0.y = 10+i*25
            button0.width = 100
            button0.height = 20
            wnd.addChild(button0)
    if False:
        grid = biui.FlexGrid()
        grid.alignment = biui.Alignment.FILL
        
        pane = biui.FlexPane()
        pane.x = 0
        pane.y = 0
        pane.width = 1024
        pane.height = 768
          
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