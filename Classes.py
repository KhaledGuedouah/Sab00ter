print("Here's where we can code the Classes")

# Definition of the Mother class CARD
class Card():

    def __init__(self,name,function="Nu"):
        self.name=name
        self.function=function
    
    def display_card(self):

        fst=" "*len(self.name)
        snd=self.name
        thd=" "*len(self.name)
        shwd= f"({fst})\n({snd})\n({thd})"
        return shwd

    def __str__(self):
        return f"{self.name} ({self.function}) card "

# Definition of the inheriting classes of Card

class PathCard(Card):
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


class ActionCard(Card):
    def display_card(self):

        if self.function == "Nx":
            fst=f"ATT"
            snd=f"{self.name}"
            thd=f"   "
        elif self.function == "N+":
            fst=f"DIF"
            snd=f"{self.name}"
            thd=f"   "
        else:
            fst=f" {self.name[0]} "
            snd=f"{self.name}"
            thd=f" {self.name[2]} "
        shwd= f"({fst})\n({snd})\n({thd})"
        return shwd


class GoldCard(Card):

    def __init__(self, name, function="Nu",gain=1):
        Card.__init__(self,name,function)
        self.gain=gain

    def display_card(self):
        fst=f" {self.gain} "
        snd=f"{self.name}"
        thd=f"   "
        shwd= f"({fst})\n({snd})\n({thd})"
        return shwd


class GoalCard(PathCard):
    def __init__(self, name, function="Nu",value='N'):
        PathCard.__init__(self,name,function)
        self.value=value

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
        
    def display_card(self):
        fst=f"   "
        snd=f"END"
        thd=f"   "
        shwd= f"({fst})\n({snd})\n({thd})"
        return shwd

# Fucntion to create all cards of the game 

def create_dec():
    card_list=[]

# 4 cards Saboteurs
    for _ in range(4):
        S=Card("SAB")
        card_list.append(S)

# 7 cards Saboteurs
    for _ in range(7):
        S=Card("CHR")
        card_list.append(S)

# 6 cards End reveal
    for _ in range(6):
        S=ActionCard("MAP")
        card_list.append(S)

# 3 cards Rock fall
    for _ in range(3):
        S=ActionCard("RoF")
        card_list.append(S)

# 2 cards P repair
    for _ in range(2):
        S=ActionCard(" P ","N+")
        card_list.append(S)

# 2 cards Light repair
    for _ in range(2):
        S=ActionCard(" Li","N+")
        card_list.append(S)

# 2 cards Wagon repair  
    for _ in range(2):
        S=ActionCard(" W ","N+")
        card_list.append(S)

# 3 cards P break
    for _ in range(3):
        S=ActionCard(" P ","Nx")
        card_list.append(S)

# 3 cards Light break
    for _ in range(3):
        S=ActionCard(" Li","Nx")
        card_list.append(S)

# 3 cards Wagon break    
    for _ in range(3):
        S=ActionCard(" W ","Nx")
        card_list.append(S)

 # 3 cards combination of reparations
    S=ActionCard("LiW","N+")
    card_list.append(S)
    S=ActionCard("LiP","N+")
    card_list.append(S)
    S=ActionCard(" PW","N+")
    card_list.append(S)

#3 goal cards

    S=GoalCard("UR",value='N')
    card_list.append(S)
    S=GoalCard("UL",value='N')
    card_list.append(S)
    S=GoalCard("URLD",value='G')
    card_list.append(S)

# 5 card URDL N+
    for _ in range(5):
        S=PathCard("URDL","N+")
        card_list.append(S)

# 5 card URD N+    
    for _ in range(5):
        S=PathCard("URD","N+")
        card_list.append(S)

# 5 card URL N+
    for _ in range(5):
        S=PathCard("URL","N+")
        card_list.append(S)

# 5 card UR N+
    for _ in range(5):
        S=PathCard("UR","N+")
        card_list.append(S)

# 5 card UL N+
    for _ in range(5):
        S=PathCard("UL","N+")
        card_list.append(S)
# 5 card UD N+
    for _ in range(5):
        S=PathCard("UD","N+")
        card_list.append(S)
# 5 card RL N+
    for _ in range(5):
        S=PathCard("RL","N+")
        card_list.append(S)

# a card URDL Nx
    S=PathCard("URDL","Nx")
    card_list.append(S)
# a card URD Nx   
    S=PathCard("URD","Nx")
    card_list.append(S)
# a card URL Nx
    S=PathCard("URL","Nx")
    card_list.append(S)
# a card UR Nx
    S=PathCard("UR","Nx")
    card_list.append(S)
# a card UL Nx
    S=PathCard("UL","Nx")
    card_list.append(S)
# a card UD Nx
    S=PathCard("UD","Nx")
    card_list.append(S)
# a card RL Nx
    S=PathCard("RL","Nx")
    card_list.append(S)
# a card R Nx
    S=PathCard("R","Nx")
    card_list.append(S)
# a card U Nx
    S=PathCard("U","Nx")
    card_list.append(S)

# 16 1G Gold card RL N+
    for _ in range(5):
        S=GoldCard(" G ",gain=1)
        card_list.append(S) 

# 8 2G Gold card RL N+
    for _ in range(5):
        S=GoldCard(" G ",gain=2)
        card_list.append(S)    

# 4 3G Gold card RL N+
    for _ in range(5):
        S=GoldCard(" G ",gain=3)
        card_list.append(S)   

    return card_list

'''
p=create_dec()

for i in p:
    print(i.display_card())
    print("\n")



carta=PathCard("UDL",'Nx')
print(carta)
carta.display_card()
carta=ActionCard("MAP",'Nu')
print(carta)
carta.display_card()
carta=ActionCard("Lit",'N+')
print(carta)
carta.display_card()
carta=GoldCard("Gld",'Nu',4)
print(carta)
carta.display_card()

carta=GoalCard("ULD",'Nu','N')
print(carta)
dis=carta.display_card()
print(dis)
print(carta.showcard())
'''