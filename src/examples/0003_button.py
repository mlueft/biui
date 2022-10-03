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
    wnd = biui.Window(640,480)

    ##
    ## Buttons
    ##
    for i in range(10):
        button0 = biui.Button()
        ##button0.onMouseUp.add(_test.upHandler)
        button0.x = 100
        button0.y = 100+i*45
        button0.width = 150
        button0.height = 40
        button0.label.font.size = 25
        button0.label.color = (200,200,200)
        wnd.addChild(button0)
        
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