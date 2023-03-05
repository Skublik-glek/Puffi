import pygame as pg


class Music():
    def __init__(self, file):
        pg.init()
        pg.mixer.music.load(file)
        pg.mixer.music.play()

    def play(self):
        pg.mixer.music.play(loops=-1)
    
    def stop(self):
        pg.mixer.music.stop()
    
    def play_new(self, file):
        pg.mixer.music.load(file)
        pg.mixer.music.play()