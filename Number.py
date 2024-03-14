import pygame
from Config import NUMBER_IMG_PATHS, NUMBER_WIDTH, NUMBER_HEIGHT
from Helper import image_loader
from typing import Tuple, Optional

class Number(pygame.sprite.Sprite):
    imgs = [image_loader(path, (NUMBER_WIDTH, NUMBER_HEIGHT)) for path in NUMBER_IMG_PATHS]
    
    @property
    def number(self):
        return self.number_
    
    @number.setter
    def number(self, value: int):
        self.number_ = value
        self.image = Number.imgs[self.number_]
        return

    def __init__(self, position: Tuple[float, float], init_value: int):
        pygame.sprite.Sprite.__init__(self)
        self.number = init_value
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self, new_value: Optional[int] = -1):

        if not (new_value == -1 or new_value == self.number):
            self.number = new_value
