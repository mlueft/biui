import sys

sys.path.append('./')

import math
import time
import biui

def init():
    
    biui.init()
    biui.setThemeFolder("./../themes")
    biui.selectTheme("blocks")
    initWindow(10)
    ##initWindow(190)
    ##initWindow(190+180)
    
def initWindow(x = 0):
    ###############################################
    ##                                       WINDOW
    ###############################################
    wnd = biui.Window(170,480)
    wnd.x = x
    wnd.y = 200
    
    ##
    ## Buttons
    ##
    for i in range(1):
        button0 = biui.Button()
        ##button0.onMouseUp.add(_test.upHandler)
        button0.x = 10
        button0.y = 100+i*45
        button0.width = 150
        button0.height = 40
        button0.label.font.size = 25
        button0.label.color = biui.Color(200,200,200)
        button0.name = "test"+str(i)
        wnd.addChild(button0)
        
def main():
    init()
    ##
    ## Temporary main loop
    ##
    while biui.main():
        time.sleep(0.1)
        pass

if __name__ == '__main__':
    main()
    
print("fertig")   