import pygame as pg


class Music():
    def __init__(self, file, loop=-1):
        pg.init()
        pg.mixer.music.load(file)
        pg.mixer.music.play(loops=loop)

    def play(self, loop=-1):
        pg.mixer.music.play(loops=loop)
    
    def stop(self):
        pg.mixer.music.stop()
    
    def play_new(self, file, loop=-1):
        self.stop()
        pg.mixer.music.load(file)
        pg.mixer.music.play(loops=loop)