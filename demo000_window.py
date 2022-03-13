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
	wnd.width = 1024
	wnd.height = 768
	
	
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
			b0.x = end[0]		
			b0.y = end[1]

if __name__ == "__main__":
	main()