import pygame as pg
from Config import *
from typing import Tuple
from Helper import image_loader

class Bird(pg.sprite.Sprite):
    images = [image_loader(path, (BIRD_WIDTH, BIRD_HEIGHT)) for path in BIRD_IMG_PATHS]
    
    # position: 初始位置 (x, y)
    def __init__(self, position: Tuple[float, float]):
        pg.sprite.Sprite.__init__(self)
        self._image_index = 1
        self.image = Bird.images[self._image_index]
        self.rect = self.image.get_rect()
        self.rect.center = position
        self._rotation_degree = 0
        return  
    def get_input(self) -> bool: # 回傳滑鼠是否按下(True: 按下/False: 沒有按下)
        if pg.mouse.get_pressed()[0]:
            return True
        return False
    @property
    def y(self):
        return self.rect.y
    @y.setter
    def y(self, value: float):
        self.rect.y = value
        return
    @property
    def rotation_degree(self):
        return self._rotation_degree
    @rotation_degree.setter
    def rotation_degree(self, value: float):
        self._rotation_degree = value
        self.image = pg.transform.rotate(self.image, self._rotation_degree)
        return
    @property
    def image_index(self):
        return self._image_index
    @image_index.setter
    def image_index(self, value: int):
        self._image_index = value
        self.image = Bird.images[self._image_index]
        return

    """
    self.y 為玩家(鳥)目前的 y 值(向下為正, 向上為負, 視窗頂端為 0)
    self.rotation_degree 為鳥的旋轉角度(degree), 逆時針為正
    self.image_index 為鳥的圖片狀態(0-翅膀朝下, 1-翅膀置中, 2-翅膀朝上, 3-翅膀置中)
    """
    # 處理鳥的移動
    def move(self): 
        # TODO1 讓鳥鳥動起來
        pass
        return

    # 處理鳥的圖片設定(實現動畫)
    def update_img(self):
        # TODO4 讓鳥鳥更生動(增加動畫)
        pass
        return

    def update(self):
        self.update_img()
        if self.get_input(): # 當滑鼠點擊時條件為True, 反之為False
            # TODO2 在接受到 input 時讓鳥有向上的抬升力
            pass
        self.move()
        return
