import os
import math
import time
import biui
from biui.Widgets import Button,Window,ContainerWidget,ScrollNavigator, Pane
from biui.Enum import Alignment

pane = None

def init():
    biui.init()
    biui.setThemeFolder(
        os.path.abspath(
            os.path.join(os.getcwd(),"../themes")
        )
    )
    biui.selectTheme("blocks")
    
def initWindow(x=0,y=0):
    wnd = Window(1024,768)
    wnd.x = x
    wnd.y = y
    
    pane = Pane()
    pane.x = 100
    pane.y = 100
    pane.width = 400
    pane.height = 400
    pane.verticalScrollbar = True
    pane.horizontalScrollbar = True
    
    wnd.addChild(pane)
    
    button = Button()
    button.value = "TL"
    button.x = 0
    button.y = 0
    button.width = 200
    button.height = 200
    button.borderColor = biui.Color(255,255,255)
    pane.addChild(button)
    
    button = Button()
    button.value = "BR"
    button.x = 380
    button.y = 460
    pane.addChild(button)
    
def initWindow0(x=0,y=0):
    global pane

    wnd = Window(1024,768)
    wnd.x = x
    wnd.y = y

    ##pane = biui.Pane()
    pane = ContainerWidget()
    pane.x = 10
    pane.y = 200
    pane.width = 600
    pane.height = 500
    pane.alignment = Alignment.FILL
    ##pane.verticalScrollbar = True
    ##pane.horizontalScrollbar = True
    wnd.addChild(pane,0,1)
    
    sn = ScrollNavigator()
    sn.width = 150
    sn.height = 150
    sn.x = 10
    sn.y = 10
    sn.alignment = Alignment.FILL
    ##pane.connectScrollNavigator(sn)
    sn.connectPane(pane)
    wnd.addChild(sn,0,0)


    ##return
    b = Button()
    b.value = "TL"
    b.width = b.height = 50
    b.x = 0
    b.y = 0
    pane.addChild(b)

    b = Button()
    b.value = "TR"
    b.width = b.height = 50
    b.x = 3000-50
    b.y = 0
    pane.addChild(b)
    
    b = Button()
    b.value = "BR"
    b.width = b.height = 50
    b.x = 1000-50
    b.y = 1000-50
    pane.addChild(b)

    b = Button()
    b.value = "BL"
    b.width = b.height = 50
    b.x = 0
    b.y = 1000-50
    pane.addChild(b)
    
    b = Button()
    b.value = "C"
    b.width = b.height = 50
    b.x = 300
    b.y = 300
    pane.addChild(b)
        

def main():
    init()
    initWindow(800,200)
    
    ##
    ## Temporary main loop
    ##
    while biui.main():
        time.sleep(0.05)
        pass

if __name__ == '__main__':
    main()
    
print("fertig")   