import pygame
from pygame.sprite import Sprite


class AlienB(Sprite):
    # a class to represent a single alien in the fleet
    def __init__(self, ai_settings, screen):
        # initialize the alien and set its starting position
        super(AlienB, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the alien image and set its rect attribute
        self.image = pygame.image.load('images/enemy2_a.png')
        self.rect = self.image.get_rect()

        # start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's exact position
        self.x = float(self.rect.x)
        self.cnt = 1
        self.swap = False

    def blitme(self):
        # draw the alien at its current location
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        # return True if alien is at the edge of screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        # move alien to the right
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

        # animate alien
        if self.cnt < 50:
            self.cnt = self.cnt + 1
        elif self.swap and self.cnt == 50:
            self.cnt = 1
            self.image = pygame.image.load('images/enemy2_b.png')
            self.swap = False
        elif not self.swap and self.cnt == 50:
            self.cnt = 1
            self.image = pygame.image.load('images/enemy2_a.png')
            self.swap = True
