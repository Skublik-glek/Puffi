import pygame as pg
import sys


sc = pg.display.set_mode((0, 0), pg.FULLSCREEN)
pg.font.init()


class Background(pg.sprite.Sprite):
    def __init__(self, filename):
        self.widght, self.higth = sc.get_size()
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(
            filename).convert_alpha()
        self.old_image = None
        self.image = pg.transform.scale(self.image, sc.get_size())
        self.rect = self.image.get_rect(
            center=(self.widght // 2, self.higth // 2))
        self.alpha = 0
        self.counter = 0
        
    def send(self, filename):
        self.old_image = self.image
        self.image = pg.image.load(
            filename).convert_alpha()
        self.image = pg.transform.scale(self.image, sc.get_size())
        self.rect = self.image.get_rect(
            center=(self.widght // 2, self.higth // 2))
        self.alpha = 0
        self.counter = 0

    def update(self):
        if self.old_image == None:
            sc.blit(self.image, self.rect)
        else:
            if self.counter % 2 == 0:
                self.alpha += 8
                if self.alpha >= 255:
                    self.alpha = 255
                self.image.set_alpha(self.alpha)
            self.counter += 1    
            sc.blit(self.old_image, self.rect)
            sc.blit(self.image, self.rect)
            if self.alpha == 255:
                self.old_image = None
                self.alpha = 0
                self.counter = 0


class Update_text():
    def __init__(self, text: str, text_color=(255,255,255), border_color=pg.Color('black'),
                 rect_color=pg.Color('darkgrey')):
        self.text = text
        self.text_color = text_color
        self.border_color = border_color
        self.rect_color = rect_color
        self.sps = 20
        self.active_part = ""
        self.counter = 0
        self.text_counter = 0
        self.text_pos_y = sc.get_height() - 210
        self.my_font = pg.font.SysFont(pg.font.get_default_font(), 40)
        self.stroks = []
        self.box = pg.Rect(20, self.text_pos_y - 20, sc.get_width() - 40, sc.get_height() - sc.get_height() // 4)
        self.active = True
        self.fast_render = False
        self.done = False
        self.void_color = False

    def update(self):
        self.counter += 1
        if not self.active:
            return
        
        elif self.fast_render:
            if self.text_counter < len(self.text):
                for buk in self.text:
                    if buk == "`" or (len(self.active_part) >= 70 and buk == " ") \
                        or sc.get_width() < (self.my_font.render(self.active_part, True, self.text_color).get_width() + 80):
                        text_surface = self.my_font.render(self.active_part, True, self.text_color)
                        self.stroks.append([text_surface, (sc.get_width() // 2 - (text_surface.get_width() // 2),
                                                        self.text_pos_y)])
                        self.text_pos_y += 35
                        self.active_part = ""
                    if ord(buk) != 10:
                        self.active_part += buk
                    else:
                        self.active_part += " "
                    self.text_counter += 1
                if not self.void_color:
                    pg.draw.rect(sc, self.rect_color, self.box)
                    pg.draw.rect(sc, self.border_color, self.box, 2)
                for stroka in self.stroks:
                    text_surface = stroka[0]
                    sc.blit(text_surface, stroka[1])
                text_surface = self.my_font.render(self.active_part, True, self.text_color)
                sc.blit(text_surface,
                        (sc.get_width() // 2 - (text_surface.get_width() // 2),
                        self.text_pos_y))
                self.done = True
            else:
                if not self.void_color:
                    pg.draw.rect(sc, self.rect_color, self.box)
                    pg.draw.rect(sc, self.border_color, self.box, 2)
                for stroka in self.stroks:
                    text_surface = stroka[0]
                    sc.blit(text_surface, stroka[1])
                text_surface = self.my_font.render(self.active_part, True, self.text_color)
                sc.blit(text_surface,
                        (sc.get_width() // 2 - (text_surface.get_width() // 2),
                        self.text_pos_y))
                self.done = True
                self.counter = 0

        elif ((self.counter % (60 // self.sps)) == 0) and self.text_counter < len(self.text):
            if self.text[self.text_counter] == "`" or (len(self.active_part) >= 70 and self.text[self.text_counter] == " ") \
                    or sc.get_width() < (self.my_font.render(self.active_part, True, self.text_color).get_width() + 80):
                text_surface = self.my_font.render(self.active_part, True, self.text_color)
                self.stroks.append([text_surface, (sc.get_width() // 2 - (text_surface.get_width() // 2),
                                                   self.text_pos_y)])
                self.text_pos_y += 35
                self.active_part = ""
            if ord(self.text[self.text_counter]) != 10:
                self.active_part += self.text[self.text_counter]
            else:
                self.active_part += " "
            self.text_counter += 1
            if not self.void_color:
                pg.draw.rect(sc, self.rect_color, self.box)
                pg.draw.rect(sc, self.border_color, self.box, 2)
            for stroka in self.stroks:
                text_surface = stroka[0]
                sc.blit(text_surface, stroka[1])
            text_surface = self.my_font.render(self.active_part, True, self.text_color)
            sc.blit(text_surface,
                    (sc.get_width() // 2 - (text_surface.get_width() // 2),
                     self.text_pos_y))
        else:
            if not self.void_color:
                pg.draw.rect(sc, self.rect_color, self.box)
                pg.draw.rect(sc, self.border_color, self.box, 2)
            for stroka in self.stroks:
                text_surface = stroka[0]
                sc.blit(text_surface, stroka[1])
            text_surface = self.my_font.render(self.active_part, True, self.text_color)
            sc.blit(text_surface,
                    (sc.get_width() // 2 - (text_surface.get_width() // 2),
                    self.text_pos_y))
            if self.text_counter > len(self.text) - 1:
                self.done = True
                self.counter = 0

    def to_fast_render(self):
        self.fast_render = True
        self.active_part = ""
        self.stroks = []
        self.text_pos_y = sc.get_height() - 210
        self.text_counter = 0

    def send_text(self, text, text_color=(255,255,255), border_color=pg.Color('black'), rect_color=pg.Color('darkgrey')):
        self.text = text
        self.text_color = text_color
        self.border_color = border_color
        self.rect_color = rect_color
        self.active_part = ""
        self.counter = 1
        self.text_counter = 0
        self.text_pos_y = sc.get_height() - 210
        self.stroks = []
        self.active = True
        self.done = False
        self.fast_render = False
        self.void_color = False

class Choises():
    def __init__(self, choises: dict):
        self.choises = choises
        self.active = True
        self.text_pos_y = sc.get_height() // 4
        self.my_font = pg.font.SysFont(pg.font.get_default_font(), 40)
        self.boxes = []
        self.result = None
        self.done = False

    def update(self, event):
        if not self.active:
            return
        self.text_pos_y = sc.get_height() // 4
        for choise in self.choises.keys():
            text_surface = self.my_font.render(choise, True, self.choises[choise][1])
            box = pg.Rect(sc.get_width() // 2 - ((text_surface.get_width() + 10) // 2), self.text_pos_y - 5, text_surface.get_width() + 10, text_surface.get_height() + 10)
            self.boxes.append([box, choise])
            pg.draw.rect(sc, self.choises[choise][2], box)
            sc.blit(text_surface, (sc.get_width() // 2 - (text_surface.get_width() // 2), self.text_pos_y))
            self.text_pos_y += 45
        for box in self.boxes:
            if box[0].collidepoint(pg.mouse.get_pos()):
                pg.draw.rect(sc, self.choises[choise][3], box[0], 2)
            if event == None:
                continue
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if box[0].collidepoint(pg.mouse.get_pos()):
                    self.result = self.choises[box[1]][0]
                    self.done = True
                    self.active = False
                    break

    def send(self, choises):
        self.choises = choises
        self.active = True
        self.text_pos_y = sc.get_height() // 4
        self.boxes = []
        self.result = None
        self.done = True
        

class Game_gui():
    def __init__(self, sc, background: Background, update_text: Update_text, choises: Choises):
        self.sc = sc
        self.background = background
        self.update_text = update_text
        self.choises = choises
        self.next_text = False

    def update(self, event):
        self.background.update()
        self.update_text.update()
        self.choises.update(event)
