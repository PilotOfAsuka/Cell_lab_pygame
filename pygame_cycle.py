import random
from simulation.simulation import update_simulation
from vars import cells, new_cells, FPS
from pygame_init import *
from func import *
from pymunk_init import space, draw_options
from func import delete_obj_out_of_screen



def pygame_cycle(run=False):
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

        # Заливка фона
        surface.fill(pg.Color("#038A9D"))

        space.step(1 / FPS)

        update_simulation(cells)

        update_physics_space(cells=cells, new_cells=new_cells, space=space)

        delete_obj_out_of_screen(cells, space)


        space.debug_draw(draw_options)

        pg.display.flip()
        clock.tick(FPS)
