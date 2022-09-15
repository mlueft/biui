import biui
import os
import sdl2


#debug
from random import random

## Does all the drawing stuff.
#
#
class Theme:
    
    def __init__(self, baseFolder):
        self.__lib = biui.ImageLibrary()
        self.__baseFolder = baseFolder
        self.__themeFolder = None
      
    ##
    #
    #
    def quit(self):
        self.__lib.quit()
            
    ##
    #
    #
    def getImageLibrary(self):
        return self.__lib
    
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
        return (10,10)
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
        
        return ( sf.contents.w,sf.contents.h)        
        
    ## Draws nothing.
    # 
    def drawEmpty(self, renderer, widget, texture):
        return
    
    #######################################################
    #
    #   WINDOW
    #
    #######################################################
    
    ## Is called before the child objects are drawn.
    #  So, it's useed to draw the background.
    #
    def drawWindowBeforeChildren(self, renderer, widget, texture):
        biui.DL.fill( renderer,texture, (66,66,66,255) )

    ## Is called after the child objects are drawn.
    #  So it's used to draw everything that has to be
    #  top most like border
    #
    def drawWindowAfterChildren(self, renderer, widget, texture):
        return
    
    #######################################################
    #
    #   FLEXGRID
    #
    #######################################################
        
    ## Is called before the window child objects are drawn.
    #  So, it's useed to draw the background.
    # 
    def drawFlexGridBeforeChildren(self, renderer, widget, texture):
        biui.DL.drawRect(
            renderer,
            texture,
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
    def drawFlexGridAfterChildren(self, renderer, widget, texture):
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
    def drawFlexPaneBeforeChildren(self, renderer, widget, texture):
        biui.DL.drawRect(
            renderer,
            texture,
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
    def drawFlexPaneAfterChildren(self, renderer, widget, texture):
        biui.DL.drawRect(
            renderer,
            texture,
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
    def drawFlexSpacer(self, renderer, widget, texture):
        return
        biui.DL.drawRect(
            renderer,
            texture,
            (50+random()*205,0,0),
            (
                widget.x,
                widget.y,
                widget.width,
                widget.height
            )
        )
            
    #######################################################
    #
    #   PANE
    #
    #######################################################
        
    ## Is called before the child objects are drawn.
    #  So, it's useed to draw the background.
    # 
    def drawPaneBeforeChildren(self, renderer, widget, texture):
        name = os.path.join(self.__themeFolder ,"pane_bg")
        img = self.__lib.getI9(renderer,name,widget.width,widget.height)
        #img = self.__lib.getImage(renderer,name,widget.width,widget.height)
        biui.DL.blit(
            renderer,
            texture,
            img,
            (0,0,widget.width,widget.height),
            (0,0,widget.width,widget.height)
        )
    
    ## Is called after the child objects are drawn.
    #  So it's used to draw everything that has to be
    #  top most like border
    #
    def drawPaneAfterChildren(self, renderer, widget, texture):
        
        name = os.path.join(self.__themeFolder ,"pane_fg")
        img = self.__lib.getI9(renderer,name,widget.width,widget.height)
        biui.DL.blit(
            renderer,
            texture,
            img,
            (0,0,widget.width,widget.height),
            (0,0,widget.width,widget.height)
        )
    
    #######################################################
    #
    #   BUTTON
    #
    #######################################################
        
    ## Is called to draw a button.
    #
    #
    def drawButtonBeforeChildren(self, renderer, widget, texture):
        
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
        img = self.__lib.getI9(renderer,name,widget.width,widget.height)
        biui.DL.blit(
            renderer,
            texture,
            img,
            (0,0,widget.width,widget.height),
            (0,0,widget.width,widget.height)
        )

    ##
    #
    #
    def drawButtonAfterChildren(self, renderer, widget, texture):

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
        img = self.__lib.getI9(renderer,name,widget.width,widget.height)
        biui.DL.blit(
            renderer,
            texture,
            img
        )
    
    #######################################################
    #
    #   BUTTONGROUP
    #
    #######################################################
        
    ## Is called before the child objects are drawn.
    #  So, it's useed to draw the background.
    # 
    def drawButtonGroupBeforeChildren(self, renderer, widget, texture):
        return
    
    ## Is called after the child objects are drawn.
    #  So it's used to draw everything that has to be
    #  top most like border
    #
    def drawButtonGroupChildren(self, renderer, widget, texture):
        return
        
    #######################################################
    #
    #   PROGRESSBAR
    #
    #######################################################

    ## Is called before the child objects are drawn.
    #  So, it's useed to draw the background.
    # 
    def drawProgressbarBeforeChildren(self, renderer, widget, texture):
        # background
        biui.DL.drawRect(
            renderer,
            texture,
            (80,80,80),
            (
                0,
                0,
                widget.width,
                widget.height
            )
        )
        
        # bar
        if widget.value == widget.minValue:
            return

        width = widget.width*(1/((widget.maxValue-widget.minValue)/(widget.value-widget.minValue)))
            
        biui.DL.drawRect(
            renderer,
            texture,
            (100,100,100),
            (
                0,
                0,
                int(width),
                widget.height
            )
        )
        
    ## Is called after the child objects are drawn.
    #  So it's used to draw everything that has to be
    #  top most like border
    #
    def drawProgressbarChildren(self, renderer, widget, texture):
        biui.DL.drawRect(
            renderer,
            texture,
            (0,0,0),
            (
                0,
                0,
                widget.width,
                widget.height
            ),1
        )
        
    #######################################################
    #
    #   NUMBERSLIDER
    #   The numberslider it self has nothing to draw.
    #   It contains buttons, Progreessbar or textField
    #
    #######################################################
        
    #######################################################
    #
    #   LABEL
    #
    #######################################################
        
    ## 
    #  
    #  
    def drawLabel(self, renderer, widget, texture):
        return
        font = pygame.font.SysFont(
            widget.font.name,
            widget.font.size
        )
        
        sf = font.render(
            widget.format.format(widget.value),
            widget.antialiased,
            widget.color
        )
        
        biui.DL.blit(
            renderer,
            texture,
            sf,
            widget.position,
            (0,0,widget.width,widget.height)
        )

    #######################################################
    #
    #   CHECKBOX
    #
    #######################################################
        
    ## Is called before the child objects are drawn.
    #  So, it's useed to draw the background.
    # 
    def drawCheckboxBeforeChildren(self, renderer, widget, texture):
        state = widget.state

        if state == biui.ButtonStates.OVER:
            name = "checkbox_hover_bg.png"
        elif state == biui.ButtonStates.DOWN:
            name = "checkbox_hover_bg.png"
        elif state == biui.ButtonStates.CHECKED:
            name = "checkbox_checked_bg.png"
        else:
            name = "checkbox_normal_bg.png"
                    
        name = os.path.join(self.__themeFolder ,name)
        img = self.__lib.getImage(renderer,name)
        sizeIMG = biui.DL.getTextureSize(img)
        biui.DL.blit(
            renderer,
            texture,
            img,
            (
                0,
                widget.height/2-sizeIMG[3]/2,
                sizeIMG[2],
                sizeIMG[3]
            ),
            (
                0,
                widget.height/2-sizeIMG[3]/2,
                sizeIMG[2],
                sizeIMG[3]
            )
        )
        
        # TODO: If checked we draw a symbol on it
    
    #######################################################
    #
    #   SPACER
    #
    #######################################################
    
    ## Is called to draw a spacer.
    #
    #
    def drawSpacer(self, renderer, widget, texture):
        pass

        
    
        
        