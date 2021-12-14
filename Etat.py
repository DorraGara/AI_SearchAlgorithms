import copy

from random import seed
import random

class Etat:
    def __init__(self, matrix, pos_empty = None, etat_final = None, depth = 0) -> None:
        #print(f"state depth = {depth}")
        self.matrix = matrix
        self.taille = len(matrix)
        self.depth = depth
        if(pos_empty == None):
            self.pos_empty = self.find_pos(matrix, 0)
        else:
            self.pos_empty = pos_empty
        self.etat_final = etat_final
        self.heuristicCache = None
        self.hashCache = None

    def up(self):
        newMatrix = copy.deepcopy(self.matrix)
        empty_x, empty_y = self.pos_empty
        empty_y -= 1
        self.permute(newMatrix, self.pos_empty, (empty_x, empty_y))
        return Etat(newMatrix, (empty_x, empty_y), self.etat_final,depth = self.depth + 1)
    
    def right(self):
        newMatrix = copy.deepcopy(self.matrix)
        empty_x, empty_y = self.pos_empty
        empty_x += 1
        self.permute(newMatrix, self.pos_empty, (empty_x, empty_y))
        return Etat(newMatrix, (empty_x, empty_y), self.etat_final,depth = self.depth + 1)

    def down(self):
        newMatrix = copy.deepcopy(self.matrix)
        empty_x, empty_y = self.pos_empty
        empty_y += 1
        self.permute(newMatrix, self.pos_empty, (empty_x, empty_y))
        return Etat(newMatrix, (empty_x, empty_y), self.etat_final,depth = self.depth + 1)

    def left(self):
        newMatrix = copy.deepcopy(self.matrix)
        empty_x, empty_y = self.pos_empty
        empty_x -= 1
        self.permute(newMatrix, self.pos_empty, (empty_x, empty_y))
        return Etat(newMatrix, (empty_x, empty_y), self.etat_final,depth = self.depth + 1)

    def canGoUp(self):
        x, y = self.pos_empty
        return y != 0
    
    def canGoDown(self):
        x, y = self.pos_empty
        return y != self.taille-1
    
    def canGoRight(self):
        x, y = self.pos_empty
        return x != self.taille-1

    def canGoLeft(self):
        x, y = self.pos_empty
        return x != 0
    
    def permute(self, matrix, old_pos, new_pos):
        old_x, old_y = old_pos
        new_x, new_y = new_pos
        temp = matrix[old_y][old_x]
        matrix[old_y][old_x] = matrix[new_y][new_x]
        matrix[new_y][new_x] = temp

    
    def toString(self):
        x, y = self.pos_empty
        result = ""
        for row in range(self.taille):
            for col in range(self.taille):
                if row != y or col != x:
                    if(self.matrix[row][col]<10 and self.taille>3 ):
                        result += f"  {self.matrix[row][col]} "
                    else:
                        result += f" {self.matrix[row][col]} "
                else:
                    result += "   "
            result += "\n"
        return result

    def get_hash(self) -> int:
        if(self.hashCache != None):
            return self.hashCache
        modulo = self.taille**2 - 1
        prop = 1
        result = 0
        for row in range(self.taille):
            for col in range(self.taille):
                result += self.matrix[row][col]*prop
                prop = prop * modulo
        self.hashCache = result
        return result
                

    def __eq__(self, o: object) -> bool:
        if(type(self) != type(o) or self.taille != o.taille or self.pos_empty != o.pos_empty):
            return False
        return self.get_hash() == o.get_hash()

    def find_pos(self,matrix, value):
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                if(matrix[row][col]==value): return (col, row)
        return (0,0)

    def get_heuristic(self):
        if(self.heuristicCache != None):
            return self.heuristicCache
        self.heuristicCache = self.difference2()
        return self.heuristicCache


    def difference1(self):
        if self.etat_final == None: return 0
        sum = 0
        for row in range(self.taille):
            for col in range(self.taille):
                if(self.etat_final.matrix[row][col]!= self.matrix[row][col]):
                    sum += 1
        return sum

    def difference2(self):
        if self.etat_final == None: return 0
        sum = 0
        other_pos_dict = {}
        for row in range(self.taille):
            for col in range(self.taille):
                other_pos_dict[self.etat_final.matrix[row][col]] = (col, row)
        for row in range(self.taille):
            for col in range(self.taille):
                col2, row2 = other_pos_dict[self.matrix[row][col]]
                sum += abs(col - col2) + abs(row - row2)    
        return sum

    def shuffle(self, seed_number, iterations = 10000):
        seed(seed_number)
        newMatrix = copy.deepcopy(self.matrix)
        new_etat = Etat(newMatrix, self.pos_empty, self.etat_final,depth = self.depth)
        for i in range(iterations):
            random_number = random.randint(0,3)
            if(random_number==0 and new_etat.canGoUp()):
                new_etat = new_etat.up()
            if(random_number==1 and new_etat.canGoRight()):
                new_etat = new_etat.right()
            if(random_number==2 and new_etat.canGoDown()):
                new_etat = new_etat.down()
            if(random_number==3 and new_etat.canGoLeft()):
                new_etat = new_etat.left()
        new_etat.depth = 0
        new_etat.etat_final = self
        new_etat.heuristicCache = None
        new_etat.hashCache = None
        return new_etat
        

                

