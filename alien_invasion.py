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
    aliens = Group()

    # create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # start the main loop for the game
    while True:
        # watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()

            # redraw the screen during each pass through the loop
            # make the most recently drawn screen visible
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, stats, sb, aliens, bullets, play_button)


run_game()
