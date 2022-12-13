import sys
<<<<<<< HEAD
import time
=======

>>>>>>> macros
sys.path.append('./')

import biui

def main():
    
    biui.init()
    biui.setThemeFolder("../themes")
    
    ################################################
    ###                                       WINDOW
    ################################################
    wnd = biui.Window(1024,768)
    wnd.y = 0
    wnd.x = 20
    
    grid = biui.FlexGrid()
    grid.alignment = biui.Alignment.FILL
    
    pane = biui.FlexPane()

      
    grid.addFlexPane(pane)
    
    wnd.addChild(grid)
        
    while biui.main():
        time.sleep(0.1)
        pass

if __name__ == "__main__":
    main()