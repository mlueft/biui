import sys,os
from biui.Color import Color

sys.path.append('./')

import math
import biui
import time
from biui.Widgets import Window,ContainerWidget,Pane, Label

def paneResize(ev):
    ##print("W")
    pass
    
def init():
    
    biui.init()
    biui.setThemeFolder(
        os.path.abspath(
            os.path.join(os.getcwd(),"../themes")
        )
    )
    
    biui.selectTheme("blocks")
    
    ###############################################
    ##                                       WINDOW
    ###############################################
    wnd = Window(640,480)
    wnd.name = "window"
    wnd.x = 500
    wnd.y = 500

    ##
    ## Pane
    ##
    pane = Pane()
    pane.name = "Pane"
    pane.x = 100
    pane.y = 100
    pane.width = 200
    pane.height = 200
    pane.onResized.add(paneResize)
    wnd.addChild(pane)
    
    label = Label()
    label.name = "label"
    label.x = 00
    label.y = 100
    label.text = "HHH"
    label.borderColor = Color(255,255,255)
    pane.addChild(label)
        
def main():
    init()
    ##
    ## Temporary main loop
    ##
    while biui.main():
        ##sf.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))
        pass
    

if __name__ == "__main__":
    main()