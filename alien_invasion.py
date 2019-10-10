import pygame
import sys
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
import game_functions as gf
from high_score import HighScore



def run_game():
    """initialize game and create a screen object"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    screen.fill([255, 255, 255])
    test = pygame.image.load("images/startup_image.png")
    screen.blit(test, [0, 0])
    pygame.display.flip()

    high_score = HighScore(screen)

    endintro = False
    openhighscore = False
    while endintro == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    endintro = True
                elif event.key == pygame.K_s:
                    endintro = True
                    openhighscore = True

    if openhighscore:
        high_score.scores()
        pygame.display.flip()

    while openhighscore == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    openhighscore = False

    play_button = Button(ai_settings, screen, "Play")
    # create an instance to store game statistics
    stats = GameStats(ai_settings)
    # Create an instance to store game statistics and create a scoreboard.
    sb = Scoreboard(ai_settings, screen, stats)

    # make a ship, group of bullets, and a group of aliens
    ship = Ship(ai_settings, screen)
    # make a group to store bullets in
    bullets = Group()
    alien_bullets = Group()
    aliens = Group()
    aliens_b = Group()
    aliens_c = Group()
    ufos = Group()

    # create the fleet of aliens
    gf.create_fleet(ai_settings, screen, aliens)
    gf.create_b_fleet(ai_settings, screen, ship, aliens_b)
    gf.create_c_fleet(ai_settings, screen, ship, aliens_c)
    gf.create_ufo(ai_settings, screen, ufos)

    # start the main loop for the game
    while True:
        # watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, aliens_b, aliens_c,
                        bullets, alien_bullets)
        if stats.game_active:
            ship.update()
            gf.random_ufo(ai_settings, screen, ufos)
            # gf.update_ufo(ufos)
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, aliens_b, aliens_c, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, aliens_b, aliens_c, bullets)
            gf.update_alien_bullets(ai_settings, screen, stats, sb, ship, alien_bullets)
            gf.random_alien_shoot(ai_settings, screen, ship, alien_bullets, aliens)
            gf.check_alien_bullet_ship_collisions(ai_settings, screen, stats, sb, ship, aliens, aliens_b, aliens_c,
                                                  bullets, alien_bullets)
            gf.check_bullet_ufo_collisions(ai_settings, screen, stats, sb, bullets, ufos)
            if ufos.__len__() > 0:
                for ufo in ufos.copy():
                    ufo.move()
                    if ufo.rect.x > 600:
                        ufos.remove(ufo)
                        print("its gone")

        bullets.update()
        alien_bullets.update()

        gf.update_screen(ai_settings, screen, ship, stats, sb, aliens, aliens_b, aliens_c, bullets,
                         play_button, alien_bullets, ufos)


run_game()
