import pygame as pg
from typing import Tuple

def image_loader(path: str, size: Tuple[float, float]) -> pg.Surface:
    image = pg.image.load(path);
    image = pg.transform.scale(image, size)
    return image