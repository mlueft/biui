import sys

sys.path.append('./')

import biui

def main():
    
    biui.init()
    biui.setThemeFolder("../themes")
    
    ################################################
    ###                                       WINDOW
    ################################################
    wnd = biui.Window(1024,768)
    
    grid = biui.FlexGrid()
    grid.alignment = biui.Alignment.FILL
    
    pane = biui.FlexPane()

      
    grid.addFlexPane(pane)
    
    wnd.addChild(grid)
        
    while biui.main():
        pass

if __name__ == "__main__":
    main()