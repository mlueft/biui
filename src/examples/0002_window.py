import sys,os

sys.path.append('./')

import math
import biui
import time
from biui.Widgets import Window

def hndWindowResize(ex):
    ##print("W")
    pass
    
def init():
    
    biui.init()
    biui.setThemeFolder(
        os.path.abspath(
            os.path.join(os.getcwd(),"./themes")
        )
    )
    
    biui.selectTheme("blocks")
    
    ###############################################
    ##                                       WINDOW
    ###############################################
    wnd = Window(200,200)
    wnd.title = "Window title!1"
    wnd.x = 500
    wnd.y = 0
    wnd.width = 640
    wnd.height = 100
    wnd.onWindowResized.add(hndWindowResize)
    wnd.onWindowSizeChanged.add(hndWindowResize)
    

    """ "
    wnd = Window(1024,768)
    wnd.title = "Window title!2"
    wnd.x = 500
    wnd.y = 300
    wnd.width = 640
    wnd.height = 100
    """ #"
    
    print( "Window title: {}".format(wnd.title) )
    print( "windowposiion : {}x{}".format(wnd.x,wnd.y))
    print( "windowsize : {}x{}".format(wnd.width,wnd.height))
    
    ##wnd.left = 10
    ##wnd.bottom = 10
    ##wnd.right = 10
    ##wnd.top = 10
    
def main():
    init()
    
    ##
    ## Temporary main loop
    ##
    while biui.main():
        ##sf.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))
        pass

    biui.quit()
    
    print("quit application")
    
if __name__ == "__main__":
    main()