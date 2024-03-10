import sys,os

sys.path.append('./')

import math
import biui
import time
from biui.Widgets import Window,NumberSlider

def init():
    
    biui.init()
    biui.setThemeFolder(
        os.path.abspath(
            os.path.join(os.getcwd(),"../themes")
        )
    )
    
    biui.selectTheme("blocks")    
    ###############################################
    ##                                       WINDOW
    ###############################################
    wnd = Window(640,480)
    wnd.x = 200
    wnd.y = 100
    ##
    ## Buttons
    ##

    slider = NumberSlider()
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
        slider = NumberSlider()
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
        
        slider = NumberSlider()
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
        time.sleep(0.1)
        pass

if __name__ == '__main__':
    main()

    
print("fertig")   