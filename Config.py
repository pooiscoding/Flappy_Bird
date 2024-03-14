import pygame as pg

"""
Constants
"""

BACKGROUND_SCALE = 1.5
BIRD_SCALE = 1.1

CAPTION = "Flappy Bird"
FPS = 75
SCREEN_WIDTH = 288 * BACKGROUND_SCALE
SCREEN_HEIGHT = 512 * BACKGROUND_SCALE

# images size related
BASE_WIDTH = 336 * BACKGROUND_SCALE
BASE_HEIGHT = 112 * BACKGROUND_SCALE
PIPE_WIDTH = 52 * BACKGROUND_SCALE
PIPE_HEIGHT = 320 * BACKGROUND_SCALE
BIRD_WIDTH = 34 * BIRD_SCALE
BIRD_HEIGHT = 24 * BIRD_SCALE
NUMBER_WIDTH = 24 * BACKGROUND_SCALE
NUMBER_HEIGHT = 36 * BACKGROUND_SCALE

# images paths
BACKGROUND_IMG_PATH = "./img/background.png"
BASE_IMG_PATH = "./img/base.png"
PIPE_IMG_PATH = "./img/pipe-green.png"
BIRD_IMG_PATHS = ("./img/bluebird-downflap.png", "./img/bluebird-midflap.png", "./img/bluebird-upflap.png", "./img/bluebird-midflap.png")
NUMBER_IMG_PATHS = (f"./img/numbers/{i}.png" for i in range(10))

# bird flying physics related
GRAVITY = .5
FLY_SPEED = -5

# bird animation related
BIRD_ANIMATION_COOLDOWN = 8
BIRD_ROTATION_LIMIT = 12
BIRD_ROTATION_SPEED = .5

# base animation related
BASE_SCROLLING_SPEED = 5


HEIGHT_LIMIT = SCREEN_HEIGHT - BASE_HEIGHT
