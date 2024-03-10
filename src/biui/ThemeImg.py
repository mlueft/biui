#include "biui.inc"
#include "pysdl2.inc"

import os
import sdl2
import random
import ctypes
import biui
from biui.Theme import Theme
from biui.Enum import ButtonStates

### Does all the drawing stuff.
##
##
class ThemeImg(Theme):
    
    def __init__(self, baseFolder):
        super().__init__(baseFolder)

      
    ###
    ##
    ##
    def quit(self):
        super.quit()
            
    ########################################################
    ##
    ##   WINDOW
    ##
    ########################################################
    
    ### Is called before the child objects are drawn.
    ##  So, it is used to draw the background.
    ##
    def drawWindowBeforeChildren(self, renderer, widget, texture):
        super().drawWindowBeforeChildren(renderer, widget, texture)

    ### Is called after the child objects are drawn.
    ##  So it is used to draw everything that has to be
    ##  top most like border
    ##
    def drawWindowAfterChildren(self, renderer, widget, texture):
        super().drawWindowAfterChildren(renderer, widget, texture)
    
    ########################################################
    ##
    ##   FLEXGRID
    ##
    ########################################################
        
    ### Is called before the window child objects are drawn.
    ##  So, it is used to draw the background.
    ## 
    def drawFlexGridBeforeChildren(self, renderer, widget, texture):
        
        #ifdef BIUI_THEME_DEBUG
        self.blinkBox1(renderer, widget, texture)
        return 
        #endif
        
        if widget.backColor != None:
            PYSDL2_DRAWRECTFILLED(renderer,texture,widget.backColor.rgba,(0,0,widget.width,widget.height))
            return
                
        PYSDL2_DRAWRECTFILLED(renderer,texture,biui.Color(0,0,0,255).rgba,(0,0,widget.width,widget.height))
    
    ### Is called after the child objects are drawn.
    ##  So it is used to draw everything that has to be
    ##  top most like border
    ##
    def drawFlexGridAfterChildren(self, renderer, widget, texture):

        if widget.borderColor != None:
            PYSDL2_DRAWRECT(renderer,texture,widget.borderColor.rgba,(0,0,widget.width,widget.height))
            return
        
    ########################################################
    ##
    ##   FLEXPANE
    ##
    ##   The Flexpane is the base container used in the
    ##   FlexGrid element.
    ##
    ########################################################
        
    ### Is called before the child objects are drawn.
    ##  So, it is used to draw the background.
    ## 
    def drawFlexPaneBeforeChildren(self, renderer, widget, texture):
        
        #ifdef BIUI_THEME_DEBUG
        self.blinkBox1(renderer, widget, texture)
        return 
        #endif
        
        if widget.backColor != None:
            PYSDL2_DRAWRECTFILLED(renderer,texture,widget.backColor.rgba,(0,0,widget.width,widget.height))
            return
                
        PYSDL2_DRAWRECTFILLED(renderer,texture,biui.Color(155,155,155,255).rgba,(0,0,widget.width,widget.height))
    
    ### Is called after the child objects are drawn.
    ##  So it is used to draw everything that has to be
    ##  top most like border
    ##
    def drawFlexPaneAfterChildren(self, renderer, widget, texture):
        
        if widget.borderColor != None:
            PYSDL2_DRAWRECT(renderer,texture,widget.borderColor.rgba,(0,0,widget.width,widget.height))
            return
                
        PYSDL2_DRAWRECT(renderer,texture,biui.Color(255,255,255,255).rgba,(0,0,widget.width,widget.height))
    
    ########################################################
    ##
    ##   FLEXSPACER
    ##
    ##   The Flexspacer to handle the gaps between Flexpanes
    ##   in the Flexgrid.
    ##
    ########################################################
    
    ### Is called to draw a button.
    ##
    ##
    def drawFlexSpacer(self, renderer, widget, texture):
        
        #ifdef BIUI_THEME_DEBUG
        self.blinkBox(renderer, widget, texture)
        return 
        #endif

        PYSDL2_DRAWRECTFILLED(renderer,texture,widget.backColor.rgba,(widget.x,widget.y,widget.width,widget.height))

    ########################################################
    ##
    ##   Menubar
    ##
    ########################################################
        
    ### Is called before the child objects are drawn.
    ##  So, it is used to draw the background.
    ## 
    def drawMenubarBeforeChildren(self, renderer, widget, texture):
        
        #ifdef BIUI_THEME_DEBUG
        self.blinkBox1(renderer, widget, texture)
        return 
        #endif
        
        PYSDL2_DRAWRECTFILLED(renderer,texture,widget.backColor.rgba,(0,0,widget.width,widget.height))
    
    ### Is called after the child objects are drawn.
    ##  So it is used to draw everything that has to be
    ##  top most like border
    ##
    def drawMenubarAfterChildren(self, renderer, widget, texture):
        
        if widget.borderColor != None:
            PYSDL2_DRAWRECT(renderer,texture,widget.borderColor.rgba,(0,0,widget.width,widget.height))
            return
                
        PYSDL2_DRAWRECT(renderer,texture,biui.Color(80,80,80,255).rgba,(0,0,widget.width,widget.height))

    ########################################################
    ##
    ##   MenuPane
    ##
    ########################################################
        
    ### Is called before the child objects are drawn.
    ##  So, it is used to draw the background.
    ## 
    def drawMenuPaneBeforeChildren(self, renderer, widget, texture):
        
        #ifdef BIUI_THEME_DEBUG
        self.blinkBox1(renderer, widget, texture)
        return 
        #endif
        
        PYSDL2_DRAWRECTFILLED(renderer,texture,widget.backColor.rgba,(0,0,widget.width,widget.height))
    
    ### Is called after the child objects are drawn.
    ##  So it is used to draw everything that has to be
    ##  top most like border
    ##
    def drawMenuPaneAfterChildren(self, renderer, widget, texture):
        if widget.borderColor != None:
            PYSDL2_DRAWRECT(renderer,texture,widget.borderColor.rgba,(0,0,widget.width,widget.height))
            return
                
    ########################################################
    ##
    ##   Menubutton
    ##
    ########################################################
        
    ### Is called before the child objects are drawn.
    ##  So, it is used to draw the background.
    ## 
    def drawMenubuttonBeforeChildren(self, renderer, widget, texture):
        
        #ifdef BIUI_THEME_DEBUG
        self.blinkBox1(renderer, widget, texture)
        return 
        #endif
        
        if widget.backColor != None:
            PYSDL2_DRAWRECTFILLED(renderer,texture,widget.backColor.rgba,(0,0,widget.width,widget.height))
            return
                
        state = widget.state

        if state == ButtonStates.OVER:
            color = biui.Color(150,150,150,255)
        elif state == ButtonStates.DOWN:
            color = biui.Color(120,120,120,255)
        elif state == ButtonStates.CHECKED:
            color = biui.Color(128,128,128,255)
        else:
            color = biui.Color(128,128,128,255)
                    
        PYSDL2_DRAWRECTFILLED(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
    
    ### Is called after the child objects are drawn.
    ##  So it is used to draw everything that has to be
    ##  top most like border
    ##
    def drawMenubuttonAfterChildren(self, renderer, widget, texture):
        if widget.borderColor != None:
            PYSDL2_DRAWRECT(renderer,texture,widget.borderColor.rgba,(0,0,widget.width,widget.height))
            return
    
    ########################################################
    ##
    ##   PANE
    ##
    ########################################################
        
    ### Is called before the child objects are drawn.
    ##  So, it is used to draw the background.
    ## 
    def drawPaneBeforeChildren(self, renderer, widget, texture):
        
        #ifdef BIUI_THEME_DEBUG
        self.blinkBox1(renderer, widget, texture)
        return 
        #endif
        
        if widget.backColor != None:
            PYSDL2_DRAWRECTFILLED(renderer,texture,widget.backColor.rgba,(0,0,widget.width,widget.height))
            return
                
        name = os.path.join(self._themeFolder ,"pane_bg")
        img = self._lib.getI9(renderer,name,widget.width,widget.height)
        ##img = self._lib.getImage(renderer,name,widget.width,widget.height)
        r = (0,0,widget.width,widget.height)
        PYSDL2_RENDER_COPY1(renderer,texture,img,r,r)
    
    ### Is called after the child objects are drawn.
    ##  So it is used to draw everything that has to be
    ##  top most like border
    ##
    def drawPaneAfterChildren(self, renderer, widget, texture):
        
        if widget.borderColor != None:
            PYSDL2_DRAWRECT(renderer,texture,widget.borderColor.rgba,(0,0,widget.width,widget.height))
            return
                
        name = os.path.join(self._themeFolder ,"pane_fg")
        img = self._lib.getI9(renderer,name,widget.width,widget.height)
        r = (0,0,widget.width,widget.height)
        PYSDL2_RENDER_COPY1(renderer,texture,img,r,r)
    
    ########################################################
    ##
    ##   BUTTON
    ##
    ########################################################
        
    ### Is called to draw a button.
    ##
    ##
    def drawButtonBeforeChildren(self, renderer, widget, texture):
        
        #ifdef BIUI_THEME_DEBUG
        self.blinkBox1(renderer, widget, texture)
        return 
        #endif
        
        if widget.backColor != None:
            PYSDL2_DRAWRECTFILLED(renderer,texture,widget.backColor.rgba,(0,0,widget.width,widget.height))
            return
                
        state = widget.state

        if state == ButtonStates.OVER:
            name = "button_hover_bg"
        elif state == ButtonStates.DOWN:
            name = "button_down_bg"
        elif state == ButtonStates.CHECKED:
            name = "button_checked_bg"
        else:
            name = "button_normal_bg"
                    
        name = os.path.join(self._themeFolder ,name)
        img = self._lib.getI9(renderer,name,widget.width,widget.height)
        r = (0,0,widget.width,widget.height)
        PYSDL2_RENDER_COPY1(renderer,texture,img,r,r)

    ###
    ##
    ##
    def drawButtonAfterChildren(self, renderer, widget, texture):

        if widget.borderColor != None:
            PYSDL2_DRAWRECT(renderer,texture,widget.borderColor.rgba,(0,0,widget.width,widget.height))
            return
        
        state = widget.state
        
        if state == ButtonStates.OVER:
            name = "button_hover_fg"
        elif state == ButtonStates.DOWN:
            name = "button_down_fg"
        elif state == ButtonStates.CHECKED:
            name = "button_checked_fg"
        else:
            name = "button_normal_fg"
                    
        name = os.path.join(self._themeFolder ,name)
        img = self._lib.getI9(renderer,name,widget.width,widget.height)
        r = (0,0,widget.width,widget.height)
        PYSDL2_RENDER_COPY1(renderer,texture,img,r,r)
    
    ########################################################
    ##
    ##   BUTTONGROUP
    ##
    ########################################################
        
    ### Is called before the child objects are drawn.
    ##  So, it is used to draw the background.
    ## 
    def drawButtonGroupBeforeChildren(self, renderer, widget, texture):
        #ifdef BIUI_THEME_DEBUG
        self.blinkBox1(renderer, widget, texture)
        return 
        #endif
        if widget.backColor != None:
            PYSDL2_DRAWRECTFILLED(renderer,texture,widget.backColor.rgba,(0,0,widget.width,widget.height))
            return
    
    ### Is called after the child objects are drawn.
    ##  So it is used to draw everything that has to be
    ##  top most like border
    ##
    def drawButtonGroupAfterChildren(self, renderer, widget, texture):
        if widget.borderColor != None:
            PYSDL2_DRAWRECT(renderer,texture,widget.borderColor.rgba,(0,0,widget.width,widget.height))
            return
        
    ########################################################
    ##
    ##   PROGRESSBAR
    ##
    ########################################################

    ### Is called before the child objects are drawn.
    ##  So, it is used to draw the background.
    ## 
    def drawProgressbarBeforeChildren(self, renderer, widget, texture):
        #ifdef BIUI_THEME_DEBUG
        self.blinkBox1(renderer, widget, texture)
        return 
        #endif
        
        if widget.backColor != None:
            PYSDL2_DRAWRECTFILLED(renderer,texture,widget.backColor.rgba,(0,0,widget.width,widget.height))
            return
                
        ## background
        PYSDL2_DRAWRECTFILLED(renderer,texture,biui.Color(80,80,80,255).rgba,(0,0,widget.width,widget.height))
        
        ## bar
        if widget.value == widget.minValue:
            return

        width = widget.width*(1/((widget.maxValue-widget.minValue)/(widget.value-widget.minValue)))
            
        PYSDL2_DRAWRECTFILLED(renderer,texture,biui.Color(100,100,100,255).rgba,(0,0,int(width),widget.height))
        
    ### Is called after the child objects are drawn.
    ##  So it is used to draw everything that has to be
    ##  top most like border
    ##
    def drawProgressbarAfterChildren(self, renderer, widget, texture):
        
        if widget.borderColor != None:
            PYSDL2_DRAWRECT(renderer,texture,widget.borderColor.rgba,(0,0,widget.width,widget.height))
            return
                
        PYSDL2_DRAWRECT(renderer,texture,biui.Color(0,0,0,255).rgba,(0,0,widget.width,widget.height))
        
    ########################################################
    ##
    ##   NUMBERSLIDER
    ##   The numberslider it self has nothing to draw.
    ##   It contains buttons, Progreessbar or textField
    ##
    ########################################################
        
    ########################################################
    ##
    ##   LABEL
    ##
    ########################################################
        
    ### 
    ##  
    ##  
    def drawLabel(self, renderer, widget, texture):

        p = widget.position
        
        if widget.backColor != None:
            PYSDL2_DRAWRECTFILLED(renderer,texture,widget.backColor.rgba,(p[0],p[1],widget.width,widget.height))
                
        tx = widget.font.render(
            renderer,
            widget.format.format(widget.value),
            widget.color
        )
        
        PYSDL2_GETTEXTURESIZE(tx,r)
        ## If not autosize just copy the size of the widget
        ## or of the rendered text, if it is smaller than the widget.
        if not widget.autoSize:
            r = (r[0],r[1],min(r[2],widget.width),min(r[3],widget.height))        
        PYSDL2_RENDER_COPY1(renderer,texture,tx,(p[0],p[1],r[2],r[3]),r)
        sdl2.SDL_DestroyTexture( tx )

        if widget.borderColor != None:
            PYSDL2_DRAWRECT(renderer,texture,widget.borderColor.rgba,(p[0],p[1],widget.width,widget.height))
            
    ########################################################
    ##
    ##   CHECKBOX
    ##
    ########################################################
        
    ### Is called before the child objects are drawn.
    ##  So, it is used to draw the background.
    ## 
    def drawCheckboxBeforeChildren(self, renderer, widget, texture):
        
        #ifdef BIUI_THEME_DEBUG
        self.blinkBox1(renderer, widget, texture)
        return 
        #endif
        
        if widget.backColor != None:
            PYSDL2_DRAWRECTFILLED(renderer,texture,widget.backColor.rgba,(0,0,widget.width,widget.height))
                
        state = widget.state

        if state == ButtonStates.OVER:
            name = "checkbox_hover_bg.png"
        elif state == ButtonStates.DOWN:
            name = "checkbox_hover_bg.png"
        elif state == ButtonStates.CHECKED:
            name = "checkbox_checked_bg.png"
        else:
            name = "checkbox_normal_bg.png"
                    
        name = os.path.join(self._themeFolder ,name)
        img = self._lib.getImage(renderer,name)
        PYSDL2_GETTEXTURESIZE(img,sizeIMG)
        r = (0,widget.height/2-sizeIMG[3]/2,sizeIMG[2],sizeIMG[3])
        PYSDL2_RENDER_COPY1(renderer,texture,img,r,r)
        
        ## TODO: If checked we draw a symbol on it
    
    ### Is called after the child objects are drawn.
    ##  So it is used to draw everything that has to be
    ##  top most like border
    ##
    def drawCheckboxAfterChildren(self, renderer, widget, texture):
        
        if widget.borderColor != None:
            PYSDL2_DRAWRECT(renderer,texture,widget.borderColor.rgba,(0,0,widget.width,widget.height))
            return
                
    ########################################################
    ##
    ##   SPACER
    ##
    ########################################################
    
    ### Is called to draw a spacer.
    ##
    ##
    def drawSpacer(self, renderer, widget, texture):
        pass

        
    
        
        