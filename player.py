import pygame as pg
from settings import *
from image import Image


class Player(Image):
    def __init__(self, game):
        self._layer = PLAYER_LAYER
        Image.__init__(self, filename=PLAYER_IMG)
        self.set_size(PLAYER_WIDTH, PLAYER_HEIGHT)
        self.add(game.allGroup)

        self.game = game
        self.walking = False
        self.jumping = False

        self.sc_width, self.sc_height = game.screen.get_size()
        self.pos = pg.math.Vector2(PLAYER_OFFSET_X, self.sc_height + PLAYER_OFFSET_Y)
        self.vel = pg.math.Vector2(0, 0)
        self.acc = pg.math.Vector2(0, 0)

        self.floor = self.pos.y
        self.vv = pg.math.Vector2(0, 0)

    def jump_cut(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

    def jump(self):
        if self.pos.y >= self.floor and not self.jumping:
            self.jumping = True
            self.vel.y = - PLAYER_JUMP

    def update(self):
        self.acc = pg.math.Vector2(0, PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.acc.x = PLAYER_ACC

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0

        self.vv = self.vel + 0.5 * self.acc
        self.pos += self.vv
        # wrap around the sides of the screen
        if self.pos.x > self.sc_width:
            self.pos.x = self.sc_width
            # self.pos.x = 0 - self.rect.width / 2
        if self.pos.x <= 0:
            self.pos.x = 0

        if self.pos.y >= self.floor:
            self.pos.y = self.floor
            # self.vel.y = 0
        self.rect.midbottom = self.pos

        # check if player hits a platform
        if self.vel.y < 0:
            self.jumping = False

