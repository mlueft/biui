import sys
from reportlab.graphics.barcode.qrencoder import QRFNC1Second
from biui.Widgets import Window,Pane
sys.path.append('./')

import biui
from biui.Enum import Alignment

import time
import math

pano0 = None
width = 1300
height = 600
panes = []

def init():
    global pane0,eifth,height, panes
    
    biui.init()
    biui.setThemeFolder("../themes")
    
    ################################################
    ###                                       WINDOW
    ################################################
    
    wnd = Window(width,height)
    wnd.y = 0
    
    for i in range(5):
        pane0 = Pane()
        pane0.x = 10
        pane0.y = 10
        pane0.width = 300
        pane0.height = 300
        btn = Button()
        btn.x = 10
        btn.y = 10
        btn.alignment = Alignment.FILL

        
        pane0.layoutManager.rowHeights = [10,0,10]
        pane0.layoutManager.columnWidths = [5,0,5]
        
        pane0.addChild(btn,1,1)
        
        wnd.addChild(pane0)
        panes.append([pane0,100+i*200,200,100,80,11+i,12+i])
        
def main():
    global pane0,width,height, panes
    init()
    i = 0
    start = time.time()
    while i < 2000:
        
        for pane in panes:
            pane[0].width = pane[3]+math.sin(i/pane[5])*50
            pane[0].height = pane[4]-math.cos(i/pane[6])*50
            pane[0].x = pane[1]+pane[0].width/2
            pane[0].y = pane[2]+pane[0].height/2+math.cos(i/10)*150
            
        time.sleep(0.01)
        i +=1
        
        biui.main()
        pass
    end = time.time()
    
    print("duration: {} sec.".format((end-start)))
    print("avg:{} sec/cyc".format((end-start)/i))
    
if __name__ == '__main__':
    main()
    

print("fertig")   