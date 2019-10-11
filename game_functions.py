import sys
import pygame
import random
from bullet import Bullet
from alien import Alien
from alien_b import AlienB
from alien_c import AlienC
from alien_bullet import AlienBullet
from ufo import UFO
from high_score import HighScore
from time import sleep
fps = pygame.time.Clock()

"""
def alien_c_explosion(aliens_c):
    alien_explode = ['alien_explosion/expl_11_0020.png', 'alien_explosion/expl_11_0021.png',
                     'alien_explosion/expl_11_0022.png', 'alien_explosion/expl_11_0023.png']
    for num in range(4):
        aliens_c.image = pygame.image.load(alien_explode[num])
        aliens_c.update()
        aliens_c.blitme()
        pygame.display.flip()
        pygame.time.wait(50)
"""


def alien_shooting(ai_settings, screen, ship, alien_bullets, aliens):
    alien_bullets.update()
    # Get rid of bullets that have disappeared.
    for alien in aliens.sprites():
        i = alien.rect.y

    # if len(alien_bullets) < ai_settings.bullets_allowed:
        bullet_sound = pygame.mixer.Sound("sounds/fire_sound.ogg")
        pygame.mixer.Sound.play(bullet_sound)
        new_bullet = AlienBullet(ai_settings, screen, ship, i)
        alien_bullets.add(new_bullet)


def check_key_down_events(event, ai_settings, screen, ship, bullets, alien_bullets, aliens):
    """respond to key presses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # create a new bullet and add it to the bullets group
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_r:
        alien_shooting(ai_settings, screen, ship, alien_bullets, aliens)


def check_key_up_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, aliens_b, aliens_c, bullets):
    """check if any aliens have reached the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # treat this the same as if the ship got hit
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, aliens_b, aliens_c, bullets)
            break
    for alien in aliens_b.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, aliens_b, aliens_c, bullets)
            break
    for alien in aliens_c.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # treat this the same as if the ship got hit
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, aliens_b, aliens_c, bullets)
            break


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, aliens_b, aliens_c, bullets, alien_bullets):
    """respond to key presses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, aliens_b, aliens_c,
                              bullets, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, ai_settings, screen, ship, bullets, alien_bullets, aliens)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, aliens_b, aliens_c, bullets,
                      mouse_x, mouse_y):
    # start a new game when player clicks play
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        pygame.mixer.music.load('sounds/bg_music.ogg')
        pygame.mixer.music.play(-1)
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # Empty the list of aliens and bullets.
        aliens.empty()
        aliens_b.empty()
        aliens_c.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, aliens)
        create_b_fleet(ai_settings, screen, ship, aliens_b)
        create_c_fleet(ai_settings, screen, ship, aliens_c)
        ship.center_ship()


def check_fleet_edges(ai_settings, aliens, aliens_b, aliens_c):
    # respond appropriately if any aliens have reached an edge
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens, aliens_b, aliens_c)
            break
    for alien in aliens_b.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens, aliens_b, aliens_c)
            break
    for alien in aliens_c.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens, aliens_b, aliens_c)
            break


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, aliens_b, aliens_c, bullets):
    # respond to bullet-alien collisions
    # check for any bullets that have hit aliens
    # if so, get rid of the bullet and alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    collisions_b = pygame.sprite.groupcollide(bullets, aliens_b, True, True)
    collisions_c = pygame.sprite.groupcollide(bullets, aliens_c, True, True)

    if collisions:
        alien_death = pygame.mixer.Sound("sounds/alien_explode.ogg")
        pygame.mixer.Sound.play(alien_death)
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    elif collisions_b:
        alien_death = pygame.mixer.Sound("sounds/alien_explode.ogg")
        pygame.mixer.Sound.play(alien_death)
        for aliens_b in collisions_b.values():
            stats.score += ai_settings.alien_b_points * len(aliens_b)
            sb.prep_score()
        check_high_score(stats, sb)
    elif collisions_c:
        alien_death = pygame.mixer.Sound("sounds/alien_explode.ogg")
        pygame.mixer.Sound.play(alien_death)
        for aliens_c in collisions_c.values():
            stats.score += ai_settings.alien_c_points * len(aliens_c)
            sb.prep_score()
        check_high_score(stats, sb)

    # remove any bullets and aliens that have collided
    if len(aliens) == 0:
        # Destroy existing bullets and create new fleet.
        bullets.empty()
        ai_settings.increase_speed()

        # Increase level.
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, aliens)
        create_b_fleet(ai_settings, screen, ship, aliens_b)
        create_c_fleet(ai_settings, screen, ship, aliens_c)

    if len(aliens_b) == 0:
        # If the entire fleet is destroyed, start a new level.
        # aliens.empty()
        # aliens_b.empty()
        bullets.empty()
        ai_settings.increase_speed()

        # Increase level.
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, aliens)
        create_b_fleet(ai_settings, screen, ship, aliens_b)
        create_c_fleet(ai_settings, screen, ship, aliens_c)

    if len(aliens_c) == 0:
        # If the entire fleet is destroyed, start a new level.
        # aliens.empty()
        # aliens_b.empty()
        bullets.empty()
        ai_settings.increase_speed()

        # Increase level.
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, aliens)
        create_b_fleet(ai_settings, screen, ship, aliens_b)
        create_c_fleet(ai_settings, screen, ship, aliens_c)


def check_bullet_ufo_collisions(ai_settings, screen, stats, sb, bullets, ufos):
    collisions = pygame.sprite.groupcollide(bullets, ufos, True, True)
    random_score = random.randint(200, 1000)
    if collisions:
        for ufo in ufos:
            ufos.remove(ufo)

        stats.score += random_score
        sb.prep_score()
        sb.prep_high_score()
        sb.show_score()


def check_alien_bullet_ship_collisions(si_settings, screen, stats, sb, ship, aliens, aliens_b, aliens_c, bullets,
                                       alien_bullets):
    collisions = pygame.sprite.spritecollideany(ship, alien_bullets)

    if collisions:
        for bullet in alien_bullets:
            alien_bullets.remove(bullet)
        alien_bullets.update()
        ship_hit(si_settings, screen, stats, sb, ship, aliens, aliens_b, aliens_c, bullets)
        stats.level -= 1


def check_bunker_collisions(bullets, alien_bullets, bunkers):

    for bunker in bunkers:
        for pixel in bunker.bunker:
            bullet_collisions = shot = pygame.sprite.spritecollideany(pixel, bullets)
            if bullet_collisions:
                shot = pygame.sprite.spritecollideany(pixel, bullets)
                if shot:
                    for bullet in bullets:
                        bullets.remove(bullet)
                    pixel.remove(bunker.bunker)

    for bunker in bunkers:
        for pixel in bunker.bunker:
            bullet_collisions = shot = pygame.sprite.spritecollideany(pixel, alien_bullets)
            if bullet_collisions:
                shot = pygame.sprite.spritecollideany(pixel, alien_bullets)
                if shot:
                    for bullet in alien_bullets:
                        alien_bullets.remove(bullet)
                    pixel.remove(bunker.bunker)


def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def change_fleet_direction(ai_settings, aliens, aliens_b, aliens_c):
    # drop the entire fleet and change the fleet's direction
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    for alien in aliens_b.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    for alien in aliens_c.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # create an alien and place it in the row
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * (row_number + 2)
    aliens.add(alien)


def create_alien_b(ai_settings, screen, aliens_b, alien_b_number, row_number):
    # create an alien and place it in the row
    alien_b = AlienB(ai_settings, screen)
    alien_width_b = alien_b.rect.width
    alien_b.x = alien_width_b + 2 * alien_width_b * alien_b_number
    alien_b.rect.x = alien_b.x
    alien_b.rect.y = alien_b.rect.height + 2 * alien_b.rect.height * (row_number + 5)
    aliens_b.add(alien_b)


def create_alien_c(ai_settings, screen, aliens_c, alien_c_number, row_number):
    # create an alien and place it in the row
    alien_c = AlienC(ai_settings, screen)
    alien_width_c = alien_c.rect.width
    alien_c.x = alien_width_c + 2 * alien_width_c * alien_c_number
    alien_c.rect.x = alien_c.x
    alien_c.rect.y = alien_c.rect.height + 2 * alien_c.rect.height * (row_number + 7)
    aliens_c.add(alien_c)


def create_fleet(ai_settings, screen, aliens):
    # create a full fleet of aliens
    # create an alien and find the number of aliens in a row
    # spacing between each alien is equal to one alien width
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    row_number = 2
    # create the first row of aliens
    for row_number in range(row_number):
        for alien_number in range(number_aliens_x):
            # create an alien and place it in the row
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def create_b_fleet(ai_settings, screen, ship, aliens_b):
    row_number = 2
    alien = AlienB(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    for row_number in range(row_number):
        for alien_number in range(number_aliens_x):
            create_alien_b(ai_settings, screen, aliens_b, alien_number, row_number)


def create_c_fleet(si_settings, screen, ship, aliens_c):
    row_number = 2
    alien = AlienC(si_settings, screen)
    number_aliens_x = get_number_aliens_x(si_settings, alien.rect.width)
    for row_number in range(row_number):
        for alien_number in range(number_aliens_x):
            create_alien_c(si_settings, screen, aliens_c, alien_number, row_number)


def create_ufo(ai_settings, screen, ufos):
    ufo = UFO(ai_settings, screen)
    ufo.rect.y = random.randint(20, 80)
    ufos.add(ufo)


def fire_bullet(ai_settings, screen, ship, bullets):
    # fire a bullet if limit not reached
    # create a new bullet and add it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        bullet_fire = pygame.mixer.Sound("sounds/fire_sound.ogg")
        pygame.mixer.Sound.play(bullet_fire)
        # pygame.mixer.music.load('fire_sound.ogg')
        # pygame.mixer.music.play(0)
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    # determine the number of aliens that fit in a row
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def random_ufo(ai_settings, screen, ufos):
    if ufos.__len__() == 0:
        if random.randint(1, 2000) == 10:         # change for even more random
            create_ufo(ai_settings, screen, ufos)


def random_alien_shoot(ai_settings, screen, ship, alien_bullets, aliens):
    if random.randint(1, 4000) == 25:
        alien_shooting(ai_settings, screen, ship, alien_bullets, aliens)


def ship_explosion(ship):
    ship_images = ['ship_explosion/expl_02_0012.png', 'ship_explosion/expl_02_0013.png',
                   'ship_explosion/expl_02_0014.png', 'ship_explosion/expl_02_0015.png',
                   'ship_explosion/expl_02_0016.png', 'ship_explosion/expl_02_0017.png',
                   'ship_explosion/expl_02_0018.png', 'ship_explosion/expl_02_0019.png',
                   'ship_explosion/expl_02_0020.png', 'ship_explosion/expl_02_0021.png',
                   'ship_explosion/expl_02_0022.png', 'ship_explosion/expl_02_0023.png']
    for num in range(12):
        ship.image = pygame.image.load(ship_images[num])
        ship.update()
        ship.blitme()
        pygame.display.flip()
        pygame.time.wait(100)


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, aliens_b, aliens_c, bullets):
    # respond to ship being hit by alien
    if stats.ships_left > 0:
        explode_sound = pygame.mixer.Sound("sounds/ship_explode.ogg")
        pygame.mixer.Sound.play(explode_sound)

        # decrement ships_left
        stats.ships_left -= 1
        ship_explosion(ship)

        # Update scoreboard.
        sb.prep_ships()

        # empty the list of aliens and bullets
        aliens.empty()
        aliens_b.empty()
        aliens_c.empty()
        bullets.empty()

        # create a new fleet and center the ship
        create_fleet(ai_settings, screen, aliens)
        ship.center_ship()

        # pause
        sleep(0.1)
        ship.image = pygame.image.load("images/ship.png")

    else:
        hs = HighScore(screen)
        if stats.score > hs.get_lowest_score():
            new_name = hs.get_name()
            hs.add_score(new_name, stats.score)
            print(stats.score)

            open_score_window = True
            hs.scores()
            pygame.display.flip()

            while open_score_window == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            open_score_window = False

        stats.game_active = False
        pygame.mouse.set_visible(True)


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, aliens_b, aliens_c, bullets):
    # check if the fleet is at an edge and then update
    # the positions of all aliens in the fleet
    check_fleet_edges(ai_settings, aliens, aliens_b, aliens_c)

    # update the positions of all aliens in the fleet
    aliens.update()
    aliens_b.update()
    aliens_c.update()

    # look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, aliens_b, aliens_c, bullets)

    # look for aliens hitting the bottom of the screen
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, aliens_b, aliens_c, bullets)


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, aliens_b, aliens_c, bullets):
    # update position of bullets and get rid of old bullets
    # update bullet position
    bullets.update()

    # get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, aliens_b, aliens_c, bullets)


def update_alien_bullets(si_settings, screen, stats, sb, ship, alien_bullets):
    alien_bullets.update()
    for bullet in alien_bullets.copy():
        if bullet.rect.y <= 0:
            alien_bullets.remove(bullet)


def update_screen(ai_settings, screen, ship, stats, sb, aliens, aliens_b, aliens_c, bullets, play_button,
                  alien_bullets, ufos, bunker):
    # update images on the screen and flip to the new screen
    # redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)

    # redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for bullet in alien_bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    aliens_b.draw(screen)
    aliens_c.draw(screen)
    ufos.draw(screen)

    # draw the score information
    sb.show_score()
    for bunk in bunker:
        bunk.draw_bunker()

    # draw the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()

    # make the most recently drawn screen visible
    pygame.display.flip()


def update_ufo(ufos):
    ufos.update()
