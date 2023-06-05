import pygame as pg


class Image(pg.sprite.Sprite):
    def __init__(self, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()

    def set_size(self, width, height):
        # self.image = pg.Surface((width, height))
        # image.blit(self.image, (0, 0), (0, 0, width, height))
        self.image = pg.transform.smoothscale(self.image, (width, height))
        self.rect = self.image.get_rect()