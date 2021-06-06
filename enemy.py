from abc import ABC, abstractmethod

from pygame import Rect


class Enemy(Rect, ABC):
    def __init__(self, x, y, height, width, start_direction):
        super().__init__(x, y, height, width)
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.start_direction = start_direction

    @abstractmethod
    def update_state(self):
        raise NotImplementedError("Not Implemented!")


class VerticalEnemy(Enemy):
    def __init__(self, x, y, height, width, start_direction, max_height, low_height):
        super().__init__(x, y, height, width, start_direction)
        self.max_height = max_height
        self.low_height = low_height
        self.velocity = start_direction

    def update_state(self):
        self.y += self.velocity
        if self.velocity == -1 and self.y <= self.max_height:
            self.velocity = self.velocity * -1
        if self.velocity == 1 and self.y > self.low_height:
            self.velocity = self.velocity * -1


class HorizontalEnemy(Enemy):
    def __init__(self, x, y, height, width, start_direction, max_left, max_right):
        super().__init__(x, y, height, width, start_direction)
        self.max_left = max_left
        self.max_right = max_right
        self.velocity = start_direction

    def update_state(self):
        self.x += self.velocity
        if self.velocity == -1 and self.x <= self.max_left:
            self.velocity = self.velocity * -1
        if self.velocity == 1 and self.x > self.max_right:
            self.velocity = self.velocity * -1
