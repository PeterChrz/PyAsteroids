import pygame
import circleshape

# Base class for asteroid objects
class Asteroid(circleshape):
    def __init__(self, x, y, radius):
        #self.position = position
        #self.velocity = velocity
        #self.radius = radius
        #self.width = 2
        super().__init__(x,y,radius)
        
    def draw(self, screen):
        # sub-classes must override
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)


    def update(self, dt):
        # sub-classes must override
        self.position += self.velocity * dt