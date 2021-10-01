from random import randint

col_selected = (255, 100, 100)
squares_x, squares_y, square_size = (20, 20, 30)
col_background = (200, 200, 200)
col_empty = (0, 0, 0)
material_size = 50
UPS = 20



class Material:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.life = 0
        self.amount = 1
    
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
        
    def can_move(self,cell):
        if cell.state in ("", "liquid", "gas"): return True
        elif cell.name == self.name and cell.amount < self.amount: return True
        else: return False
    
    def move(self, cells, cells_grid, dimx, dimy):
        x, y = self.x, self.y
        for n in get_nearby_cells(x, y, cells, cells_grid, dimx, dimy):
            if n.name == self.name:
                ta = n.amount + self.amount
                n.amount = min(1,ta)
                self.amount = max(0,ta-1)
        
        
        cell_1 = get_cell(x-1, y+1, cells_grid, dimx, dimy)      #789
        cell_2 = get_cell(x, y+1, cells_grid, dimx, dimy)        #4 6
        cell_3 = get_cell(x+1, y+1, cells_grid, dimx, dimy)      #123
        cell_4 = get_cell(x-1, y, cells_grid, dimx, dimy)
        cell_6 = get_cell(x+1, y, cells_grid, dimx, dimy)
        empty = [False, self.can_move(cell_1), self.can_move(cell_2), self.can_move(cell_3), self.can_move(cell_4), False, self.can_move(cell_6)]
##        fluid = [False, cell_1.state in ("liquid", "gas"), cell_2.state in ("liquid", "gas"), cell_3.state in ("liquid", "gas"), cell_4.state in ("liquid", "gas"), False, cell_6.state in ("liquid", "gas")]

        if empty[2]:
            move_cell(0, 1, cells_grid, self, dimx, dimy)

        elif empty[1] and empty[3] and empty[4] and empty[6]:
            if randint(0, 1) == 0:
                move_cell(-1, 1, cells_grid, self, dimx, dimy)
            else:
                move_cell(1, 1, cells_grid, self, dimx, dimy)
        elif empty[1] and empty[4]:
            move_cell(-1, 1, cells_grid, self, dimx, dimy)
                
        elif empty[3] and empty[6]:
            move_cell(+1, 1, cells_grid, self, dimx, dimy)

##        elif fluid[2]:
##            move_cell(0, 1, cells_grid, self, dimx, dimy)
##            cells_grid[self.y - 1, self.x] = cell_2
##            cell_2.y -= 1
##
##        elif fluid[1] and fluid[3] and (fluid[4] or empty[4]) and (fluid[6] or empty[6]):
##            if randint(0, 1) == 0:
##                move_cell(-1, 1, cells_grid, self, dimx, dimy)
##                cells_grid[self.y - 1, self.x + 1] = cell_1
##                cell_1.x += 1
##                cell_1.y -= 1
##            else:
##                move_cell(1, 1, cells_grid, self, dimx, dimy)
##                cells_grid[self.y - 1, self.x - 1] = cell_3
##                cell_3.x -= 1
##                cell_3.y -= 1
##        elif fluid[1] and (fluid[4] or empty[4]):
##            move_cell(-1, 1, cells_grid, self, dimx, dimy)
##            cells_grid[self.y - 1, self.x + 1] = cell_1
##            cell_1.x += 1
##            cell_1.y -= 1
##                
##        elif fluid[3] and (fluid[6] or empty[6]):
##            move_cell(1, 1, cells_grid, self, dimx, dimy)
##            cells_grid[self.y - 1, self.x - 1] = cell_3
##            cell_3.x -= 1
##            cell_3.y -= 1
        

class Solid(Material):
    state = "solid"
    pass

class Liquid(Material):
    state = "liquid"
    
    def update(self, cells, cells_grid, dimx, dimy):
        self.move(cells, cells_grid, dimx, dimy)

    def can_move(self,cell):
        if cell.state in ("", "gas"): return True
        #elif cell.name == self.name and cell.amount < self.amount: return True
        else: return False
        
    def move(self, cells, cells_grid, dimx, dimy):
        x, y = self.x, self.y
        for n in get_nearby_cells(x, y, cells, cells_grid, dimx, dimy):
            if n.name == self.name:
                ta = n.amount + self.amount
                n.amount = min(1,ta)
                self.amount = max(0,ta-1)
        
        if  self.amount < 0.1: return
        
        
        cell_1 = get_cell(x-1, y+1, cells_grid, dimx, dimy)      #789
        cell_2 = get_cell(x, y+1, cells_grid, dimx, dimy)        #4 6
        cell_3 = get_cell(x+1, y+1, cells_grid, dimx, dimy)      #123
        cell_4 = get_cell(x-1, y, cells_grid, dimx, dimy)
        cell_6 = get_cell(x+1, y, cells_grid, dimx, dimy)
        empty = [False, self.can_move(cell_1), self.can_move(cell_2), self.can_move(cell_3), self.can_move(cell_4), False, self.can_move(cell_6)]
        
        if empty[2]:
            move_cell(0, 1, cells_grid, self, dimx, dimy)

##        elif empty[1] and empty[3] and empty[4] and empty[6]:
##            if randint(0, 1) == 0:
##                move_cell(-1, 1, cells_grid, self, dimx, dimy)
##            else:
##                move_cell(1, 1, cells_grid, self, dimx, dimy)
##        elif empty[1] and empty[4]:
##            move_cell(-1, 1, cells_grid, self, dimx, dimy)
##                
##        elif empty[3] and empty[6]:
##            move_cell(1, 1, cells_grid, self, dimx, dimy)

        elif empty[4] and empty[6]:
            if randint(0,1):
                move_cell(1, 0, cells_grid, self, dimx, dimy)
            else:
                move_cell(-1, 0, cells_grid, self, dimx, dimy)
            
        elif empty[4]:
            move_cell(-1, 0, cells_grid, self, dimx, dimy)
            
        elif empty[6]:
            move_cell(1, 0, cells_grid, self, dimx, dimy)

##        elif gas[2]:
##            move_cell(0, 1, cells_grid, self, dimx, dimy)
##            cells_grid[self.y - 1, self.x] = cell_2
##            cell_2.y -= 1
##
##        elif gas[1] and gas[3] and gas[4] and gas[6]:
##            if randint(0, 1) == 0:
##                move_cell(-1, 1, cells_grid, self, dimx, dimy)
##                cells_grid[self.y - 1, self.x + 1] = cell_1
##                cell_1.x += 1
##                cell_1.y -= 1
##            else:
##                move_cell(1, 1, cells_grid, self, dimx, dimy)
##                cells_grid[self.y - 1, self.x - 1] = cell_3
##                cell_3.x -= 1
##                cell_3.y -= 1
##        elif gas[1] and gas[4]:
##            move_cell(-1, 1, cells_grid, self, dimx, dimy)
##            cells_grid[self.y - 1, self.x + 1] = cell_1
##            cell_1.x += 1
##            cell_1.y -= 1
##                
##        elif gas[3] and gas[6]:
##            move_cell(1, 1, cells_grid, self, dimx, dimy)
##            cells_grid[self.y - 1, self.x - 1] = cell_3
##            cell_3.x -= 1
##            cell_3.y -= 1
class Gas(Material):
    state = "gas"
    
    def update(self, cells, cells_grid, dimx, dimy):
        self.move(cells, cells_grid, dimx, dimy)

    def can_move(self,cell):
        if cell.state in (""): return True
        elif cell.name == self.name and cell.amount < self.amount: return True
        else: return False
    
    def move(self, cells, cells_grid, dimx, dimy):
        x, y = self.x, self.y
        cell_7 = get_cell(x-1, y-1, cells_grid, dimx, dimy)      #789
        cell_8 = get_cell(x, y-1, cells_grid, dimx, dimy)        #4 6
        cell_9 = get_cell(x+1, y-1, cells_grid, dimx, dimy)      #123
        cell_4 = get_cell(x-1, y, cells_grid, dimx, dimy)
        cell_6 = get_cell(x+1, y, cells_grid, dimx, dimy)
        empty = [False, False, False, False, self.can_move(cell_4), False, self.can_move(cell_6), self.can_move(cell_7), self.can_move(cell_8), self.can_move(cell_9)]

        if empty[8]:
            move_cell(0, -1, cells_grid, self, dimx, dimy)

        elif empty[7] and empty[9]:
            if randint(0, 1) == 0:
                move_cell(-1, -1, cells_grid, self, dimx, dimy)
            else:
                move_cell(1, -1, cells_grid, self, dimx, dimy)
        elif empty[7]:
            move_cell(-1, -1, cells_grid, self, dimx, dimy)
                
        elif empty[9]:
            move_cell(1, -1, cells_grid, self, dimx, dimy)

        elif empty[4] and empty[6]:
            if randint(0,1):
                move_cell(-1, 0, cells_grid, self, dimx, dimy)
            else:
                move_cell(1, 0, cells_grid, self, dimx, dimy)
            
        elif empty[4]:
            move_cell(-1, 0, cells_grid, self, dimx, dimy)
            
        elif empty[6]:
            move_cell(1, 0, cells_grid, self, dimx, dimy)
##<<<<<<< HEAD
##            self.x += 1
##    def diffuse(self, cells, dimx, dimy):
##        x, y = self.x, self.y
##        cell_2 = get_cell(x, y+1, cells, dimx, dimy)      #789
##        cell_4 = get_cell(x-1, y, cells, dimx, dimy)      #4 6
##        cell_6 = get_cell(x+1, y, cells, dimx, dimy)      #123
##        cell_8 = get_cell(x, y-1, cells, dimx, dimy)
##        empty = [False,False,cell_2 == 0, False, cell_4 == 0, False, cell_6 == 0, False, cell_8 == 0]
##        
####        if empty[2] and randint(0,3) == 0:
####            self.y += 1
####        elif empty[4] and randint(0,2) == 0:
####            self.x -= 1
####        elif empty[6] and randint(0,1) == 0:
####            self.x += 1
####        elif empty[8]:
####            self.y -= 1
##        c = 3
##        if empty[2]:
##            if randint(0,c) == 0:
##                self.y += 1
##                return
##            else:
##                c -= 1
##        if empty[4]:
##            if randint(0,c) == 0:
##                self.x -= 1
##                return
##            else:
##                c -= 1
##        if empty[6]:
##            if randint(0,c) == 0:
##                self.x += 1
##                return
##            else:
##                c -= 1
##        if empty[8]:
##            if randint(0,c) == 0:
##                self.y -= 1
##                return
##            else:
##                c -= 1
##=======
            #move_cell(1, 0, cells_grid, self, dimx, dimy)

class Fire(Material):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.life = randint(-200, -100)
        self.amount = 1
        
    def update(self, cells, cells_grid, dimx, dimy):
        if self.spread(cells, cells_grid, dimx, dimy) == 0:
            self.extinguish(cells, cells_grid, dimx, dimy)

    def extinguish(self, cells, cells_grid, dimx, dimy):
        self.life += 1
        if 0 < self.life:
            remove_cell(self, cells, cells_grid)
            smoke = Smoke(self.x,self.y)
            #cells.append(smoke)
            add_cell(self.x, self.y, cells, cells_grid, smoke)
            #return 1
        #return 0

##    def spread(self, cells, dimx, dimy):
##        for cell in get_nearby_cells(self.x, self.y, cells):
##            if cell.name == "water":
##                cells.remove(cell)
##                cells.append(Steam(cell.x, cell.y))
##            elif randint(0, 100) < cell.flammability:
##                cells.remove(cell)
##                if cell.state == "powder":
##                    fire_type = PowderFire
##                elif cell.state == "solid":
##                    fire_type = SolidFire
##                elif cell.state == "liquid":
##                    fire_type = LiquidFire
##                elif cell.state == "gas":
##                    fire_type = GasFire
##                fire = fire_type(cell.x, cell.y)
##                fire.life = cell.burn_time * -1
##                cells.append(fire)
    
    def spread(self, cells, cells_grid, dimx, dimy):
        
        for cell in get_nearby_cells(self.x, self.y, cells, cells_grid, dimx, dimy):
            if cell.name == "water":
                remove_cell(self, cells, cells_grid)
                remove_cell(cell, cells, cells_grid)
                add_cell(self.x, self.y, cells, cells_grid, Smoke(self.x, self.y))
                add_cell(cell.x, cell.y, cells, cells_grid, Steam(cell.x, cell.y))
                
                #print(self.x, self.y, cell.x, cell.y, self, cell, cells_grid[self.y, self.x], cells_grid[cell.y, cell.x])
                #del cell
                #del self
                return 1

            
            elif randint(0, 100) < cell.flammability:
                self.burn(cell.x, cell.y, cells, cells_grid, dimx, dimy)
        return 0
                
    def burn(self, x, y, cells, cells_grid, dimx, dimy):
        #print(34)
        o = 0
        cell = get_cell(x, y, cells_grid, dimx, dimy)
        for c in get_nearby_cells(cell.x, cell.y, cells, cells_grid, dimx, dimy):
            if c.state == "": o += 1
        if o == 0: return
        for dx in range(-1,2):
            for dy in range(-1,2):
                if get_cell(x+dx, y+dy, cells_grid, dimx, dimy).state == "":
                    #print(4)
                    if randint(0,o) == 0:
                        #print(3)
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
                        fire.life = -cell.burn_time
                        if cell.name == "sawgoop" and cell.life > 0:
                            f2 = SawGoop(cell.x + dx, cell.y + dy)
                            f2.life = cell.life - 1
                            
                        else:
                            f2 = fire_type(cell.x + dx, cell.y + dy)
                            f2.life = -cell.burn_time

                        add_cell(fire.x, fire.y, cells, cells_grid, fire)
                        add_cell(f2.x, f2.y, cells, cells_grid, f2)
##                        cells.append(fire)
##                        cells.append(f2)
                        return
                    else: o -= 1

            

##    def spread(self, cells, cells_grid, dimx, dimy):
##        for cell in get_nearby_cells(self.x, self.y, cells_grid, dimx, dimy):
##            if cell.name == "water":
##                remove_cell(cell, cells, cells_grid, dimx, dimy)
##                add_cell(cell.x, cell.y, cells, cells_grid, Steam(cell.x, cell.y))
##            elif randint(0, 100) < cell.flammability:
##                remove_cell(cell, cells, cells_grid)
##                if cell.state == "powder":
##                    fire_type = PowderFire
##                elif cell.state == "solid":
##                    fire_type = SolidFire
##                elif cell.state == "liquid":
##                    fire_type = LiquidFire
##                elif cell.state == "gas":
##                    fire_type = GasFire
##                fire = fire_type(cell.x, cell.y)
##                fire.life = cell.burn_time * -1
##                add_cell(cell.x, cell.y, cells, cells_grid, fire)


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
        self.amount = 1

    def update(self, cells, cells_grid, dimx, dimy):
        self.move(cells, cells_grid, dimx, dimy)
        self.condense(cells, cells_grid, dimx, dimy)
        

    def condense(self, cells, cells_grid, dimx, dimy):
        self.life += 1
        if 0 < self.life:
            #remove_cell(get_cell(self.x, self.y, cells_grid, dimx, dimy), cells, cells_grid)
            remove_cell(self, cells, cells_grid)
            add_cell(self.x, self.y, cells, cells_grid, Water(self.x, self.y))

class PowderFire(Fire, Powder):
    name = "powderfire"
    color = (255, 100, 0)
    flammability = 0

    def update(self, cells, cells_grid, dimx, dimy):
        if self.spread(cells, cells_grid, dimx, dimy) == 0:
            self.move(cells, cells_grid, dimx, dimy)
            self.extinguish(cells, cells_grid, dimx, dimy)
        

class SolidFire(Fire, Solid):
    name = "solidfire"
    color = (255, 100, 30)
    flammability = 0

class LiquidFire(Fire, Liquid):
    name = "liquidfire"
    color = (255, 90, 0)
    flammability = 0

    def update(self, cells, cells_grid, dimx, dimy):
        if self.spread(cells, cells_grid, dimx, dimy) == 0:
            self.move(cells, cells_grid, dimx, dimy)
            self.extinguish(cells, cells_grid, dimx, dimy)

class GasFire(Fire, Gas):
    name = "gasfire"
    color = (230, 100, 0)
    flammability = 0

    def update(self, cells, cells_grid, dimx, dimy):
        if self.spread(cells, cells_grid, dimx, dimy) == 0:
            self.move(cells, cells_grid, dimx, dimy)
            self.extinguish(cells, cells_grid, dimx, dimy)
    

class Smoke(Gas):
    name = "anoxic air"
    color = (50, 50, 50)
    flammability = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.life = randint(-200, -100)
        self.amount = 1
        
    def update(self, cells, cells_grid, dimx, dimy):
        self.move(cells, cells_grid, dimx, dimy)
        self.extinguish(cells, cells_grid, dimx, dimy)
        
    def extinguish(self, cells, cells_grid, dimx, dimy):
        for n in get_nearby_cells(self.x, self.y, cells, cells_grid, dimx, dimy):
            if n.name == "full": self.life += 1
        if 0 < self.life:
            remove_cell(self, cells, cells_grid)

class SawGoop(Liquid):
    name = "sawgoop"
    color = (100, 60, 30)
    flammability = 50
    burn_time = 200

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.life = randint(50, 100)
        self.amount = 1

    def update(self, cells, cells_grid, dimx, dimy):
        for c in get_nearby_cells(self.x, self.y, cells, cells_grid, dimx, dimy):
            if c.state in ("solid", "powder"): return
        self.move(cells, cells_grid, dimx, dimy)


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
"11":GasFire,
"12":Smoke,
"13":SawGoop
    }

num_materials = len(material_dict)
    

def get_cell(x, y, cells_grid, dimx, dimy):
    if 0 <= x < dimx and 0 <= y < dimy:
        cell = cells_grid[int(y), int(x)]
        if cell != 0:
            return cell
    else:
        return Full
    return Empty

def get_nearby_cells(x, y, cells, cells_grid, dimx, dimy):
    results = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if 0 <= i < dimx and 0 <= j < dimy:
                results.append(get_cell(i, j, cells_grid, dimx, dimy))
    #for c in cells:
    #    if c.x in range(x-1, x+2) and c.y in range(y-1, y+2)
    return(results)

def add_cell(x, y, cells, cells_grid, cell):
    cells_grid[y, x] = cell
    cells.append(cell)

def remove_cell(cell, cells, cells_grid):
    cells.remove(cell)
    cells_grid[cell.y, cell.x] = 0

def move_cell(x, y, cells_grid, cell, dimx, dimy):
    if cell.x+x < 0 or cell.x+x >= dimx or cell.y+y < 0 or cell.y+y >= dimy:
        print("Bad movement",cell, cell.x, cell.y, cell.x+x, cell.y+y)
        return
    b = get_cell(cell.x+x, cell.y+y, cells_grid, dimx, dimy)
    
    if b.state not in ("", "1"):
        cells_grid[cell.y, cell.x] = b
        b.x -= x
        b.y -= y
    elif b.state == "": cells_grid[cell.y, cell.x] = 0
    else: print("dfadasdasdf")
    #print("m",cell, cell.x, cell.y, cell.x+x, cell.y+y)
    cell.x += x
    cell.y += y
    
    cells_grid[cell.y, cell.x] = cell
