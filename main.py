import pygame

import constants
from level import Level1, Level2
from player import Player

pygame.init()


class Game:

    def __init__(self, width, height, fps):
        self.screen = pygame.display.set_mode([width, height])
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = fps

        self.levels = [Level1(), Level2()]
        self.level_counter = 0
        self.level = self.levels[self.level_counter]
        self.player = Player(*self.level.player_pos)

    def reset_level(self):
        self.player = Player(*self.level.player_pos)

    def start(self):
        self.main()

    def main(self):
        while self.running:
            self.clock.tick(self.fps)
            self.handle_event()
            self.update_state()
            self.draw()
        pygame.quit()

    def update_state(self):
        keys = pygame.key.get_pressed()
        self.player.update_state_movement(keys, self.level.hard_obstacles)
        if self.player.colliderect(self.level.target):
            self.next_level()
        for enemy in self.level.enemies:
            enemy.update_state()
            if self.player.colliderect(enemy):
                self.reset_level()

    def next_level(self):
        self.level_counter += 1
        if self.level_counter < len(self.levels):
            self.level = self.levels[self.level_counter]
            self.reset_level()
        else:
            print("you won!")
            self.running = False

    def draw(self):
        self.screen.fill(constants.COLOR_WHITE)
        pygame.draw.rect(self.screen, constants.COLOR_I, self.player)
        pygame.draw.rect(self.screen, constants.COLOR_K, self.level.target)

        for rect in self.level.hard_obstacles:
            pygame.draw.rect(self.screen, constants.COLOR_C, rect)

        for enemy in self.level.enemies:
            pygame.draw.rect(self.screen, constants.COLOR_D, enemy)

        pygame.display.flip()

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


g = Game(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.FPS)
g.start()
