import time
import sys
import os
import biui

    
def p0Click(ev):
    print("p0.click:"+str(ev.phase))
    

def p1Click(ev):
    print("p1.click:"+str(ev.phase))
    
    if ev.phase == biui.EventPhase.DOWN:
        ###ev.stopPropagation()
        pass
    else:
        ###ev.stopPropagation()
        pass

        
def p2Click(ev):
    print("p2.click:"+str(ev.phase))
    
def p3Click(ev):
    print("p3.click:"+str(ev.phase))
    
def createMenu():
    
    ms = biui.Menubar()

    mnu0 = biui.MenuItem()
    mnu0.value = "Datei"
    mnu0.tooltip = "File menu"
    ms.addItem(mnu0)
    
    mnu1 = biui.MenuItem()
    mnu1.value = "New ..."
    mnu1.tooltip = "New Document"
    mnu0.addItem(mnu1)
    
    mnu1 = biui.MenuItem()
    mnu1.value = "Open ..."
    mnu1.tooltip = "Open Document"
    mnu0.addItem(mnu1)
    
    mnu2 = biui.MenuItem()
    mnu2.value = "TXT"
    mnu2.tooltip = "Open Document"
    mnu1.addItem(mnu2)
    
    mnu2 = biui.MenuItem()
    mnu2.value = "SVG"
    mnu2.tooltip = "Open Document"
    mnu1.addItem(mnu2)
    
    mnu2 = biui.MenuItem()
    mnu2.value = "PNG"
    mnu2.tooltip = "Open Document"
    mnu1.addItem(mnu2)
    
    mnu2 = biui.MenuItem()
    mnu2.value = "JPG"
    mnu2.tooltip = "Open Document"
    mnu1.addItem(mnu2)
    
    mnu3 = biui.MenuItem()
    mnu3.value = "JPG regular"
    mnu3.tooltip = "Open Document"
    mnu2.addItem(mnu3)
    
    mnu3 = biui.MenuItem()
    mnu3.value = "JPG 2000"
    mnu3.tooltip = "Open Document"
    mnu2.addItem(mnu3)
    
    
    mnu1 = biui.MenuItem()
    mnu1.value = "Save ..."
    mnu1.tooltip = "Save Document"
    mnu0.addItem(mnu1)
    
    
    
    mnubutton = biui.MenuItem()
    mnubutton.value = "Test"
    mnubutton.tooltip = "Test button"
    ms.addItem(mnubutton)




    mnu0 = biui.MenuItem()
    mnu0.value = "Bearbeiten"
    mnu0.tooltip = "Edit"
    ms.addItem(mnu0)
    
    mnu1 = biui.MenuItem()
    mnu1.value = "Copy ..."
    mnu1.tooltip = "copy selection"
    mnu0.addItem(mnu1)
    
    mnu1 = biui.MenuItem()
    mnu1.value = "Cut ..."
    mnu1.tooltip = "cut data"
    mnu0.addItem(mnu1)
    
    mnu1 = biui.MenuItem()
    mnu1.value = "Insert ..."
    mnu1.tooltip = "insert data"
    mnu0.addItem(mnu1)
                    
    mnu2 = biui.MenuItem()
    mnu2.value = "Insert before"
    mnu2.tooltip = "insert data"
    mnu1.addItem(mnu2)
    
    mnu3 = biui.MenuItem()
    mnu3.value = "as text"
    mnu3.tooltip = "Open Document"
    mnu2.addItem(mnu3)
    
    mnu3 = biui.MenuItem()
    mnu3.value = "as grafik"
    mnu3.tooltip = "Open Document"
    mnu2.addItem(mnu3)
    
    mnu2 = biui.MenuItem()
    mnu2.value = "Insert after"
    mnu2.tooltip = "insert data"
    mnu1.addItem(mnu2)
    
    mnu3 = biui.MenuItem()
    mnu3.value = "as text"
    mnu3.tooltip = "Open Document"
    mnu2.addItem(mnu3)
    
    mnu3 = biui.MenuItem()
    mnu3.value = "as grafik"
    mnu3.tooltip = "Open Document"
    mnu2.addItem(mnu3)
    
        
    mnu2 = biui.MenuItem()
    mnu2.value = "Insert anywhere"
    mnu2.tooltip = "insert data"
    mnu1.addItem(mnu2)
    
    mnu3 = biui.MenuItem()
    mnu3.value = "as text"
    mnu3.tooltip = "Open Document"
    mnu2.addItem(mnu3)
    
    mnu3 = biui.MenuItem()
    mnu3.value = "as grafik"
    mnu3.tooltip = "Open Document"
    mnu2.addItem(mnu3)
    
    return ms
        
def createGUI0():
    ################################################
    ###                                       WINDOW
    ################################################
    wnd = biui.Window(1300,500)
    wnd.title = "title"
    wnd.x = 200
    wnd.y = 100
    
    
    ################################################
    ###                                       TOPBAR
    ################################################
    if True:
        
        mnu = createMenu()
        mnu.tooltip = "menubar"
        mnu.alignment = biui.Alignment.DOCK_TOP
        mnu.menuAlignment = biui.Alignment.DOCK_LEFT
        wnd.addChild(mnu)

        if False:
            mnu = createMenu()
            mnu.alignment = biui.Alignment.DOCK_LEFT
            mnu.menuAlignment = biui.Alignment.DOCK_TOP
            wnd.addChild(mnu)
            
            mnu = createMenu()
            mnu.alignment = biui.Alignment.DOCK_BOTTOM
            mnu.menuAlignment = biui.Alignment.DOCK_LEFT
            wnd.addChild(mnu)
            
            mnu = createMenu()
            mnu.alignment = biui.Alignment.DOCK_RIGHT
            mnu.menuAlignment = biui.Alignment.DOCK_TOP
            wnd.addChild(mnu)
    
    
            mnu = createMenu()
            mnu.alignment = biui.Alignment.DOCK_TOP
            mnu.menuAlignment = biui.Alignment.DOCK_RIGHT
            wnd.addChild(mnu)
    
            mnu = createMenu()
            mnu.alignment = biui.Alignment.DOCK_LEFT
            mnu.menuAlignment = biui.Alignment.DOCK_BOTTOM
            wnd.addChild(mnu)
            
            mnu = createMenu()
            mnu.alignment = biui.Alignment.DOCK_BOTTOM
            mnu.menuAlignment = biui.Alignment.DOCK_RIGHT
            wnd.addChild(mnu)
            
            mnu = createMenu()
            mnu.alignment = biui.Alignment.DOCK_RIGHT
            mnu.menuAlignment = biui.Alignment.DOCK_BOTTOM
            wnd.addChild(mnu)
        
        
    if True:
        ################################################
        ###                                      Panel 0
        ################################################
        pane0 = biui.Pane()
        pane0.tooltip = "First pane"
        pane0.alignment = biui.Alignment.FILL
        pane0.x = 10
        pane0.y = 10
        pane0.width = 300
        pane0.height = 300
        wnd.addChild(pane0,0,0)
        
        ###
        ### Buttons
        ###
        for i in range(3):
            button0 = biui.Button()
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
        pb = biui.Progressbar()
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
        ns = biui.NumberSlider()
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
        cb = biui.Checkbox()
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
        pane1 = biui.Pane()
        pane1.tooltip = "second tooltip"
        pane1.alignment = biui.Alignment.FILL
        pane1.x = 320
        pane1.y = 10
        pane1.width = 300
        pane1.height = 300
        wnd.addChild(pane1,1,0)
        
        ###
        ### Creating a ToggleButton
        ###
        for i in range(3):
            button0 = biui.ToggleButton()
            button0.tooltip = "button{}".format(i)
            button0.x = 10
            button0.y = 10+i    *35
            button0.width = 200
            button0.height = 30        
            pane1.addChild(button0)
            
        ###
        ### Progressbar
        ###
        pb = biui.Progressbar()
        pb.tooltip = "progress bar ..."
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
        ns = biui.NumberSlider()
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
        pane2 = biui.Pane()
        pane2.tooltip = "thirt pane"
        pane2.alignment = biui.Alignment.FILL
        pane2.x = 630
        pane2.y = 10
        pane2.width = 300
        pane2.height = 300
        wnd.addChild(pane2,2,0)
            
        ###
        ### ButtonGroup
        ###
        buttonGroup = biui.ButtonGroup()
        buttonGroup.tooltip = "this is a button group"
        buttonGroup.x = 0
        buttonGroup.y = 0
        buttonGroup.width = 180
        buttonGroup.height = 280
        pane2.addChild(buttonGroup)
        
        ###
        ### Add Buttons to group
        ###
        for i in range(3):
            button0 = biui.ToggleButton()
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
        pane3 = biui.Pane()
        pane3.tooltip  = "fourth pane"
        pane3.alignment = biui.Alignment.FILL
        pane3.x = 630+320
        pane3.y = 10
        pane3.width = 300
        pane3.height = 300
        pane3.onMouseClick.add(p0Click)
        wnd.addChild(pane3,0,1)
        
        ### content
        pane3_1 = biui.Pane()
        pane3_1.tooltip = "nested pane"
        pane3_1.x = 50
        pane3_1.y = 50
        pane3_1.width = pane3.width-100    
        pane3_1.height = pane3.height-100
        pane3_1.onMouseClick.add(p1Click)
        pane3.addChild(pane3_1)
    
        pane3_2 = biui.Pane()
        pane3_2.tooltip = "nested nested pane"
        pane3_2.x = 50
        pane3_2.y = 50
        pane3_2.width = pane3_1.width-100    
        pane3_2.height = pane3_1.height-100
        pane3_2.onMouseClick.add(p2Click)
        pane3_1.addChild(pane3_2)
            
        button0 = biui.Label()
        button0.tooltip = "label"
        button0.format = "{:,} mm"
        button0.value = 1000
        ###button0.onMouseUp.add(_test.upHandler)
        button0.x = 5
        button0.y = 10
        button0.width = 100
        button0.height = 30
        button0.onMouseClick.add(p3Click)
        pane3_1.addChild(button0)

        button0 = biui.Button()
        button0.format = "{:,} mm"
        button0.value = 1000
        ###button0.onMouseUp.add(_test.upHandler)
        button0.x = 5
        button0.y = 50
        button0.width = 100
        button0.height = 30
        button0.onMouseClick.add(p3Click)
        pane3_1.addChild(button0)
        
        ################################################
        ###                                      PANEL 4
        ################################################
        pane4 = biui.Pane()
        pane4.tooltip  = "fiveth pane"
        pane4.alignment = biui.Alignment.FILL
        pane4.x = 630+320
        pane4.y = 10
        pane4.width = 300
        pane4.height = 300
        wnd.addChild(pane4,1,1)
        
        img = biui.Image()
        pane4.addChild(img)
        img.file = "../test.jpeg"
        img.x = 10
        img.y = 10
        img.alignment = biui.Alignment.FILL
        ##img.alignment = biui.Alignment.CENTER_CENTER

        ################################################
        ###                                      PANEL 5
        ################################################
        pane5 = biui.Pane()
        pane5.tooltip  = "fiveth pane"
        pane5.alignment = biui.Alignment.FILL
        pane5.x = 630+320
        pane5.y = 10
        pane5.width = 300
        pane5.height = 300
        pane5.verticalScrollbar = True
        pane5.horizontalScrollbar = True        
        wnd.addChild(pane5,2,1)
        
        b = biui.Button()
        b.value = "TL"
        b.width = b.height = 50
        b.x = 0
        b.y = 0
        pane5.addChild(b)
    
        b = biui.Button()
        b.value = "TR"
        b.width = b.height = 50
        b.x = 1000-50
        b.y = 0
        pane5.addChild(b)
        
        b = biui.Button()
        b.value = "BR"
        b.width = b.height = 50
        b.x = 1000-50
        b.y = 1000-50
        pane5.addChild(b)
    
        b = biui.Button()
        b.value = "BL"
        b.width = b.height = 50
        b.x = 0
        b.y = 1000-50
        pane5.addChild(b)
        
        b = biui.Button()
        b.width = b.height = 50
        b.x = 500-25
        b.y = 500-25
        pane5.addChild(b)
        
            
def createGUI1():
    ################################################
    ###                                       WINDOW
    ################################################
    
    wnd = biui.Window(1300,500)
    
    ##pane0 = biui.Pane()
    ##pane0.alignment = biui.Alignment.FILL
    ##wnd.addChild(pane0,0,0)
    
    ##pane1 = biui.Pane()
    ##pane1.alignment = biui.Alignment.FILL
    ##wnd.addChild(pane1,1,0)
            
    
    button0 = biui.Button()
    button0.x = 10
    button0.y = 45
    button0.width = 200
    button0.height = 30
    wnd.addChild(button0)
                
    ##pane2 = biui.Pane()
    ##pane2.alignment = biui.Alignment.FILL
    ##wnd.addChild(pane2,3,2)

def init():

    biui.init()
    ##biui.setThemeFolder("~/programming/biui/themes/")
    biui.setThemeFolder("/home/work/programming/biui/themes/")
    ##biui.setThemeFolder("/home/daily/programming/biui/themes/")
    
    biui.selectTheme("blocks")
    ##biui.selectTheme("default")
    createGUI0()
    ##createGUI()
    ##createGUI()
            
def main():
    init()
    
    while biui.main():
        time.sleep(0.05)
        pass

if __name__ == '__main__':
    main()
    
biui.quit()

print("fertig")