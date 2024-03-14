import pygame as pg
from Game import Game
from Config import CAPTION, SCREEN_WIDTH, SCREEN_HEIGHT

if __name__ == "__main__":
    pg.init()
    pg.display.set_caption(CAPTION)
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    game = Game(screen)
    game.run()

    pg.quit()