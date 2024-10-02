import time
import sys
import os
import biui
from biui.Widgets import Window,Menubar,MenuItem
from biui.Events import EventPhase
from biui.Enum import Alignment

    
def createMenu():
    
    ms = Menubar()

    mnuMain = MenuItem()
    mnuMain.value = "Datei"
    mnuMain.tooltip = "File menu"
    ms.addItem(mnuMain)
    
    mnuFile = MenuItem()
    mnuFile.value = "New"
    mnuFile.tooltip = "New Document"
    mnuMain.addItem(mnuFile)

    mnuFile = MenuItem()
    mnuFile.value = "New 1     fffff"
    mnuFile.tooltip = "New Document"
    mnuMain.addItem(mnuFile)
    
    return ms

def init():

    biui.init()
    biui.setThemeFolder(
        os.path.abspath(
            os.path.join(os.getcwd(),"./themes")
        )
    )
    
    biui.selectTheme("blocks")


    wnd = Window(1300,500)
    wnd.title = "title"
    wnd.x = 200
    wnd.y = 100
    wnd.width = 1300
    wnd.height = 500
    
    mnu = createMenu()
    mnu.tooltip = "menubar"
    mnu.alignment = Alignment.DOCK_TOP
    mnu.menuAlignment = Alignment.DOCK_LEFT
    wnd.addChild(mnu)

            
def main():
    init()
    
    while biui.main():
        time.sleep(0.1)
        pass

if __name__ == '__main__':
    main()
    
biui.quit()

print("fertig")