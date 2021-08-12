from random import randint

col_selected = (255, 100, 100)
squares_x, squares_y, square_size = (30, 30, 20)




class Material:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.life = 0
    
    def update(self, cells, dimx, dimy):
        return
        
class Powder(Material):
    def update(self, cells, dimx, dimy):
        self.move(cells, dimy, dimx)
    
    def move(self, cells, dimx, dimy):
        x, y = self.x, self.y
        cell_1 = get_cell(x-1, y+1, cells, dimx, dimy)      #789
        cell_2 = get_cell(x, y+1, cells, dimx, dimy)        #4 6
        cell_3 = get_cell(x+1, y+1, cells, dimx, dimy)      #123
        cell_4 = get_cell(x-1, y, cells, dimx, dimy)
        cell_6 = get_cell(x+1, y, cells, dimx, dimy)
        empty = [False, cell_1 == 0, cell_2 == 0, cell_3 == 0, cell_4 == 0, False, cell_6 == 0]

        if empty[2]:
            self.y += 1

        elif empty[1] and empty[3] and empty[4] and empty[6]:
            self.y += 1
            if randint(0, 1) == 0:
                self.x -= 1
            else:
                self.x += 1
        elif empty[1] and empty[4]:
            self.y += 1
            self.x -= 1
                
        elif empty[3] and empty[6]:
            self.y += 1
            self.x += 1

class Liquid(Material):
    def update(self, cells, dimx, dimy):
        self.move(cells, dimy, dimx)

    def move(self, cells, dimy, dimx):
        x, y = self.x, self.y
        cell_1 = get_cell(x-1, y+1, cells, dimx, dimy)      #789
        cell_2 = get_cell(x, y+1, cells, dimx, dimy)        #4 6
        cell_3 = get_cell(x+1, y+1, cells, dimx, dimy)      #123
        cell_4 = get_cell(x-1, y, cells, dimx, dimy)
        cell_6 = get_cell(x+1, y, cells, dimx, dimy)
        empty = [False, cell_1 == 0, cell_2 == 0, cell_3 == 0, cell_4 == 0, False, cell_6 == 0]

        if empty[2]:
            self.y += 1

        elif empty[1] and empty[3] and empty[4] and empty[6]:
            self.y += 1
            if randint(0, 1) == 0:
                self.x -= 1
            else:
                self.x += 1
        elif empty[1] and empty[4]:
            self.y += 1
            self.x -= 1
                
        elif empty[3] and empty[6]:
            self.y += 1
            self.x += 1

        elif empty[4] and empty[6]:
            if randint(0,1):
                self.x += 1
            else:
                self.x -= 1
            
        elif empty[4]:
            self.x -= 1
            
        elif empty[6]:
            self.x += 1

class Gas(Material):
    def update(self, cells, dimx, dimy):
        self.move(cells, dimy, dimx)

    def move(self, cells, dimy, dimx):
        x, y = self.x, self.y
        cell_7 = get_cell(x-1, y-1, cells, dimx, dimy)      #789
        cell_8 = get_cell(x, y-1, cells, dimx, dimy)        #4 6
        cell_9 = get_cell(x+1, y-1, cells, dimx, dimy)      #123
        cell_4 = get_cell(x-1, y, cells, dimx, dimy)
        cell_6 = get_cell(x+1, y, cells, dimx, dimy)
        empty = [False, False, False, False, cell_4 == 0, False, cell_6 == 0, cell_7 == 0, cell_8 == 0, cell_9 == 0]

        if empty[8]:
            self.y -= 1

        elif empty[7] and empty[9]:
            self.y -= 1
            if randint(0, 1) == 0:
                self.x -= 1
            else:
                self.x += 1
        elif empty[7]:
            self.y -= 1
            self.x -= 1
                
        elif empty[9]:
            self.y -= 1
            self.x += 1

        elif empty[4] and empty[6]:
            if randint(0,1):
                self.x += 1
            else:
                self.x -= 1
            
        elif empty[4]:
            self.x -= 1
            
        elif empty[6]:
            self.x += 1

class Solid(Material):
    
    def update(self, cells, dimx, dimy):
        return


class Sand(Powder):
    name = "sand"
    color = (200, 200, 150)
    flammability = 0
    
class Sawdust(Powder):
    name = "sawdust"
    color = (255, 255, 200)
    flammability = 7

class Wall(Solid):
    name = "wood"
    color = (100, 100, 100)
    flammability = 0

class Saw(Solid):
    name = "saw"
    color = (150, 150, 150)
    flammability = 1

class Water(Liquid):
    name = "water"
    color = (50, 100, 200)
    flammability = 0

class SawGas(Gas):
    name = "sawgas"
    color = (0, 100, 0)
    flammability = 20

class Steam(Gas):
    name = "Steam"
    color = (100, 150, 255)
    flammability = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.life = randint(-200, -100)

    def update(self, cells, dimx, dimy):
        self.condensate(cells, dimx, dimy)
        self.move(cells, dimy, dimx)

    def condensate(self, cells, dimx, dimy):
        self.life += 1
        if 0 < self.life:
            cells.remove(get_cell(self.x, self.y, cells, dimx, dimy))
            cells.append(Water(self.x, self.y))

class Fire(Solid):
    name = "fire"
    color = (255, 100, 0)
    flammability = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.life = randint(-200, -100)

    def update(self, cells, dimx, dimy):
        self.extinguish(cells, dimx, dimy)
        self.spread(cells, dimy, dimx)

    def extinguish(self, cells, dimx, dimy):
        self.life += 1
        if 0 < self.life:
            cells.remove(get_cell(self.x, self.y, cells, dimx, dimy))

    def spread(self, cells, dimx, dimy):
        for cell in get_nearby_cells(self.x, self.y, cells):
            if cell.name == "water":
                cells.remove(cell)
                cells.append(Steam(cell.x, cell.y))
            elif randint(0, 100) < cell.flammability:
                cells.remove(cell)
                fire = Fire(cell.x, cell.y)
                fire.life = -100 / cell.flammability
                cells.append(fire)
                
                


material_dict = {
"0":Sand,
"1":Sawdust,
"2":Wall,
"3":Saw,
"4":Water,
"5":Steam,
"6":SawGas,
"7":Fire
    }

num_materials = len(material_dict)
    

def get_cell(x, y, cells, dimx, dimy):
    if 0 <= x < dimx and 0 <= y < dimy:
        for cell in cells:
            if cell.x == x and cell.y == y:
                return cell
    else:
        return 1
    return 0

def get_nearby_cells(x, y, cells):
    results = []
    for cell in cells:
        if cell.x in range(x-1, x+2) and cell.y in range(y-1, y+2):
            results.append(cell)
    return(results)

