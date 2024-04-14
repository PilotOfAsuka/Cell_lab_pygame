import pymunk
import random


class OBJ:
    def __init__(self, x, y, radius, mass):
        self.mass = mass
        self.radius = radius
        self.moment = pymunk.moment_for_circle(self.mass, 0, self.radius)
        self.body = pymunk.Body(self.mass, self.moment)
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, self.radius)
        self.shape.elasticity = 0.8
        self.shape.friction = 0.5



class CELL(OBJ):
    def __init__(self, x, y, radius, mass):
        super().__init__(x, y, radius, mass)
        self.food = 100

    def reproduce(self, new_cells, threshold=0.1):
        # Генерация случайного числа в диапазоне от 0 до 1
        chance = random.uniform(0, 1)
        # Задайте пороговое значение для шанса
        # Если случайное число меньше порога, клетка воспроизводится
        if chance < threshold:
            x, y = self.body.position
            new_cell = CELL(x=x, y=y, radius=random.randint(10, 20), mass=1)
            new_cells.append(new_cell)

        pass


