import pygame as pg

from typing import Tuple
from Config import *
from Helper import image_loader

# a single pipe
class Pipe(pg.sprite.Sprite):
    img = image_loader(PIPE_IMG_PATH, (PIPE_WIDTH, PIPE_HEIGHT))
    flipped_img = pg.transform.flip(img, False, True)
    """ 
    position: 水管的初始位置, 為水管最左方, 最靠近管口的位置(x, y)
    is_flip: 此水管需不需要翻轉(翻轉為管口朝下, 不翻轉為管口朝上)
    """
    def __init__(self, position: Tuple[float, float], is_flip: bool):
        pg.sprite.Sprite.__init__(self)
        if is_flip: # 上面(管口朝下)
            self.image = Pipe.flipped_img
            self.rect = self.image.get_rect()
            self.rect.bottomleft = position
        else: # 下面(管口朝上)
            self.image = Pipe.img
            self.rect = self.image.get_rect()
            self.rect.topleft = position
    @property
    def x(self):
        return self.rect.x
    @x.setter
    def x(self, value):
        self.rect.x = value
    @property
    def y(self):
        return self.rect.y
    @y.setter
    def y(self, value):
        self.rect.y = value

    def update(self):
        self.x -= BASE_SCROLLING_SPEED
        if self.x + PIPE_WIDTH < 0:
            self.kill()

# an upper pipe and a lower pipe
class Pipe_pair:
    def __init__(self):
        # TODO5 讓每次新增的 Pipe_pair 略有不同 !
        """
        透過 random library 來輔助達成目標
        """
        # -----------------以下要修改----------------- #

        pipe_gap = 100
        center = HEIGHT_LIMIT / 2
        pipe_top = Pipe((SCREEN_WIDTH, center - (pipe_gap / 2)), True)
        pipe_btm = Pipe((SCREEN_WIDTH, center + (pipe_gap / 2)), False)

        # -----------------以上要修改----------------- #

        self.pipes = pg.sprite.Group()
        self.pipes.add(pipe_btm), self.pipes.add(pipe_top)

    @property
    def bottom_pipe(self):
        return self.pipes.sprites()[0]
    @property
    def top_pipe(self):
        return self.pipes.sprites()[1]
    @property
    def x(self):
        return self.bottom_pipe.x

    def update(self) -> bool: 
        self.pipes.update()

    def draw(self, surface: pg.surface):
        self.pipes.draw(surface)

    def is_alive(self) -> bool: # 回傳此 pipe_pair 是否還存活在 window 中，即仍需要被更新
        if len(self.pipes) == 0: return False
        return True

# all pipes
class Pipes:
    def __init__(self):
        self.pipepair_counter = 0
        self.pipe_pairs = []

    @property
    def pipes(self):
        re = pg.sprite.Group()
        for pipe_pair in self.pipe_pairs:
            sprites = pipe_pair.pipes.sprites()
            re.add(sprites[0]), re.add(sprites[1])
        return re

    def add_pipe(self):
        self.pipepair_counter += 1
        self.pipe_pairs.append(Pipe_pair())
    
    def update(self):
        # 更新所有水管
        for pipe_pair in self.pipe_pairs:
            pipe_pair.update()

        # 刪除已經超出螢幕的水管
        while len(self.pipe_pairs) != 0 and not self.pipe_pairs[0].is_alive():
            self.pipe_pairs.pop(0)
        
        # TODO3 決定何時新增水管
        """
        控制這次更新需不需要新增水管
        呼叫self.add_pipe()即會新增一對水管對
        """
        # FIXME 取消下行的註解看看不做控制直接新增會發生什麼事
        # self.add_pipe()

    def draw(self, surface: pg.surface):
        for pipe_pair in self.pipe_pairs:
            pipe_pair.draw(surface)

# TODO8 過動的水管
"""
可以直接修改, 也可以透過繼承 Pipe, Pipe_pair 創造不同行為的水管
"""