import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, ai_setting, screen, ship, bullet_list):
    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
        ship.is_move_left = True
    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        ship.is_move_right = True
    elif event.key == pygame.K_w or event.key == pygame.K_UP:
        ship.is_move_up = True
    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
        ship.is_move_down = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_setting, screen, ship, bullet_list)


def check_keyup_events(event, ship):
    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
        ship.is_move_left = False
    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        ship.is_move_right = False
    elif event.key == pygame.K_w or event.key == pygame.K_UP:
        ship.is_move_up = False
    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
        ship.is_move_down = False


def check_events(ai_setting, screen, ship, bullet_list):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_setting, screen, ship, bullet_list)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def fire_bullet(ai_setting, screen, ship, bullet_list):
    new_bullet = Bullet(ai_setting, screen, ship)
    bullet_list.add(new_bullet)
    new_bullet.draw_bullet()


def update_bullets(bullet_list):
    bullet_list.update()
    for bullet in bullet_list.copy():
        if bullet.rect.bottom <= 0:
            bullet_list.remove(bullet)


def uodate_screen(ai_setting, screen, ship, bullet_list):
    pygame.display.update()
    screen.fill(ai_setting.backgrounColor)
    ship.show_ship()
    ship.update()
    for bullet in bullet_list:
        bullet.draw_bullet()
