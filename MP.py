
import random 
import Classes
class map():
    def __init__(self,grid,n,m,start_coord,dec):   
        self.dec=dec
        self.n=9
        self.m=4
        self.start_coord=[2,0]

        goalcards=random.shuffle(self.dec["Goal"])
        grid= [ [ 0 for i in range(n) ] for j in range(m) ] #creating an empty grid     
        grid[2][0]= self.dec["Start"]#filling the starting card
        #filling the goal cards
        grid[0][8]=  goalcards[0]
        grid[2][8]=  goalcards[1]
        grid[4][8]=  goalcards[2] 
        self.grid=grid
