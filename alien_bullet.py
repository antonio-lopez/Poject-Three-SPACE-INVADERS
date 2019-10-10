import pygame
from pygame.sprite import Sprite


class AlienBullet(Sprite):
    def __init__(self, ai_settings, screen, ship, pace):
        """Create a bullet object at the ship's current position."""
        super(AlienBullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = 10 + pace

        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.alien_bullet_speed_factor

    def update(self):
        self.y += self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
