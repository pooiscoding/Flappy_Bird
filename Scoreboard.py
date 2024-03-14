import pygame as pg
from Number import Number

# TODO6 完成記分板物件
"""
記分板物件需至少支援三個方法
1. constructor(__init__): 用來建構一個記分板物件實體
2. update: 用來作為遊戲迴圈中每次更新呼叫的更新函式
3. draw: 遊戲迴圈更新後將記分板畫到視窗中的函式
"""

"""
可以利用實作好的Number物件

x = Number(position: Tuple[float, float], init_value: int)
position: 此實體的位置 (x, y)
init_value: 0~9 的整數, 表示此實體初始顯示的數字

可使用的方法: 
更新此實體的數字 .update()
x.update(new_value: Optional[int])
new_value: 0~9的整數, 表示此實體欲顯示的新數字

將此實體畫到視窗中 .draw()
x.draw(surface: pygame.surface)

可使用的屬性:
x.number 目前此實體顯示的數字
"""

class Scoreboard:
    def __init__(self):
        pass
    def update(self):
        pass
    def draw(self, surface: pg.surface):
        pass