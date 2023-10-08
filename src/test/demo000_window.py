import math
import biui

sub = None
wnd = None
pane3 = None
widget = None
localPos = None

def main():
	global wnd, pane3, widget
	
	biui.init()
	biui.setThemeFolder("../../themes")
		
	################################################
	###                                       WINDOW
	################################################
	wnd = biui.Window(1024,768)
	
	widget = biui.Pane()
	widget.width = widget.height = 30
	widget.x = widget.y = 100
	
	wnd.addChild(widget)
	###
	### Temporary main loop
	###
	###clock = pygame.time.Clock()
	
	radius = 100
	angle = 0
	speed = 0.01
	
	while biui.main():
		
		### movement
		angle += speed
		
		widget.width = 100 + math.cos(angle)*50
		widget.height = 100 + math.sin(angle)*50
		widget.x = 300 + math.cos(angle)*200 - widget.width/2
		widget.y = 300 + math.sin(angle)*200 - widget.height/2

		
		###print( biui.getTheme().getImageLibrary().getSize())
		###biui.getTheme().getImageLibrary().clearCache()
		
if __name__ == "__main__":
	main()