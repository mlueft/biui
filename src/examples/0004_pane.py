import sys,os

sys.path.append('./')

import math
import biui
import time
from biui.Widgets import Window,Pane
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

    ##
    ## Pane
    ##
    pane = Pane()
    pane.x = 100
    pane.y = 100
    pane.width = 200
    pane.height = 200
    pane.onResized.add(paneResize)
    wnd.addChild(pane)
    
        
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