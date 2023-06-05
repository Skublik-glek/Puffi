import pygame as pg


class ExtendedGroup(pg.sprite.Group):

    def draw(self, screen):
        sprites = self.sprites()
        for sprite in sprites:
            sprite.draw(screen)



