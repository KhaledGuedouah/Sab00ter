# -*- coding: utf-8 -*-

from abc import ABC , abstractmethod
import random

#Abstract mother class of all card classes 
class Card(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def display_card(self):
        #This methode is for Displaying the card in a visual way
        pass
    
    def __str__(self):
        #Printing of name and function of a card
        return f"{self.name} ({self.function}) card "

# Definition of the inheriting classes of Card
class RoleCard(Card):
    def __init__(self,name,function="Nu"):
        super().__init__()
        self.name = name  # Name of the card
        self.function = function # The function of the card (Neutral : Nu Positiive : N+ of negative : N-)
    def display_card(self):

        fst=" "*len(self.name)
        snd=self.name
        thd=" "*len(self.name)
        shwd= f"({fst})\n({snd})\n({thd})"
        return shwd

    def __str__(self):
        return super().__str__()

class PathCard(Card):
    def __init__ (self,name,function):
        super().__init__()
        self.name = name  # Name of the card
        self.function = function # The function of the card (Neutral : Nu Positiive : N+ of negative : N-)
    def display_card(self):
        fst="   "
        snd=f" {self.function[1]} "
        thd="   "

        if "U" in self.name:
            fst=" | "
        if "L" in self.name:
            snd="-"+snd[1:]
        if "R" in self.name:
            snd=snd[:2]+"-"
        if "D" in self.name:
            thd=" | "
    
        shwd= f"({fst})\n({snd})\n({thd})"
        return shwd
    def reverse(self):
        #This methode reverses the Card 
        self.name=self.name.replace('U','d')
        self.name=self.name.replace('D','u')
        self.name=self.name.replace('R','l')
        self.name=self.name.replace('L','r')
        self.name=self.name.upper()
    def __str__(self):
        return super().__str__()
class ActionCard(Card):
    def __init__(self,name,function="Nu"):
        super().__init__()
        self.name = name  # Name of the card
        self.function = function # The function of the card (Neutral : Nu Positiive : N+ of negative : N-)
    def display_card(self):

        if self.function == "Nx":
            fst= "ATT"
            snd= f"{self.name}"
            thd= "   "
        elif self.function == "N+":
            fst= "DIF"
            snd= f"{self.name}"
            thd= "   "
        else:
            fst=f" {self.name[0]} "
            snd=f"{self.name}"
            thd=f" {self.name[2]} "
        shwd= f"({fst})\n({snd})\n({thd})"
        return shwd
    def __str__(self):
        return super().__str__()

class GoldCard(Card):

    def __init__(self, name, function="Nu",gain=0):
        super().__init__()
        self.name = name  # Name of the card
        self.function = function # The function of the card (Neutral : Nu Positiive : N+ of negative : N-)
        self.gain=gain # This attibut is the gain of the gold card

    def display_card(self):
        fst=f" {self.gain} "
        snd=f"{self.name}"
        thd= "   "
        shwd= f"({fst})\n({snd})\n({thd})"
        return shwd
    def __str__(self):
        return super().__str__()
    
# A void card displays nothing in the map 
class VoidCard(Card):
    def __init__(self):
        super().__init__()
        self.name = "void" 
        self.function = "void"
    def display_card(self):
        fst= "   "
        snd= "   "
        thd= "   "
        shwd= f" {fst} \n {snd} \n {thd} "
        return shwd
    def __str__(self):
        return super().__str__()

class GoalCard(PathCard):
    def __init__(self, name, function="Nu",value='N', revealed=False):
        super().__init__(name,function)
        self.__value=value # The value of a gold card or N if it is a nugget
        self.revealed = revealed # True when the END card is revealed 
    @property
    def value( self ) :
        return self.__value
    @value.setter
    def value( self ,value) :
        self.__value = value

    def show_card(self):
        fst="   "
        snd=f" {self.value} "
        thd="   "

        if "U" in self.name:
            fst=" | "
        if "L" in self.name:
            snd="-"+snd[1:]
        if "R" in self.name:
            snd=snd[:2]+"-"
        if "D" in self.name:
            thd=" | "
    
        shwd= f"({fst})\n({snd})\n({thd})"
        return shwd
    def __str__(self):
        return super().__str__()
    
    def display_card(self):
        if (self.revealed==False):
            fst= "   "
            snd= "END"
            thd= "   "
            shwd= f"({fst})\n({snd})\n({thd})"
            return shwd
        else :
            return self.show_card()
    
    def __str__(self):
        return super().__str__()
    
# Fucntion to create all cards of the game 
def create_dec():
    card_list={"Role" :{"S":[],"C":[]},
               "Action":[],
               "Goal":[],
               "Path":[],
               "Gold":[]}
# 1 card Start
    S=PathCard("UDRL","NS")
    card_list["Start"]=S
# 4 cards Saboteurs
    for _ in range(4):
        S=RoleCard("SAB")
        card_list["Role"]["S"].append(S)

# 7 cards Chercheurs
    for _ in range(7):
        S=RoleCard("CHR")
        card_list["Role"]["C"].append(S)

# 6 cards End reveal
    for _ in range(6):
        S=ActionCard("MAP")
        card_list["Action"].append(S)

# 3 cards Rock fall
    for _ in range(3):
        S=ActionCard("RoF")
        card_list["Action"].append(S)

# 2 cards P repair
    for _ in range(2):
        S=ActionCard(" P ","N+")
        card_list["Action"].append(S)

# 2 cards Light repair
    for _ in range(2):
        S=ActionCard(" Li","N+")
        card_list["Action"].append(S)

# 2 cards Wagon repair  
    for _ in range(2):
        S=ActionCard(" W ","N+")
        card_list["Action"].append(S)

# 3 cards P break
    for _ in range(3):
        S=ActionCard(" P ","Nx")
        card_list["Action"].append(S)

# 3 cards Light break
    for _ in range(3):
        S=ActionCard(" Li","Nx")
        card_list["Action"].append(S)

# 3 cards Wagon break    
    for _ in range(3):
        S=ActionCard(" W ","Nx")
        card_list["Action"].append(S)

 # 3 cards combination of reparations
    S=ActionCard("LiW","N+")
    card_list["Action"].append(S)
    S=ActionCard("LiP","N+")
    card_list["Action"].append(S)
    S=ActionCard(" PW","N+")
    card_list["Action"].append(S)

#3 goal cards

    S=GoalCard("UR",value='N')
    card_list["Goal"].append(S)
    S=GoalCard("UL",value='N')
    card_list["Goal"].append(S)
    S=GoalCard("URLD",value='G')
    card_list["Goal"].append(S)

# 5 card URDL N+
    for _ in range(5):
        S=PathCard("URDL","N+")
        card_list["Path"].append(S)

# 5 card URD N+    
    for _ in range(5):
        S=PathCard("URD","N+")
        card_list["Path"].append(S)

# 5 card URL N+
    for _ in range(5):
        S=PathCard("URL","N+")
        card_list["Path"].append(S)

# 5 card UR N+
    for _ in range(5):
        S=PathCard("UR","N+")
        card_list["Path"].append(S)

# 5 card UL N+
    for _ in range(5):
        S=PathCard("UL","N+")
        card_list["Path"].append(S)
# 5 card UD N+
    for _ in range(5):
        S=PathCard("UD","N+")
        card_list["Path"].append(S)
# 5 card RL N+
    for _ in range(5):
        S=PathCard("RL","N+")
        card_list["Path"].append(S)

# a card URDL Nx
    S=PathCard("URDL","Nx")
    card_list["Path"].append(S)
# a card URD Nx   
    S=PathCard("URD","Nx")
    card_list["Path"].append(S)
# a card URL Nx
    S=PathCard("URL","Nx")
    card_list["Path"].append(S)
# a card UR Nx
    S=PathCard("UR","Nx")
    card_list["Path"].append(S)
# a card UL Nx
    S=PathCard("UL","Nx")
    card_list["Path"].append(S)
# a card UD Nx
    S=PathCard("UD","Nx")
    card_list["Path"].append(S)
# a card RL Nx
    S=PathCard("RL","Nx")
    card_list["Path"].append(S)
# a card R Nx
    S=PathCard("R","Nx")
    card_list["Path"].append(S)
# a card U Nx
    S=PathCard("U","Nx")
    card_list["Path"].append(S)

# 16 1G Gold card RL N+
    for _ in range(5):
        S=GoldCard(" G ",gain=1)
        card_list["Gold"].append(S) 

# 8 2G Gold card RL N+
    for _ in range(5):
        S=GoldCard(" G ",gain=2)
        card_list["Gold"].append(S)    

# 4 3G Gold card RL N+
    for _ in range(5):
        S=GoldCard(" G ",gain=3)
        card_list["Gold"].append(S)   

    return card_list
# This function output a random number of card from a list of cards
def random_cards(avcards,num_cr) :
    cards = []
    for i in range(num_cr) : 
        cards.append(avcards.pop(random.randrange(len(avcards))))  
    return cards
