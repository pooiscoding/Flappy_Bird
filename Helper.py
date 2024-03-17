import pygame as pg
from typing import Tuple


def image_loader(path: str, size: Tuple[float, float]) -> pg.Surface:
    """
    載入圖片函式

    Args:
        path (str): 欲載入圖片之路徑
        size (Tuple[float, float]): 圖片之寬, 高
    Returns:
        pg.Surface: 載入好的圖片物件
    """
    image = pg.image.load(path)
    scaled_image = pg.transform.scale(image, size)
    return scaled_image
