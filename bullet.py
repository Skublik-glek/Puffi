import pygame as pg
from settings2 import *


class Bullet(pg.sprite.Sprite):
    def __init__(self, game, screen, mouse_pos, player):
        """создаем пулю"""
        super(Bullet, self).__init__()
        self.add(game.allGroup, game.bulletsGroup)
        self._layer = BULLET_LAYER
        self.color = 139, 195, 74
        self.screen = screen
        self.rect = pg.Rect(0, 15, 5, 40)
        self.color = 139, 195, 74
        self.speed = 7.1
        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top

        self.image = pg.Surface(self.rect.size).convert_alpha()
        self.image.fill(self.color)
        pg.image.load("data//pictures/bullit.png")
        vec_mouse = pg.math.Vector2(mouse_pos)
        vec_player = pg.math.Vector2(player.pos)
        vec_norm = (vec_player - vec_mouse).normalize()
        self.vx = vec_norm.x
        self.vy = vec_norm.y

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """перемещение пули по X Y"""
        self.x -= self.speed * self.vx
        self.y -= self.speed * self.vy
        self.rect.x = self.x
        self.rect.y = self.y

