import sys

sys.path.append('./../')

import math
import biui

sub = None
wnd = None
pane3 = None
b0 = None
b1 = None
localPos = None

def b0OnDown(ev):
	global sub, localPos
	sub = ev.eventSource
	localPos = sub.toLocal(ev.position)
	sub.onMouseUp.add(b0OnUp)
	sub.onMouseMove.add(b0OnMove)
	
def b0OnMove(ev):
	global sub, pane3, b0, b1, localPos
	curPos = ev.position
	sub.x = curPos[0]-localPos[0]
	sub.y = curPos[1]-localPos[0]
	pane3.x = b0.x
	pane3.y = b0.y
	pane3.width = b1.x-b0.x+b1.width
	pane3.height = b1.y-b0.y+b1.height
	
def b0OnUp(ev):
	global sub
	b0OnMove(ev)
	sub.onMouseUp.remove(b0OnUp)
	sub.onMouseMove.remove(b0OnMove)
	
def stopMousePropagation(ev):
	ev.stopPropagation()

####
###
###
def main():
	global wnd, pane3, b0, b1
	
	biui.init()
	biui.setThemeFolder("../../themes")
		
	################################################
	###                                       WINDOW
	################################################
	wnd = biui.Window(1900,1024)
	
	
	################################################
	###                                      Panel 0
	################################################
	pane0 = biui.Pane()
	pane0.x = 10
	pane0.y = 10
	pane0.width = 300
	pane0.height = 300
	wnd.addChild(pane0)
	
	###
	### Buttons
	###
	for i in range(3):
		button0 = biui.Button()
		###button0.onMouseUp.add(_test.upHandler)
		button0.x = 10
		button0.y = 10+i*35
		pane0.addChild(button0)
			
	
	################################################
	###                                      PANEL 1
	################################################
	pane1 = biui.Pane()
	pane1.x = 320
	pane1.y = 10
	pane1.width = 300
	pane1.height = 300
	wnd.addChild(pane1)
	
	###
	### Creating a ToggleButton
	###
	for i in range(3):
		button0 = biui.ToggleButton()
		button0.x = 10
		button0.y = 10+i*35
		pane1.addChild(button0)
		
	
	
	
	################################################
	###                                      PANEL 2
	################################################
	pane2 = biui.Pane()
	pane2.x = 630
	pane2.y = 10
	pane2.width = 300
	pane2.height = 300
	wnd.addChild(pane2)
		
	###
	### ButtonGroup
	###
	buttonGroup = biui.ButtonGroup()
	buttonGroup.onMouseDown.add(stopMousePropagation)
	buttonGroup.x = 10
	buttonGroup.y = 10
	buttonGroup.width = 180
	buttonGroup.height = 280
	pane2.addChild(buttonGroup)
	
	###
	### Add Buttons to group
	###
	for i in range(5):
		button0 = biui.ToggleButton()
		button0.x = 10
		button0.y = 10+i*40
		buttonGroup.addChild(button0)
	
	
	
	
	################################################
	###                                      PANEL 3
	################################################
	pane3 = biui.Pane()
	pane3.x = 630+320
	pane3.y = 10
	pane3.width = 300
	pane3.height = 300
	wnd.addChild(pane3)
	
	### content
	pane3_1 = biui.Pane()
	pane3_1.x = 10
	pane3_1.y = 10
	pane3_1.width = 30
	pane3_1.height = 30
	pane3_1.alignment = biui.Alignment.CENTER_CENTER
	pane3.addChild(pane3_1,0,1)

	pane3_2 = biui.Pane()
	pane3_2.x = 120
	pane3_2.y = 10
	pane3_2.width = 100
	pane3_2.height = 100
	pane3_2.alignment = biui.Alignment.FILL
	pane3.addChild(pane3_2,1,1)
			
	lm = pane3.layoutManager
	lm.columnWidths = [0,50.0]
	lm.rowHeights = [0,50,0]
	
	### Drag buttons
	b0 = biui.Button()
	b0.onMouseDown.add(b0OnDown)
	b0.onMouseUp.add(b0OnUp)
	b0.x = pane3.x
	b0.y = pane3.y
	b0.width = 15
	b0.height = 15
	wnd.addChild(b0)
	
	
	b1 = biui.Button()
	b1.onMouseDown.add(b0OnDown)
	b1.onMouseUp.add(b0OnUp)
	b1.x = pane3.right-15
	b1.y = pane3.bottom-15
	b1.width = 15
	b1.height = 15
	wnd.addChild(b1)
	
	
	################################################
	###                                      PANEL 4
	################################################
		
	grid = biui.FlexGrid()
	grid.x = 10
	grid.y = 320
	grid.width = 600
	grid.height = 600
		
	pane = biui.FlexPane()
	pane.x = 0
	pane.y = 0
	pane.width = 600
	pane.height = 600
	  
	grid.addFlexPane(pane)
	
	wnd.addChild(grid)
		
			
	radius = 100
	angle = 0
	speed = 0.01
	pos = [80.0,100.0]
	
	while biui.main():
		
		### movement
		if False:
			angle += speed
			end = (
				pos[0]+math.cos(angle)*radius,
				pos[1]+math.sin(angle)*radius
			)
			b0.x = end[0]		
			b0.y = end[1]
		
	
	##em = biui.EventManager()
	##em.register(biui.EventTypes.MISC, eventHandler0 )
	##em.register(biui.EventTypes.MISC, eventHandler1 )
	##em.unregister(biui.EventTypes.MISC, eventHandler1 )
	##em.pour( biui.EventTypes.MISC )
	

if __name__ == "__main__":
	main()