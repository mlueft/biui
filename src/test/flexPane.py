import time

import biui


def init():

    biui.init()
    ##biui.setThemeFolder("/home/work/programming/biui/themes")
    biui.setThemeFolder("/home/work/programming/biui/themes/")
    ##biui.setThemeFolder("/home/daily/programming/biui/themes/")
    biui.selectTheme("blocks")

    ################################################
    ###                                       WINDOW
    ################################################
    wnd = biui.Window(1300,500)
    wnd.title = "title"
    wnd.x = 200
    wnd.y = 100
    
    grid = biui.FlexGrid()
    grid.alignment = biui.Alignment.FILL
    grid.x = 10
    grid.y = 320
    
    pane = biui.FlexPane()
    pane.alignment = biui.Alignment.FILL
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