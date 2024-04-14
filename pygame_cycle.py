from vars import *
from pygame_init import *
from func import *
from pymunk_init import space, draw_options, cells, new_cells
from func import delete_obj_out_of_screen


def pygame_cycle(run=False):
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

        # Заливка фона
        surface.fill(pg.Color("black"))

        space.step(1 / FPS)

        for cell in cells:
            cell.reproduce(new_cells=new_cells)


        for new_cell in new_cells:
            cells.append(new_cell)
            space.add(new_cell.body, new_cell.shape)
        new_cells.clear()

        delete_obj_out_of_screen(cells, space)


        space.debug_draw(draw_options)

        pg.display.flip()
        clock.tick(FPS)
