import pygame
import math
import biui

sub = None
wnd = None
pane3 = None
b0 = None
b1 = None
localPos = None

def main():
	global wnd, pane3, b0, b1
	
	##############################################
	#                                       WINDOW
	##############################################
	wnd = biui.Window()
	wnd.setWidth(1024)
	wnd.setHeight(768)
	
	
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

if __name__ == "__main__":
	main()