import sys
import pygame
from setting import Setting


def run_game():
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height), 0, 0)
    pygame.display.set_caption("AlienInvasion")
    while True:
        pygame.display.flip()
        screen.fill(ai_setting.backgrounColor)
        image = pygame.image.load("images/ship.bmp")
        screen.blit(image, (100, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


run_game()
