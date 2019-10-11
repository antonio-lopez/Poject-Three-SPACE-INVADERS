import pygame.font


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
                self.high_scores[int(key)] = int(val), val2

    def scores(self):
        test = pygame.image.load("images/bg_space_image.png")
        self.screen.blit(test, [0, 0])
        self.screen.blit(self.font.render('HIGH SCORES:', True, self.text_color), [self.x - 10, self.y - 50])
        self.screen.blit(self.font.render(str(self.high_scores[0]).strip('()').replace(',', ' -').replace("'", ''),
                                          True, self.text_color), [self.x, self.y + 450])
        self.screen.blit(self.font.render(str(self.high_scores[1]).strip('()').replace(',', ' -').replace("'", ''),
                                          True, self.text_color), [self.x, self.y])
        self.screen.blit(self.font.render(str(self.high_scores[2]).strip('()').replace(',', ' -').replace("'", ''),
                                          True, self.text_color), [self.x, self.y + 50])
        self.screen.blit(self.font.render(str(self.high_scores[3]).strip('()').replace(',', ' -').replace("'", ''),
                                          True, self.text_color), [self.x, self.y + 100])
        self.screen.blit(self.font.render(str(self.high_scores[4]).strip('()').replace(',', ' -').replace("'", ''),
                                          True, self.text_color), [self.x, self.y + 150])
        self.screen.blit(self.font.render(str(self.high_scores[5]).strip('()').replace(',', ' -').replace("'", ''),
                                          True, self.text_color), [self.x, self.y + 200])
        self.screen.blit(self.font.render(str(self.high_scores[6]).strip('()').replace(',', ' -').replace("'", ''),
                                          True, self.text_color), [self.x, self.y + 250])
        self.screen.blit(self.font.render(str(self.high_scores[7]).strip('()').replace(',', ' -').replace("'", ''),
                                          True, self.text_color), [self.x, self.y + 300])
        self.screen.blit(self.font.render(str(self.high_scores[8]).strip('()').replace(',', ' -').replace("'", ''),
                                          True, self.text_color), [self.x, self.y + 350])
        self.screen.blit(self.font.render(str(self.high_scores[9]).strip('()').replace(',', ' -').replace("'", ''),
                                          True, self.text_color), [self.x, self.y + 400])
        self.screen.blit(self.font.render('PRESS "SPACE" TO PLAY', True, self.text_color), [self.x - 70, self.y + 500])

    def get_lowest_score(self):
        return int(self.high_scores[9].__getitem__(0))

    def get_name(self):
        test = pygame.image.load("images/bg_space_image.png")
        self.screen.blit(test, [0, 0])
        self.screen.blit(self.font.render('ENTER INITIALS', True, self.text_color), [self.x, self.y])
        pygame.display.flip()

        cnt = 0
        initials = ''
        while cnt < 3:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        initials += 'A'
                        self.screen.blit(self.font.render(initials, True, self.text_color), [self.x, self.y + 50])
                        pygame.display.flip()
                        cnt += 1
                    elif event.key == pygame.K_b:
                        initials += 'B'
                        self.screen.blit(self.font.render(initials, True, self.text_color), [self.x, self.y + 50])
                        pygame.display.flip()
                        cnt += 1
                    elif event.key == pygame.K_c:
                        initials += 'C'
                        self.screen.blit(self.font.render(initials, True, self.text_color), [self.x, self.y + 50])
                        pygame.display.flip()
                        cnt += 1
                    elif event.key == pygame.K_d:
                        initials += 'D'
                        self.screen.blit(self.font.render(initials, True, self.text_color), [self.x, self.y + 50])
                        pygame.display.flip()
                        cnt += 1
                    elif event.key == pygame.K_e:
                        initials += 'E'
                        self.screen.blit(self.font.render(initials, True, self.text_color), [self.x, self.y + 50])
                        pygame.display.flip()
                        cnt += 1
                    elif event.key == pygame.K_f:
                        initials += 'F'
                        self.screen.blit(self.font.render(initials, True, self.text_color), [self.x, self.y + 50])
                        pygame.display.flip()
                        cnt += 1
                    elif event.key == pygame.K_g:
                        initials += 'G'
                        self.screen.blit(self.font.render(initials, True, self.text_color), [self.x, self.y + 50])
                        pygame.display.flip()
                        cnt += 1
                    elif event.key == pygame.K_h:
                        initials += 'H'
                        self.screen.blit(self.font.render(initials, True, self.text_color), [self.x, self.y + 50])
                        pygame.display.flip()
                        cnt += 1
                    elif event.key == pygame.K_i:
                        initials += 'I'
                        self.screen.blit(self.font.render(initials, True, self.text_color), [self.x, self.y + 50])
                        pygame.display.flip()
                        cnt += 1
                    elif event.key == pygame.K_j:
                        initials += 'J'
                        self.screen.blit(self.font.render(initials, True, self.text_color), [self.x, self.y + 50])
                        pygame.display.flip()
                        cnt += 1
                    elif event.key == pygame.K_k:
                        initials += 'K'
                        self.screen.blit(self.font.render(initials, True, self.text_color), [self.x, self.y + 50])
                        pygame.display.flip()
                        cnt += 1
                    elif event.key == pygame.K_l:
                        initials += 'L'
                        self.screen.blit(self.font.render(initials, True, self.text_color), [self.x, self.y + 50])
                        pygame.display.flip()
                        cnt += 1
                    elif event.key == pygame.K_m:
                        initials += 'M'
                        self.screen.blit(self.font.render(initials, True, self.text_color), [self.x, self.y + 50])
                        pygame.display.flip()
                        cnt += 1
                    elif event.key == pygame.K_n:
                        initials += 'N'
                        self.screen.blit(self.font.render(initials, True, self.text_color), [self.x, self.y + 50])
                        pygame.display.flip()
                        cnt += 1
                    elif event.key == pygame.K_o:
                        initials += 'O'
                        self.screen.blit(self.font.render(initials, True, self.text_color), [self.x, self.y + 50])
                        pygame.display.flip()
                        cnt += 1
                    elif event.key == pygame.K_p:
                        initials += 'P'
                        self.screen.blit(self.font.render(initials, True, self.text_color), [self.x, self.y + 50])
                        pygame.display.flip()
                        cnt += 1
                    elif event.key == pygame.K_q:
                        initials += 'Q'
                        self.screen.blit(self.font.render(initials, True, self.text_color), [self.x, self.y + 50])
                        pygame.display.flip()
                        cnt += 1
                    elif event.key == pygame.K_r:
                        initials += 'R'
                        self.screen.blit(self.font.render(initials, True, self.text_color), [self.x, self.y + 50])
                        pygame.display.flip()
                        cnt += 1
                    elif event.key == pygame.K_s:
                        initials += 'S'
                        self.screen.blit(self.font.render(initials, True, self.text_color), [self.x, self.y + 50])
                        pygame.display.flip()
                        cnt += 1
                    elif event.key == pygame.K_t:
                        initials += 'T'
                        self.screen.blit(self.font.render(initials, True, self.text_color), [self.x, self.y + 50])
                        pygame.display.flip()
                        cnt += 1
                    elif event.key == pygame.K_u:
                        initials += 'U'
                        self.screen.blit(self.font.render(initials, True, self.text_color), [self.x, self.y + 50])
                        pygame.display.flip()
                        cnt += 1
                    elif event.key == pygame.K_v:
                        initials += 'V'
                        self.screen.blit(self.font.render(initials, True, self.text_color), [self.x, self.y + 50])
                        pygame.display.flip()
                        cnt += 1
                    elif event.key == pygame.K_w:
                        initials += 'W'
                        self.screen.blit(self.font.render(initials, True, self.text_color), [self.x, self.y + 50])
                        pygame.display.flip()
                        cnt += 1
                    elif event.key == pygame.K_x:
                        initials += 'X'
                        self.screen.blit(self.font.render(initials, True, self.text_color), [self.x, self.y + 50])
                        pygame.display.flip()
                        cnt += 1
                    elif event.key == pygame.K_y:
                        initials += 'Y'
                        self.screen.blit(self.font.render(initials, True, self.text_color), [self.x, self.y + 50])
                        pygame.display.flip()
                        cnt += 1
                    elif event.key == pygame.K_z:
                        initials += 'Z'
                        self.screen.blit(self.font.render(initials, True, self.text_color), [self.x, self.y + 50])
                        pygame.display.flip()
                        cnt += 1
                    elif event.key == pygame.K_BACKSPACE:
                        if cnt > 0:
                            initials = initials[:-1]
                            self.screen.blit(test, [0, 0])
                            self.screen.blit(self.font.render('TYPE IN INITIALS', True, self.text_color),
                                             [self.x, self.y])
                            self.screen.blit(self.font.render(initials, True, self.text_color), [self.x, self.y + 50])
                            pygame.display.flip()
                            cnt -= 1
        return initials

    def add_score(self, name, score):

        self.high_scores[10] = score, name
        sorted_scores = sorted(self.high_scores.values(), reverse=True)
        self.high_scores = sorted_scores
        print(self.high_scores)

        f = open("scores.txt", "w+")

        for i in range(9):
            f.write(str(i) + " " + str(self.high_scores[i]).strip('()').replace(',', '').replace("'", '') + '\n')

        f.write("9 " + str(self.high_scores[9]).strip('()').replace(',', '').replace("'", ''))
