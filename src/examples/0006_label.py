import sys

sys.path.append('./')

import math
import biui
import time

def main():
    
    biui.init()
    biui.setThemeFolder("../themes")
    biui.addFontFolder("../fonts")
    
    ################################################
    ###                                       WINDOW
    ################################################
    wnd = biui.Window(800,600)
    
    lbl = biui.Label()
    lbl.value = "-------------------hello world!-------------------"
    lbl.x = -100
    lbl.y = 10
    lbl.font.size = 50
    lbl.alignment = biui.Alignment.ABSOLUTE
    lbl.color = biui.Color(255,255,0,255)
    
    wnd.addChild(lbl)
        

    while biui.main():
        time.sleep(0.2)
    
if __name__ == "__main__":
    main()