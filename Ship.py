import pygame
import sys
from enum import Enum

class move_direction(Enum):
    stop = 0
    up = 1
    down = 2
    left = 3
    right = 4

class Ship(object):
    def __init__(self, screen):
        self.screen = screen
        self.imgae = pygame.image.load("images/ship.bmp")
        self.rect = self.imgae.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10
        self.direction = move_direction.stop

    def show_ship(self):
        self.screen.blit(self.imgae, self.rect)

    def move_left(self):
        self.rect.centerx -= 5

    def move_right(self):
        self.rect.centerx += 5

    def move_up(self):
        self.rect.bottom -= 5

    def move_down(self):
         self.rect.bottom += 5

    def move(self):
        if self.direction == move_direction.up:
            self.move_up()
        elif self.direction == move_direction.down:
            self.move_down()
        elif self.direction == move_direction.left:
            self.move_left()
        elif self.direction == move_direction.right:
            self.move_right()

    def move_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.direction = move_direction.left
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.direction = move_direction.right
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.direction = move_direction.up
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.direction = move_direction.down
            elif event.type == pygame.KEYUP:
                self.direction = move_direction.stop
        self.move()