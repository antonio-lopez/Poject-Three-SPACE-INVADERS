import pygame
from pygame.sprite import Sprite


class Pixel(Sprite):
    # tiny pixel that will be used to create a bunker
    def __init__(self, x, y, screen):
        super(Pixel, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/pixel.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
