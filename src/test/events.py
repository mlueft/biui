#include "biui.inc"

import time
import sys
import os
import random

print( os.environ["PYTHONPATH"] )

import biui
from biui.Events import EventPhase
from biui.Enum import Alignment
from biui.Color import Color

from biui.Widgets import Window,Button,Menubar,MenuItem,Pane,Progressbar,NumberSlider
from biui.Widgets import FlexGrid,FlexPane,Checkbox,ToggleButton,Label,Image,ButtonGroup,TextField
from biui.Widgets import ScrollNavigator, TabPane, TabControl


events = {}
    
def createWidgetSubject(subject = None):
    global events

    events["hndOnMouseMove"] = { "value": 0, "widget":None }
    events["hndOnMouseLeave"] = { "value": 0, "widget":None }
    events["hndOnMouseEnter"] = { "value": 0, "widget":None }
    events["hndOnMouseWheel"] = { "value": 0, "widget":None }
    events["hndOnMouseUp"] = { "value": 0, "widget":None }
    events["hndOnMouseDown"] = { "value": 0, "widget":None }
    events["hndOnMouseClick"] = { "value": 0, "widget":None }
    
    events["hndOnTextInput"] = { "value": 0, "widget":None }
    events["hndOnKeyUp"] = { "value": 0, "widget":None }
    events["hndOnKeyDown"] = { "value": 0, "widget":None }
    
    events["hndOnFocus"] = { "value": 0, "widget":None }
    events["hndOnFocusLost"] = { "value": 0, "widget":None }
    events["hndOnShortcut"] = { "value": 0, "widget":None }
    
    events["hndOnResized"] = { "value": 0, "widget":None }
    events["hndOnGotAdded"] = { "value": 0, "widget":None }
    events["hndOnGotRemoved"] = { "value": 0, "widget":None }
    
    events["hndOnBeforeRender"] = { "value": 0, "widget":None }
    events["hndOnAfterRender"] = { "value": 0, "widget":None }
    
    if subject == None:
        subject = Button()
    
    subject.x = 100
    subject.y = 100
    
    subject.onMouseMove.add( hndOnMouseMove )
    subject.onMouseLeave.add( hndOnMouseLeave )
    subject.onMouseEnter.add( hndOnMouseEnter )
    subject.onMouseWheel.add( hndOnMouseWheel )
    subject.onMouseUp.add( hndOnMouseUp )
    subject.onMouseDown.add( hndOnMouseDown )
    subject.onMouseClick.add( hndOnMouseClick )
    
    subject.onTextInput.add( hndOnTextInput )
    subject.onKeyUp.add( hndOnKeyUp )
    subject.onKeyDown.add( hndOnKeyDown )
    
    subject.onFocus.add( hndOnFocus )
    subject.onFocusLost.add( hndOnFocusLost )
    subject.onShortcut.add( hndOnShortcut )
    
    subject.onResized.add( hndOnResized )
    subject.onGotAdded.add( hndOnGotAdded )
    subject.onGotRemoved.add( hndOnGotRemoved )
    
    ##subject.onBeforeRender.add( hndOnBeforeRender )
    ##subject.onAfterRender.add( hndOnAfterRender )

    return subject
FUNCTIONEND

def createContainerWidgetSubject(subject = None):
    global events

    events["hndOnChildAdded"] = { "value": 0, "widget":None }
    events["hndOnChildRemoved"] = { "value": 0, "widget":None }
    events["hndOnScrollPositionChanged"] = { "value": 0, "widget":None }
    events["hndOnScrollSizeChanged"] = { "value": 0, "widget":None }
    
    if subject == None:
        subject = ContainerWidget()
        createWidgetSubject(subject)
        
    subject.x = 100
    subject.y = 100
    
    subject.onChildAdded.add( hndOnChildAdded )
    subject.onChildRemoved.add( hndOnChildRemoved )
    subject.onScrollPositionChanged.add( hndOnScrollPositionChanged )
    subject.onScrollSizeChanged.add( hndOnScrollSizeChanged )
    return subject
FUNCTIONEND

def createButtonGroupWidgetSubject(subject = None):
    global events

    events["hndOnChanged"] = { "value": 0, "widget":None }
    
    if subject == None:
        subject = ContainerWidget()
    
    subject.x = 100
    subject.y = 100
    
    subject.onChanged.add( hndOnChanged )

    return subject
FUNCTIONEND

##
## WIDGET
##

def hndOnMouseMove(ev):
    global events
    key = "hndOnMouseMove"
    print(key)
    events[key]["value"] += 1
    redrawSidePane()
FUNCTIONEND

def hndOnMouseLeave(ev):
    global events
    key = "hndOnMouseLeave"
    print(key)
    events[key]["value"] += 1
    redrawSidePane()
FUNCTIONEND

def hndOnMouseEnter(ev):
    global events
    key = "hndOnMouseEnter"
    print(key)
    events[key]["value"] += 1
    redrawSidePane()
FUNCTIONEND

def hndOnMouseWheel(ev):
    global events
    key = "hndOnMouseWheel"
    print(key)
    events[key]["value"] += 1
    redrawSidePane()
FUNCTIONEND

def hndOnMouseUp(ev):
    global events
    key = "hndOnMouseUp"
    print(key)
    events[key]["value"] += 1
    redrawSidePane()
FUNCTIONEND

def hndOnMouseDown(ev):
    global events
    key = "hndOnMouseDown"
    print(key)
    events[key]["value"] += 1
    redrawSidePane()
FUNCTIONEND

def hndOnMouseClick(ev):
    global events
    key = "hndOnMouseClick"
    print(key)
    events[key]["value"] += 1
    redrawSidePane()
FUNCTIONEND

def hndOnTextInput(ev):
    global events
    key = "hndOnTextInput"
    print(key)
    events[key]["value"] += 1
    redrawSidePane()
FUNCTIONEND

def hndOnKeyUp(ev):
    global events
    key = "hndOnKeyUp"
    print(key)
    events[key]["value"] += 1
    redrawSidePane()
FUNCTIONEND

def hndOnKeyDown(ev):
    global events
    key = "hndOnKeyDown"
    print(key)
    events[key]["value"] += 1
    redrawSidePane()
FUNCTIONEND

def hndOnFocus(ev):
    global events
    key = "hndOnFocus"
    print(key)
    events[key]["value"] += 1
    redrawSidePane()
FUNCTIONEND

def hndOnFocusLost(ev):
    global events
    key = "hndOnFocusLost"
    print(key)
    events[key]["value"] += 1
    redrawSidePane()
FUNCTIONEND

def hndOnShortcut(ev):
    global events
    key = "hndOnShortcut"
    print(key)
    events[key]["value"] += 1
    redrawSidePane()
FUNCTIONEND

def hndOnResized(ev):
    global events
    key = "hndOnResized"
    print(key)
    events[key]["value"] += 1
    redrawSidePane()
FUNCTIONEND

def hndOnGotAdded(ev):
    global events
    key = "hndOnGotAdded"
    print(key)
    events[key]["value"] += 1
    redrawSidePane()
FUNCTIONEND

def hndOnGotRemoved(ev):
    global events
    key = "hndOnGotRemoved"
    print(key)
    events[key]["value"] += 1
    redrawSidePane()
FUNCTIONEND

def hndOnBeforeRender(ev):
    global events
    key = "hndOnBeforeRender"
    print(key)
    events[key]["value"] += 1
    redrawSidePane()
FUNCTIONEND

def hndOnAfterRender(ev):
    global events
    key = "hndOnAfterRender"
    print(key)
    events[key]["value"] += 1
    redrawSidePane()
FUNCTIONEND

##
## CONTAINERWIDGET
##

def hndOnChildAdded(ev):
    global events
    key = "hndOnChildAdded"
    print(key)
    events[key]["value"] += 1
    redrawSidePane()
FUNCTIONEND

def hndOnChildRemoved(ev):
    global events
    key = "hndOnChildRemoved"
    print(key)
    events[key]["value"] += 1
    redrawSidePane()
FUNCTIONEND

def hndOnScrollPositionChanged(ev):
    global events
    key = "hndOnScrollPositionChanged"
    print(key)
    events[key]["value"] += 1
    redrawSidePane()
def hndOnScrollSizeChanged(ev):
    global events
    key = "hndOnScrollSizeChanged"
    print(key)
    events[key]["value"] += 1
    redrawSidePane()
FUNCTIONEND

##
## BUTTONGROUP
##
def hndOnChanged(ev):
    global events
    key = "hndOnChanged"
    print(key)
    events[key]["value"] += 1
    redrawSidePane()
FUNCTIONEND    
    
    
def createSidePane():
    global events
    subject = Pane()
    
    y = 10
    
    for k,v in events.items():
        print(k,v)
        l = Label()
        l.x = 10
        l.y = y
        l.value = k
        subject.addChild(l)
        
        lv = Label()
        lv.x = 200
        lv.y = y
        lv.value = v["value"]
        subject.addChild(lv)
        v["widget"] = lv
                 
        y += 20
    
    return subject

def redrawSidePane():
    for k,v in events.items():
        v["widget"].value = v["value"]

def createGUI():
    wnd = Window(1024,768)
    wnd.title = "BIUI - Demo app - Mouse interaction"
    wnd.x = 200
    wnd.y = 100
    wnd.layoutManager.columnWidths = [300,0]
    wnd.rowHeights = [0]
    
    contentPane = Pane()
    ##contentPane.backColor = Color(0,255,0)
    contentPane.alignment = Alignment.FILL
    wnd.addChild(contentPane,1,0)

    subject = createWidgetSubject()

    sidePane = createSidePane()
    ##sidePane.backColor = Color(255,0,0)
    sidePane.alignment = Alignment.FILL
    wnd.addChild(sidePane,0,0)

    contentPane.addChild(subject)
        
def init():

    biui.init()
    biui.setThemeFolder(
        os.path.abspath(
            os.path.join(os.getcwd(),"./themes")
        )
    )
    
    biui.selectTheme("blocks")
    ##biui.selectTheme("default")
    createGUI()
            
def main():
    init()
    
    while biui.main():
        time.sleep(0.01)
        pass

if __name__ == '__main__':
    main()
    
biui.quit()
