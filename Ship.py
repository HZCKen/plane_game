import pygame


class Ship(object):
    def __init__(self, screen, ai_setting):
        self.screen = screen
        self.icon_imgae = pygame.image.load("images/ship.bmp")
        self.rect = self.icon_imgae.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10

        self.is_move_left = False
        self.is_move_right = False
        self.is_move_up = False
        self.is_move_down = False
        self.ai_setting = ai_setting


    # 显示飞船
    def show(self):
        self.screen.blit(self.icon_imgae, self.rect)
    # 更新飞船位置
    def update(self):
        if self.is_move_left:
            self.__move_left()
        elif self.is_move_right:
            self.__move_right()
        elif self.is_move_up:
            self.__move_up()
        elif self.is_move_down:
            self.__move_down()

    # 向左
    def __move_left(self):
        if self.rect.left > 0:
            self.rect.centerx -= self.ai_setting.ship_speed_factor

    # 向右
    def __move_right(self):
        if self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_setting.ship_speed_factor

    # 向上
    def __move_up(self):
        if self.rect.top > self.screen_rect.top + self.ai_setting.ship_speed_factor:
            self.rect.top -= self.ai_setting.ship_speed_factor

    # 向下
    def __move_down(self):
        if self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += self.ai_setting.ship_speed_factor
