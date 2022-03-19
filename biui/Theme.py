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
                widget.width,
                widget.height
            ),1
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
                widget.width,
                widget.height
            )  
        )
    
    ## Is called after the child objects are drawn.
    #  So it's used to draw everything that has to be
    #  top most like border
    #
    def drawPaneAfterChildren(self, widget, surface):
        return
        pygame.draw.rect(
            surface,
            (255,255,255),
            (
                0,
                0,
                widget.width,
                widget.height
            ),1
        )
    
    #######################################################
    #
    #                                              FLEXPANE
    #
    #######################################################
        
    ## Is called before the window child objects are drawn.
    #  So, it's useed to draw the background.
    # 
    def drawFlexPaneBeforeChildren(self, widget, surface):
        pygame.draw.rect(
            surface,
            (55,55,55),
            (
                0,
                0,
                widget.width,
                widget.height
            )  
        )
    
    ## Is called after the child objects are drawn.
    #  So it's used to draw everything that has to be
    #  top most like border
    #
    def drawFlexPaneAfterChildren(self, widget, surface):
        pygame.draw.rect(
            surface,
            (255,255,255),
            (
                0,
                0,
                widget.width,
                widget.height
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
    def drawButtonBeforeChildren(self, widget, surface):
        
        state = widget.state
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
                0,
                0,
                widget.width,
                widget.height
            )  
        )
        
    def drawButtonAfterChildren(self, widget, surface):
        pass
    
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
    #                                            FLEXSPACER
    #
    #######################################################
    
    ## Is called to draw a button.
    #
    #
    def drawFlexSpacer(self, widget, surface):
        pygame.draw.rect(
            surface,
            (55,55,55),
            (
                widget.x,
                widget.y,
                widget.width,
                widget.height
            )
        )
                
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
                widget.width,
                widget.height
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
                widget.width,
                widget.height
            ),1
        )
    
    #######################################################
    #
    #                                              SPLITTER
    #
    #######################################################
        
    ## Is called before the window child objects are drawn.
    #  So, it's useed to draw the background.
    # 
    def drawSplitterBeforeChildren(self, widget, surface):
        pygame.draw.rect(
            surface,
            (100,53,53),
            (
                0,
                0,
                widget.width,
                widget.height
            )  
        )
    
    ## Is called after the child objects are drawn.
    #  So it's used to draw everything that has to be
    #  top most like border
    #
    def drawSplitterAfterChildren(self, widget, surface):
        pygame.draw.rect(
            surface,
            (255,255,255),
            (
                0,
                0,
                widget.width,
                widget.height
            ),1
        )
        
    #######################################################
    #
    #                                             FLEXGRID
    #
    #######################################################
        
    ## Is called before the window child objects are drawn.
    #  So, it's useed to draw the background.
    # 
    def drawFlexGridBeforeChildren(self, widget, surface):
        pygame.draw.rect(
            surface,
            (100,53,53),
            (
                0,
                0,
                widget.width,
                widget.height
            )  
        )
    
    ## Is called after the child objects are drawn.
    #  So it's used to draw everything that has to be
    #  top most like border
    #
    def drawFlexGridAfterChildren(self, widget, surface):
        pygame.draw.rect(
            surface,
            (255,255,255),
            (
                0,
                0,
                widget.width,
                widget.height
            ),1
        )
        
    #######################################################
    #
    #                                                 LABEL
    #
    #######################################################
        
    ## 
    #  
    #  
    def drawLabel(self, widget, surface):
        
        font = pygame.font.SysFont(
            widget.font.name,
            widget.font.size
        )
        
        sf = font.render(
            widget.text,
            widget.antialiased,
            widget.color
        )
        
        surface.blit(
            sf,
            widget.position,
            (0,0,widget.width,widget.height)
        )

        
        