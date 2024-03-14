import pygame as pg
from Config import *
from Helper import image_loader

from Base import Base
from Bird import Bird
from Pipes import Pipes
from Scoreboard import Scoreboard

class Game:
    def __init__(self, surface: pg.surface):
        self.screen = surface
        self.background_img = image_loader(BACKGROUND_IMG_PATH, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # TODO7 讓遊戲流程更豐富
    def run(self):
        
        clock = pg.time.Clock()
        running = True
        base = pg.sprite.GroupSingle(Base())
        bird = pg.sprite.GroupSingle(Bird((SCREEN_WIDTH / 10, HEIGHT_LIMIT / 2)))
        pipes = Pipes()
        scoreboard = Scoreboard()
        # game loop
        while running:

            clock.tick(FPS)

            for event in pg.event.get():
                if event.type == pg.QUIT: # "視窗關閉"事件
                    running = False

            # 更新遊戲
            base.update()
            bird.update()
            pipes.update()
            scoreboard.update()
            ## 遊戲結束
            if  pg.sprite.groupcollide(bird, pipes.pipes, False, False):
                running = False

            # 畫背景、物件
            self.screen.blit(self.background_img, (0, 0))
            base.draw(self.screen)
            bird.draw(self.screen)
            pipes.draw(self.screen)
            scoreboard.draw(self.screen)
            pg.display.update()