import sys

sys.path.append('./../')

import biui

def main():
    
    biui.init()
    biui.setThemeFolder("../../themes")
    
    ################################################
    ###                                       WINDOW
    ################################################
    wnd = biui.Window(1024,768)
    
    grid = biui.FlexGrid()
    grid.alignment = biui.Alignment.FILL
    
    pane = biui.FlexPane()
    pane.x = 0
    pane.y = 0
    pane.width = 1024
    pane.height = 768
      
    grid.addFlexPane(pane)
    
    wnd.addChild(grid)
        
    while biui.main():
        pass

if __name__ == "__main__":
    main()