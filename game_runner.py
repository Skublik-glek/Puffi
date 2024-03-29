import pygame as pg
import sys
from gui_elements import sc
from main import Game

from controller import StartLocacion, Pufi, game_gui, loc_manager, game_mode, game, clock, game2

ico = pg.image.load("data/pictures/ico.png")
pg.display.set_icon(ico)
pg.display.set_caption("Puffi", "Puffi")
pg.display.update()
cursor_img = pg.image.load("data/pictures/cursor.png").convert_alpha()
cursor_img_rect = cursor_img.get_rect()
pg.mouse.set_visible(False)


while True:
    local_event = None
    for event in pg.event.get():
        local_event = event
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN and not game_gui.update_text.done and event.button == 1:
            game_gui.update_text.to_fast_render()
            game_gui.next_text = False
        elif event.type == pg.MOUSEBUTTONDOWN and game_gui.update_text.done and event.button == 1 and not game_gui.choises.done:
            game_gui.next_text = True
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
            game_gui.update_text.active = not game_gui.update_text.active
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                sys.exit()
            if event.key == pg.K_SPACE and not game_gui.update_text.done:
                game_gui.update_text.to_fast_render()
                game_gui.next_text = False
                check = False
            if event.key == pg.K_SPACE and game_gui.update_text.done and not game_gui.choises.done:
                game_gui.next_text = True
            if event.key == pg.K_r:
                loc_manager.loc = StartLocacion(Pufi(name="Пуфи"))

    clock.tick(60)
    if game_mode.game_mode == 0:
        game_gui.update(local_event)
        loc_manager.loc.next_action()
        cursor_img_rect.midtop = pg.mouse.get_pos()
        sc.blit(cursor_img, cursor_img_rect)
        pg.display.update()
    elif game_mode.game_mode == 1:
        game.update()
        if not game.playing:
            game_mode.game_mode = 0
    elif game_mode.game_mode == 2:
        pg.mouse.set_visible(True)
        game2.update()
        if not game2.playing:
            game_mode.game_mode = 0
            pg.mouse.set_visible(False)