import pygame
import sys
from enum import Enum


class MoveDirection(Enum):
    stop = 0
    up = 1
    down = 2
    left = 3
    right = 4


class Ship(object):
    def __init__(self, screen):
        self.screen = screen
        self.icon_imgae = pygame.image.load("images/ship.bmp")
        self.rect = self.icon_imgae.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10
        self.__direction = MoveDirection.stop

    # 显示飞船
    def show_ship(self):
        self.screen.blit(self.icon_imgae, self.rect)

    # 飞船监听事件移动
    def move_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.__direction = MoveDirection.left
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.__direction = MoveDirection.right
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.__direction = MoveDirection.up
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.__direction = MoveDirection.down
                elif event.key == pygame.K_q:
                    sys.exit()
            elif event.type == pygame.KEYUP:
                self.__direction = MoveDirection.stop
        self.__move()

    # 向左
    def __move_left(self):
        self.rect.centerx -= 5
        if self.rect.centerx - (self.rect.width / 2) <= 0:
            self.rect.centerx = self.rect.width / 2

    # 向右
    def __move_right(self):
        self.rect.centerx += 5
        if self.rect.centerx + (self.rect.width / 2) >= self.screen_rect.width:
            self.rect.centerx = self.screen_rect.width - (self.rect.width / 2)

    # 向上
    def __move_up(self):
        self.rect.bottom -= 5
        if self.rect.bottom - self.rect.height <= 0:
            self.rect.bottom = self.rect.height

    # 向下
    def __move_down(self):
        self.rect.bottom += 5
        if self.rect.bottom + (self.rect.height / 2) >= self.screen_rect.height:
            self.rect.bottom = self.screen_rect.bottom

    # 飞船移动
    def __move(self):
        if self.__direction == MoveDirection.up:
            self.__move_up()
        elif self.__direction == MoveDirection.down:
            self.__move_down()
        elif self.__direction == MoveDirection.left:
            self.__move_left()
        elif self.__direction == MoveDirection.right:
            self.__move_right()
