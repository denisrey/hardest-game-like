from pygame import Rect

from enemy import VerticalEnemy, HorizontalEnemy


class Level1:
    def __init__(self):
        self.hard_obstacles = [
            Rect(0, 0, 220, 220),
            Rect(410, 0, 220, 220),
            Rect(0, 410, 220, 220),
            Rect(410, 410, 220, 220)
        ]
        self.enemies = [
            VerticalEnemy(255, 255, 60, 60, -1, 0, 450),
            HorizontalEnemy(255, 255, 60, 60, -1, 0, 450),

            VerticalEnemy(400, 255, 60, 60, -1, 0, 450),
            HorizontalEnemy(400, 255, 60, 60, -1, 0, 450),

            VerticalEnemy(255, 400, 60, 60, -1, 0, 450),
            HorizontalEnemy(255, 400, 60, 60, -1, 0, 450),
        ]

        self.target = Rect(500, 300, 50, 300)
        self.player_pos = (0, 350, 50, 50)


class Level2:
    def __init__(self):
        self.hard_obstacles = [
            Rect(0, 0, 220, 220),
            Rect(410, 0, 220, 220),
            Rect(0, 410, 220, 220),
            Rect(410, 410, 220, 220)
        ]
        self.enemies = [
            VerticalEnemy(255, 255, 60, 60, -1, 0, 450),
            HorizontalEnemy(255, 255, 60, 60, -1, 0, 450),

            VerticalEnemy(400, 255, 60, 60, -1, 0, 450),
            HorizontalEnemy(400, 255, 60, 60, -1, 0, 450),

            VerticalEnemy(255, 400, 60, 60, -1, 0, 450),
            HorizontalEnemy(255, 400, 60, 60, -1, 0, 450),

            VerticalEnemy(400, 400, 60, 60, -1, 0, 450),
            HorizontalEnemy(400, 400, 60, 60, -1, 0, 450),
        ]

        self.target = Rect(500, 300, 50, 300)
        self.player_pos = (0, 350, 50, 50)
