import pygame
import math
import biui
import time

   
def main():
    
    ##############################################
    #                                       WINDOW
    ##############################################
    wnd = biui.Window()
    wnd.width = 1024
    wnd.height = 768
        

    #
    # Buttons
    #
    for i in range(10):
        button0 = biui.Button()
        #button0.onMouseUp.add(_test.upHandler)
        button0.x = 10
        button0.y = 10+i*25
        wnd.addChild(button0)
        
    #
    # Temporary main loop
    #
    clock = pygame.time.Clock()
    
    while biui.main():
        #sf.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))
        pygame.display.flip()

if __name__ == "__main__":
    main()