# this allows us to use code from
# the open-source pygame library
# throught this file

import sys
import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    background_color = (0,0,0)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    dt = 0

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return



        #updatable
        updatable.update(dt)
        #drawable.update(dt)
        #print(drawable)
        #drawable

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()


        screen.fill(background_color)

        for obj in drawable:
            obj.draw(screen)
        #player.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()