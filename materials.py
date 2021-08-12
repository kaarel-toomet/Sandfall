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

class Empty:
    state = ""

class Full:
    state = "1"
        
class Powder(Material):
    state = "powder"
    
    def update(self, cells, dimx, dimy):
        self.move(cells, dimx, dimy)
    
    def move(self, cells, dimx, dimy):
        x, y = self.x, self.y
        cell_1 = get_cell(x-1, y+1, cells, dimx, dimy)      #789
        cell_2 = get_cell(x, y+1, cells, dimx, dimy)        #4 6
        cell_3 = get_cell(x+1, y+1, cells, dimx, dimy)      #123
        cell_4 = get_cell(x-1, y, cells, dimx, dimy)
        cell_6 = get_cell(x+1, y, cells, dimx, dimy)
        empty = [False, cell_1.state == "", cell_2.state == "", cell_3.state == "", cell_4.state == "", False, cell_6.state == ""]
        fluid = [False, cell_1.state in ("liquid", "gas"), cell_2.state in ("liquid", "gas"), cell_3.state in ("liquid", "gas"), cell_4.state in ("liquid", "gas"), False, cell_6.state in ("liquid", "gas")]

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

        elif fluid[2]:
            cell_2.y -= 1
            self.y += 1

        elif fluid[1] and fluid[3] and fluid[4] and fluid[6]:
            self.y += 1
            if randint(0, 1) == 0:
                cell_1.x += 1
                cell_1.y -= 1
                self.x -= 1
            else:
                cell_3.x -= 1
                cell_3.y -= 1
                self.x += 1
        elif fluid[1] and fluid[4]:
            cell_1.x += 1
            cell_1.y -= 1
            self.y += 1
            self.x -= 1
                
        elif fluid[3] and fluid[6]:
            cell_3.x -= 1
            cell_3.y -= 1
            self.y += 1
            self.x += 1
        

class Solid(Material):
    state = "solid"
    pass

class Liquid(Material):
    state = "liquid"
    
    def update(self, cells, dimx, dimy):
        self.move(cells, dimx, dimy)

    def move(self, cells, dimx, dimy):
        x, y = self.x, self.y
        cell_1 = get_cell(x-1, y+1, cells, dimx, dimy)      #789
        cell_2 = get_cell(x, y+1, cells, dimx, dimy)        #4 6
        cell_3 = get_cell(x+1, y+1, cells, dimx, dimy)      #123
        cell_4 = get_cell(x-1, y, cells, dimx, dimy)
        cell_6 = get_cell(x+1, y, cells, dimx, dimy)
        empty = [False, cell_1.state == "", cell_2.state == "", cell_3.state == "", cell_4.state == "", False, cell_6.state == ""]
        gas = [False, cell_1.state == "gas", cell_2.state == "gas", cell_3.state == "gas", cell_4.state == "gas", False, cell_6.state == "gas"]

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

        elif gas[2]:
            cell_2.y -= 1
            self.y += 1

        elif gas[1] and gas[3] and gas[4] and gas[6]:
            self.y += 1
            if randint(0, 1) == 0:
                cell_1.x += 1
                cell_1.y -= 1
                self.x -= 1
            else:
                cell_3.x -= 1
                cell_3.y -= 1
                self.x += 1
        elif gas[1] and gas[4]:
            cell_1.x += 1
            cell_1.y -= 1
            self.y += 1
            self.x -= 1
                
        elif gas[3] and gas[6]:
            cell_3.x -= 1
            cell_3.y -= 1
            self.y += 1
            self.x += 1

class Gas(Material):
    state = "gas"
    
    def update(self, cells, dimx, dimy):
        self.move(cells, dimx, dimy)

    def move(self, cells, dimx, dimy):
        x, y = self.x, self.y
        cell_7 = get_cell(x-1, y-1, cells, dimx, dimy)      #789
        cell_8 = get_cell(x, y-1, cells, dimx, dimy)        #4 6
        cell_9 = get_cell(x+1, y-1, cells, dimx, dimy)      #123
        cell_4 = get_cell(x-1, y, cells, dimx, dimy)
        cell_6 = get_cell(x+1, y, cells, dimx, dimy)
        empty = [False, False, False, False, cell_4.state == "", False, cell_6.state == "", cell_7.state == "", cell_8.state == "", cell_9.state == ""]

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

class Fire(Material):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.life = randint(-200, -100)

    def update(self, cells, dimx, dimy):
        self.extinguish(cells, dimx, dimy)
        self.spread(cells, dimx, dimy)

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
                cells.append(fire)


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
    color = (50, 100, 75)
    flammability = 15
    burn_time = 200

class SawGas(Gas):
    name = "sawgas"
    color = (0, 100, 0)
    flammability = 20
    burn_time = 5

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
        self.move(cells, dimx, dimy)

    def condensate(self, cells, dimx, dimy):
        self.life += 1
        if 0 < self.life:
            cells.remove(get_cell(self.x, self.y, cells, dimx, dimy))
            cells.append(Water(self.x, self.y))

class PowderFire(Fire, Powder):
    name = "fire"
    color = (255, 100, 0)
    flammability = 0

    def update(self, cells, dimx, dimy):
        self.extinguish(cells, dimx, dimy)
        self.spread(cells, dimx, dimy)
        self.move(cells, dimx, dimy)

class SolidFire(Fire, Solid):
    name = "fire"
    color = (255, 100, 0)
    flammability = 0

class LiquidFire(Fire, Liquid):
    name = "fire"
    color = (255, 100, 0)
    flammability = 0

    def update(self, cells, dimx, dimy):
        self.extinguish(cells, dimx, dimy)
        self.spread(cells, dimx, dimy)
        self.move(cells, dimx, dimy)

class GasFire(Fire, Gas):
    name = "fire"
    color = (255, 100, 0)
    flammability = 0

    def update(self, cells, dimx, dimy):
        self.extinguish(cells, dimx, dimy)
        self.spread(cells, dimx, dimy)
        self.move(cells, dimx, dimy)


material_dict = {
"0":Sand,
"1":Wall,
"2":Water,
"3":Steam,
"4":SawDust,
"5":Saw,
"6":SawLiquid,
"7":SawGas,
"8":PowderFire,
"9":SolidFire,
"10":LiquidFire,
"11":GasFire
    }

num_materials = len(material_dict)
    

def get_cell(x, y, cells, dimx, dimy):
    if 0 <= x < dimx and 0 <= y < dimy:
        for cell in cells:
            if cell.x == x and cell.y == y:
                return cell
    else:
        return Full
    return Empty

def get_nearby_cells(x, y, cells):
    results = []
    for cell in cells:
        if cell.x in range(x-1, x+2) and cell.y in range(y-1, y+2):
            results.append(cell)
    return(results)

