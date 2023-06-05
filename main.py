import sys
import random
import time
from collections import deque
from sprites import *
from settings import *
from player import Player
from background import Background
from offsetGroup import ExtendedGroup

class Game:
    def __init__(self, sc, clock):
        self.playing = True

        self.screen = sc

        self.timer = time.time()

        self.clock = clock
        self.font_name = pg.font.match_font(FONT_NAME)

        self.mob_timer = 0

        self.allGroup = pg.sprite.LayeredUpdates()

        self.forwardCameraGroup = ExtendedGroup()  # pg.sprite.Group()
        self.wallGroup = pg.sprite.Group()

        self.background = Background(self)
        self.player = Player(self)
        self.wall = Wall(self)

        self.offset = 0
        self.obstacles = deque()

    def start(self):
        self.timer = time.time()
        pg.mixer.music.load("data/music/game 2.mp3")
        pg.mixer.music.play(-1)
        pg.mixer.music.set_volume(0.5)

    def update(self):
        now = pg.time.get_ticks()
        if now - self.mob_timer > 0:
            self.mob_timer = now + random.choice([3000, 4000, 5000, 6000])
            self.obstacles.append(Obstacle(self))

        self.offset = -1

        self.allGroup.update()
        self.forwardCameraGroup.update(self.offset)

        # delete old obstacles
        if self.obstacles:
            item = self.obstacles[0]
            if item.pos.x + item.width < 0:
                self.obstacles.popleft()

        # stop player if collide with obstacle
        for obstacle in self.obstacles:
            rect = self.player.rect
            # vx = self.prev_pos.x - self.pos.x
            if rect.colliderect(obstacle.rect):
                if self.player.pos.x < obstacle.pos.x and self.player.vv.x >= 0.0:  # player go right
                    self.player.pos.x = obstacle.pos.x - 10
                    self.player.vel.x = 0.0
                elif self.player.pos.x > obstacle.pos.x + obstacle.width and self.player.vv.x < 0.0:  # player go left
                    self.player.pos.x = obstacle.pos.x + obstacle.width + 10
                    self.player.vel.x = 0
                # ground py 764 oy 664 100
                elif ((obstacle.pos.x <= self.player.pos.x <= obstacle.pos.x + obstacle.width) and
                        (self.player.pos.y >= obstacle.pos.y)):
                    self.player.vel.x = 0
                    self.player.vel.y = 0
                    self.player.pos.y = obstacle.pos.y

        # wall collision
        wall_hits = pg.sprite.spritecollide(self.player, self.wallGroup, False)

        if wall_hits:
            self.__init__(self.screen, self.clock)
            self.start()

        if self.playing:
            self.events()
            self.draw()
            if time.time() - self.timer >= 25:
                self.playing = False

        # self.playing = True
        # if self.playing:
        #     self.screen.fill(BGCOLOR)
        #     self.draw_text("YOU DIE !", 48, WHITE, self.screen.get_width() // 2, self.screen.get_height() // 2)
        #     pg.display.flip()


    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                    self.player.jump_cut()

    def draw(self):
        self.screen.fill(BGCOLOR)

        self.forwardCameraGroup.draw(self.screen)
        self.allGroup.draw(self.screen)

        pg.display.flip()

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


if __name__ == '__main__':
    game = Game()
    pg.quit()


    
    
