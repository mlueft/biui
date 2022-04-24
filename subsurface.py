import pygame

pygame.init()

wnd = pygame.display.set_mode( (1024, 768), pygame.RESIZABLE, vsync=1 )

rect = pygame.Rect(-10, 100, 100, 100)
sub = wnd.subsurface(rect)

sub.fill( (0, 255, 0) )

pygame.draw.circle( sub, (255, 255, 255),(0,0),100 )

clock = pygame.time.Clock()
 
while 1:
    
    pygame.display.update()
    clock.tick(1000)