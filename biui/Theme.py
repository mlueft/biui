import pygame

## Does all the drawing stuff.
#
#
class Theme:
    
    #######################################################
    #
    #                                                WINDOW
    #
    #######################################################
    
    ## Is called before the window child objects are drawn.
    #  So, it's useed to draw the background.
    #
    def drawWindowBeforeChildren(self, widget, surface):
        surface.fill( (50,50,50) )

    ## Is called after the child objects are drawn.
    #  So it's used to draw everything that has to be
    #  top most like border
    #
    def drawWindowAfterChildren(self, widget, surface):
        pygame.draw.rect(
            surface,
            (50,255,50),
            (
                0,
                0,
                widget.getWidth(),
                widget.getHeight()
            ),5
        )
    
    #######################################################
    #
    #                                                  PANE
    #
    #######################################################
        
    ## Is called before the window child objects are drawn.
    #  So, it's useed to draw the background.
    # 
    def drawPaneBeforeChildren(self, widget, surface):
        pygame.draw.rect(
            surface,
            (50,100,50),
            (
                0,
                0,
                widget.getWidth(),
                widget.getHeight()
            )  
        )
    
    ## Is called after the child objects are drawn.
    #  So it's used to draw everything that has to be
    #  top most like border
    #
    def drawPaneAfterChildren(self, widget, surface):
        pygame.draw.rect(
            surface,
            (255,255,255),
            (
                0,
                0,
                widget.getWidth(),
                widget.getHeight()
            ),1
        )
    
    #######################################################
    #
    #                                                BUTTON
    #
    #######################################################
        
    ## Is called to draw a button.
    #
    #
    def drawButton(self, widget, surface):
        pos = widget.getPosition()
        pygame.draw.rect(
            surface,
            (100,50,150),
            (
                pos[0],
                pos[1],
                widget.getWidth(),
                widget.getHeight()
            )  
        )