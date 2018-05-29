import pygame
import time
from setting import Setting
from Ship import Ship
import game_function as gf
from alien import Alien

def run_game():
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height), 0, 0)
    pygame.display.set_caption("AlienInvasion")
    ai_ship = Ship(screen, ai_setting)
    bullet_list = []
    alien_list = []
    gf.create_alien_list(ai_setting, screen, ai_ship, alien_list)

    while True:

        gf.check_events(ai_setting, screen, ai_ship, bullet_list)
        gf.update_bullets(bullet_list)
        gf.update_screen(ai_setting, screen, ai_ship, alien_list, bullet_list)
        time.sleep(0.01)


if __name__ == '__main__':
    run_game()
