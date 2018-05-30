import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, screen, ai_setting):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_setting = ai_setting
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)


    # 显示
    def show(self):
        self.screen.blit(self.image, self.rect)


    # 更新位置
    def update(self):
        self.x += (self.ai_setting.alien_speed_factor * self.ai_setting.fleet_direction)
        self.rect.x = self.x


    #  判断边界
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
