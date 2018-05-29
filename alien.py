import pygame


class Alien(object):
    def __init__(self, screen, ai_setting):
        self.screen = screen
        self.ai_setting = ai_setting
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def show(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += self.ai_setting.alien_speed_factor
        self.rect.x = self.x