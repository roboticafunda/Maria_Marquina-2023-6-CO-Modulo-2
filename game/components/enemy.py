import random
import pygame
from pygame.sprite import Sprite
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy(Sprite):
    def __init__(self, name, image):
        super().__init__()
        self.image_x_factor = 40
        self.image_y_factor = 60
        self.movement_factor = 5
        self.image_x_init = (SCREEN_WIDTH // 2) - self.image_x_factor
        self.image = image
        self.image = pygame.transform.scale(self.image, (self.image_x_factor, self.image_y_factor))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.image_x_factor)  # Random x-coordinate # self.image_x_init
        self.rect.y = -self.image_y_factor
        self.name = name

    def update(self):
        self.rect.y += self.movement_factor
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = -self.image_y_factor
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.image_x_factor)  # Random x-coordinate

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        font = pygame.font.Font(None, 20)
        label = font.render(self.name, True, (255, 255, 255))
        screen.blit(label, (self.rect.x, self.rect.y - 30))