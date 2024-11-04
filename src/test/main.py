import time
import sys
import os
import random

import biui
from biui.Events import EventPhase
from biui.Enum import Alignment
from biui.Color import Color

from biui.Widgets import Window,Button,Menubar,MenuItem,Pane,Progressbar,NumberSlider
from biui.Widgets import FlexGrid,FlexPane,Checkbox,ToggleButton,Label,Image,ButtonGroup,TextField
from biui.Widgets import ScrollNavigator

sidePane    = None
contentPane = None
content     = None
optionPane  = None
option      = None

childrenFocused = None
childrenPane0 = None
childrenPane1 = None


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



def createOptionPaneEmpty():
    result = Pane()
    result.alignment = Alignment.FILL
    result.verticalScrollbar = True
    return result

def createOptionPaneLabel():
    return createOptionPaneEmpty()

def createOptionPanePane():
    return createOptionPaneEmpty()

def createOptionPaneButton():
    return createOptionPaneEmpty()

def createOptionPaneToggleButton():
    return createOptionPaneEmpty()

def createOptionPaneButtonGroup():
    return createOptionPaneEmpty()

def createOptionPaneTextField():
    return createOptionPaneEmpty()

def createOptionPaneProgressbar():
    return createOptionPaneEmpty()

def createOptionPaneNumberSlider():
    return createOptionPaneEmpty()

def createOptionPaneCheckbox():
    return createOptionPaneEmpty()

def createOptionPaneFlexGrid():
    return createOptionPaneEmpty()

def createOptionPaneMenubar():
    return createOptionPaneEmpty()

def createOptionPaneScrollNavigator():
    return createOptionPaneEmpty()

def createOptionPaneImage():
    return createOptionPaneEmpty()

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

def createOptionPaneLayoutManager():
    return createOptionPaneEmpty()

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
        
    return result

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

def createProgressPane():
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
    
    return result

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

def createContentPaneFlexGrid():
    result = Pane()
    result.alignment = Alignment.FILL

    flexgrid = FlexGrid()
    flexgrid.alignment = Alignment.FILL
    result.addChild(flexgrid)

    flexPane = FlexPane()
    flexgrid.addFlexPane(flexPane)
    return result

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

def createContentScrollNavigator():
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

def createContentImage():
    
    padding = 50
    
    result = Pane()
    result.alignment = Alignment.FILL


    image = createSubject("image")
    result.addChild(image)
    image.alignment = Alignment.FILL
    
    return result

def createContentDock(type = "button"):
    
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

def createContentLayoutManager(type = "button"):
    
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

def createContentChildren(type = "button"):
    global childrenPane0, childrenPane1
    result = Pane()
    result.alignment = Alignment.FILL

    childrenPane0 = Pane()
    childrenPane0.x = 100
    childrenPane0.y = 100
    childrenPane0.width = 300
    childrenPane0.height = 300
    result.addChild(childrenPane0)
    
    childrenPane1 = Pane()
    childrenPane1.x = 450
    childrenPane1.y = 100
    childrenPane1.width = 300
    childrenPane1.height = 300
    result.addChild(childrenPane1)
           
    return result



def hndDockOptionImage(ev):
    global content
    if content != None:
        contentPane.removeChild(content)
    content = createContentDock("image")
    contentPane.addChild(content)

def hndDockOptionButton(ev):
    global content
    if content != None:
        contentPane.removeChild(content)
    content = createContentDock("button")
    contentPane.addChild(content)

def hndDockOptionLabel(ev):
    global content
    if content != None:
        contentPane.removeChild(content)
    content = createContentDock("label")
    contentPane.addChild(content)
    
    
    
def hndChildrenOptionAdd(ev):
    global childrenPane0,childrenPane1,childrenFocused
    
    button = Button()
    button.x = random.uniform(0, childrenPane0.width-10)
    button.y = random.uniform(0, childrenPane0.height-10)
    button.value = int(random.uniform(0,99))
    button.width = 30
    button.height = 30
    button.onMouseClick.add( hndChildrenMouseClick)
    childrenPane0.addChild(button)
    childrenFocused = button

def hndChildrenOptionRemove(ev):
    global childrenPane0,childrenPane1,childrenFocused
    
    if childrenPane0.hasChild(childrenFocused):
        childrenPane0.removeChild(childrenFocused)
        
    if childrenPane1.hasChild(childrenFocused):
        childrenPane1.removeChild(childrenFocused)

def hndChildrenOptionSwap(ev):
    global childrenPane0,childrenPane1,childrenFocused
    
    if childrenPane0.hasChild(childrenFocused):
        print("Swap to pane1")
        childrenPane0.removeChild(childrenFocused)
        childrenPane1.addChild(childrenFocused)
        childrenFocused.x = random.uniform(0, childrenPane1.width-10)
        childrenFocused.y = random.uniform(0, childrenPane1.height-10)        
        return
    
    if childrenPane1.hasChild(childrenFocused):
        print("Swap to pane0")
        childrenPane1.removeChild(childrenFocused)
        childrenPane0.addChild(childrenFocused)
        childrenFocused.x = random.uniform(0, childrenPane0.width-10)
        childrenFocused.y = random.uniform(0, childrenPane0.height-10)        
        return
    
def hndChildrenOptionDebug(ev):
    global childrenPane0,childrenPane1,childrenFocused
    print("children Pane0: {}".format(len(childrenPane0.getChildren())))
    print("children Pane1: {}".format(len(childrenPane1.getChildren())))
    
    if childrenFocused:
        print("focused button parent: {}".format(childrenFocused.parent))
    
    childrenPane0.layoutManager.debug()
    childrenPane1.layoutManager.debug()
    print("---------------------------")
    
def hndChildrenMouseClick(ev):
    global childrenFocused
    childrenFocused = ev.eventSource




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
    
def hndProgressbarClick(ev):
    global content, option
    
    if content != None:
        contentPane.removeChild(content)
    content = createProgressPane()
    contentPane.addChild(content)
    
    if option != None:
        sidePane.removeChild(option)
        
    option = createOptionPaneProgressbar()
    optionPane.addChild(option)
    
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
    
def hndScrollnavigatorClick(ev):
    global content, option
    
    if content != None:
        contentPane.removeChild(content)
    content = createContentScrollNavigator()
    contentPane.addChild(content)
    
    if option != None:
        sidePane.removeChild(option)
        
    option = createOptionPaneScrollNavigator()
    optionPane.addChild(option)
    
def hndImageClick(ev):
    global content, option
    
    if content != None:
        contentPane.removeChild(content)
    content = createContentImage()
    contentPane.addChild(content)
    
    if option != None:
        sidePane.removeChild(option)
        
    option = createOptionPaneImage()
    optionPane.addChild(option)
    
def hndDockClick(ev):
    global content, option
    
    type="image"
    
    if content != None:
        contentPane.removeChild(content)
    content = createContentDock(type)
    contentPane.addChild(content)
    
    if option != None:
        sidePane.removeChild(option)
        
    option = createOptionPaneDock()
    optionPane.addChild(option)

def hndLayoutManagerClick(ev):
    global content, option
    
    type="image"
    
    if content != None:
        contentPane.removeChild(content)
    content = createContentLayoutManager(type)
    contentPane.addChild(content)
    
    if option != None:
        sidePane.removeChild(option)
        
    option = createOptionPaneLayoutManager()
    optionPane.addChild(option)
    
def hndChildrenClick(ev):
    global content, option
    
    type="button"
    
    if content != None:
        contentPane.removeChild(content)
    content = createContentChildren(type)
    contentPane.addChild(content)
    
    if option != None:
        sidePane.removeChild(option)
        
    option = createOptionPaneChildren()
    optionPane.addChild(option)        
        
        
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
        buttonGroup.layoutManager.rowHeights = [buttonHeight,buttonHeight,buttonHeight,buttonHeight,buttonHeight,buttonHeight,buttonHeight,buttonHeight,buttonHeight,buttonHeight,buttonHeight,buttonHeight,buttonHeight,buttonHeight,0]
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
              
        
    if True:
        optionPane = Pane()
        optionPane.alignment = Alignment.FILL
        sidePane.addChild(optionPane,0,1)

    return
        
def createGUI0():
    ################################################
    ###                                       WINDOW
    ################################################
    wnd = Window(1024,768)
    wnd.title = "BIUI - Demo app"
    wnd.x = 200
    wnd.y = 100
    
    
    if True:
        
        mnu = createMenu()
        mnu.tooltip = "menubar"
        mnu.alignment = Alignment.DOCK_TOP
        mnu.menuAlignment = Alignment.DOCK_LEFT
        wnd.addChild(mnu)

        if False:
            mnu = createMenu()
            mnu.alignment = Alignment.DOCK_LEFT
            mnu.menuAlignment = Alignment.DOCK_TOP
            wnd.addChild(mnu)
            
            mnu = createMenu()
            mnu.alignment = Alignment.DOCK_BOTTOM
            mnu.menuAlignment = Alignment.DOCK_LEFT
            wnd.addChild(mnu)
            
            mnu = createMenu()
            mnu.alignment = Alignment.DOCK_RIGHT
            mnu.menuAlignment = Alignment.DOCK_TOP
            wnd.addChild(mnu)
    
    
            mnu = createMenu()
            mnu.alignment = Alignment.DOCK_TOP
            mnu.menuAlignment = Alignment.DOCK_RIGHT
            wnd.addChild(mnu)
    
            mnu = createMenu()
            mnu.alignment = Alignment.DOCK_LEFT
            mnu.menuAlignment = Alignment.DOCK_BOTTOM
            wnd.addChild(mnu)
            
            mnu = createMenu()
            mnu.alignment = Alignment.DOCK_BOTTOM
            mnu.menuAlignment = Alignment.DOCK_RIGHT
            wnd.addChild(mnu)
            
            mnu = createMenu()
            mnu.alignment = Alignment.DOCK_RIGHT
            mnu.menuAlignment = Alignment.DOCK_BOTTOM
            wnd.addChild(mnu)
        
        
    if True:
        ################################################
        ###                                      Panel 0
        ################################################
        pane0 = Pane()
        pane0.tooltip = "First pane"
        pane0.alignment = Alignment.FILL
        pane0.x = 0
        pane0.y = 0
        pane0.width = 300
        pane0.height = 300
        wnd.addChild(pane0,0,0)
        
        if True:
            ###
            ### Buttons
            ###
            for i in range(3):
                button0 = Button()
                button0.tooltip = "button{}".format(i)
                button0.label.format = "{:,} mm"
                button0.value = 1000
                ###button0.onMouseUp.add(_test.upHandler)
                button0.x = 10
                button0.y = 10+i*35
                button0.width = 100
                button0.height = 30
                button0.id = "test"
                pane0.addChild(button0)
                    
            ###
            ### Progressbar
            ###
            pb = Progressbar()
            pb.tooltip = "Progressbar"
            pb.x = 10
            pb.y = 120
            pb.width = 150
            pb.height = 30    
            pb.minValue = -30
            pb.maxValue = 30
            pb.value = 0
            pb.step = 1
            pb.showValue = False
            pb.label.format = "{}"
            pane0.addChild(pb)
            ##return 
            ###
            ### NumberSlider
            ###
            ns = NumberSlider()
            ns.tooltip = "number slider"
            ns.x = 10
            ns.y = 160
            ns.width = 150
            ns.height = 30
            ns.minValue = 0
            ns.maxValue = 100
            ns.value = 50
            ns.step = 1
            ns.label.format = "{} %"
            pane0.addChild(ns)
                     
            ###
            ### Checkbox
            ###
            cb = Checkbox()
            cb.tooltip = "this is a checkbox"
            cb.backColor = biui.Color(255,255,0)
            cb.backColorOver = biui.Color(255,255,0)
            cb.backColorDown = biui.Color(255,255,0)
            cb.backColorChecked = biui.Color(255,0,0)
            cb.x = 10
            cb.y = 200
            
            pane0.addChild(cb)
        
        ################################################
        ###                                      PANEL 1
        ################################################
        pane1 = Pane()
        pane1.tooltip = "second tooltip"
        pane1.alignment = Alignment.FILL
        pane1.x = 320
        pane1.y = 10
        pane1.width = 300
        pane1.height = 300
        wnd.addChild(pane1,1,0)
        
        if True:
            ###
            ### Creating a ToggleButton
            ###
            for i in range(3):
                button0 = ToggleButton()
                button0.tooltip = "button{}".format(i)
                button0.x = 10
                button0.y = 10+i    *35
                button0.width = 200
                button0.height = 30        
                pane1.addChild(button0)
                
            ###
            ### Progressbar
            ###
            pb = Progressbar()
            pb.tooltip = "progress bar"
            pb.x = 10
            pb.y = 120
            pb.width = 150
            pb.height = 30    
            pb.minValue = -30
            pb.maxValue = 30
            pb.value = 12
            pb.step = 1
            pb.label.format = "{} mm"    
            pane1.addChild(pb)
            
            ###
            ### NumberSlider
            ###
            ns = NumberSlider()
            ns.tooltip = "number slider"
            ns.showNavigation = False
            ns.x = 10
            ns.y = 160
            ns.width = 150
            ns.height = 30    
            ns.minValue = -30
            ns.maxValue = 30
            ns.value = 12
            ns.step = 1
            ns.label.format = "{} mm"    
            pane1.addChild(ns)
                
        ################################################
        ###                                      PANEL 2
        ################################################
        pane2 = Pane()
        pane2.tooltip = "thirt pane"
        pane2.alignment = Alignment.FILL
        pane2.x = 630
        pane2.y = 10
        pane2.width = 300
        pane2.height = 300
        wnd.addChild(pane2,2,0)
            
        if True:
            ###
            ### ButtonGroup
            ###
            buttonGroup = ButtonGroup()
            buttonGroup.tooltip = "this is a button group"
            buttonGroup.x = 0
            buttonGroup.y = 0
            buttonGroup.width = 180
            buttonGroup.height = 350
            pane2.addChild(buttonGroup)
            
            ###
            ### Add Buttons to group
            ###
            for i in range(3):
                button0 = ToggleButton()
                ##button0.checked = False
                button0.tooltip = "button{}".format(i)
                button0.x = 10
                button0.y = 10+i*35
                button0.width = 100
                button0.height = 30        
                buttonGroup.addChild(button0)
            
            
        
        ################################################
        ###                                      PANEL 3
        ################################################
        pane3 = Pane()
        pane3.tooltip  = "fourth pane"
        pane3.alignment = Alignment.FILL
        pane3.x = 630+320
        pane3.y = 10
        pane3.width = 300
        pane3.height = 300
        
        wnd.addChild(pane3,0,1)
        
        ### content
        pane3_1 = Pane()
        pane3_1.tooltip = "nested pane"
        pane3_1.x = 50
        pane3_1.y = 50
        pane3_1.width = 100    
        pane3_1.height = 100
        
        pane3_1.backColor = Color(50,50,50)
        pane3.addChild(pane3_1)
        
        if True:
            pane3_2 = Pane()
            pane3_2.tooltip = "nested nested pane"
            pane3_2.x = 50
            pane3_2.y = 50
            pane3_2.width = 50    
            pane3_2.height = 50
            
            pane3_2.backColor = Color(70,70,70)
            pane3_1.addChild(pane3_2)
            
        if True:
            button0 = Label()
            button0.tooltip = "label"
            button0.format = "{:,} mm"
            button0.value = 1000
            ###button0.onMouseUp.add(_test.upHandler)
            button0.x = 5
            button0.y = 10
            button0.width = 100
            button0.height = 30
            
            pane3_1.addChild(button0)
    
            button0 = Button()
            button0.format = "{:,} mm"
            button0.value = 1000
            ###button0.onMouseUp.add(_test.upHandler)
            button0.x = 5
            button0.y = 50
            button0.width = 100
            button0.height = 30
            
            pane3_1.addChild(button0)
            
        ################################################
        ###                                      PANEL 4
        ################################################
        pane4 = Pane()
        pane4.tooltip  = "fiveth pane"
        pane4.alignment = Alignment.FILL
        pane4.x = 630+320
        pane4.y = 10
        pane4.width = 300
        pane4.height = 300
        wnd.addChild(pane4,1,1)
        
        if True:
            img = Image()
            #
            pane4.addChild(img)
            img.file = "./test.jpg"
            img.alignment = Alignment.FILL
            ##img.alignment = Alignment.CENTER_CENTER

        ################################################
        ###                                      PANEL 5
        ################################################
        pane5 = Pane()
        pane5.tooltip  = "fiveth pane"
        pane5.alignment = Alignment.FILL
        pane5.x = 630+320
        pane5.y = 10
        pane5.width = 300
        pane5.height = 300
        pane5.verticalScrollbar = True
        pane5.horizontalScrollbar = True        
        wnd.addChild(pane5,2,1)
        
        if True:
            b = Button()
            b.value = "TL"
            b.width = b.height = 50
            b.x = 0
            b.y = 0
            pane5.addChild(b)
        
            b = Button()
            b.value = "TR"
            b.width = b.height = 50
            b.x = 1000-50
            b.y = 0
            pane5.addChild(b)
            
            b = Button()
            b.value = "BR"
            b.width = b.height = 50
            b.x = 1000-50
            b.y = 1000-50
            pane5.addChild(b)
        
            b = Button()
            b.value = "BL"
            b.width = b.height = 50
            b.x = 0
            b.y = 1000-50
            pane5.addChild(b)
            
            b = Button()
            b.width = b.height = 50
            b.x = 500-25
            b.y = 500-25
            pane5.addChild(b)



    
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
