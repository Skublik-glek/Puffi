import sys
import os


TITLE = "Game"
FPS = 60
FONT_NAME = 'arial'

#
OBSTACLE_IMG = r'img/obstacle.png'
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 100

# Player properties
PLAYER_IMG = 'img/player.png'
PLAYER_WIDTH = 68
PLAYER_HEIGHT = 89
PLAYER_OFFSET_Y = -100
PLAYER_OFFSET_X = 180

PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20

WALL_IMG = 'img/wall.png'
WALL_SPEED = 0.5
WALL_WIDTH = 100

BACKGROUND_IMG = r'img/bg.png'

BACKGROUND_LAYER = 0
PLAYER_LAYER = 2
OBSTACLE_LAYER = 2
WALL_LAYER = 2


# define colors
WHITE = (0, 0, 0)
BGCOLOR = (110, 152, 230)

