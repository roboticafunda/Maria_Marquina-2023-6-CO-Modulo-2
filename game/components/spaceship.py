import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH

# Spaceship es una clase derivada(hija) de la clase Sprite (Herencia)
class Spaceship(Sprite):
    def __init__(self, name):
        self.image_x_factor = 40
        self.image_y_factor = 60
        self.movement_factor = 10
        self.image_x_init = (SCREEN_WIDTH // 2) - self.image_x_factor
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.image_x_factor, self.image_y_factor))
        self.rect = self.image.get_rect()
        self.rect.x = self.image_x_init
        self.rect.y = self.image_y_factor
        self.name = name

    def update(self, events):
        if events[pygame.K_RIGHT]:
            self.move_right()
        elif events[pygame.K_LEFT]:
            self.move_left()

    def move_right(self):
        if self.rect.x < SCREEN_WIDTH:
            print(f"moving to the right with {self.movement_factor} blocks starting from", self.rect.x)
            self.rect.x += self.movement_factor
        else:
            self.rect.x = self.image_x_init

    def move_left(self):
        if self.rect.x > 0:
            print(f"moving to the left with  {self.movement_factor} blocks starting from", self.rect.x)
            self.rect.x -= self.movement_factor
        else:
            self.rect.x = self.image_x_init
        
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        font = pygame.font.Font(None, 20)  # Choose a font and size for the label
        label = font.render(self.name, True, (255, 255, 255))  # Create a label surface
        screen.blit(label, (self.rect.x, self.rect.y - 20))  # Draw the label above the spaceship
