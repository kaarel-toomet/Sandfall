from random import randint

col_selected = (255, 100, 100)
squares_x, squares_y, square_size = (30, 30, 20)
col_background = (200, 200, 200)
col_empty = (0, 0, 0)
material_size = 50
UPS = 20



class Material:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.life = 0
    
    def update(self, cells, cells_grid, dimx, dimy):
        return

class Empty:
    state = ""
    name = "empty"
    flammability = 0

class Full:
    state = "1"
    name = "full"
    flammability = 0
        
class Powder(Material):
    state = "powder"
    
    def update(self, cells, cells_grid, dimx, dimy):
        self.move(cells, cells_grid, dimx, dimy)
    
    def move(self, cells, cells_grid, dimx, dimy):
        x, y = self.x, self.y
        cell_1 = get_cell(x-1, y+1, cells_grid, dimx, dimy)      #789
        cell_2 = get_cell(x, y+1, cells_grid, dimx, dimy)        #4 6
        cell_3 = get_cell(x+1, y+1, cells_grid, dimx, dimy)      #123
        cell_4 = get_cell(x-1, y, cells_grid, dimx, dimy)
        cell_6 = get_cell(x+1, y, cells_grid, dimx, dimy)
        empty = [False, cell_1.state == "", cell_2.state == "", cell_3.state == "", cell_4.state == "", False, cell_6.state == ""]
        fluid = [False, cell_1.state in ("liquid", "gas"), cell_2.state in ("liquid", "gas"), cell_3.state in ("liquid", "gas"), cell_4.state in ("liquid", "gas"), False, cell_6.state in ("liquid", "gas")]

        if empty[2]:
            move_cell(0, 1, cells_grid, self)

        elif empty[1] and empty[3] and empty[4] and empty[6]:
            if randint(0, 1) == 0:
                move_cell(-1, 1, cells_grid, self)
            else:
                move_cell(1, 1, cells_grid, self)
        elif empty[1] and empty[4]:
            move_cell(-1, 1, cells_grid, self)
                
        elif empty[3] and empty[6]:
            move_cell(+1, 1, cells_grid, self)

        elif fluid[2]:
            move_cell(0, 1, cells_grid, self)
            cells_grid[self.y - 1, self.x] = cell_2
            cell_2.y -= 1

        elif fluid[1] and fluid[3] and (fluid[4] or empty[4]) and (fluid[6] or empty[6]):
            if randint(0, 1) == 0:
                move_cell(-1, 1, cells_grid, self)
                cells_grid[self.y - 1, self.x + 1] = cell_1
                cell_1.x += 1
                cell_1.y -= 1
            else:
                move_cell(1, 1, cells_grid, self)
                cells_grid[self.y - 1, self.x - 1] = cell_3
                cell_3.x -= 1
                cell_3.y -= 1
        elif fluid[1] and (fluid[4] or empty[4]):
            move_cell(-1, 1, cells_grid, self)
            cells_grid[self.y - 1, self.x + 1] = cell_1
            cell_1.x += 1
            cell_1.y -= 1
                
        elif fluid[3] and (fluid[6] or empty[6]):
            move_cell(1, 1, cells_grid, self)
            cells_grid[self.y - 1, self.x - 1] = cell_3
            cell_3.x -= 1
            cell_3.y -= 1
        

class Solid(Material):
    state = "solid"
    pass

class Liquid(Material):
    state = "liquid"
    
    def update(self, cells, cells_grid, dimx, dimy):
        self.move(cells, cells_grid, dimx, dimy)

    def move(self, cells, cells_grid, dimx, dimy):
        x, y = self.x, self.y
        cell_1 = get_cell(x-1, y+1, cells_grid, dimx, dimy)      #789
        cell_2 = get_cell(x, y+1, cells_grid, dimx, dimy)        #4 6
        cell_3 = get_cell(x+1, y+1, cells_grid, dimx, dimy)      #123
        cell_4 = get_cell(x-1, y, cells_grid, dimx, dimy)
        cell_6 = get_cell(x+1, y, cells_grid, dimx, dimy)
        empty = [False, cell_1.state == "", cell_2.state == "", cell_3.state == "", cell_4.state == "", False, cell_6.state == ""]
        gas = [False, cell_1.state == "gas", cell_2.state == "gas", cell_3.state == "gas", cell_4.state == "gas", False, cell_6.state == "gas"]

        if empty[2]:
            move_cell(0, 1, cells_grid, self)

        elif empty[1] and empty[3] and empty[4] and empty[6]:
            if randint(0, 1) == 0:
                move_cell(-1, 1, cells_grid, self)
            else:
                move_cell(1, 1, cells_grid, self)
        elif empty[1] and empty[4]:
            move_cell(-1, 1, cells_grid, self)
                
        elif empty[3] and empty[6]:
            move_cell(1, 1, cells_grid, self)

        elif empty[4] and empty[6]:
            if randint(0,1):
                move_cell(1, 0, cells_grid, self)
            else:
                move_cell(-1, 0, cells_grid, self)
            
        elif empty[4]:
            move_cell(-1, 0, cells_grid, self)
            
        elif empty[6]:
            move_cell(1, 0, cells_grid, self)

        elif gas[2]:
            move_cell(0, 1, cells_grid, self)
            cells_grid[self.y - 1, self.x] = cell_2
            cell_2.y -= 1

        elif gas[1] and gas[3] and gas[4] and gas[6]:
            if randint(0, 1) == 0:
                move_cell(-1, 1, cells_grid, self)
                cells_grid[self.y - 1, self.x + 1] = cell_1
                cell_1.x += 1
                cell_1.y -= 1
            else:
                move_cell(1, 1, cells_grid, self)
                cells_grid[self.y - 1, self.x - 1] = cell_3
                cell_3.x -= 1
                cell_3.y -= 1
        elif gas[1] and gas[4]:
            move_cell(-1, 1, cells_grid, self)
            cells_grid[self.y - 1, self.x + 1] = cell_1
            cell_1.x += 1
            cell_1.y -= 1
                
        elif gas[3] and gas[6]:
            move_cell(1, 1, cells_grid, self)
            cells_grid[self.y - 1, self.x - 1] = cell_3
            cell_3.x -= 1
            cell_3.y -= 1
class Gas(Material):
    state = "gas"
    
    def update(self, cells, cells_grid, dimx, dimy):
        self.move(cells, cells_grid, dimx, dimy)

    def move(self, cells, cells_grid, dimx, dimy):
        x, y = self.x, self.y
        cell_7 = get_cell(x-1, y-1, cells_grid, dimx, dimy)      #789
        cell_8 = get_cell(x, y-1, cells_grid, dimx, dimy)        #4 6
        cell_9 = get_cell(x+1, y-1, cells_grid, dimx, dimy)      #123
        cell_4 = get_cell(x-1, y, cells_grid, dimx, dimy)
        cell_6 = get_cell(x+1, y, cells_grid, dimx, dimy)
        empty = [False, False, False, False, cell_4.state == "", False, cell_6.state == "", cell_7.state == "", cell_8.state == "", cell_9.state == ""]

        if empty[8]:
            move_cell(0, -1, cells_grid, self)

        elif empty[7] and empty[9]:
            if randint(0, 1) == 0:
                move_cell(-1, -1, cells_grid, self)
            else:
                move_cell(1, -1, cells_grid, self)
        elif empty[7]:
            move_cell(-1, -1, cells_grid, self)
                
        elif empty[9]:
            move_cell(1, -1, cells_grid, self)

        elif empty[4] and empty[6]:
            if randint(0,1):
                move_cell(-1, 0, cells_grid, self)
            else:
                move_cell(1, 0, cells_grid, self)
            
        elif empty[4]:
            move_cell(-1, 0, cells_grid, self)
            
        elif empty[6]:
            move_cell(1, 0, cells_grid, self)

class Fire(Material):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.life = randint(-200, -100)

    def update(self, cells, cells_grid, dimx, dimy):
        self.extinguish(cells, cells_grid, dimx, dimy)
        self.spread(cells, cells_grid, dimx, dimy)

    def extinguish(self, cells, cells_grid, dimx, dimy):
        self.life += 1
        if 0 < self.life:
            remove_cell(self, cells, cells_grid)

    def spread(self, cells, cells_grid, dimx, dimy):
        for cell in get_nearby_cells(self.x, self.y, cells_grid, dimx, dimy):
            if cell.name == "water":
                remove_cell(cell, cells, cells_grid, dimx, dimy)
                set_cell(cell.x, cell.y, cells, cells_grid, Steam(cell.x, cell.y))
            elif randint(0, 100) < cell.flammability:
                remove_cell(cell, cells, cells_grid)
                if cell.state == "powder":
                    fire_type = PowderFire
                elif cell.state == "solid":
                    fire_type = SolidFire
                elif cell.state == "liquid":
                    fire_type = LiquidFire
                elif cell.state == "gas":
                    fire_type = GasFire
                fire = fire_type(cell.x, cell.y)
                fire.life = cell.burn_time * -1
                set_cell(cell.x, cell.y, cells, cells_grid, fire)


class Sand(Powder):
    name = "sand"
    color = (200, 200, 150)
    flammability = 0
    
class SawDust(Powder):
    name = "sawdust"
    color = (255, 255, 200)
    flammability = 10
    burn_time = 20

class Wall(Solid):
    name = "wood"
    color = (100, 100, 100)
    flammability = 0

class Saw(Solid):
    name = "saw"
    color = (150, 150, 150)
    flammability = 1
    burn_time = 100

class Water(Liquid):
    name = "water"
    color = (50, 100, 200)
    flammability = 0

class SawLiquid(Liquid):
    name = "sawliquid"
    color = (0, 100, 0)
    flammability = 15
    burn_time = 200

class SawGas(Gas):
    name = "sawgas"
    color = (50, 150, 75)
    flammability = 50
    burn_time = 5

class Steam(Gas):
    name = "Steam"
    color = (100, 150, 255)
    flammability = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.life = randint(-200, -100)

    def update(self, cells, cells_grid, dimx, dimy):
        self.condensate(cells, dimx, dimy)
        self.move(cells, cells_grid, dimx, dimy)

    def condensate(self, cells, dimx, dimy):
        self.life += 1
        if 0 < self.life:
            remove_cell(get_cell(self.x, self.y, cells_grid, dimx, dimy), cells, cells_grid)
            set_cell(cell.x, cell.y, cells, cells_grid, Water(cell.x, cell.y))

class PowderFire(Fire, Powder):
    name = "fire"
    color = (255, 100, 0)
    flammability = 0

    def update(self, cells, cells_grid, dimx, dimy):
        self.move(cells, cells_grid, dimx, dimy)
        self.extinguish(cells, cells_grid, dimx, dimy)
        self.spread(cells, cells_grid, dimx, dimy)

class SolidFire(Fire, Solid):
    name = "fire"
    color = (255, 100, 0)
    flammability = 0

class LiquidFire(Fire, Liquid):
    name = "fire"
    color = (255, 100, 0)
    flammability = 0

    def update(self, cells, cells_grid, dimx, dimy):
        self.move(cells, cells_grid, dimx, dimy)
        self.extinguish(cells, cells_grid, dimx, dimy)
        self.spread(cells, cells_grid, dimx, dimy)

class GasFire(Fire, Gas):
    name = "fire"
    color = (255, 100, 0)
    flammability = 0

    def update(self, cells, cells_grid, dimx, dimy):
        self.move(cells, cells_grid, dimx, dimy)
        self.extinguish(cells, cells_grid, dimx, dimy)
        self.spread(cells, cells_grid, dimx, dimy)


material_dict = {
"0":Sand,
"1":Wall,
"2":Water,
"3":Steam,
"4":SawDust,
"5":Saw,
"6":SawLiquid,
"7":SawGas,
"8":SolidFire
    }

num_materials = len(material_dict)
    

def get_cell(x, y, cells, dimx, dimy):
    if 0 <= x < dimx and 0 <= y < dimy:
        cell = cells[int(y), int(x)]
        if cell != 0:
            return cell
    else:
        return Full
    return Empty

def get_nearby_cells(x, y, cells, dimx, dimy):
    results = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            results.append(get_cell(i, j, cells, dimx, dimy))
    return(results)

def set_cell(x, y, cells, cells_grid, cell):
    cells_grid[y, x] = cell
    cells.append(cell)

def remove_cell(cell, cells, cells_grid):
    cells.remove(cell)
    cells_grid[cell.y, cell.x] = 0

def move_cell(x, y, cells_grid, cell):
    cells_grid[cell.y, cell.x] = 0
    cell.x += x
    cell.y += y
    cells_grid[cell.y, cell.x] = cell
