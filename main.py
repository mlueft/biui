import pygame
import math
import biui


def p0Click(ev):
    print("p0.click:"+str(ev.phase))
    

def p1Click(ev):
    print("p1.click:"+str(ev.phase))
    
    if ev.phase == biui.EventPhase.DOWN:
        #ev.stopPropagation()
        pass
    else:
        #ev.stopPropagation()
        pass
        
def p2Click(ev):
    print("p2.click:"+str(ev.phase))
    
def p3Click(ev):
    print("p3.click:"+str(ev.phase))
    
def init():

    biui.init()
    
    ##############################################
    #                                       WINDOW
    ##############################################
    wnd = biui.Window(1500,800)
    
    if True:
        ##############################################
        #                                      Panel 0
        ##############################################
        pane0 = biui.Pane()
        pane0.x = 10
        pane0.y = 10
        pane0.width = 300
        pane0.height = 300
        wnd.addChild(pane0)
        
        #
        # Buttons
        #
        for i in range(3):
            button0 = biui.Button()
            button0.label.format = "{:,} mm"
            button0.value = 1000
            #button0.onMouseUp.add(_test.upHandler)
            button0.x = 10
            button0.y = 10+i*35
            button0.width = 100
            button0.height = 30
            pane0.addChild(button0)
                
        #
        # Progressbar
        #
        pb = biui.Progressbar()
        pb.x = 10
        pb.y = 120
        pb.width = 150
        pb.height = 30    
        pb.minValue = -30
        pb.maxValue = 30
        pb.value = 0
        pb.step = 1
        pb.showValue = False
        pane0.addChild(pb)
        
        #
        # NumberSlider
        #
        ns = biui.NumberSlider()
        ns.x = 10
        ns.y = 160
        ns.width = 150
        ns.height = 30
        ns.minValue = 0
        ns.maxValue = 100
        ns.value = 50
        ns.step = 1
        ns.label.format = "{} %"
        pane0.addChild(ns)
                 
        #
        # Checkbox
        #
        cb = biui.Checkbox()
        cb.x = 10
        cb.y = 200
        
        pane0.addChild(cb)
        
        ##############################################
        #                                      PANEL 1
        ##############################################
        pane1 = biui.Pane()
        pane1.x = 320
        pane1.y = 10
        pane1.width = 300
        pane1.height = 300
        wnd.addChild(pane1)
        
        #
        # Creating a ToggleButton
        #
        for i in range(3):
            button0 = biui.ToggleButton()
            button0.x = 10
            button0.y = 10+i*35
            button0.width = 200
            button0.height = 30        
            pane1.addChild(button0)
            
        #
        # Progressbar
        #
        pb = biui.Progressbar()
        pb.x = 10
        pb.y = 120
        pb.width = 150
        pb.height = 30    
        pb.minValue = -30
        pb.maxValue = 30
        pb.value = 12
        pb.step = 1
        pb.label.format = "{} mm"    
        pane1.addChild(pb)
        
        #
        # NumberSlider
        #
        ns = biui.NumberSlider()
        ns.showNavigation = False
        ns.x = 10
        ns.y = 160
        ns.width = 150
        ns.height = 30    
        ns.minValue = -30
        ns.maxValue = 30
        ns.value = 12
        ns.step = 1
        ns.label.format = "{} mm"    
        pane1.addChild(ns)
                
        ##############################################
        #                                      PANEL 2
        ##############################################
        pane2 = biui.Pane()
        pane2.x = 630
        pane2.y = 10
        pane2.width = 300
        pane2.height = 300
        wnd.addChild(pane2)
            
        #
        # ButtonGroup
        #
        buttonGroup = biui.ButtonGroup()
        buttonGroup.x = 0
        buttonGroup.y = 0
        buttonGroup.width = 180
        buttonGroup.height = 280
        pane2.addChild(buttonGroup)
        
        #
        # Add Buttons to group
        #
        for i in range(3):
            button0 = biui.ToggleButton()
            button0.x = 10
            button0.y = 10+i*35
            button0.width = 100
            button0.height = 30        
            buttonGroup.addChild(button0)
        
        
        
        
        ##############################################
        #                                      PANEL 3
        ##############################################
        pane3 = biui.Pane()
        pane3.x = 630+320
        pane3.y = 10
        pane3.width = 300
        pane3.height = 300
        pane3.onMouseClick.add(p0Click)
        wnd.addChild(pane3)
        
        # content
        pane3_1 = biui.Pane()
        pane3_1.x = 50
        pane3_1.y = 50
        pane3_1.width = pane3.width-100    
        pane3_1.height = pane3.height-100
        pane3_1.onMouseClick.add(p1Click)
        pane3.addChild(pane3_1)
    
        pane3_2 = biui.Pane()
        pane3_2.x = 50
        pane3_2.y = 50
        pane3_2.width = pane3_1.width-100    
        pane3_2.height = pane3_1.height-100
        pane3_2.onMouseClick.add(p2Click)
        pane3_1.addChild(pane3_2)
            
        button0 = biui.Label()
        button0.format = "{:,} mm"
        button0.value = 1000
        #button0.onMouseUp.add(_test.upHandler)
        button0.x = 5
        button0.y = 10
        button0.width = 100
        button0.height = 30
        button0.onMouseClick.add(p3Click)
        pane3_1.addChild(button0)

        button0 = biui.Button()
        button0.format = "{:,} mm"
        button0.value = 1000
        #button0.onMouseUp.add(_test.upHandler)
        button0.x = 5
        button0.y = 50
        button0.width = 100
        button0.height = 30
        button0.onMouseClick.add(p3Click)
        pane3_1.addChild(button0)
        
    if False:
        ##############################################
        #                                      PANEL 4
        ##############################################
            
        grid = biui.FlexGrid()
        grid.alignment = biui.Alignment.FILL
        grid.x = 10
        grid.y = 320
            
        pane = biui.FlexPane()
          
        grid.addFlexPane(pane)
        
        wnd.addChild(grid)
                
def main():

    # Temporary main loop
    clock = pygame.time.Clock()
    
    while biui.main():
        clock.tick(1000)
        
init()
if __name__ == "__main__":
    main()