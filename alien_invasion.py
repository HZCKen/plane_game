import pygame
import time
from setting import Setting
from Ship import Ship



def run_game():
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height), 0, 0)
    pygame.display.set_caption("AlienInvasion")
    ai_ship = Ship(screen)

    while True:
        pygame.display.update()
        screen.fill(ai_setting.backgrounColor)
        ai_ship.show_ship()
        ai_ship.move_event()




if __name__ == '__main__':

    run_game()
