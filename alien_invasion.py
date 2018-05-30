import pygame
import time
from setting import Setting
from Ship import Ship
import game_function as gf
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height), 0, 0)
    pygame.display.set_caption("AlienInvasion")
    ai_ship = Ship(screen, ai_setting)
    bullet_list = Group()
    alien_list = Group()
    gf.create_alien_list(ai_setting, screen, ai_ship, alien_list)

    while True:

        gf.check_events(ai_setting, screen, ai_ship, bullet_list)
        gf.update_bullets(bullet_list, alien_list, ai_setting, ai_ship, screen)
        gf.update_screen(ai_setting, screen, ai_ship, alien_list, bullet_list)
        gf.update_aliens(ai_setting, alien_list, ai_ship)
        time.sleep(0.01)


if __name__ == '__main__':
    run_game()
