import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    is_running = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create a clock and delta time instances
    clock = pygame.time.Clock()
    dt = 0

    # create groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # add clases to groups
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)

    # create class instances
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y) 
    asteroid_field = AsteroidField()

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # draw the background    
        screen.fill(000000)
        # handle the player
        updatables.update(dt)
        for drawable in drawables:
            drawable.draw(screen)
        # check for player collisions
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
        # check for bullet collisions
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()

        # update the screen
        pygame.display.flip()
        
        # limit the framerate to 60 fps
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()