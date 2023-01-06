# -*- coding: utf-8 -*-
from Cards import *
import random 
# This class provides utility functions for the MAP of the Game
class map():
    def __init__(self,dec,n=9,m=5,start_coord=[2,0]): 
        """
        Constructor of a class map

        Attributes
        ----------
        dec : hash table (Dictionnary)
            Card Deck
        n : integer, optional
            The width of the map. The default is 9.
        m : integer, optional
            The width of the map. The default is 5.
        start_coord : list, optional
            The coordinates of the starting card. The default is [2,0].

       

        """
        self.dec=dec
        self.n=n
        self.m=m
        self.start_coord=start_coord
        goalcards = self.dec["Goal"]
        voidcard = VoidCard()
        random.shuffle(goalcards)
        grid= [ [ voidcard for i in range(n) ] for j in range(m) ] #creating an empty grid  
        grid[2][0]= self.dec["Start"]#filling the starting card
        #filling the goal cards
        grid[0][8]=  goalcards[0]
        grid[2][8]=  goalcards[1]
        grid[4][8]=  goalcards[2]
        self.__grid=grid
      
    @property
    def grid( self ) :
        return self.__grid
    @grid.setter
    def grid(self ,grid) :
        self.__grid= grid

    def display_map(self) :
        """
        display_map : Displays the entire Map for the players

        Returns
        -------
        None.

        """
        first = ''
        for p in range(self.n):
            first+= "  " + f"{p}" + "  "
        first = " |" + first
        second = "-"* 5 * self.n
        second = "-+"+second
        grid_to_print=''
        print(first)
        print(second)
        for i in range (self.m) :
            for k in range(3):
                line=''
                if (k==1) : line = f"{i}|"
                else : line =  " |"
                for j in range (self.n):
                    a=self.grid[i][j].display_card().split("\n")
                    line = line + a[k]
                grid_to_print+=line+'\n'
        print(grid_to_print)

    def update_map(self,Cardplayed,x,y):
        """
        update_map : Updates the map by adding the played card (if it is a path card) or omiting another 
        card if the card is a Rock fall card and expends the map if the player plays in the outer coordinates 

        Parameters
        ----------
        Cardplayed card
            The played card
        x : integer
            x coordinate where the player wants to play his card 
        y : integer
            y coordinate where the player wants to play his card 

        Returns
        -------
        None.

        """

        if (x == self.m  ) :
            self.grid.append([VoidCard()]*self.n)
            self.grid[x][y]=Cardplayed
            self.m += 1
            
                
        elif (x == -1) :
            self.grid.insert(0,[VoidCard()]*self.n)
            self.grid[x+1][y]=Cardplayed
            self.m += 1
            self.start_coord[0]+=1

        elif (y == self.n) :
            for i in range(self.m):
                self.grid[i].append(VoidCard())
            self.grid[x][y]=Cardplayed
            self.n+=1
        elif (y == -1):
            for i in range(self.m):
                self.grid[i].insert(0,VoidCard())
            self.grid[x][y+1]=Cardplayed
            self.n+=1
            self.start_coord[1]+=1
        else : 
            if (Cardplayed.name == "RoF"):
                self.grid[x][y]= VoidCard()
            elif(self.grid[x][y].name == "void"):
                self.grid[x][y]=Cardplayed
            else :
                print("Error : Card Position")

  
