#include "biui.inc"

import time
import sys
import os
import random

sys.path.append(os.getcwd()+"/py")

import biui
from biui.Events import EventPhase
from biui.Enum import Alignment
from biui.Color import Color

from biui.Widgets import Window,Button,Menubar,MenuItem,Pane,Progressbar,NumberSlider
from biui.Widgets import FlexGrid,FlexPane,Checkbox,ToggleButton,Label,Image,ButtonGroup,TextField
from biui.Widgets import ScrollNavigator, TabPane, TabControl

sidePane    = None
contentPane = None
content     = None
optionPane  = None
option      = None

childrenFocused = None
childrenPane0 = None
childrenPane1 = None

tabNavigator = None

runner = 0


def createMenu():
    
    ms = Menubar()

    mnu0 = MenuItem()
    mnu0.value = "Datei"
    mnu0.tooltip = "File menu"
    ms.addItem(mnu0)
    
    mnu1 = MenuItem()
    mnu1.value = "New"
    mnu1.tooltip = "New Document"
    mnu0.addItem(mnu1)
    
    mnu1 = MenuItem()
    mnu1.value = "Open"
    mnu1.tooltip = "Open Document"
    mnu0.addItem(mnu1)
    
    mnu2 = MenuItem()
    mnu2.value = "TXT"
    mnu2.tooltip = "Open Document"
    mnu1.addItem(mnu2)
    
    mnu2 = MenuItem()
    mnu2.value = "SVG"
    mnu2.tooltip = "Open Document"
    mnu1.addItem(mnu2)
    
    mnu2 = MenuItem()
    mnu2.value = "PNG"
    mnu2.tooltip = "Open Document"
    mnu1.addItem(mnu2)
    
    mnu2 = MenuItem()
    mnu2.value = "JPG"
    mnu2.tooltip = "Open Document"
    mnu1.addItem(mnu2)
    
    mnu3 = MenuItem()
    mnu3.value = "JPG regular"
    mnu3.tooltip = "Open Document"
    mnu2.addItem(mnu3)
    
    mnu3 = MenuItem()
    mnu3.value = "JPG 2000"
    mnu3.tooltip = "Open Document"
    mnu2.addItem(mnu3)
    
    
    mnu1 = MenuItem()
    mnu1.value = "Save"
    mnu1.tooltip = "Save Document"
    mnu0.addItem(mnu1)
    
    
    
    mnubutton = MenuItem()
    mnubutton.value = "Test"
    mnubutton.tooltip = "Test button"
    ms.addItem(mnubutton)




    mnu0 = MenuItem()
    mnu0.value = "Bearbeiten"
    mnu0.tooltip = "Edit"
    ms.addItem(mnu0)
    
    mnu1 = MenuItem()
    mnu1.value = "Copy"
    mnu1.tooltip = "copy selection"
    mnu0.addItem(mnu1)
    
    mnu1 = MenuItem()
    mnu1.value = "Cut"
    mnu1.tooltip = "cut data"
    mnu0.addItem(mnu1)
    
    mnu1 = MenuItem()
    mnu1.value = "Insert"
    mnu1.tooltip = "insert data"
    mnu0.addItem(mnu1)
                    
    mnu2 = MenuItem()
    mnu2.value = "Insert before"
    mnu2.tooltip = "insert data"
    mnu1.addItem(mnu2)
    
    mnu3 = MenuItem()
    mnu3.value = "as text"
    mnu3.tooltip = "Open Document"
    mnu2.addItem(mnu3)
    
    mnu3 = MenuItem()
    mnu3.value = "as grafik"
    mnu3.tooltip = "Open Document"
    mnu2.addItem(mnu3)
    
    mnu2 = MenuItem()
    mnu2.value = "Insert after"
    mnu2.tooltip = "insert data"
    mnu1.addItem(mnu2)
    
    mnu3 = MenuItem()
    mnu3.value = "as text"
    mnu3.tooltip = "Open Document"
    mnu2.addItem(mnu3)
    
    mnu3 = MenuItem()
    mnu3.value = "as grafik"
    mnu3.tooltip = "Open Document"
    mnu2.addItem(mnu3)
    
        
    mnu2 = MenuItem()
    mnu2.value = "Insert anywhere"
    mnu2.tooltip = "insert data"
    mnu1.addItem(mnu2)
    
    mnu3 = MenuItem()
    mnu3.value = "as text"
    mnu3.tooltip = "Open Document"
    mnu2.addItem(mnu3)
    
    mnu3 = MenuItem()
    mnu3.value = "as grafik"
    mnu3.tooltip = "Open Document"
    mnu2.addItem(mnu3)
    
    return ms
FUNCTIONEND

def createSubject(type="button"):
    
    if type=="label":
        result = Label()
        result.backColor = Color(50,70,50)
        result.value = "Label"
        return result
    
    if type=="button":
        result = Button()
        result.value = "Button"
        return result

    if type=="togglebutton":
        result = ToggleButton()
        result.value = "Button"
        return result
    
    if type=="image":
        result = Image()
        result.file = "./test.jpg"
        return result
FUNCTIONEND

##
## CONTENT PANELS
##

def createContentPaneLabel():
    result = Pane()
    result.alignment = Alignment.FILL
    
    label = Label()
    label.value = "hello world!"
    label.x = 100
    label.y = 100
    result.addChild(label)
    
    label = Label()
    label.backColor = Color(100,100,100)
    label.value = "hello world!"
    label.x = 100
    label.y = 140
    result.addChild(label)
    
    label = Label()
    label.borderColor = Color(255,255,0)
    label.value = "hello world!"
    label.x = 100
    label.y = 180
    result.addChild(label)
    
    label = Label()
    label.color = Color(50,0,0)
    label.value = "hello world!"
    label.x = 100
    label.y = 220
    result.addChild(label)

    label = Label()
    label.color = Color(50,0,0)
    label.value = "10"
    label.format = "{} %"
    label.x = 100
    label.y = 260
    result.addChild(label)

    label = Label()
    label.color = Color(50,0,0)
    label.value = None
    label.format = "{} %"
    label.x = 100
    label.y = 300
    result.addChild(label)
            
    return result

def createContentPanePane():
    
    result = Pane()
    result.alignment = Alignment.FILL
    
    pane = Pane()
    pane.x = 30
    pane.y = 30
    pane.width = 300
    pane.height = 300
    result.addChild(pane)
        
    button = Button()
    button.alignment = Alignment.FILL
    pane.addChild(button)
    
    
    pane = Pane()
    pane.verticalScrollbar = True
    pane.horizontalScrollbar = True
    pane.x = 350
    pane.y = 30
    pane.width = 300
    pane.height = 300
    result.addChild(pane)
    
    button = Button()
    button.alignment = Alignment.FILL
    pane.addChild(button)
    
    
    pane = Pane()
    pane.verticalScrollbar = True
    pane.x = 30
    pane.y = 350
    pane.width = 300
    pane.height = 300
    result.addChild(pane)
    
    button = Button()
    button.alignment = Alignment.FILL
    pane.addChild(button)
    
    
    pane = Pane()
    pane.horizontalScrollbar = True
    pane.x = 350
    pane.y = 350
    pane.width = 300
    pane.height = 300
    result.addChild(pane)
    
    button = Button()
    button.alignment = Alignment.FILL
    pane.addChild(button)
    
    return result
FUNCTIONEND

def createContentPaneButton():
    result = Pane()
    result.alignment = Alignment.FILL
    
    label = Button()
    label.value = "hello world!"
    label.x = 100
    label.y = 100
    result.addChild(label)
    
    label = Button()
    label.backColor = Color(100,100,100)
    label.value = "hello world!"
    label.x = 100
    label.y = 140
    result.addChild(label)
    
    label = Button()
    label.borderColor = Color(255,255,0)
    label.value = "hello world!"
    label.x = 100
    label.y = 180
    result.addChild(label)
    
    label = Button()
    label.label.color = Color(50,0,0)
    label.value = "hello world!"
    label.x = 100
    label.y = 220
    result.addChild(label)

    label = Button()
    label.label.color = Color(50,0,0)
    label.value = "10"
    label.label.format = "{} %"
    label.x = 100
    label.y = 260
    result.addChild(label)

    label = Button()
    label.label.color = Color(50,0,0)
    label.value = None
    label.label.format = "{} %"
    label.x = 100
    label.y = 260
    result.addChild(label)
            
    return result
FUNCTIONEND

def createContentPaneToggleButton():
    result = Pane()
    result.alignment = Alignment.FILL
    
    label = ToggleButton()
    label.value = "hello world!"
    label.x = 100
    label.y = 100
    result.addChild(label)
    
    label = ToggleButton()
    label.backColor = Color(100,100,100)
    label.value = "hello world!"
    label.x = 100
    label.y = 140
    result.addChild(label)
    
    label = ToggleButton()
    label.borderColor = Color(255,255,0)
    label.value = "hello world!"
    label.x = 100
    label.y = 180
    result.addChild(label)
    
    label = ToggleButton()
    label.label.color = Color(50,0,0)
    label.value = "hello world!"
    label.x = 100
    label.y = 220
    result.addChild(label)

    label = ToggleButton()
    label.label.color = Color(50,0,0)
    label.value = "10"
    label.label.format = "{} %"
    label.x = 100
    label.y = 260
    result.addChild(label)
        
    return result
FUNCTIONEND

def createContentPaneButtonGroup():
    result = Pane()
    result.alignment = Alignment.FILL
    
    buttonGroup = ButtonGroup()
    buttonGroup.tooltip = "this is the first button group"
    buttonGroup.x = 20
    buttonGroup.y = 20
    buttonGroup.width = 180
    buttonGroup.height = 260
    buttonGroup.borderColor = Color(50,50,50)
    result.addChild(buttonGroup)
    
    label = ToggleButton()
    label.value = "hello world!"
    label.x = 10
    label.y = 10
    buttonGroup.addChild(label)
    
    label = ToggleButton()
    label.backColor = Color(100,100,100)
    label.value = "hello world!"
    label.x = 10
    label.y = 50
    buttonGroup.addChild(label)
    
    label = ToggleButton()
    label.borderColor = Color(255,255,0)
    label.value = "hello world!"
    label.x = 10
    label.y = 90
    buttonGroup.addChild(label)
    
    label = ToggleButton()
    label.label.color = Color(50,0,0)
    label.value = "hello world!"
    label.x = 10
    label.y = 130
    buttonGroup.addChild(label)

    label = ToggleButton()
    label.label.color = Color(50,0,0)
    label.value = "10"
    label.label.format = "{} %"
    label.x = 10
    label.y = 170
    buttonGroup.addChild(label)
        
        
    buttonGroup = ButtonGroup()
    buttonGroup.tooltip = "this is the second button group"
    buttonGroup.x = 220
    buttonGroup.y = 20
    buttonGroup.width = 180
    buttonGroup.height = 260
    buttonGroup.borderColor = Color(50,50,50)
    result.addChild(buttonGroup)
    
    label = ToggleButton()
    label.value = "hello world!"
    label.x = 10
    label.y = 10
    buttonGroup.addChild(label)
    
    label = ToggleButton()
    label.backColor = Color(100,100,100)
    label.value = "hello world!"
    label.x = 10
    label.y = 50
    buttonGroup.addChild(label)
    
    label = ToggleButton()
    label.borderColor = Color(255,255,0)
    label.value = "hello world!"
    label.x = 10
    label.y = 90
    buttonGroup.addChild(label)
    
    label = ToggleButton()
    label.label.color = Color(50,0,0)
    label.value = "hello world!"
    label.x = 10
    label.y = 130
    buttonGroup.addChild(label)

    label = ToggleButton()
    label.label.color = Color(50,0,0)
    label.value = "10"
    label.label.format = "{} %"
    label.x = 10
    label.y = 170
    buttonGroup.addChild(label)
    
    
    type = "togglebutton"
    
    h = 50
    buttonGroup = ButtonGroup()
    buttonGroup.tooltip = "this is the second button group"
    buttonGroup.x = 420
    buttonGroup.y = 20
    buttonGroup.width = 180
    buttonGroup.height = 260
    buttonGroup.borderColor = Color(50,50,50)
    buttonGroup.layoutManager.rowHeights = [h,h,h, h,h,h, h,h,h, h,h,h ]
    result.addChild(buttonGroup)
    
    for i,v in enumerate(buttonGroup.layoutManager.rowHeights):
        subject = createSubject(type)
        subject.alignment = Alignment.FILL
        buttonGroup.addChild(subject,0,i)
    
    return result
FUNCTIONEND

def createContentPaneTextField():
    result = Pane()
    result.alignment = Alignment.FILL

    textfield = TextField()
    textfield.value = "hello world!"
    textfield.x = 20
    textfield.y = 20
    textfield.width = 200
    textfield.height = 30
    result.addChild(textfield)

    textfield = TextField()
    textfield.value = "same text!"
    textfield.x = 250
    textfield.y = 20
    textfield.width = 200
    textfield.height = 30
    result.addChild(textfield)
    
    textfield0 = TextField()
    textfield0.x = 250
    textfield0.y = 60
    textfield0.width = 200
    textfield0.height = 30
    textfield0.dataComponent = textfield.dataComponent
    result.addChild(textfield0)
    
    return result
FUNCTIONEND

def createContentPaneProgressbar():
    result = Pane()
    result.alignment = Alignment.FILL

    progressbar = Progressbar()
    progressbar.minValue = 0
    progressbar.maxValue = 100
    progressbar.value = 50
    progressbar.x = 20
    progressbar.y = 20
    progressbar.width = 200
    progressbar.height = 30
    result.addChild(progressbar)

    progressbar = Progressbar()
    progressbar.minValue = 0
    progressbar.maxValue = 100
    progressbar.value = 50
    progressbar.label.format = "{} %"
    progressbar.x = 20
    progressbar.y = 60
    progressbar.width = 200
    progressbar.height = 30
    result.addChild(progressbar)

    progressbar = Progressbar()
    progressbar.minValue = 0
    progressbar.maxValue = 100
    progressbar.value = 50
    progressbar.label.format = "{} %"
    progressbar.x = 20
    progressbar.y = 110
    progressbar.width = 200
    progressbar.height = 30
    progressbar.showValue = False
    result.addChild(progressbar)
            
    return result
FUNCTIONEND

def createContentPaneNumberSlider():
    result = Pane()
    result.alignment = Alignment.FILL

    progressbar = NumberSlider()
    progressbar.minValue = 0
    progressbar.maxValue = 100
    progressbar.value = 50
    progressbar.x = 20
    progressbar.y = 20
    progressbar.width = 200
    progressbar.height = 30
    result.addChild(progressbar)

    progressbar = NumberSlider()
    progressbar.showNavigation = False
    progressbar.minValue = 0
    progressbar.maxValue = 100
    progressbar.value = 50
    progressbar.x = 20
    progressbar.y = 80
    progressbar.width = 200
    progressbar.height = 30
    result.addChild(progressbar)

    progressbar = NumberSlider()
    progressbar.minValue = 0
    progressbar.maxValue = 100
    progressbar.value = 50
    progressbar.x = 20
    progressbar.y = 140
    progressbar.width = 200
    progressbar.height = 30
    result.addChild(progressbar)
    
    progressbar = NumberSlider()
    progressbar.allowManualInput = False
    progressbar.minValue = 0
    progressbar.maxValue = 100
    progressbar.value = 50
    progressbar.x = 20
    progressbar.y = 200
    progressbar.width = 200
    progressbar.height = 30
    result.addChild(progressbar)
        
    return result
FUNCTIONEND

def createContentPaneCheckBox():
    result = Pane()
    result.alignment = Alignment.FILL

    progressbar = Checkbox()
    progressbar.value = 50
    progressbar.x = 20
    progressbar.y = 20
    progressbar.width = 200
    progressbar.height = 30
    result.addChild(progressbar)

    return result
FUNCTIONEND

def createContentPaneFlexGrid():
    result = Pane()
    result.alignment = Alignment.FILL

    flexgrid = FlexGrid()
    flexgrid.alignment = Alignment.FILL
    result.addChild(flexgrid)

    flexPane = FlexPane()
    flexgrid.addFlexPane(flexPane)
    return result
FUNCTIONEND

def createContentPaneMenubar():
    result = Pane()
    result.alignment = Alignment.FILL

    menu = createMenu()
    menu.tooltip = "menubar"
    menu.alignment = Alignment.DOCK_TOP
    menu.menuAlignment = Alignment.DOCK_LEFT
    result.addChild(menu)
        
    menu = createMenu()
    menu.tooltip = "menubar"
    menu.alignment = Alignment.DOCK_LEFT
    menu.menuAlignment = Alignment.DOCK_TOP
    result.addChild(menu)
            
    menu = createMenu()
    menu.tooltip = "menubar"
    menu.alignment = Alignment.DOCK_RIGHT
    menu.menuAlignment = Alignment.DOCK_BOTTOM
    result.addChild(menu)
                
    menu = createMenu()
    menu.tooltip = "menubar"
    menu.alignment = Alignment.DOCK_BOTTOM
    menu.menuAlignment = Alignment.DOCK_RIGHT
    result.addChild(menu)
    
    
    pane = Pane()
    pane.backColor = Color(50,50,50)
    pane.x = 130
    pane.y = 130
    pane.width = 350
    pane.height = 350
    result.addChild(pane)

    menu = createMenu()
    menu.tooltip = "menubar"
    menu.alignment = Alignment.DOCK_TOP
    menu.menuAlignment = Alignment.DOCK_LEFT
    pane.addChild(menu)
        
    return result
FUNCTIONEND

def createContentPaneScrollNavigator():
    result = Pane()
    result.alignment = Alignment.FILL

    pane = Pane()
    pane.x = 100
    pane.y = 100
    pane.width = 400
    pane.height = 400
    pane.verticalScrollbar = True
    pane.horizontalScrollbar = True
    
    result.addChild(pane)
    
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

    scrollNavigator = ScrollNavigator()
    pane.connectScrollNavigator(scrollNavigator)
    scrollNavigator.x = 550
    scrollNavigator.y = 150
    scrollNavigator.width = 200
    scrollNavigator.height = 200
    result.addChild(scrollNavigator)
    return result
FUNCTIONEND

def createContentPaneImage():
    
    padding = 50
    
    result = Pane()
    result.alignment = Alignment.FILL


    image = createSubject("image")
    result.addChild(image)
    image.alignment = Alignment.FILL
    
    return result
FUNCTIONEND

def createContentPaneDock(type = "button"):
    
    padding = 50
    
    result = Pane()
    result.layoutManager.columnWidths = [padding,0,padding,0,padding,0,padding,0,padding]
    result.layoutManager.rowHeights   = [padding,0,padding,0,padding,0,padding,0,padding]
    result.alignment = Alignment.FILL


    ##
    ## ROW 0
    ##
    if True:
        pane = Pane()
        pane.alignment = Alignment.FILL
        result.addChild(pane,1,1)
        
        subject = createSubject(type)
        pane.addChild(subject)
        subject.alignment = Alignment.TOP_LEFT
        
        label = Label()
        label.value = "TOP_LEFT"
        label.alignment = Alignment.TOP_CENTER
        result.addChild(label,1,2)
        
        
        pane = Pane()
        pane.alignment = Alignment.FILL
        result.addChild(pane,3,1)
        
        subject = createSubject(type)
        pane.addChild(subject)
        subject.alignment = Alignment.TOP_CENTER
        
        label = Label()
        label.value = "TOP_CENTER"
        label.alignment = Alignment.TOP_CENTER
        result.addChild(label,3,2)
        
        
        
        pane = Pane()
        pane.alignment = Alignment.FILL
        result.addChild(pane,5,1)
        
        subject = createSubject(type)
        pane.addChild(subject)
        subject.alignment = Alignment.TOP_RIGHT    
        
        label = Label()
        label.value = "TOP_RIGHT"
        label.alignment = Alignment.TOP_CENTER
        result.addChild(label,5,2)
        
        
        
        pane = Pane()
        pane.alignment = Alignment.FILL
        result.addChild(pane,7,1)
            
        subject = createSubject(type)
        pane.addChild(subject)
        subject.alignment = Alignment.FILL    
    
        label = Label()
        label.value = "FILL"
        label.alignment = Alignment.TOP_CENTER
        result.addChild(label,7,2)    
    
    ##
    ## ROW 1
    ##    
    if True:
        pane = Pane()
        pane.alignment = Alignment.FILL
        result.addChild(pane,1,3)
        
        subject = createSubject(type)
        pane.addChild(subject)
        subject.alignment = Alignment.CENTER_LEFT
        
        label = Label()
        label.value = "CENTER_LEFT"
        label.alignment = Alignment.TOP_CENTER
        result.addChild(label,1,4)
        
        
            
        pane = Pane()
        pane.alignment = Alignment.FILL
        result.addChild(pane,3,3)
        
        subject = createSubject(type)
        pane.addChild(subject)
        subject.alignment = Alignment.CENTER_CENTER
        
        label = Label()
        label.value = "CENTER_CENTER"
        label.alignment = Alignment.TOP_CENTER
        result.addChild(label,3,4)
        
        
        
        pane = Pane()
        pane.alignment = Alignment.FILL
        result.addChild(pane,5,3)
        
        subject = createSubject(type)
        pane.addChild(subject)
        subject.alignment = Alignment.CENTER_RIGHT
        
        label = Label()
        label.value = "CENTER_RIGHT"
        label.alignment = Alignment.TOP_CENTER
        result.addChild(label,5,4)
        
        
        pane = Pane()
        pane.alignment = Alignment.FILL
        result.addChild(pane,7,3)
        
        subject = createSubject(type)
        pane.addChild(subject)
        subject.alignment = Alignment.ABSOLUTE
        subject.x = 10
        subject.y = 10   
    
        label = Label()
        label.value = "ABSOLUTE"
        label.alignment = Alignment.TOP_CENTER
        result.addChild(label,7,4)
        
        
    ##
    ## ROW 2
    ##    
    if True:
        pane = Pane()
        pane.alignment = Alignment.FILL
        result.addChild(pane,1,5)
        
        subject = createSubject(type)
        pane.addChild(subject)
        subject.alignment = Alignment.BOTTOM_LEFT
        
        label = Label()
        label.value = "BOTTOM_LEFT"
        label.alignment = Alignment.TOP_CENTER
        result.addChild(label,1,6)
        
        
        
        pane = Pane()
        pane.alignment = Alignment.FILL
        result.addChild(pane,3,5)
        
        subject = createSubject(type)
        pane.addChild(subject)
        subject.alignment = Alignment.BOTTOM_CENTER
        
        label = Label()
        label.value = "BOTTOM_CENTER"
        label.alignment = Alignment.TOP_CENTER
        result.addChild(label,3,6)
        
        
        pane = Pane()
        pane.alignment = Alignment.FILL
        result.addChild(pane,5,5)
        
        subject = createSubject(type)
        pane.addChild(subject)
        subject.alignment = Alignment.BOTTOM_RIGHT
        
        label = Label()
        label.value = "BOTTOM_RIGHT"
        label.alignment = Alignment.TOP_CENTER
        result.addChild(label,5,6)
        
        
        
    ##
    ## ROW 3
    ##
    if True:
        pane = Pane()
        pane.alignment = Alignment.FILL
        result.addChild(pane,1,7)
        
        subject = createSubject(type)
        pane.addChild(subject)
        subject.alignment = Alignment.DOCK_LEFT
        
        label = Label()
        label.value = "DOCK_LEFT"
        label.alignment = Alignment.TOP_CENTER
        result.addChild(label,1,8)
        
        
        pane = Pane()
        pane.alignment = Alignment.FILL
        result.addChild(pane,3,7)
        
        subject = createSubject(type)
        pane.addChild(subject)
        subject.alignment = Alignment.DOCK_TOP
        
        label = Label()
        label.value = "DOCK_TOP"
        label.alignment = Alignment.TOP_CENTER
        result.addChild(label,3,8)
        
        
        
        pane = Pane()
        pane.alignment = Alignment.FILL
        result.addChild(pane,5,7)
        
        subject = createSubject(type)
        pane.addChild(subject)
        subject.alignment = Alignment.DOCK_RIGHT
        
        label = Label()
        label.value = "DOCK_RIGHT"
        label.alignment = Alignment.TOP_CENTER
        result.addChild(label,5,8)
        
        
        
        pane = Pane()
        pane.alignment = Alignment.FILL
        result.addChild(pane,7,7)
    
        subject = createSubject(type)
        pane.addChild(subject)
        subject.x = 10
        subject.y = 10
        subject.alignment = Alignment.DOCK_BOTTOM
    
        label = Label()
        label.value = "DOCK_BOTTOM"
        label.alignment = Alignment.TOP_CENTER
        result.addChild(label,7,8)
        
    return result
FUNCTIONEND

def createContentPaneLayoutManager(type = "button"):
    
    padding = 50
    
    result = Pane()
    result.alignment = Alignment.FILL


    ##
    ## ROW 0
    ##
    if True:
        
        type = "button"
        
        h = 50
        pane = Pane()
        pane.verticalScrollbar = True
        pane.horizontalScrollbar = True
        pane.x = 100
        pane.y = 100
        pane.width = 300
        pane.height = 300
        pane.layoutManager.rowHeights = [h,h,h, h,h,h, h,h,h, h,h,h ]
        result.addChild(pane)
        
        for i,v in enumerate(pane.layoutManager.rowHeights):
            subject = createSubject(type)
            subject.alignment = Alignment.FILL
            pane.addChild(subject,0,i)
        
        pane = Pane()
        pane.x = 450
        pane.y = 100
        pane.width = 300
        pane.height = 300
        result.addChild(pane)
        
        subject = createSubject(type)
        pane.addChild(subject)

        
    return result
FUNCTIONEND

def createContentPaneChildren(type = "button"):
    global childrenPane0, childrenPane1
    result = Pane()
    result.alignment = Alignment.FILL

    childrenPane0 = Pane()
    childrenPane0.x = 100
    childrenPane0.y = 100
    childrenPane0.width = 300
    childrenPane0.height = 300
    childrenPane0.verticalScrollbar = True
    childrenPane0.horizontalScrollbar = True
    result.addChild(childrenPane0)
    
    childrenPane1 = Pane()
    childrenPane1.x = 450
    childrenPane1.y = 100
    childrenPane1.width = 300
    childrenPane1.height = 300
    childrenPane1.verticalScrollbar = True
    childrenPane1.horizontalScrollbar = True
    result.addChild(childrenPane1)
           
    return result
FUNCTIONEND

def createContentPaneTabPane(type = "button"):
    global childrenPane0, childrenPane1, tabNavigator
    result = Pane()
    result.alignment = Alignment.FILL
    
    navigator = TabControl()
    navigator.tabWidth = 150
    navigator.tabHeight = 20
    navigator.onTabShown.add(hndTabPaneOnTabShown)
    navigator.onTabHidden.add(hndTabPaneOnTabHidden)
    navigator.onTabChanged.add(hndTabPaneOnTabChanged)
    navigator.alignment = Alignment.FILL
    result.addChild(navigator)
    
    tabNavigator = navigator
    
    return result
FUNCTIONEND


##
## OPTION PANELS
##

def createOptionPaneEmpty():
    result = Pane()
    result.alignment = Alignment.FILL
    result.verticalScrollbar = True
    return result
FUNCTIONEND

def createOptionPaneLabel():
    return createOptionPaneEmpty()
FUNCTIONEND

def createOptionPanePane():
    return createOptionPaneEmpty()
FUNCTIONEND

def createOptionPaneButton():
    return createOptionPaneEmpty()
FUNCTIONEND

def createOptionPaneToggleButton():
    return createOptionPaneEmpty()
FUNCTIONEND

def createOptionPaneButtonGroup():
    return createOptionPaneEmpty()
FUNCTIONEND

def createOptionPaneTextField():
    return createOptionPaneEmpty()
FUNCTIONEND

def createOptionPaneProgressbar():
    return createOptionPaneEmpty()
FUNCTIONEND

def createOptionPaneNumberSlider():
    return createOptionPaneEmpty()
FUNCTIONEND

def createOptionPaneCheckbox():
    return createOptionPaneEmpty()
FUNCTIONEND

def createOptionPaneFlexGrid():
    return createOptionPaneEmpty()
FUNCTIONEND

def createOptionPaneMenubar():
    return createOptionPaneEmpty()
FUNCTIONEND

def createOptionPaneScrollNavigator():
    return createOptionPaneEmpty()
FUNCTIONEND

def createOptionPaneImage():
    return createOptionPaneEmpty()
FUNCTIONEND

def createOptionPaneDock():
    result = createOptionPaneEmpty()
    
    buttonHeight = 25
    result.layoutManager.rowHeights = [10,buttonHeight,buttonHeight,buttonHeight]
    
    row = 1
    button = Button()
    button.alignment = Alignment.FILL
    button.value = "Image"
    button.onMouseClick.add(hndDockOptionImage)
    result.addChild(button,0,row)
    row += 1
    
    button = Button()
    button.alignment = Alignment.FILL
    button.value = "Button"
    button.onMouseClick.add(hndDockOptionButton)
    result.addChild(button,0,row)
    row += 1

    button = Button()
    button.alignment = Alignment.FILL
    button.value = "label"
    button.onMouseClick.add(hndDockOptionLabel)
    result.addChild(button,0,row)
    row += 1
        
    return result
FUNCTIONEND

def createOptionPaneLayoutManager():
    return createOptionPaneEmpty()
FUNCTIONEND

def createOptionPaneChildren():
    result = createOptionPaneEmpty()
    
    buttonHeight = 25
    result.layoutManager.rowHeights = [10,buttonHeight,buttonHeight,buttonHeight,buttonHeight]

    row = 1
    button = Button()
    button.alignment = Alignment.FILL
    button.value = "debug"
    button.onMouseClick.add(hndChildrenOptionDebug)
    result.addChild(button,0,row)
    row += 1
        
    button = Button()
    button.alignment = Alignment.FILL
    button.value = "Add Child"
    button.onMouseClick.add(hndChildrenOptionAdd)
    result.addChild(button,0,row)
    row += 1
    
    button = Button()
    button.alignment = Alignment.FILL
    button.value = "Remove Child"
    button.onMouseClick.add(hndChildrenOptionRemove)
    result.addChild(button,0,row)
    row += 1

    button = Button()
    button.alignment = Alignment.FILL
    button.value = "swap Child"
    button.onMouseClick.add(hndChildrenOptionSwap)
    result.addChild(button,0,row)
    row += 1
        
    return result
FUNCTIONEND

def createOptionPaneTabPane():
    result = createOptionPaneEmpty()
    
    buttonHeight = 25
    result.layoutManager.rowHeights = [10,buttonHeight,buttonHeight,buttonHeight,buttonHeight,buttonHeight]

    row = 1
    button = Button()
    button.alignment = Alignment.FILL
    button.value = "add"
    button.onMouseClick.add(hndTabNavigatorOptionAdd)
    result.addChild(button,0,row)
    row += 1

    button = Button()
    button.alignment = Alignment.FILL
    button.value = "remove tab"
    button.onMouseClick.add(hndTabNavigatorOptionRemove0)
    result.addChild(button,0,row)
    row += 1

    button = Button()
    button.alignment = Alignment.FILL
    button.value = "remove index"
    button.onMouseClick.add(hndTabNavigatorOptionRemove1)
    result.addChild(button,0,row)
    row += 1

    pane = Pane()
    pane.alignment = Alignment.FILL
    pane.layoutManager.columnWidths = [0,0]
    result.addChild(pane,0,row)
    row += 1
    
    button = Button()
    button.alignment = Alignment.FILL
    button.value = "show"
    button.onMouseClick.add(hndTabNavigatorOptionShowTabs)
    pane.addChild(button,0,0)

    
    button = Button()
    button.alignment = Alignment.FILL
    button.value = "hide"
    button.onMouseClick.add(hndTabNavigatorOptionHideTabs)
    pane.addChild(button,1,0)

    pane = Pane()
    pane.alignment = Alignment.FILL
    pane.layoutManager.columnWidths = [0,0]
    result.addChild(pane,0,row)
    row += 1
    
    button = Button()
    button.alignment = Alignment.FILL
    button.value = "prev"
    button.onMouseClick.add(hndTabNavigatorOptionPrevTabs)
    pane.addChild(button,0,0)

    
    button = Button()
    button.alignment = Alignment.FILL
    button.value = "next"
    button.onMouseClick.add(hndTabNavigatorOptionNextTabs)
    pane.addChild(button,1,0)
        

    pane = Pane()
    
    pane.y = row*buttonHeight+10
    pane.x = 40
    pane.width = 90
    pane.height = 90
    
    button = Button();
    button.value = "T"
    button.width = 30
    button.height = 30
    button.x = 30
    button.y = 0
    button.onMouseClick.add(hndTabAlignTOP)
    pane.addChild(button)

    button = Button();
    button.value = "R"
    button.width = 30
    button.height = 30
    button.x = 60
    button.y = 30
    button.onMouseClick.add(hndTabAlignRIGHT)
    pane.addChild(button)
        
    button = Button();
    button.value = "B"
    button.width = 30
    button.height = 30
    button.x = 30
    button.y = 60
    button.onMouseClick.add(hndTabAlignBOTTOM)
    pane.addChild(button)

    button = Button();
    button.value = "L"
    button.width = 30
    button.height = 30
    button.x = 0
    button.y = 30
    button.onMouseClick.add(hndTabAlignLEFT)
    pane.addChild(button)
        
    result.addChild(pane,0,row)
    row += 1
    
    return result
FUNCTIONEND

##
## EVENT HANDLERS
##

def hndTabPaneOnTabHidden(ev):
    print("hndTabPaneOnTabHidden")
FUNCTIONEND

def hndTabPaneOnTabShown(ev):
    print("hndTabPaneOnTabShown")
FUNCTIONEND
    
def hndTabPaneOnTabChanged(ev):
    print("hndTabPaneOnTabChanged")
FUNCTIONEND
    
def hndTabNavigatorOptionAdd(ev):
    global tabNavigator, runner
    
    tab = TabPane()
    tab.name = "tab{}".format(runner)
    
    button = Button()
    button.value = "{}".format(runner)
    button.x = random.uniform(0, 300)
    button.y = random.uniform(0, 300)
    button.width = 200
    button.height = 200
    tab.addChild(button)
    
    tabNavigator.addTab(tab)
    
    runner+=1
FUNCTIONEND
    
def hndTabNavigatorOptionRemove0(ev):
    global tabNavigator
    tabNavigator.removeTab(
        tabNavigator.activeItem
    )
FUNCTIONEND

def hndTabNavigatorOptionRemove1(ev):
    global tabNavigator
    tabNavigator.removeTab(
        tabNavigator.activeTab
    )
FUNCTIONEND

def hndTabNavigatorOptionShowTabs(ev):
    global tabNavigator
    tabNavigator.showNavigation = True
FUNCTIONEND
    
def hndTabNavigatorOptionHideTabs(ev):
    global tabNavigator
    tabNavigator.showNavigation = False
FUNCTIONEND

def hndTabNavigatorOptionPrevTabs(ev):
    global tabNavigator
    tabNavigator.activeTab = max(0,tabNavigator.activeTab-1)
FUNCTIONEND
    
def hndTabNavigatorOptionNextTabs(ev):
    global tabNavigator
    tabNavigator.activeTab = min(tabNavigator.tabCount,tabNavigator.activeTab+1)
FUNCTIONEND
    
def hndTabAlignTOP(ev):
    global tabNavigator
    tabNavigator.tabAlignment = Alignment.DOCK_TOP
FUNCTIONEND
    
def hndTabAlignRIGHT(ev):
    global tabNavigator
    tabNavigator.tabAlignment = Alignment.DOCK_RIGHT
FUNCTIONEND
    
def hndTabAlignBOTTOM(ev):
    global tabNavigator
    tabNavigator.tabAlignment = Alignment.DOCK_BOTTOM
FUNCTIONEND
    
def hndTabAlignLEFT(ev):
    global tabNavigator
    tabNavigator.tabAlignment = Alignment.DOCK_LEFT
FUNCTIONEND
    
def hndDockOptionImage(ev):
    global content
    if content != None:
        contentPane.removeChild(content)
    content = createContentPaneDock("image")
    contentPane.addChild(content)
FUNCTIONEND

def hndDockOptionButton(ev):
    global content
    if content != None:
        contentPane.removeChild(content)
    content = createContentPaneDock("button")
    contentPane.addChild(content)
FUNCTIONEND

def hndDockOptionLabel(ev):
    global content
    if content != None:
        contentPane.removeChild(content)
    content = createContentPaneDock("label")
    contentPane.addChild(content)
FUNCTIONEND
    
def hndChildrenOptionAdd(ev):
    global childrenPane0,childrenPane1,childrenFocused
    
    button = Button()
    button.x = random.uniform(0, 2*childrenPane0.width-10)
    button.y = random.uniform(0, 2*childrenPane0.height-10)
    button.value = int(random.uniform(0,99))
    button.width = 30
    button.height = 30
    button.onMouseClick.add( hndChildrenMouseClick)
    childrenPane0.addChild(button)
    childrenFocused = button
FUNCTIONEND

def hndChildrenOptionRemove(ev):
    global childrenPane0,childrenPane1,childrenFocused
    
    if childrenPane0.hasChild(childrenFocused):
        childrenPane0.removeChild(childrenFocused)
        
    if childrenPane1.hasChild(childrenFocused):
        childrenPane1.removeChild(childrenFocused)
FUNCTIONEND

def hndChildrenOptionSwap(ev):
    global childrenPane0,childrenPane1,childrenFocused
    
    if childrenPane0.hasChild(childrenFocused):
        print("Swap to pane1")
        childrenPane0.removeChild(childrenFocused)
        childrenPane1.addChild(childrenFocused)
        childrenFocused.x = random.uniform(0, 2*childrenPane1.width-10)
        childrenFocused.y = random.uniform(0, 2*childrenPane1.height-10)        
        return
    
    if childrenPane1.hasChild(childrenFocused):
        print("Swap to pane0")
        childrenPane1.removeChild(childrenFocused)
        childrenPane0.addChild(childrenFocused)
        childrenFocused.x = random.uniform(0, 2*childrenPane0.width-10)
        childrenFocused.y = random.uniform(0, 2*childrenPane0.height-10)        
        return
FUNCTIONEND
    
def hndChildrenOptionDebug(ev):
    global childrenPane0,childrenPane1,childrenFocused
    print("children Pane0: {}".format(len(childrenPane0.children)))
    print("children Pane1: {}".format(len(childrenPane1.children)))
    
    if childrenFocused:
        print("focused button parent: {}".format(childrenFocused.parent))
    
    childrenPane0.layoutManager.debug()
    childrenPane1.layoutManager.debug()
    print("---------------------------")
FUNCTIONEND
    
def hndChildrenMouseClick(ev):
    global childrenFocused
    childrenFocused = ev.eventSource
FUNCTIONEND

def hndLabelClick(ev):
    global content, option
    
    if content != None:
        contentPane.removeChild(content)
        
    content = createContentPaneLabel()
    contentPane.addChild(content)

    if option != None:
        sidePane.removeChild(option)
        
    option = createOptionPaneLabel()
    optionPane.addChild(option)
FUNCTIONEND

def hndPaneClick(ev):
    global content, option
    
    if content != None:
        contentPane.removeChild(content)
        
    content = createContentPanePane()
    contentPane.addChild(content)

    if option != None:
        sidePane.removeChild(option)
        
    option = createOptionPanePane()
    optionPane.addChild(option)
FUNCTIONEND

def hndButtonClick(ev):
    global content,option
    
    if content != None:
        contentPane.removeChild(content)
    content = createContentPaneButton()
    contentPane.addChild(content)
    
    if option != None:
        sidePane.removeChild(option)
        
    option = createOptionPaneButton()
    optionPane.addChild(option)
FUNCTIONEND
        
def hndToggleButtonClick(ev):
    global content, option
    
    if content != None:
        contentPane.removeChild(content)
    content = createContentPaneToggleButton()
    contentPane.addChild(content)
    
    if option != None:
        sidePane.removeChild(option)
        
    option = createOptionPaneToggleButton()
    optionPane.addChild(option)
FUNCTIONEND
    
def hndButtonGroupClick(ev):
    global content, option
    
    if content != None:
        contentPane.removeChild(content)
    content = createContentPaneButtonGroup()
    contentPane.addChild(content)
    
    if option != None:
        sidePane.removeChild(option)
        
    option = createOptionPaneButtonGroup()
    optionPane.addChild(option)
FUNCTIONEND
    
def hndTextFieldClick(ev):
    global content, option
    
    if content != None:
        contentPane.removeChild(content)
    content = createContentPaneTextField()
    contentPane.addChild(content)
    
    if option != None:
        sidePane.removeChild(option)
        
    option = createOptionPaneTextField()
    optionPane.addChild(option)
FUNCTIONEND
    
def hndProgressbarClick(ev):
    global content, option
    
    if content != None:
        contentPane.removeChild(content)
    content = createContentPaneProgressbar()
    contentPane.addChild(content)
    
    if option != None:
        sidePane.removeChild(option)
        
    option = createOptionPaneProgressbar()
    optionPane.addChild(option)
FUNCTIONEND
    
def hndNumberSliderClick(ev):
    global content, option
    
    if content != None:
        contentPane.removeChild(content)
    content = createContentPaneNumberSlider()
    contentPane.addChild(content)
    
    if option != None:
        sidePane.removeChild(option)
        
    option = createOptionPaneNumberSlider()
    optionPane.addChild(option)
FUNCTIONEND
    
def hndCheckboxClick(ev):
    global content, option
    
    if content != None:
        contentPane.removeChild(content)
    content = createContentPaneCheckBox()
    contentPane.addChild(content)

    if option != None:
        sidePane.removeChild(option)
        
    option = createOptionPaneCheckbox()
    optionPane.addChild(option)
FUNCTIONEND
    
def hndFlexgridClick(ev):
    global content, option
    
    if content != None:
        contentPane.removeChild(content)
    content = createContentPaneFlexGrid()
    contentPane.addChild(content)

    if option != None:
        sidePane.removeChild(option)
        
    option = createOptionPaneFlexGrid()
    optionPane.addChild(option)
FUNCTIONEND
    
def hndMenubarClick(ev):
    global content, option
    
    if content != None:
        contentPane.removeChild(content)
    content = createContentPaneMenubar()
    contentPane.addChild(content)
       
    if option != None:
        sidePane.removeChild(option)
        
    option = createOptionPaneMenubar()
    optionPane.addChild(option)
FUNCTIONEND
    
def hndScrollnavigatorClick(ev):
    global content, option
    
    if content != None:
        contentPane.removeChild(content)
    content = createContentPaneScrollNavigator()
    contentPane.addChild(content)
    
    if option != None:
        sidePane.removeChild(option)
        
    option = createOptionPaneScrollNavigator()
    optionPane.addChild(option)
FUNCTIONEND
    
def hndImageClick(ev):
    global content, option
    
    if content != None:
        contentPane.removeChild(content)
    content = createContentPaneImage()
    contentPane.addChild(content)
    
    if option != None:
        sidePane.removeChild(option)
        
    option = createOptionPaneImage()
    optionPane.addChild(option)
FUNCTIONEND
    
def hndDockClick(ev):
    global content, option
    
    type="image"
    
    if content != None:
        contentPane.removeChild(content)
    content = createContentPaneDock(type)
    contentPane.addChild(content)
    
    if option != None:
        sidePane.removeChild(option)
        
    option = createOptionPaneDock()
    optionPane.addChild(option)
FUNCTIONEND

def hndLayoutManagerClick(ev):
    global content, option
    
    type="image"
    
    if content != None:
        contentPane.removeChild(content)
    content = createContentPaneLayoutManager(type)
    contentPane.addChild(content)
    
    if option != None:
        sidePane.removeChild(option)
        
    option = createOptionPaneLayoutManager()
    optionPane.addChild(option)
FUNCTIONEND
    
def hndChildrenClick(ev):
    global content, option
    
    type="button"
    
    if content != None:
        contentPane.removeChild(content)
    content = createContentPaneChildren(type)
    contentPane.addChild(content)
    
    if option != None:
        sidePane.removeChild(option)
        
    option = createOptionPaneChildren()
    optionPane.addChild(option)        
FUNCTIONEND
        
def hndTabPaneClick(ev):
    global content, option
    
    type="button"
    
    if content != None:
        contentPane.removeChild(content)
    content = createContentPaneTabPane(type)
    contentPane.addChild(content)
    
    if option != None:
        sidePane.removeChild(option)
        
    option = createOptionPaneTabPane()
    optionPane.addChild(option)
FUNCTIONEND
        
def createGUI():
    global sidePane, contentPane, optionPane
    
    ################################################
    ###                                       WINDOW
    ################################################
    wnd = Window(1024,768)
    wnd.title = "BIUI - Demo app"
    wnd.x = 200
    wnd.y = 100
    
    
    ################################################
    ###                                  MAIN LAYOUT
    ################################################
    sidePane = Pane()
    sidePane.alignment = Alignment.FILL
    sidePane.layoutManager.rowHeights = [500,0]
    
    contentPane = Pane()
    contentPane.alignment = Alignment.FILL
    
    wnd.addChild(sidePane,0,0)
    wnd.addChild(contentPane,1,0)
    wnd.layoutManager.columnWidths = [200,0]
    
    ################################################
    ###                                      SIDEBAR
    ################################################
    if True:
        buttonHeight = 30

        buttonGroup = ButtonGroup()
        buttonGroup.verticalScrollbar = True        
        buttonGroup.layoutManager.rowHeights = [buttonHeight,buttonHeight,buttonHeight,buttonHeight,buttonHeight,buttonHeight,buttonHeight,buttonHeight,buttonHeight,buttonHeight,buttonHeight,buttonHeight,buttonHeight,buttonHeight,buttonHeight,0]
        buttonGroup.alignment = Alignment.FILL
        sidePane.addChild(buttonGroup)
        
        
        if True:
            row = 0
            btn = ToggleButton()
            btn.value = "Pane"
            btn.onMouseClick.add(hndPaneClick)
            btn.alignment = Alignment.FILL
            buttonGroup.addChild(btn,0,row)
            row+=1
            
            btn = ToggleButton()
            btn.value = "Label"
            btn.onMouseClick.add(hndLabelClick)
            btn.alignment = Alignment.FILL
            buttonGroup.addChild(btn,0,row)
            row+=1

            btn = ToggleButton()
            btn.onMouseClick.add(hndButtonClick)
            btn.alignment = Alignment.FILL
            btn.value = "Button"
            btn.alignment = Alignment.FILL
            buttonGroup.addChild(btn,0,row)
            row+=1
            
            btn = ToggleButton()
            btn.onMouseClick.add(hndToggleButtonClick)
            btn.alignment = Alignment.FILL
            btn.value = "ToggleButton"
            buttonGroup.addChild(btn,0,row)
            row+=1
            
            btn = ToggleButton()
            btn.onMouseClick.add(hndButtonGroupClick)
            btn.alignment = Alignment.FILL
            btn.value = "ButtonGroup"
            buttonGroup.addChild(btn,0,row)
            row+=1
            
            btn = ToggleButton()
            btn.onMouseClick.add(hndTextFieldClick)
            btn.alignment = Alignment.FILL
            btn.value = "TextField"
            buttonGroup.addChild(btn,0,row)
            row+=1
            
            btn = ToggleButton()
            btn.onMouseClick.add(hndProgressbarClick)
            btn.alignment = Alignment.FILL
            btn.value = "Progressbar"
            buttonGroup.addChild(btn,0,row)
            row+=1
            
            btn = ToggleButton()
            btn.onMouseClick.add(hndNumberSliderClick)
            btn.alignment = Alignment.FILL
            btn.value = "Numberslider"
            buttonGroup.addChild(btn,0,row)
            row+=1
            
            btn = ToggleButton()
            btn.onMouseClick.add(hndCheckboxClick)
            btn.alignment = Alignment.FILL
            btn.value = "Checkbox"
            buttonGroup.addChild(btn,0,row)
            row+=1
            
            btn = ToggleButton()
            btn.onMouseClick.add(hndFlexgridClick)
            btn.alignment = Alignment.FILL
            btn.value = "Flexgrid"
            buttonGroup.addChild(btn,0,row)
            row+=1
            
            btn = ToggleButton()
            btn.onMouseClick.add(hndMenubarClick)
            btn.alignment = Alignment.FILL
            btn.value = "Menubar"
            buttonGroup.addChild(btn,0,row)
            row+=1
            
            btn = ToggleButton()
            btn.onMouseClick.add(hndScrollnavigatorClick)
            btn.alignment = Alignment.FILL
            btn.value = "ScrollNavigator"
            buttonGroup.addChild(btn,0,row)
            row+=1
            
            btn = ToggleButton()
            btn.onMouseClick.add(hndImageClick)
            btn.alignment = Alignment.FILL
            btn.value = "Image"
            buttonGroup.addChild(btn,0,row)
            row+=1
            
            btn = ToggleButton()
            btn.onMouseClick.add(hndDockClick)
            btn.alignment = Alignment.FILL
            btn.value = "DOCK"
            buttonGroup.addChild(btn,0,row)
            row+=1

            btn = ToggleButton()
            btn.onMouseClick.add(hndLayoutManagerClick)
            btn.alignment = Alignment.FILL
            btn.value = "LayoutManager"
            buttonGroup.addChild(btn,0,row)
            row+=1
            
            btn = ToggleButton()
            btn.onMouseClick.add(hndChildrenClick)
            btn.alignment = Alignment.FILL
            btn.value = "Children"
            buttonGroup.addChild(btn,0,row)
            row+=1
              
            btn = ToggleButton()
            btn.onMouseClick.add(hndTabPaneClick)
            btn.alignment = Alignment.FILL
            btn.value = "TabPane"
            buttonGroup.addChild(btn,0,row)
            row+=1
                    
    if True:
        optionPane = Pane()
        optionPane.alignment = Alignment.FILL
        sidePane.addChild(optionPane,0,1)
FUNCTIONEND

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
FUNCTIONEND
            
def main():
    init()
    
    while biui.main():
        time.sleep(0.01)
        pass
FUNCTIONEND

if __name__ == '__main__':
    main()
    
biui.quit()
