import sys,os

sys.path.append('./')

import math
import time
import biui
from biui.Widgets import Button,Window

def createButton():
    result = Button()

    result.onTextInput.add(hndOnTextInput)
    result.onKeyUp.add(hndOnKeyUp)
    result.onKeyDown.add(hndOnKeyDown)
    result.onMouseMove.add(hndOnMouseMove)
    result.onMouseLeave.add(hndOnMouseLeave)
    result.onMouseEnter.add(hndOnMouseEnter)
    result.onMouseWheel.add(hndOnMouseWheel)
    result.onMouseUp.add(hndOnMouseUp)    
    result.onMouseDown.add(hndOnMouseDown)
    result.onMouseClick.add(hndOnMouseClick)
    
    result.onBeforeDraw.add(hndOnBeforeDraw)
    result.onAfterDraw.add(hndOnAfterDraw)
    result.onFocus.add(hndOnFocus)
    result.onFocusLost.add(hndOnFocusLost)
    
    result.onResized.add(hndOnResized)
    result.onGotAdded.add(hndOnGotAdded)
    result.onGotRemoved.add(hndOnGotRemoved)
    
    result.onChildAdded.add(hndOnChildAdded)
    result.onChildRemoved.add(hndOnChildRemoved)
    
    result.onScrollPositionChanged.add(hndOnScrollPositionChanged)
    
    return result

def hndOnTextInput(ev):
    print("hndOnTextInput")

def hndOnKeyUp(ev):
    print("hndOnKeyUp")

def hndOnKeyDown(ev):
    print("hndOnKeyDown")
    
def hndOnMouseMove(ev):
    print("hndOnMouseMove")
    
def hndOnMouseLeave(ev):
    print("hndOnMouseLeave")

def hndOnMouseEnter(ev):
    print("hndOnMouseEnter")
    
def hndOnMouseWheel(ev):
    print("hndOnMouseWheel")

def hndOnMouseUp(ev):
    print("hndOnMouseUp")
    
def hndOnMouseDown(ev):
    print("hndOnMouseDown")
    
def hndOnMouseClick(ev):
    print("hndOnMouseClick")
    
def hndOnBeforeDraw(ev):
    print("hndOnBeforeDraw")
    
def hndOnAfterDraw(ev):
    print("hndOnAfterDraw")
    
def hndOnFocus(ev):
    print("hndOnFocus")
    
def hndOnFocusLost(ev):
    print("hndOnFocusLost")
    
def hndOnResized(ev):
    print("hndOnResized")
    
def hndOnGotAdded(ev):
    print("hndOnGotAdded")
    
def hndOnGotRemoved(ev):
    print("hndOnGotRemoved")
    
def hndOnChildAdded(ev):
    print("hndOnChildAdded")
    
def hndOnChildRemoved(ev):
    print("hndOnChildRemoved")
    
def hndOnScrollPositionChanged(ev):
    print("hndOnScrollPositionChanged")
    
def init():
    
    biui.init()
    biui.setThemeFolder(
        os.path.abspath(
            os.path.join(os.getcwd(),"../themes")
        )
    )
    
    biui.selectTheme("blocks")
    initWindow(10)
    ##initWindow(190)
    ##initWindow(190+180)
    
def initWindow(x = 0):
    ###############################################
    ##                                       WINDOW
    ###############################################
    wnd = Window(170,480)
    wnd.x = x
    wnd.y = 200
    
    ##
    ## Buttons
    ##
    for i in range(1):
        button0 = createButton()
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