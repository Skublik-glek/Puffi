import pygame as pg
from settings import *
from image import Image


class Obstacle(Image):
    def __init__(self, game):
        self._layer = OBSTACLE_LAYER
        Image.__init__(self, filename=OBSTACLE_IMG)
        self.set_size(OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
        self.add(game.forwardCameraGroup)

        pos_x = game.screen.get_width() + self.width + 1
        pos_y = game.screen.get_height() + 2 * PLAYER_OFFSET_Y
        self.pos = pg.Vector2(pos_x, pos_y)
        self.rect.x = pos_x
        self.rect.y = pos_y

    def update(self, offset_x):
        self.pos.x += offset_x
        self.rect.x = self.pos.x

    def draw(self, screen):
        screen.blit(self.image, self.pos)


class Wall(Image):
    def __init__(self, game):
        self._layer = OBSTACLE_LAYER
        Image.__init__(self, filename=WALL_IMG)
        self.set_size(WALL_WIDTH, game.screen.get_height())
        self.add(game.allGroup, game.wallGroup)

        pos_x = 0 - self.width // 2
        pos_y = 0
        self.pos = pg.Vector2(pos_x, pos_y)
        self.rect.x = pos_x
        self.rect.y = pos_y

    def update(self):
        self.pos.x += WALL_SPEED
        self.rect.x = self.pos.x

    def draw(self, screen):
        screen.blit(self.image, self.pos)




