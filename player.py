import pygame
from pygame.rect import Rect

import constants


class Player(Rect):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def update_state_movement(self, keys, obstacles):
        if keys[pygame.K_UP] and self.y > 0:
            self.move_y(-constants.VELOCITY, obstacles)
        if keys[pygame.K_DOWN] and self.y + constants.VELOCITY + self.height <= constants.SCREEN_HEIGHT:
            self.move_y(+constants.VELOCITY, obstacles)
        if keys[pygame.K_RIGHT] and self.x + self.width + constants.VELOCITY <= constants.SCREEN_WIDTH:
            self.move_x(constants.VELOCITY, obstacles)
        if keys[pygame.K_LEFT] and self.x > 0:
            self.move_x(-constants.VELOCITY, obstacles)

    def move_y(self, velocity, obstacles):
        current_y = self.y
        self.y += velocity
        for obstacle in obstacles:
            if self.colliderect(obstacle):
                self.y = current_y
                return

    def move_x(self, velocity, obstacles):
        current_x = self.x
        self.x += velocity
        for obstacle in obstacles:
            if self.colliderect(obstacle):
                self.x = current_x
                return
