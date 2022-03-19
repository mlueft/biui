import pygame
import math
import biui
import time

   
def main():
    
    ##############################################
    #                                       WINDOW
    ##############################################
    wnd = biui.Window(1024,768)

    #
    # Buttons
    #
    for i in range(10):
        button0 = biui.Button()
        #button0.onMouseUp.add(_test.upHandler)
        button0.x = 10
        button0.y = 10+i*45
        button0.width = 150
        button0.height = 40
        button0.label.font.size = 25
        button0.label.color = (200,200,200)
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