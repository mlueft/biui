import sys,os

sys.path.append('./')

import math
import biui
import time
from biui.Widgets import Window,Pane
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
    wnd = Window(1024,768)

    ##
    ## Panes
    ##
    startX = 100
    startY = 100
    parent = wnd
    for i in range(10):
        w = Pane()
        ##button0.onMouseUp.add(_test.upHandler)
        w.x = 30
        w.y = 30
        w.width = 200
        w.height = 200
        parent.addChild(w)
        parent = w
        
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