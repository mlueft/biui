import time
import os
import biui
from biui.Widgets import Window
from biui.Widgets import FlexGrid,FlexPane
from biui.Enum import Alignment


def init():

    biui.init()
    biui.setThemeFolder(
        os.path.abspath(
            os.path.join(os.getcwd(),"./themes")
        )
    )
    biui.selectTheme("blocks")

    ################################################
    ###                                       WINDOW
    ################################################
    wnd = Window(1300,500)
    wnd.title = "title"
    wnd.x = 200
    wnd.y = 100
    
    grid = FlexGrid()
    grid.alignment = Alignment.FILL
    grid.x = 10
    grid.y = 320
    
    pane = FlexPane()
    pane.alignment = Alignment.FILL
    grid.addFlexPane(pane)
    
    wnd.addChild(grid)
            
def main():
    init()
    
    while biui.main():
        time.sleep(0.05)
        pass

if __name__ == '__main__':
    main()
    
biui.quit()

print("fertig")