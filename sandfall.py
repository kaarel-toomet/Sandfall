import pygame
from materials import *
import numpy as np
from random import randint

col_background = (200, 200, 200)
col_empty = (0, 0, 0)
material_size = 50
UPS = 20
PAUSED = 0

def init(dimx, dimy):
    cells = []

    return cells

def draw_materials(surface, materials, material_size, selected, offset):
    pygame.draw.rect(surface, col_selected, (offset, selected * material_size, material_size, material_size))
    for key in material_dict:
        pygame.draw.rect(surface, material_dict[key].color, (offset + 5, int(key) * material_size + 5, material_size - 10, material_size - 10))

def get_line(start, end): # not mine
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1
 
    # Determine how steep the line is
    is_steep = abs(dy) > abs(dx)
 
    # Rotate line
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
 
    # Swap start and end points if necessary and store swap state
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True
 
    # Recalculate differentials
    dx = x2 - x1
    dy = y2 - y1
 
    # Calculate error
    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1
 
    # Iterate over bounding box generating points between start and end
    y = y1
    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx
 
    # Reverse the list if the coordinates were swapped
    if swapped:
        points.reverse()
    return points

def main(dimx, dimy, cellsize):
    pygame.init()
    surface = pygame.display.set_mode((dimx * cellsize + material_size, max(dimy * cellsize, material_size * num_materials)))
    pygame.display.set_caption("Sand fall")
    clock = pygame.time.Clock()

    cells = init(dimx, dimy)

    line_start = (-1, -1)

    selected = 0

    global PAUSED

    while True:
        clock.tick(UPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    PAUSED = not PAUSED
                if event.key == pygame.K_RETURN:
                    PAUSED = -1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (0, 1, 0):
                    if line_start == (-1, -1):
                        line_start = pygame.mouse.get_pos()
                        line_start = (line_start[0] // cellsize, line_start[1] // cellsize)
                    else:
                        line_end = pygame.mouse.get_pos()
                        line_end = (line_end[0] // cellsize, line_end[1] // cellsize)
                        for pos in get_line(line_start, line_end):
                            if get_cell(pos[0], pos[1], cells, dimy, dimx).state == "":
                                cells.append(material_dict[str(selected)](pos[0], pos[1]))
                        line_start = (-1, -1)
                    #print(line_start)
                elif pygame.mouse.get_pressed() == (1, 0, 0):
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if dimx * cellsize < mouse_x < dimx * cellsize + material_size and 0 < mouse_y < material_size * num_materials:
                        selected = mouse_y//material_size
                        #print(selected, material_dict[str(selected)].name)
        
        surface.fill(col_background)
        pygame.draw.rect(surface, col_empty, (0, 0, dimx * cellsize, dimy * cellsize))

        if PAUSED < 1:
            for cell in cells:
                cell.update(cells, dimx, dimy)

        if PAUSED == -1:
            PAUSED = 1

        if pygame.mouse.get_pressed() == (1, 0, 0):
            pos = pygame.mouse.get_pos()
            pos = (pos[0] // cellsize, pos[1] // cellsize)
            if get_cell(pos[0], pos[1], cells, dimy, dimx).state == "":
                cells.append(material_dict[str(selected)](pos[0], pos[1]))
            #print(pos)
        elif pygame.mouse.get_pressed() == (0, 0, 1):
            pos = pygame.mouse.get_pos()
            pos = (pos[0] // cellsize, pos[1] // cellsize)
            cell = get_cell(pos[0], pos[1], cells, dimy, dimx)
            if cell.state not in ("", "1"):
                cells.remove(cell)
        
        for cell in cells:
            col = cell.color
            pygame.draw.rect(surface, col, (cell.x*cellsize, cell.y*cellsize, cellsize-1, cellsize-1))

        if line_start != (-1, -1):
            pygame.draw.circle(surface, col_selected, ((line_start[0]+0.5) * cellsize, (line_start[1]+0.5) * cellsize), 10)
            pygame.draw.line(surface, col_selected, ((line_start[0]+0.5) * cellsize, (line_start[1]+0.5) * cellsize), ((pygame.mouse.get_pos()[0] // cellsize + 0.5) * cellsize, (pygame.mouse.get_pos()[1] // cellsize + 0.5) * cellsize))


        draw_materials(surface, material_dict, material_size, selected, dimx * cellsize)
            
        pygame.display.update()

if __name__ == "__main__":
    main(squares_x, squares_y, square_size)
