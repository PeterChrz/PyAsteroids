# this allows us to use code from
# the open-source pygame library
# throught this file

import pygame
import constants

def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    background_color = (0,0,0)

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(background_color)



if __name__ == "__main__":
    main()