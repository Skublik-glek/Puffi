import pygame as pg


class Image(pg.sprite.Sprite):
    def __init__(self, filename):
        super(Image, self).__init__()

        self.image = pg.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (self.width // 2, self.height // 2)

    def set_size(self, width, height):
        self.image = pg.transform.smoothscale(self.image, (width, height))
        self.rect = self.image.get_rect(center=(width, height))

    @property
    def width(self):
        return self.rect.width

    @property
    def height(self):
        return self.rect.height
