import pygame
import math
import biui
import time

def main():
    
    ##############################################
    #                                       WINDOW
    ##############################################
    wnd = biui.Window(800,600)
    
    lbl = biui.Label()
    lbl.x = 10
    lbl.y = 10
    lbl.alignment = biui.Alignment.CENTER_CENTER
    lbl.font.size = 50
    lbl.font.name = "Courier"
    lbl.color = (255,255,255)
    lbl.anialiased = True
    
    wnd.addChild(lbl)
        
        
    
    #
    # Temporary main loop
    #
    clock = pygame.time.Clock()
    
    while biui.main():
        #sf.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))
        pygame.display.flip()

if __name__ == "__main__":
    main()