from vars import *


def delete_obj_out_of_screen(cells, space):
    # Переменная для хранения индексов объектов, которые вышли за пределы пространства
    objects_to_remove = []

    for i, cell in enumerate(cells):
        # Проверяем, вышла ли клетка за пределы пространства
        x, y = cell.body.position
        if x < 0 or x > WIDTH or y < 0 or y > HEIGHT:
            objects_to_remove.append(i)  # Добавляем индекс клетки в список для удаления

        # Проверяем, вышла ли клетка за пределы пространства, и удаляем ее из физического пространства
        if x < 0 or x > WIDTH or y < 0 or y > HEIGHT:
            space.remove(cell.body, cell.shape)

    # Удаляем объекты из списка cells
    for index in reversed(objects_to_remove):
        del cells[index]
