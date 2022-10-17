import math
import biui
import time

def main():
    
    biui.init()
    biui.setThemeFolder("../themes")
        
    ################################################
    ###                                       WINDOW
    ################################################
    wnd = biui.Window(800,600)
    
    lbl = biui.Label()
    lbl.x = 10
    lbl.y = 10
    lbl.alignment = biui.Alignment.CENTER_CENTER
    lbl.font.size = 50
    lbl.font.name = "Courier"
    lbl.color = biui.Color(255,255,255,0)
    lbl.anialiased = True
    
    wnd.addChild(lbl)
        

    while biui.main():
        pass
    
if __name__ == "__main__":
    main()