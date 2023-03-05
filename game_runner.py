import pygame as pg
import sys

from controller import StartLocacion, Pufi, game_gui
from resourse_vars import choose_buttoms

ico = pg.image.load("data/pictures/ico.png")
pg.display.set_icon(ico)
pg.display.set_caption("Puffi", "Puffi")
pg.display.update()
clock = pg.time.Clock()
location = StartLocacion(Pufi(name="Пуфи"))

while True:
    local_event = None
    for event in pg.event.get():
        local_event = event
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN and not game_gui.update_text.done and event.button == 1:
            game_gui.update_text.to_fast_render()
        elif event.type == pg.MOUSEBUTTONDOWN and game_gui.update_text.done and event.button == 1:
            game_gui.next_text = True
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
            game_gui.update_text.active = not game_gui.update_text.active
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                sys.exit()
            if event.key == pg.K_SPACE and not game_gui.update_text.done:
                game_gui.update_text.to_fast_render()
            if event.key == pg.K_SPACE and game_gui.update_text.done:
                game_gui.next_text = True
            if event.key == pg.K_r:
                location = StartLocacion(Pufi(name="Пуфи"))
    clock.tick(60)
    game_gui.update(local_event)
    location.next_action()
    pg.display.update()