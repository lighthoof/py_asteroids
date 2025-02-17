import pygame
from constants import *

def main():
    pygame.init()
    is_running = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(000000)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick()/1000

if __name__ == "__main__":
    main()