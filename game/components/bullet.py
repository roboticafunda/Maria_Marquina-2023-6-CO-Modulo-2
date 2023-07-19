import pygame
from pygame.sprite import Sprite
from game.utils.constants import BULLET

class Bullet(Sprite):
    def __init__(self):
        super().__init__()
        self.image_x_factor = 10
        self.image_y_factor = 20
        self.movement_factor = 10
        self.image = BULLET
        self.image = pygame.transform.scale(self.image, (self.image_x_factor, self.image_y_factor))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= self.movement_factor  # Move the bullet upwards

        if self.rect.y < 0:  # If the bullet goes off the screen, remove it
            self.kill() # elimina el sprite (Bullet)