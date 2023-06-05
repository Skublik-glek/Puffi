import sys
import random
from sprites2 import *
from settings2 import *
from bullet import Bullet
from player2 import Player

pg.init()
pg.mixer.pre_init(44100, -16, 1, 512)
s_kill = pg.mixer.Sound("data/music/bax.mp3")
s_kill.set_volume(0.3)


class Game:
    def __init__(self,  sc, clock):
        # initialize game window, etc
        self.playing = True
        self.screen = sc
        self.clock = clock
        self.font_name = pg.font.match_font(FONT_NAME)

        self.num_kill = 0
        self.mob_timer = 1

        self.allGroup = pg.sprite.LayeredUpdates()
        self.platformsGroup = pg.sprite.Group()
        self.enemyGroup = pg.sprite.Group()
        self.bulletsGroup = pg.sprite.Group()

        self.background = Background(self)
        self.player = Player(self, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.platform = Platform(self, PLATFORM_WIDTH, PLATFORM_HEIGHT, x=-100, y=HEIGHT - PLAYER_HEIGHT)
        # self.platform = Platform(self, PLATFORM_WIDTH, PLATFORM_HEIGHT, x=0, y=HEIGHT - PLAYER_HEIGHT)

    def start(self):
        pg.mixer.music.load("data/music/game_1.mp3")
        pg.mixer.music.play(-1)
        pg.mixer.music.set_volume(0.5)
        
    def update(self):
        # game loop - update
        self.allGroup.update()

        # spawn a mob?
        now = pg.time.get_ticks()
        if now - self.mob_timer > 2000 + random.choice([-1000, -500, 0, 500, 1000]):
            self.mob_timer = now
            Enemy(self, ENEMY_WIDTH, ENEMY_HEIGHT,
                  random.randint(0, WIDTH), random.randint(0, HEIGHT // 3))

        self.bulletsGroup.update()

        # hit enemy?
        mob_hits = pg.sprite.spritecollide(self.player, self.enemyGroup, False, pg.sprite.collide_mask)
        if mob_hits:
            self.__init__(self.screen, self.clock)

        # kill enemy?
        killEnemyList = pg.sprite.groupcollide(self.enemyGroup, self.bulletsGroup, True, True)
        if killEnemyList:
            for _ in killEnemyList.values():
                self.num_kill += 1
                s_kill.play()
                if self.num_kill == 20:
                    self.playing = False

        # check if player hits a platform
        if self.player.vel.y > 0: 
            hits = pg.sprite.spritecollide(self.player, self.platformsGroup, False)
            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit
                if lowest.rect.right + 10 > self.player.pos.x > lowest.rect.left + 10:
                    if self.player.pos.y < lowest.rect.centery:
                        self.player.pos.y = lowest.rect.top
                        self.player.vel.y = 0
                        self.player.jumping = False
        if self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                Bullet(self, self.screen, pg.mouse.get_pos(), self.player)

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
        self.allGroup.draw(self.screen)
        self.draw_text(str(self.num_kill), 22, WHITE, WIDTH / 2, 15)

        pg.display.flip()

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


if __name__ == '__main__':
    game = Game()
    game.run()
    pg.quit()



    
