import pymunk
import random
import math
from vars import new_cells
from simulation.sim_func import *


class OBJ:
    def __init__(self, x, y, radius, mass):
        self.mass = mass
        self.radius = radius
        self.moment = pymunk.moment_for_circle(self.mass, 0, self.radius)
        self.body = pymunk.Body(self.mass, self.moment)
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, self.radius)
        self.shape.elasticity = 0.2
        self.shape.friction = 1





class CELL(OBJ):
    def __init__(self, x, y, radius, mass, cells_list, genome=None, food=100, color=None):
        super().__init__(x, y, radius, mass)
        self.genome = [random.randint(0, 63) for _ in range(63)] if genome is None else genome
        self.ptr = 0
        self.food = food
        self.space = cells_list
        self.shape.color = [0, 190, 80, 255] if color is None else color

    def execute_genome(self):
        if self.food >= 1000:  # Условие для деления клетки
            self.reproduce()
        else:
            command = self.genome[self.ptr]  # УТК
            self.food -= 1
            self.execute_command(command)  # Выполнение команды генома (УТК)


    def execute_command(self, command):
        if command in range(0, 20):
            self.photosynthesis()
            pass
        elif command in range(20, 40):
            self.move_in_direction(angle=self_get_bias(self, 1) * 5, force=self_get_bias(self, 2))
            move_ptr_to(self)
            pass
        else:
            # Если у числа нет команды, то происходит безусловный переход
            move_ptr_to(self)
        pass

    def photosynthesis(self):
        self.food += 10
        move_ptr(self)  # Переход УТК
        pass

    def reproduce(self):
        x, y = self.body.position
        new_cell = CELL(x=x, y=y, radius=max(min(self_get_bias(self,3), 30), 10), mass=100, cells_list=self.space, food=self.food//2, color=get_colors_bias(self))
        self.food = self.food // 2
        new_cells.append(new_cell)

        pass

    def move_in_direction(self, angle, force):
        angle = math.radians(angle)
        # Вычисляем компоненты x и y вектора силы
        force_x = force * math.cos(angle)
        force_y = force * math.sin(angle)
        # Применяем силу к телу объекта
        self.body.apply_force_at_local_point((force_x, force_y), (0, 0))

