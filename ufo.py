import pygame
from pygame.sprite import Sprite


class UFO(Sprite):
    def __init__(self, ai_settings, screen):
        super(UFO, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/mysterya.png')
        self.rect = self.image.get_rect()
        self.rect.x = -100
        self.rect.y = 100
        # Store the UFOS's exact position.
        # self.x = -100
        # self.y = 200

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def move(self):
        # self.rect.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.rect.x + 1