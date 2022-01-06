import pygame
import math

import biui
import pygame.locals

screen = None

def init():
	global screen

def main():
	
	wnd = biui.Window()
	wnd.setWidth(1024)
	wnd.setHeight(768)
	
	pane0 = biui.Pane()
	pane0.setX(100)
	pane0.setY(100)
	pane0.setWidth(300)
	pane0.setHeight(300)
	wnd.addChild(pane0)
	
	pane1 = biui.Pane()
	pane1.setX(50)
	pane1.setY(50)
	pane1.setWidth(300)
	pane1.setHeight(300)
	#wnd.addChild(pane1)
	
	b0 = biui.Button()
	b0.setX(10)
	b0.setY(10)
	pane1.addChild(b0)
	
	pane0.addChild(pane1)
	
	pane3 = biui.Pane()
	pane3.setX(650)
	pane3.setY(50)
	pane3.setWidth(300)
	pane3.setHeight(300)
	#wnd.addChild(pane1)
	
	b1 = biui.Button()
	b1.setX(10)
	b1.setY(10)
	pane3.addChild(b1)
		
	wnd.addChild(pane3)
	
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
		if True:
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