import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    is_running = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create a clock and delta time instances
    clock = pygame.time.Clock()
    dt = 0

    # create a player instance
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y) 

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # draw the background    
        screen.fill(000000)
        # handle the player
        player.update(dt)
        player.draw(screen)
        # update the screen
        pygame.display.flip()
        
        # limit the framerate to 60 fps
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()