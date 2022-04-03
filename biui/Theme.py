import pygame
import biui
import os

## Does all the drawing stuff.
#
#
class Theme:
    
    def __init__(self, baseFolder):
        self.__lib = biui.ImageLibrary()
        self.__baseFolder = baseFolder
        self.__themeFolder = None
        
    
    ## Sets the current used theme name.
    #
    #
    def selectTheme(self,name):
        self.__themeFolder = name
        self.__themeFolder = os.path.join(self.__baseFolder ,self.__themeFolder)
        
    #######################################################
    #
    #   MISC
    #
    #######################################################
    
    ## Returns the graphical size of the rendered text
    #  of the widget.
    #
    #
    def getTextSize(self,widget):
        # TODO: resolve Pygame dependency
        font = pygame.font.SysFont(
            widget.font.name,
            widget.font.size
        )
        
        sf = font.render(
            widget.format.format(widget.value),
            widget.antialiased,
            widget.color
        )
        
        return ( sf.get_width(),sf.get_height())        
        
    #######################################################
    #
    #   WINDOW
    #
    #######################################################
    
    ## Is called before the child objects are drawn.
    #  So, it's useed to draw the background.
    #
    def drawWindowBeforeChildren(self, widget, surface):
        surface.fill( (66,66,66) )

    ## Is called after the child objects are drawn.
    #  So it's used to draw everything that has to be
    #  top most like border
    #
    def drawWindowAfterChildren(self, widget, surface):
        return
    
    #######################################################
    #
    #   FLEXGRID
    #
    #######################################################
        
    ## Is called before the window child objects are drawn.
    #  So, it's useed to draw the background.
    # 
    def drawFlexGridBeforeChildren(self, widget, surface):
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
    def drawFlexGridAfterChildren(self, widget, surface):
        return
        
    #######################################################
    #
    #   FLEXPANE
    #
    #   The Flexpane is the base container used in the
    #   FlexGrid element.
    #
    #######################################################
        
    ## Is called before the child objects are drawn.
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
            (80,80,80),
            (
                0,
                0,
                widget.width,
                widget.height
            ),1
        )
        
    #######################################################
    #
    #   FLEXSPACER
    #
    #   The Flexspacer to handle the gaps between Flexpanes
    #   in the Flexgrid.
    #
    #######################################################
    
    ## Is called to draw a button.
    #
    #
    def drawFlexSpacer(self, widget, surface):
        return
            
    #######################################################
    #
    #   PANE
    #
    #######################################################
        
    ## Is called before the child objects are drawn.
    #  So, it's useed to draw the background.
    # 
    def drawPaneBeforeChildren(self, widget, surface):
        name = os.path.join(self.__themeFolder ,"pane_bg")
        img = self.__lib.getI9(name,widget.width,widget.height)
        surface.blit(img,(0,0,img.get_width(),img.get_height()))
    
    ## Is called after the child objects are drawn.
    #  So it's used to draw everything that has to be
    #  top most like border
    #
    def drawPaneAfterChildren(self, widget, surface):
        return
    
    #######################################################
    #
    #   BUTTON
    #
    #######################################################
        
    ## Is called to draw a button.
    #
    #
    def drawButtonBeforeChildren(self, widget, surface):
        
        state = widget.state

        if state == biui.ButtonStates.OVER:
            name = "button_hover_bg"
        elif state == biui.ButtonStates.DOWN:
            name = "button_down_bg"
        elif state == biui.ButtonStates.CHECKED:
            name = "button_checked_bg"
        else:
            name = "button_normal_bg"
                    
        name = os.path.join(self.__themeFolder ,name)
        img = self.__lib.getI9(name,widget.width,widget.height)
        surface.blit(img,(0,0,img.get_width(),img.get_height()))

    ##
    #
    #
    def drawButtonAfterChildren(self, widget, surface):

        state = widget.state
        
        if state == biui.ButtonStates.OVER:
            name = "button_hover_fg"
        elif state == biui.ButtonStates.DOWN:
            name = "button_down_fg"
        elif state == biui.ButtonStates.CHECKED:
            name = "button_checked_fg"
        else:
            name = "button_normal_fg"
                    
        name = os.path.join(self.__themeFolder ,name)
        img = self.__lib.getI9(name,widget.width,widget.height)
        surface.blit(img,(0,0,img.get_width(),img.get_height()))
    
    #######################################################
    #
    #   BUTTONGROUP
    #
    #######################################################
        
    ## Is called before the child objects are drawn.
    #  So, it's useed to draw the background.
    # 
    def drawButtonGroupBeforeChildren(self, widget, surface):
        return
    
    ## Is called after the child objects are drawn.
    #  So it's used to draw everything that has to be
    #  top most like border
    #
    def drawButtonGroupChildren(self, widget, surface):
        return
        
    #######################################################
    #
    #   NUMBERSLIDER
    #
    #######################################################
        
    ## Is called before the child objects are drawn.
    #  So, it's useed to draw the background.
    # 
    def drawNumberSliderBeforeChildren(self, widget, surface):
        name = os.path.join(self.__themeFolder ,"numberslider_bg")
        img = self.__lib.getI9(name,widget.width,widget.height)
        surface.blit(img,(0,0,img.get_width(),img.get_height()))
    
    ## Is called after the child objects are drawn.
    #  So it's used to draw everything that has to be
    #  top most like border
    #
    def drawNumberSliderAfterChildren(self, widget, surface):
        name = os.path.join(self.__themeFolder ,"numberslider_fg")
        img = self.__lib.getI9(name,widget.width,widget.height)
        surface.blit(img,(0,0,img.get_width(),img.get_height()))
    
    #######################################################
    #
    #   LABEL
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
            widget.format.format(widget.value),
            widget.antialiased,
            widget.color
        )
        
        surface.blit(
            sf,
            widget.position,
            (0,0,widget.width,widget.height)
        )

    #######################################################
    #
    #   CHECKBOX
    #
    #######################################################
        
    
    #######################################################
    #
    #   SPACER
    #
    #######################################################
    
    ## Is called to draw a spacer.
    #
    #
    def drawSpacer(self, widget, surface):
        pass

        
    
        
        