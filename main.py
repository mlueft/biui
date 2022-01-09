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

def init():
	global screen
	
def main():
	
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
	init()
	main()