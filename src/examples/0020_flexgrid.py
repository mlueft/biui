import sys,os
import time

sys.path.append('./')

import biui
from biui.Widgets import Window,FlexGrid,FlexPane
from biui.Enum import Alignment

def main():
    
    biui.init()
    biui.setThemeFolder(
        os.path.abspath(
            os.path.join(os.getcwd(),"../themes")
        )
    )
    
    biui.selectTheme("blocks")
    
    ################################################
    ###                                       WINDOW
    ################################################
    wnd = Window(1024,768)
    wnd.y = 0
    wnd.x = 20
    
    grid = FlexGrid()
    grid.alignment = Alignment.FILL
    
    pane = FlexPane()

      
    grid.addFlexPane(pane)
    
    wnd.addChild(grid)
        
    while biui.main():
        time.sleep(0.1)
        pass

if __name__ == "__main__":
    main()