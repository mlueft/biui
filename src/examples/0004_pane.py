import sys

sys.path.append('./../')

import math
import biui
import time
   
def paneResize(ev):
    ##print("W")
    pass
    
def init():
    
    biui.init()
    biui.setThemeFolder("../../themes")
    
    ###############################################
    ##                                       WINDOW
    ###############################################
    wnd = biui.Window(640,480)

    ##
    ## Pane
    ##
    pane = biui.Pane()
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