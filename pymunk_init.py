import pymunk.pygame_util
from pygame_init import surface
from cell.object import OBJ, CELL
from vars import *

pymunk.pygame_util.positive_y_is_up = False

draw_options = pymunk.pygame_util.DrawOptions(surface)

# Создание физического пространства
space = pymunk.Space()
space.gravity = 1, 1

cells = []  # Создаем пустой список для хранения экземпляров объектов
new_cells = []  # Создаем список для хранения новых клеток

for i in range(5):
    # Создаем новый экземпляр объекта OBJ и добавляем его в список circles
    cell = CELL(H_WIDTH, H_HEIGHT, radius=30, mass=2)
    cells.append(cell)
    # Добавляем тело и форму объекта в пространство space
    space.add(cell.body, cell.shape)

