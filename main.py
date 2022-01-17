import pygame
import math

import biui
import pygame.locals


screen = None

class Test():
	def upHandler(self, ev):
		print("up")
		print(self)

_test = Test()

sub = None
wnd = None
pane3 = None
b0 = None
b1 = None
localPos = None

def b0OnDown(ev):
	global sub, localPos
	sub = ev.getEventSource()
	localPos = sub.toLocal(ev.getPosition())
	sub.onMouseUp.add(b0OnUp)
	sub.onMouseMove.add(b0OnMove)
	
def b0OnMove(ev):
	global sub, pane3, b0, b1, localPos
	curPos = ev.getPosition()
	sub.setX( curPos[0]-localPos[0])
	sub.setY( curPos[1]-localPos[0])
	pane3.setX(b0.getX())
	pane3.setY(b0.getY())
	pane3.setWidth( b1.getX()-b0.getX()+b1.getWidth())
	pane3.setHeight( b1.getY()-b0.getY()+b1.getHeight())
	
def b0OnUp(ev):
	global sub
	b0OnMove(ev)
	sub.onMouseUp.remove(b0OnUp)
	sub.onMouseMove.remove(b0OnMove)
	
def main():
	global wnd, pane3, b0, b1
	
	##############################################
	#                                       WINDOW
	##############################################
	wnd = biui.Window()
	wnd.setWidth(1024)
	wnd.setHeight(768)
	
	
	##############################################
	#                                      Panel 0
	##############################################
	pane0 = biui.Pane()
	pane0.setX(10)
	pane0.setY(10)
	pane0.setWidth(300)
	pane0.setHeight(300)
	wnd.addChild(pane0)
	
	#
	# Buttons
	#
	for i in range(3):
		button0 = biui.Button()
		#button0.onMouseUp.add(_test.upHandler)
		button0.setX(10)
		button0.setY(10+i*25)
		pane0.addChild(button0)
			
	
	##############################################
	#                                      PANEL 1
	##############################################
	pane1 = biui.Pane()
	pane1.setX(320)
	pane1.setY(10)
	pane1.setWidth(300)
	pane1.setHeight(300)
	wnd.addChild(pane1)
	
	#
	# Creating a ToggleButton
	#
	for i in range(3):
		button0 = biui.ToggleButton()
		button0.setX(10)
		button0.setY(10+i*25)
		pane1.addChild(button0)
		
	
	
	
	##############################################
	#                                      PANEL 2
	##############################################
	pane2 = biui.Pane()
	pane2.setX(630)
	pane2.setY(10)
	pane2.setWidth(300)
	pane2.setHeight(300)
	wnd.addChild(pane2)
		
	#
	# ButtonGroup
	#
	buttonGroup = biui.ButtonGroup()
	buttonGroup.setX(10)
	buttonGroup.setY(10)
	buttonGroup.setWidth(80)
	buttonGroup.setHeight(280)
	pane2.addChild(buttonGroup)
	
	#
	# Add Buttons to group
	#
	for i in range(5):
		button0 = biui.ToggleButton()
		button0.setX(10)
		button0.setY(10+i*30)
		buttonGroup.addChild(button0)
	
	
	
	
	##############################################
	#                                      PANEL 3
	##############################################
	pane3 = biui.Pane()
	pane3.setX(10)
	pane3.setY(320)
	pane3.setWidth(300)
	pane3.setHeight(300)
	wnd.addChild(pane3)
	
	# content
	pane3_1 = biui.Pane()
	pane3_1.setX(10)
	pane3_1.setY(10)
	pane3_1.setWidth(30)
	pane3_1.setHeight(30)
	pane3_1.setAlignment(biui.Alignment.BOTTOM_RIGHT)
	pane3.addChild(pane3_1,0,0)

	pane3_2 = biui.Pane()
	pane3_2.setX(120)
	pane3_2.setY(10)
	pane3_2.setWidth(100)
	pane3_2.setHeight(100)
	pane3_2.setAlignment(biui.Alignment.FILL)
	#pane3.addChild(pane3_2,1,1)
			
	lm = pane3.getLayoutManager()
	lm.setColumnWidths([0])
	lm.setRowHeights([0])
	
	# Drag buttons
	b0 = biui.Button()
	b0.onMouseDown.add(b0OnDown)
	b0.onMouseUp.add(b0OnUp)
	b0.setX(10)
	b0.setY(320)
	b0.setWidth(15)
	b0.setHeight(15)
	wnd.addChild(b0)
	
	
	b1 = biui.Button()
	b1.onMouseDown.add(b0OnDown)
	b1.onMouseUp.add(b0OnUp)
	b1.setX(295)
	b1.setY(295+310)
	b1.setWidth(15)
	b1.setHeight(15)
	wnd.addChild(b1)
	
	
	
	
	
	
	
	
	
	#
	# Temporary main loop
	#
	clock = pygame.time.Clock()
	
	radius = 100
	angle = 0
	speed = 0.01
	pos = [80.0,100.0]
	
	while biui.main():
		clock.tick(1000)
		
		# movement
		if False:
			angle += speed
			end = (
				pos[0]+math.cos(angle)*radius,
				pos[1]+math.sin(angle)*radius
			)
			b0.setX(end[0])		
			b0.setY(end[1])
		
	"""
	em = biui.EventManager()
	em.register(biui.EventTypes.MISC, eventHandler0 )
	em.register(biui.EventTypes.MISC, eventHandler1 )
	em.unregister(biui.EventTypes.MISC, eventHandler1 )
	em.pour( biui.EventTypes.MISC )
	"""
	
def eventHandler0(event = None):
	print("event0")

def eventHandler1(event = None):
	print("event1")

if __name__ == "__main__":
	main()