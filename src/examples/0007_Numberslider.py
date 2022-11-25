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

    slider = biui.NumberSlider()
    slider.name = "Numberslider"
    ##button0.onMouseUp.add(_test.upHandler)
    slider.x = 200
    slider.y = 100
    slider.width = 150
    slider.height = 30
    slider.minValue = -100
    slider.maxValue = 100
    slider.value = 10
    slider.step = 3
    slider.microStep = 1
    slider.label.font.size = 15
    slider.label.color = biui.Color(200,200,200)
    wnd.addChild(slider)
    
    if False:
        slider = biui.NumberSlider()
        ##button0.onMouseUp.add(_test.upHandler)
        slider.x = 200
        slider.y = 160
        slider.width = 150
        slider.height = 30
        slider.minValue = -100
        slider.maxValue = 100
        slider.value = 10
        slider.step = 3
        slider.microStep = 1
        slider.label.font.size = 15
        slider.label.color = biui.Color(200,200,200)
        slider.showNavigation = False
        wnd.addChild(slider)
        
        slider = biui.NumberSlider()
        ##button0.onMouseUp.add(_test.upHandler)
        slider.x = 200
        slider.y = 220
        slider.width = 150
        slider.height = 30
        slider.minValue = -100
        slider.maxValue = 100
        slider.value = 10
        slider.step = 3
        slider.microStep = 1
        slider.label.font.size = 15
        slider.label.color = biui.Color(200,200,200)
        slider.label.format = "{} mm"
        slider.showNavigation = False
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