import pygame as pg
from Config import *
from Helper import image_loader

class Base(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = image_loader(BASE_IMG_PATH, (BASE_WIDTH, BASE_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0, SCREEN_HEIGHT)
        return
    @property
    def scroll(self):
        return self.rect.left
    @scroll.setter
    def scroll(self, value: float):
        self.rect.left = value
        return
    
    """
    self.scroll 為下方base圖片的向右滑動量(向左滑動為負, 向右滑動為正)
    """
    def update(self):
        # TODO0 讓底下綠色的bar動起來
        """
        hint:   透過在每次update時增加一點base圖片向左的滑動量(設定self.scroll), 可達成視覺上向左動的效果. 
                因為base的圖片並非無限延伸, 在圖片要滑出畫面(self.scroll < BASE_WIDTH)時, 可以把base拉回原位(self.scroll = 0)做修正.
        """
        pass
        return
        