import sys

sys.path.append('./')

import math
import biui
import time
   
def init():
    
    biui.init()
    biui.setThemeFolder("../themes")
    
    ###############################################
    ##                                       WINDOW
    ###############################################
    wnd = biui.Window(640,480)
    wnd.x = 200
    wnd.y = 100
    ##
    ## Buttons
    ##

    slider = biui.Progressbar()
    ##button0.onMouseUp.add(_test.upHandler)
    slider.x = 200
    slider.y = 100
    slider.width = 150
    slider.height = 30
    slider.minValue = -100
    slider.maxValue = 100
    slider.value = 10
    slider.label.font.size = 15
    slider.label.color = biui.Color(200,200,200)
    wnd.addChild(slider)
    
    slider = biui.Progressbar()
    ##button0.onMouseUp.add(_test.upHandler)
    slider.x = 200
    slider.y = 150
    slider.width = 150
    slider.height = 30
    slider.minValue = 0
    slider.maxValue = 100
    slider.value = 10
    slider.step = 3
    slider.microStep = 1
    slider.label.font.size = 20
    slider.label.color = biui.Color(200,200,200)
    slider.label.format = "{} %"
    slider.showNavigation = False
    wnd.addChild(slider)
    
    slider = biui.Progressbar()
    ##button0.onMouseUp.add(_test.upHandler)
    slider.x = 200
    slider.y = 200
    slider.width = 150
    slider.height = 30
    slider.minValue = 0
    slider.maxValue = 100
    slider.value = 10
    slider.step = 3
    slider.microStep = 1
    slider.label.font.size = 20
    slider.label.color = biui.Color(200,200,200)
    slider.label.format = "{}"
    slider.showValue = False
    wnd.addChild(slider)
    
def main():
    init()
    ##
    ## Temporary main loop
    ##
    while biui.main():
        time.sleep(1)
        pass

if __name__ == '__main__':
    main()

    
print("fertig")   