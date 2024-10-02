import sys,os
from biui.Color import Color
from biui.Enum import Alignment
from biui.Widgets import Button
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
            os.path.join(os.getcwd(),"./themes")
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

    pane5 = Pane()
    pane5.tooltip  = "fiveth pane"
    pane5.alignment = Alignment.FILL
    pane5.x = 630+320
    pane5.y = 10
    pane5.width = 300
    pane5.height = 300
    pane5.verticalScrollbar = True
    pane5.horizontalScrollbar = True        
    wnd.addChild(pane5)
    
    b = Button()
    b.value = "TL"
    b.width = b.height = 50
    b.x = 0
    b.y = 0
    pane5.addChild(b)

    b = Button()
    b.width = b.height = 50
    b.x = 500-25
    b.y = 500-25
    pane5.addChild(b)
        
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