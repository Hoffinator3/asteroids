import pygame
from circleshape import CircleShape
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        
        split_one = self.velocity.rotate(angle)
        split_two = self.velocity.rotate(-angle)

        new_rad = self.radius - ASTEROID_MIN_RADIUS
        first_a = Asteroid(self.position.x, self.position.y, new_rad)
        first_a.velocity = split_one * 1.2
        second_a = Asteroid(self.position.x, self.position.y, new_rad)
        second_a.velocity = split_two * 1.2