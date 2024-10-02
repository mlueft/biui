import time
import sys
import os
import biui
from biui.Widgets import Button,TextField,Window

def createGUI(parent):
    
    tf0 = TextField()
    tf0.name = "tf0"
    tf0.width = 600
    tf0.height = 30
    tf0.x = 100
    tf0.y = 100
    parent.addChild(tf0)
    
    tf1 = TextField()
    tf1.name = "tf1"
    tf1.borderColor = biui.Color(0,255,0)
    tf1.width = 600
    tf1.height = 30
    tf1.x = 100
    tf1.y = 150
    parent.addChild(tf1)
        
    tf2 = TextField()
    tf2.name = "tf2"
    tf2.width = 600
    tf2.height = 30
    tf2.x = 100
    tf2.y = 200
    parent.addChild(tf2)
        
                
    tf0.value = "abcdefghijklmnopqrstu000vwxyz"
    tf1.value = "zwei"
    tf2.value = "drei"
            
def init():
    biui.init()
   
    biui.setThemeFolder(
        os.path.abspath(
            os.path.join(os.getcwd(),"./themes")
        )
    )
    
    biui.selectTheme("blocks")


def main():
    init()
    
    wnd = Window(1024,400)
    wnd.name = "wnd"
    wnd.title = "title"
    wnd.x = 400
    wnd.y = 900

    createGUI(wnd)
    
    while biui.main():
        time.sleep(0.1)
        pass

if __name__ == '__main__':
    main()
    
biui.quit()

print("fertig")
