import pygame.font
from pygame.sprite import Group


class HighScore:
    def __init__(self, screen):
        self.screen = screen
        self.text_color = (255, 255, 255)
        self.black = (0, 0, 0)
        self.high_scores = {}
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.x = 200
        self.y = 100

        with open("scores.txt") as file:
            for line in file:
                (key, val, val2) = line.split()
                self.high_scores[int(key)] = val, val2

    def scores(self):
        test = pygame.image.load("images/bg_space_image.png")
        self.screen.blit(test, [0, 0])
        self.screen.blit(self.font.render('HIGH SCORES:', True, self.text_color), [self.x - 10, self.y - 50])
        self.screen.blit(self.font.render(str(self.high_scores[1]).strip('()').replace(',', ' -').replace("'", ''), True,
                                          self.text_color), [self.x, self.y])
        self.screen.blit(self.font.render(str(self.high_scores[2]).strip('()').replace(',', ' -').replace("'", ''), True,
                                          self.text_color), [self.x, self.y + 50])
        self.screen.blit(self.font.render(str(self.high_scores[3]).strip('()').replace(',', ' -').replace("'", ''), True,
                                          self.text_color), [self.x, self.y + 100])
        self.screen.blit(self.font.render(str(self.high_scores[4]).strip('()').replace(',', ' -').replace("'", ''), True,
                                          self.text_color), [self.x, self.y + 150])
        self.screen.blit(self.font.render(str(self.high_scores[5]).strip('()').replace(',', ' -').replace("'", ''), True,
                                          self.text_color), [self.x, self.y + 200])
        self.screen.blit(self.font.render(str(self.high_scores[6]).strip('()').replace(',', ' -').replace("'", ''), True,
                                          self.text_color), [self.x, self.y + 250])
        self.screen.blit(self.font.render(str(self.high_scores[7]).strip('()').replace(',', ' -').replace("'", ''), True,
                                          self.text_color), [self.x, self.y + 300])
        self.screen.blit(self.font.render(str(self.high_scores[8]).strip('()').replace(',', ' -').replace("'", ''), True,
                                          self.text_color), [self.x, self.y + 350])
        self.screen.blit(self.font.render(str(self.high_scores[9]).strip('()').replace(',', ' -').replace("'", ''), True,
                                          self.text_color), [self.x, self.y + 400])
        self.screen.blit(
            self.font.render(str(self.high_scores[10]).strip('()').replace(',', ' -').replace("'", ''), True,
                             self.text_color), [self.x, self.y + 450])
        self.screen.blit(self.font.render('PRESS "SPACE" TO PLAY', True, self.text_color), [self.x - 70, self.y + 500])

    def get_lowest_score(self):
        return int(self.high_scores[10].__getitem__(1))
