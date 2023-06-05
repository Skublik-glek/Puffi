from settings import *
from image import Image
from pygame import Vector2


class Background(Image):
    def __init__(self, game, pos=Vector2(0, 0)):
        Image.__init__(self, filename=BACKGROUND_IMG)
        self._layer = BACKGROUND_LAYER
        self.set_size(*game.screen.get_size())
        self.add(game.forwardCameraGroup)

        self.pos = pos

        self.buffers = []
        self.buffers.append(Vector2(self.pos.x - self.rect.width, self.pos.y))
        self.buffers.append(Vector2(self.pos.x + self.rect.width, self.pos.y))

    def move(self, pos):
        self.pos += pos
        for buffer in self.buffers:
            buffer += pos

    def move_x(self, pos):
        self.move(Vector2(pos, 0))

    def update(self, offset):
        self.move_x(offset)

        if self.pos.x > self.width:
            self.pos.x -= self.width
            for buffer in self.buffers:
                buffer.x -= self.width
        if self.pos.x < -self.width:
            self.pos.x += self.width
            for buffer in self.buffers:
                buffer.x += self.width

    def draw(self, screen):
        screen.blit(self.image, self.pos)
        for buffer in self.buffers:
            screen.blit(self.image, buffer)
