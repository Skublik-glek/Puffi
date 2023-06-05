import sys
import os


TITLE = "Game"
WIDTH = 1280
HEIGHT = 800
FPS = 60
FONT_NAME = 'arial'

# Platform
PLATFORM_IMG = 'img/platform.png'
PLATFORM_WIDTH = WIDTH + 200
PLATFORM_HEIGHT = 120

# Enemy property
ENEMY_IMG = 'img/enemy.png'
ENEMY_WIDTH = 80
ENEMY_HEIGHT = 80

# Player properties
PLAYER_IMG = 'img/player.png'
PLAYER_WIDTH = 48
PLAYER_HEIGHT = 69

PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20


# game properties
MOB_FREQ = 5000

BACKGROUND_IMG = 'img/background.png'

BACKGROUND_LAYER = 0
PLATFORM_LAYER = 1
PLAYER_LAYER = 2
ENEMY_LAYER = 2
BULLET_LAYER = 2

# define colors
WHITE = (0, 0, 0)
BGCOLOR = (110, 152, 230)
