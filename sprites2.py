import pygame as pg
from settings2 import *
from image2 import Image
import random


class Background(Image):
    def __init__(self, game):
        self._layer = BACKGROUND_LAYER

        Image.__init__(self, filename=BACKGROUND_IMG)
        self.set_size(self.image.get_rect().width, HEIGHT)
        self.add(game.allGroup)


class Platform(Image):
    def __init__(self, game, width, height, x, y):
        self._layer = PLATFORM_LAYER

        Image.__init__(self, PLATFORM_IMG)
        self.set_size(width, height)
        self.add(game.allGroup, game.platformsGroup)

        self.game = game

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Enemy(Image):
    def __init__(self, game, width, height, x, y):
        self._layer = ENEMY_LAYER
        way = "data/pictures/frog fps 2/"
        frogspngs = [
            "Лягушка в кокошнике",
            "Лягушка в сомбреро",
            "Лягушка в шапке ушанке",
            "Лягушка в шапке клоуна",
            "Лягушка мономах",
            "Лягушка с новогодней шапкой",
            "Лягушка Хабиб",
            "Лягушка шапка с бубенцом",
            "Кастрюля"
        ]
        frog_file = way + random.sample(frogspngs, 1)[0] + ".png"


        Image.__init__(self, filename=frog_file)
        self.set_size(width, height)
        self.add(game.allGroup, game.enemyGroup)

        self.rect = self.image.get_rect()

        self.vx = 0
        self.vy = 1
        self.dx = self.rect.x = x
        self.dy = self.rect.y = y

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center







