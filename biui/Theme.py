import pygame

import biui

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
        surface.fill( (66,66,66) )

    ## Is called after the child objects are drawn.
    #  So it's used to draw everything that has to be
    #  top most like border
    #
    def drawWindowAfterChildren(self, widget, surface):
        pygame.draw.rect(
            surface,
            (66,66,66),
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
            (53,53,53),
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
        
        state = widget.getState()
        #print(state)
        # Normal color
        color = (89,89,89)
        
        # state color
        if state == biui.ButtonStates.OVER:
            color = (107,107,107)
        elif state == biui.ButtonStates.DOWN:
            color = (85,123,182)
        elif state == biui.ButtonStates.CHECKED:
            color = (85,123,182)
         
        pygame.draw.rect(
            surface,
            color,
            (
                pos[0],
                pos[1],
                widget.getWidth(),
                widget.getHeight()
            )  
        )
        
    #######################################################
    #
    #                                                SPACER
    #
    #######################################################
    
    ## Is called to draw a button.
    #
    #
    def drawSpacer(self, widget, surface):
        pass
            
    #######################################################
    #
    #                                           BUTTONGROUP
    #
    #######################################################
        
    ## Is called before the window child objects are drawn.
    #  So, it's useed to draw the background.
    # 
    def drawButtonGroupBeforeChildren(self, widget, surface):
        pygame.draw.rect(
            surface,
            (53,53,53),
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
    def drawButtonGroupChildren(self, widget, surface):
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
    