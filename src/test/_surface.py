import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))


sprite = pygame.surface.Surface((100,100))
pygame.draw.circle( sprite, (255,0,0), (50,50),50 )
screen.blit( sprite, (10,10), (50,50,50,50) )

def test(surface):
    surface.fill((255,10,10))
    
test( screen )

pygame.display.update()

while True:
    events =  pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            break
        
pygame.quit()