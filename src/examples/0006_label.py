import sys,os

sys.path.append('./')

import math
import biui
import time
from biui.Widgets import Window,Label
from biui.Enum import Alignment
from biui import Color

wnd = None

def createLabel():
    result = Label()

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
    
    
def init():
    biui.init()
    biui.setThemeFolder(
        os.path.abspath(
            os.path.join(os.getcwd(),"../themes")
        )
    )
    
    biui.selectTheme("blocks")
    biui.addFontFolder("../fonts")
    
    ################################################
    ###                                       WINDOW
    ################################################
    wnd = Window(800,600)
    
    lbl = createLabel()
    lbl.value = "--"
    lbl.x = 100
    lbl.y = 210
    lbl.font.size = 50
    lbl.alignment = Alignment.ABSOLUTE
    lbl.color = biui.Color(255,255,0,255)
    wnd.addChild(lbl)
        
    return

    label = createLabel()
    label.backColor = Color(0,0,0)
    label.value = "hallo"
    label.x = 100
    label.y = 100
    wnd.addChild(label)

    label = createLabel()
    label.backColor = Color(0,0,0)
    label.value = "hallo welt"
    label.x = 100
    label.y = 140
    wnd.addChild(label)

    label = createLabel()
    label.backColor = Color(0,0,0)
    label.value = "hallo welt hallo welt hallo welt hallo welt hallo welt!"
    label.x = 100
    label.y = 180
    wnd.addChild(label)

    label = createLabel()
    label.autoSize = False
    label.backColor = Color(0,0,0)
    label.value = "hallo welt hallo welt hallo welt hallo welt hallo welt!"
    label.x = 100
    label.y = 220
    label.width = 120
    label.height = 125
    wnd.addChild(label)
        
def main():
    init()
    while biui.main():
        time.sleep(0.2)
    
if __name__ == "__main__":
    main()