#include "biui.inc"
#include "pysdl2.inc"

import os
import sdl2
import random
import ctypes
import json

import biui
from biui.Color import Color
from biui.Enum import ButtonStates
from biui.Widgets import Label

### Does all the drawing stuff.
##
##
class Theme():
    
    def __init__(self, baseFolder):
        self._lib = biui.ImageLibrary()
        self._baseFolder = baseFolder
        self._themeFolder = None
        self._shema = {
            "TOOLTIP_BACKGROUND":[150,150,150,255],
            "TOOLTIP_BORDER":[10,10,10,255],
            "TOOLTIP_TEXT":[0,0,0,255],
            
            "WINDOW_BACKGROUND":[50,50,50,255],
            "WINDOW_BORDER":[0,0,0,0],
            "FLEXBOX_BACKGROUND":[0,0,0,255],
            "FLEXBOX_BORDER":[0,0,0,255],
            "FLEXPANE_BACKGROUND":[0,0,0,255],
            "FLEXPANE_BORDER":[0,0,0,255],
            "FLEXSPACER":[0,0,0,255],
            "MENUBAR_BACKGROUND":[70,70,70,255],
            "MENUBAR_BORDER":[0,0,0,255],
            "MENUPANE_BACKGROUND":[0,0,0,255],
            "MENUPANE_BORDER":[0,0,0,255],
            
            "MENUBUTTON_NORMAL_BACKGROUND":[90,90,90,255],
            "MENUBUTTON_OVER_BACKGROUND":[120,120,120,255],
            "MENUBUTTON_DOWN_BACKGROUND":[120,120,120,255],
            "MENUBUTTON_CHECKED_BACKGROUND":[0,0,0,255],
            "MENUBUTTON_BORDER":[0,0,0,0],
            
            "PANE_BACKGROUND":[40,40,40,255],
            "PANE_BORDER":[30,30,30,255],
            
            "BUTTON_NORMAL_BACKGROUND":[70,70,70,255],
            "BUTTON_OVER_BACKGROUND":[90,90,90,255],
            "BUTTON_DOWN_BACKGROUND":[55,55,55,255],
            "BUTTON_CHECKED_BACKGROUND":[60,90,60,255],
            "BUTTON_BORDER":[0,0,0,255],
                        
            "BUTTONGROUP_BACKGROUND":[0,0,0,0],
            "BUTTONGROUP_BORDER":[0,0,0,0],
            
            "PROGRESSBAR_BACKGROUND":[70,70,70,255],
            "PROGRESSBAR_BAR":[60,90,60,255],
            "PROGRESSBAR_BORDER":[0,0,0,255],
            
            "LABEL_BACKGROUND":[0,0,0,0],
            "LABEL_BORDER":[0,0,0,0],
            
            "CHECKBOX_BACKGROUND":[0,0,0,0],
            "CHECKBOX_BORDER":[0,0,0,0],
            "CHECKBOX_CHECKBOX_NORMAL_BACKGROUND":[70,70,70,255],
            "CHECKBOX_CHECKBOX_OVER_BACKGROUND":[90,90,90,255],
            "CHECKBOX_CHECKBOX_DOWN_BACKGROUND":[55,55,55,255],
            "CHECKBOX_CHECKBOX_CHECKED_BACKGROUND":[60,90,60,255],
            "CHECKBOX_CHECKBOX_BORDER":[0,0,0,255],
            
            "SPACER_BACKGROUND":[50,70,50,255],
            
            "SCROLLNAVIGATOR_BACKGROUND":[50,50,50,255],
            "SCROLLNAVIGATOR_BORDER":[0,0,0,255],

            "TEXTFIELD_BACKGROUND":[250,250,250,255],
            "TEXTFIELD_BORDER":[255,0,0,255],
                        
            "IMAGE_BACKGROUND":[0,0,0,0],
            "IMAGE_BORDER":[0,0,0,0]
        }
        
        for k,v in self._shema.items():
            self._shema[k] = Color(v[0],v[1],v[2],v[3])
            
    ###
    ##
    ##
    def quit(self):
        self._lib.quit()

    ###
    ##
    ##
    def getImageLibrary(self):
        return self._lib
    
    ### Sets the current used theme name.
    ##
    ##  @param name   The folder name of the Theme.
    ##
    def selectTheme(self,name):
        
        self._themeFolder = os.path.join(self._baseFolder ,name)
        
        shemaFile = os.path.join(self._themeFolder, "shema.json")
        if os.path.exists(shemaFile):
            with open( shemaFile) as sFile:
                shema = sFile.read()
            self._shema = json.loads(shema)
        
            for k,v in self._shema.items():
                self._shema[k] = Color(v[0],v[1],v[2],v[3])

    ########################################################
    ##
    ##   MISC
    ##
    ########################################################
    
    ### Draws nothing.
    ##
    ## 
    def drawEmpty(self, widget, texture):
        return
    
    ########################################################
    ##
    ##   TOOLTIP
    ##
    ########################################################
    
    ###
    ##
    ##
    def getTooltip(self, widget):
        tt = Label()
        tt.backColor = self._shema["TOOLTIP_BACKGROUND"]
        tt.borderColor = self._shema["TOOLTIP_BORDER"]
        tt.color = self._shema["TOOLTIP_TEXT"]
        return tt

    ########################################################
    ##
    ##   WINDOW
    ##
    ########################################################
    
    ### Is called before the child objects are drawn.
    ##  So, it is used to draw the background.
    ##
    def drawWindowBeforeChildren(self, widget, texture):
        renderer = widget.renderer
        
        if widget.backColor:
            result = True
            color = widget.backColor
        else:
            result = False
            color = self._shema["WINDOW_BACKGROUND"]
            
        PYSDL2_FILL( renderer,texture, color.rgba )
        return result

    ### Is called after the child objects are drawn.
    ##  So it is used to draw everything that has to be
    ##  top most like border
    ##
    def drawWindowAfterChildren(self, widget, texture):
        renderer = widget.renderer
        
        if widget.borderColor:
            result = True
            color = widget.borderColor
        else:
            result = False
            color = self._shema["WINDOW_BORDER"]
        
        PYSDL2_DRAWRECT(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
        return result
        
    ########################################################
    ##
    ##   FLEXGRID
    ##
    ########################################################
        
    ### Is called before the window child objects are drawn.
    ##  So, it is used to draw the background.
    ## 
    def drawFlexGridBeforeChildren(self, widget, texture):
        renderer = widget.window.renderer
        
        if widget.backColor:
            result = True
            color = widget.backColor
        else:
            result = False
            color = self._shema["FLEXBOX_BACKGROUND"]
            
        PYSDL2_DRAWRECTFILLED(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
        return result
    
    ### Is called after the child objects are drawn.
    ##  So it is used to draw everything that has to be
    ##  top most like border
    ##
    def drawFlexGridAfterChildren(self, widget, texture):
        renderer = widget.window.renderer
        
        if widget.borderColor:
            result = True
            color = widget.borderColor
        else:
            result = False
            color = self._shema["FLEXBOX_BORDER"]
        
        PYSDL2_DRAWRECT(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
        return result
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
    def drawFlexPaneBeforeChildren(self, widget, texture):
        renderer = widget.window.renderer
        
        if widget.backColor:
            result = True
            color = widget.backColor
        else:
            result = False
            color = self._shema["FLEXPANE_BACKGROUND"]
        
        PYSDL2_DRAWRECTFILLED(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
        return result
    
    ### Is called after the child objects are drawn.
    ##  So it is used to draw everything that has to be
    ##  top most like border
    ##
    def drawFlexPaneAfterChildren(self, widget, texture):
        renderer = widget.window.renderer
        
        if widget.borderColor:
            result = True
            color = widget.borderColor
        else:
            result = False
            color = self._shema["FLEXPANE_BORDER"]
        
        PYSDL2_DRAWRECT(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
        return result
    
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
    def drawFlexSpacer(self, widget, texture):
        renderer = widget.window.renderer
        
        if widget.backColor:
            result = True
            color = widget.backColor
        else:
            result = False
            color = self._shema["FLEXSPACER"]
        
        PYSDL2_DRAWRECTFILLED(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
        return result
    
    ########################################################
    ##
    ##   Menubar
    ##
    ########################################################
        
    ### Is called before the child objects are drawn.
    ##  So, it is used to draw the background.
    ## 
    def drawMenubarBeforeChildren(self, widget, texture):
        renderer = widget.window.renderer
        
        if widget.backColor:
            result = True
            color = widget.backColor
        else:
            result = False
            color= self._shema["MENUBAR_BACKGROUND"]
        
        PYSDL2_DRAWRECTFILLED(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
        return result
    
    ### Is called after the child objects are drawn.
    ##  So it is used to draw everything that has to be
    ##  top most like border
    ##
    def drawMenubarAfterChildren(self, widget, texture):
        renderer = widget.window.renderer
        
        if widget.borderColor:
            result = True
            color = widget.borderColor
        else:
            result = False
            color = self._shema["MENUBAR_BORDER"]
        
        PYSDL2_DRAWRECT(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
        return result

    ########################################################
    ##
    ##   MenuPane
    ##
    ########################################################
        
    ### Is called before the child objects are drawn.
    ##  So, it is used to draw the background.
    ## 
    def drawMenuPaneBeforeChildren(self, widget, texture):
        renderer = widget.window.renderer
        
        if widget.backColor:
            result= True
            color = widget.backColor
        else:
            result = False
            color = self._shema["MENUPANE_BACKGROUND"]
            
        PYSDL2_DRAWRECTFILLED(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
        return result
    
    ### Is called after the child objects are drawn.
    ##  So it is used to draw everything that has to be
    ##  top most like border
    ##
    def drawMenuPaneAfterChildren(self, widget, texture):
        renderer = widget.window.renderer
        
        if widget.borderColor:
            result= True
            color = widget.borderColor
        else:
            result = False
            color = self._shema["MENUPANE_BORDER"]
        
        PYSDL2_DRAWRECT(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
        return result
                
    ########################################################
    ##
    ##   Menubutton
    ##
    ########################################################
        
    ### Is called before the child objects are drawn.
    ##  So, it is used to draw the background.
    ## 
    def drawMenubuttonBeforeChildren(self, widget, texture):
        renderer = widget.window.renderer
        
        
        state = widget.state

        if state == ButtonStates.OVER:
            if widget.backColorOver:
                result= True
                color = widget.backColorOver
            else:
                result = False
                color = self._shema["MENUBUTTON_OVER_BACKGROUND"]
        elif state == ButtonStates.DOWN:
            if widget.backColorDown:
                result= True
                color = widget.backColorDown
            else:
                result = False
                color = self._shema["MENUBUTTON_DOWN_BACKGROUND"]
        elif state == ButtonStates.CHECKED:
            if widget.backColorChecked:
                result= True
                color = widget.backColorChecked
            else:
                result = False
                color = self._shema["MENUBUTTON_CHECKED_BACKGROUND"]
        else:
            if widget.backColor:
                result= True
                color = widget.backColor
            else:
                result = False
                color = self._shema["MENUBUTTON_NORMAL_BACKGROUND"]
                    
        PYSDL2_DRAWRECTFILLED(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
        return result
    
    ### Is called after the child objects are drawn.
    ##  So it is used to draw everything that has to be
    ##  top most like border
    ##
    def drawMenubuttonAfterChildren(self, widget, texture):
        renderer = widget.window.renderer
        
        if widget.borderColor:
            result= True
            color = widget.borderColor
        else:
            result = False
            color = self._shema["MENUBUTTON_BORDER"]
        
        PYSDL2_DRAWRECT(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
        return result
    
    ########################################################
    ##
    ##   PANE
    ##
    ########################################################
        
    ### Is called before the child objects are drawn.
    ##  So, it is used to draw the background.
    ## 
    def drawPaneBeforeChildren(self, widget, texture):
        renderer = widget.window.renderer
        
        if widget.backColor:
            result= True
            color = widget.backColor
        else:
            result = False
            color = self._shema["PANE_BACKGROUND"]
        
        PYSDL2_DRAWRECTFILLED(renderer,texture,color.rgba,(0,0,widget._scrollWidth+widget.width,widget._scrollHeight+widget.height))
        return result
    
    ### Is called after the child objects are drawn.
    ##  So it is used to draw everything that has to be
    ##  top most like border
    ##
    def drawPaneAfterChildren(self, widget, texture):
        renderer = widget.window.renderer
        
        if widget.borderColor:
            result= True
            color = widget.borderColor
        else:
            result = False
            color = self._shema["PANE_BORDER"]
        
        ## The widget is a container for the actual scrollcontainer.
        ## its scrollposition is ever 0,0!
        PYSDL2_DRAWRECT(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
        return result
    
    ########################################################
    ##
    ##   BUTTON
    ##
    ########################################################
        
    ### Is called to draw a button.
    ##
    ##
    def drawButtonBeforeChildren(self, widget, texture):
        renderer = widget.window.renderer
        
        state = widget.state
        if state == ButtonStates.OVER:
            if widget.backColorOver:
                result= True
                color = widget.backColorOver
            else:
                result = False
                color = self._shema["BUTTON_OVER_BACKGROUND"]
        elif state == ButtonStates.DOWN:
            if widget.backColorDown:
                result= True
                color = widget.backColorDown
            else:
                result = False
                color = self._shema["BUTTON_DOWN_BACKGROUND"]
        elif state == ButtonStates.CHECKED:
            if widget.backColorChecked:
                result= True
                color = widget.backColorChecked
            else:
                result = False
                color = self._shema["BUTTON_CHECKED_BACKGROUND"]
        else:
            if widget.backColor:
                result= True
                color = widget.backColor
            else:
                result = False
                color = self._shema["BUTTON_NORMAL_BACKGROUND"]
       
        PYSDL2_DRAWRECTFILLED(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
        return result

    ###
    ##
    ##
    def drawButtonAfterChildren(self, widget, texture):
        renderer = widget.window.renderer
        
        if widget.borderColor:
            result= True
            color = widget.borderColor
        else:
            result = False
            color = self._shema["BUTTON_BORDER"]
        
        PYSDL2_DRAWRECT(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
        return result
    
    ########################################################
    ##
    ##   BUTTONGROUP
    ##
    ########################################################
        
    ### Is called before the child objects are drawn.
    ##  So, it is used to draw the background.
    ## 
    def drawButtonGroupBeforeChildren(self, widget, texture):
        renderer = widget.window.renderer
        
        if widget.backColor:
            result= True
            color = widget.backColor
        else:
            result = False
            color = self._shema["BUTTONGROUP_BACKGROUND"]
        
        PYSDL2_DRAWRECTFILLED(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
        return result
    
    ### Is called after the child objects are drawn.
    ##  So it is used to draw everything that has to be
    ##  top most like border
    ##
    def drawButtonGroupAfterChildren(self, widget, texture):
        renderer = widget.window.renderer
        
        if widget.borderColor:
            result= True
            color = widget.borderColor
        else:
            result = False
            color = self._shema["BUTTONGROUP_BORDER"]
        
        PYSDL2_DRAWRECT(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
        return result
        
    ########################################################
    ##
    ##   PROGRESSBAR
    ##
    ########################################################

    ### Is called before the child objects are drawn.
    ##  So, it is used to draw the background.
    ## 
    def drawProgressbarBeforeChildren(self, widget, texture):
        renderer = widget.window.renderer
        
        if widget.backColor:
            result= True
            color = widget.backColor
        else:
            result = False
            color = self._shema["PROGRESSBAR_BACKGROUND"]
        
        PYSDL2_DRAWRECTFILLED(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
        
        ## bar
        if widget.value == widget.minValue:
            return

        width = widget.width*(1/((widget.maxValue-widget.minValue)/(widget.value-widget.minValue)))
        if widget.backColor:
            result= True
            color = widget.backColor
        else:
            result = False
            color = self._shema["PROGRESSBAR_BAR"]
        
        PYSDL2_DRAWRECTFILLED(renderer,texture,color.rgba,(0,0,int(width),widget.height))
        return result
        
    ### Is called after the child objects are drawn.
    ##  So it is used to draw everything that has to be
    ##  top most like border
    ##
    def drawProgressbarAfterChildren(self, widget, texture):
        renderer = widget.window.renderer
        
        if widget.borderColor:
            result= True
            color = widget.borderColor
        else:
            result = False
            color = self._shema["PROGRESSBAR_BORDER"]
        
        PYSDL2_DRAWRECT(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
        return result
        
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
    def drawLabel(self, widget, texture):
        renderer = widget.window.renderer
        
        
        if widget.backColor:
            result= True
            color = widget.backColor
        else:
            result = False
            color = self._shema["LABEL_BACKGROUND"]
    
        ##PYSDL2_DRAWRECTFILLED(renderer,texture,color.rgba,(p[0],p[1],widget.width,widget.height))
        

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
        
        ## draw background
        PYSDL2_DRAWRECTFILLED(renderer,texture,color.rgba,r)
        
                
        PYSDL2_RENDER_COPY1(renderer,texture,tx,r,r)
        
        PYSDL2_DESTROYTEXTURE( tx )

        ## draw border
        if widget.borderColor:
            color = widget.borderColor
        else:
            color = self._shema["LABEL_BORDER"]
        
        PYSDL2_DRAWRECT(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
        
        return None
            
    ########################################################
    ##
    ##   CHECKBOX
    ##
    ########################################################
        
    ### Is called before the child objects are drawn.
    ##  So, it is used to draw the background.
    ## 
    def drawCheckboxBeforeChildren(self, widget, texture):
        renderer = widget.window.renderer
        
        if widget.backColor:
            result= True
            color = widget.backColor
        else:
            result = False
            color = self._shema["CHECKBOX_BACKGROUND"]
        
        PYSDL2_DRAWRECTFILLED(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
                
        state = widget.state

        if state == ButtonStates.OVER:
            if widget.checkboxBackColorCheckedOver:
                result= True
                color = widget.checkboxBackColorCheckedOver
            else:
                result = False
                color = self._shema["CHECKBOX_CHECKBOX_OVER_BACKGROUND"] 
        elif state == ButtonStates.DOWN:
            if widget.checkboxBackColorCheckedDown:
                result= True
                color = widget.checkboxBackColorCheckedDown
            else:
                result = False
                color = self._shema["CHECKBOX_CHECKBOX_DOWN_BACKGROUND"] 
        elif state == ButtonStates.CHECKED:
            if widget.checkboxBackColorCheckedChecked:
                result= True
                color = widget.checkboxBackColorCheckedChecked
            else:
                result = False
                color = self._shema["CHECKBOX_CHECKBOX_CHECKED_BACKGROUND"] 
        else:
            if widget.checkboxBackColorCheckedNormal:
                result= True
                color = widget.checkboxBackColorCheckedNormal
            else:
                result = False
                color = self._shema["CHECKBOX_CHECKBOX_NORMAL_BACKGROUND"] 
                    
        r = (0,widget.height/2-8,16,16)
        PYSDL2_DRAWRECTFILLED(renderer,texture,color.rgba,r)   
        
        if widget.checkboxBorderColor:
            result= True
            color = widget.checkboxBorderColor
        else:
            result = False
            color = self._shema["CHECKBOX_CHECKBOX_BORDER"]

        PYSDL2_DRAWRECT(renderer,texture,color.rgba,r)
        ## TODO: If checked we draw a symbol on it
    
        return result
    ### Is called after the child objects are drawn.
    ##  So it is used to draw everything that has to be
    ##  top most like border
    ##
    def drawCheckboxAfterChildren(self, widget, texture):
        renderer = widget.window.renderer
        
        if widget.backColor:
            result= True
            color = widget.backColor
        else:
            result = False
            color = self._shema["CHECKBOX_BORDER"]

        PYSDL2_DRAWRECT(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
        return result
    
    ########################################################
    ##
    ##   SPACER
    ##
    ########################################################
    
    ### Is called to draw a spacer.
    ##
    ##
    def drawSpacer(self, widget, texture):
        renderer = widget.window.renderer
        
        if widget.backColor:
            result= True
            color = widget.backColor
        else:
            result = False
            color = self._shema["SPACER_BACKGROUND"]
        
        PYSDL2_DRAWRECTFILLED(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
        return result

    ########################################################
    ##
    ##   SCROLLNAVIGATOR
    ##
    ########################################################        
    
    ### Is called before the child objects are drawn.
    ##  So, it is used to draw the background.
    ## 
    def drawScrollNavigatorBeforeChildren(self, widget, texture):
        renderer = widget.window.renderer
        
        if widget.backColor:
            result= True
            color = widget.backColor
        else:
            result = False
            color = self._shema["SCROLLNAVIGATOR_BACKGROUND"]
        
        PYSDL2_DRAWRECTFILLED(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
        return result
    
    ### Is called after the child objects are drawn.
    ##  So it is used to draw everything that has to be
    ##  top most like border
    ##
    def drawScrollNavigatorAfterChildren(self, widget, texture):
        renderer = widget.window.renderer
        
        if widget.borderColor:
            result= True
            color = widget.borderColor
        else:
            result = False
            color = self._shema["SCROLLNAVIGATOR_BORDER"]
        
        PYSDL2_DRAWRECT(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
        return result    
        
    ########################################################
    ##
    ##   IMAGE
    ##
    ########################################################        
    
    ### Is called before the child objects are drawn.
    ##  So, it is used to draw the background.
    ## 
    def drawImage(self, widget, texture):
        renderer = widget.window.renderer
        
        
        if widget.backColor:
            result= True
            color = widget.backColor
        else:
            result = False
            color = self._shema["IMAGE_BACKGROUND"]
        
        PYSDL2_DRAWRECTFILLED(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
        
        ## Draw image
        img = self._lib.getImage(renderer,widget.file,widget.width,widget.height)
        r = (0,0,widget.width,widget.height)
        PYSDL2_RENDER_COPY1(renderer,texture,img,r,r)        
        
        if widget.borderColor:
            result= True
            color = widget.borderColor
        else:
            result = False
            color = self._shema["IMAGE_BORDER"]
        
        PYSDL2_DRAWRECT(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
        return result
        
    ########################################################
    ##
    ##   TEXTFIELD
    ##
    ########################################################        
    
    ### Is called before the child objects are drawn.
    ##  So, it is used to draw the background.
    ## 
    def drawTextFieldBeforeChildren(self, widget, texture):
        renderer = widget.window.renderer
        
        if widget.backColor:
            result= True
            color = widget.backColor
        else:
            result = False
            color = self._shema["TEXTFIELD_BACKGROUND"]
        
        p = widget.position
        
        PYSDL2_DRAWRECTFILLED(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
                
        tx = widget.font.render(
            renderer,
            widget.value,
            widget.color
        )
        
        PYSDL2_GETTEXTURESIZE(tx,r)
        
        r = (r[0],r[1],min(r[2],widget.width),min(r[3],widget.height))
            
        PYSDL2_RENDER_COPY1(renderer,texture,tx,(0,0,r[2],r[3]),r)
        
        PYSDL2_DESTROYTEXTURE( tx )  

        ## TODO: Draw the selection box
        
        ## TODO: Draw the cursor
        if widget.cursorVisible:
            pos = widget.getCursorPosition()
            cb = (pos,0,2,widget.height)
            PYSDL2_DRAWRECTFILLED(renderer,texture,Color(255,0,0,255).rgba,cb)


              
        ## Draw bordertime



        if widget.borderColor:
            result= True
            color = widget.borderColor
        else:
            result = False
            color = self._shema["TEXTFIELD_BORDER"]
        
        PYSDL2_DRAWRECT(renderer,texture,color.rgba,(0,0,widget.width,widget.height))
        return result
    