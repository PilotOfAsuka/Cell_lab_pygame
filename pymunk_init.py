import pymunk.pygame_util
from pygame_init import surface
from cell.object import OBJ, CELL
from vars import cells, H_WIDTH, H_HEIGHT

pymunk.pygame_util.positive_y_is_up = False

draw_options = pymunk.pygame_util.DrawOptions(surface)
# Устанавливаем флаги для скрытия столкновений и направляющих линий
draw_options.flags = pymunk.SpaceDebugDrawOptions.DRAW_SHAPES

# Создание физического пространства
space = pymunk.Space()
space.gravity = 0, 0


for i in range(5):
    # Создаем новый экземпляр объекта OBJ и добавляем его в список circles
    cell = CELL(H_WIDTH, H_HEIGHT, radius=30, mass=100, cells_list=cells)
    cells.append(cell)
    # Добавляем тело и форму объекта в пространство space
    space.add(cell.body, cell.shape)

