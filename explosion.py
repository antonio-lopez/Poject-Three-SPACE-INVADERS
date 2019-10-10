import pygame
from os import path
from pygame.sprite import Sprite


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        # self.image = explosion_anim[self.size][0]
        self.image = pygame.image.load('alien_explosions/expl_11_0020.png')
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        explosion_anim = {'lg': []}
        for i in range(9):
            filename = 'expl_11_002{}.png'.format(i)
            img = pygame.image.load(path.join('alien_explosion', filename)).convert()
            img.set_colorkey(0, 0, 0)
            img_lg = pygame.transform.scale(img, (20, 19))
            explosion_anim['lg'].append(img_lg)
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
