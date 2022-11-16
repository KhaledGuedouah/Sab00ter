
import random 
import Classes
class map():
    def __init__(self,grid,dec,n=9,m=4,start_coord=[2,0]):   
        self.dec=dec
        self.n=n
        self.m=m
        self.start_coord=start_coord

        goalcards=random.shuffle(self.dec["Goal"])
        grid= [ [ 0 for i in range(n) ] for j in range(m) ] #creating an empty grid     
        grid[2][0]= self.dec["Start"]#filling the starting card
        #filling the goal cards
        grid[0][8]=  goalcards[0]
        grid[2][8]=  goalcards[1]
        grid[4][8]=  goalcards[2] 
        self.grid=grid
