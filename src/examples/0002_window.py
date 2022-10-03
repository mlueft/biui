import sys

sys.path.append('./../')

import math
import biui
import time
   
def init():
    
    biui.init()
    biui.setThemeFolder("../../themes")
    
    ###############################################
    ##                                       WINDOW
    ###############################################
    wnd = biui.Window(1024,768)
    wnd.title = "Window title!"
    wnd.x = 500
    wnd.y = 0
    wnd.width = 640
    wnd.height = 100
    
    ##wnd.left = 10
    ##wnd.bottom = 10
    ##wnd.right = 10
    ##wnd.top = 10
    
def main():
    init()
    
    ##
    ## Temporary main loop
    ##
    while biui.main():
        ##sf.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))
        pass

    biui.quit()
    
    print("quit application")
    
if __name__ == "__main__":
    main()