from dataclasses import dataclass as component
import pygame
import esper

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

my_font = pygame.font.SysFont('Comic Sans MS', 30)

class Player():
    def __init__(self):
        self.entity = esper.create_entity()
        esper.add_component(self.entity, Velocity(x=0.9, y=1.2))
        esper.add_component(self.entity, Position(x=5, y=5))
    
running = True
while running:
    screen.fill("purple")
    print("purple??")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw all players
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()