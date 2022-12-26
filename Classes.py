print("Here's where we can code the Classes")

import random
#import MP
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
    def reverse(self):
        self.name=self.name.replace('U','d')
        self.name=self.name.replace('D','u')
        self.name=self.name.replace('R','l')
        self.name=self.name.replace('L','r')
        self.name=self.name.upper()

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

    def __init__(self, name, function="Nu",gain=0):
        Card.__init__(self,name,function)
        self.gain=gain

    def display_card(self):
        fst=f" {self.gain} "
        snd=f"{self.name}"
        thd=f"   "
        shwd= f"({fst})\n({snd})\n({thd})"
        return shwd

class VoidCard(Card):
    def __init__(self):
        Card.__init__(self,name="void",function="void")
    def display_card(self):
        fst= "   "
        snd= "   "
        thd= "   "
        shwd= f" {fst} \n {snd} \n {thd} "
        return shwd
    
class GoalCard(PathCard):
    def __init__(self, name, function="Nu",value='N', revealed=False):
        PathCard.__init__(self,name,function)
        self.value=value
        self.revealed = revealed

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
        if (self.revealed==False):
            fst=f"   "
            snd=f"END"
            thd=f"   "
            shwd= f"({fst})\n({snd})\n({thd})"
            return shwd
        else :
            return self.show_card()
    

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
        S=Card("SAB")
        card_list["Role"]["S"].append(S)

# 7 cards Chercheurs
    for _ in range(7):
        S=Card("CHR")
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
class player():

    def __init__(self,name):
        self.name = name
        self.score = 0
        self.role = None
        self.hand =  None
        self.actions = []
            
    """ 
    def Add_Action (self,DesActCard):
      # we have to make sure that (DesActCard.function == "Nx") 
       # probably before caling this function
        if ( ( DesActCard in self.actions) or (len(self.actions)==3) ) :
            print("Cannot play this card") #Go back to choice 
        elif(len(self.actions)<3):
                self.actions.append(DesActCard)
                
    def Remove_Action (self,DesActCard):
        # we have to make sure that (DesActCard.function == "N+") 
        # probably before caling this function
        if (len(self.actions)==0) : 
            print("No action cards in the player's hand")
        for i in range(len(self.actions)): 
            if (self.actions[i].name in DesActCard.name):
                self.actions.pop(i) # case where the player have to chose
                break 
            """
class game(): #Partie

    def __init__(self,players):
        self.players = players
        dec = create_dec()
        avcards = dec["Action"] + dec["Path"] 
        random.shuffle(avcards)
        self.AvailableCards = avcards
            
        
            
     
    
    def Display_score (self):
       for player in self.players :
           print (f"The score of the player named {player.name} is {player.score}")
  #  def startGame
       
  
    
  
    
class hand () :
    def __init__(self,handCards,number_cards):
        self.handCards = handCards
        self.number_cards = number_cards 
    def Throwcard (self,CardtoThrow):
        for i in range(len(self.handCards)) : 
            if  self.handCards[i] == CardtoThrow : 
                self.handCards.pop(i)
                break
            else : print("Error")
    def AddCard (self,CardtoAdd):
        if len(self.handCards) < self.number_cards :
            self.handCards.append(CardtoAdd)
        else : print("You have Max Number of cards Already")
        
    def DisplayHand (self):
        space = "    "
        lines=[[],[],[]]
        for card in self.handCards :
            card_in_lst=card.display_card().split('\n')
            lines[0].append(card_in_lst[0])
            lines[1].append(card_in_lst[1])
            lines[2].append(card_in_lst[2])
        for line in lines:
            print(space.join(line)) 
        
        
            
    def UpdateHand(self,NewHand):
        self.handCards = NewHand
class manche () : 
    def __init__(self):
        self.stockpile = []
        self.Inprogess = False
    def DistributeRoles(self,Game):
        num_ply = len(Game.players)
        if (num_ply==3) : 
            selectioncards = random.choices(create_dec()["Role"]["S"],k=1) + random.choices(create_dec()["Role"]["C"],k=3)
        elif((num_ply==4)):
            selectioncards = random.choices(create_dec()["Role"]["S"],k=1) + random.choices(create_dec()["Role"]["C"],k=4)
        elif((num_ply==5)):
            selectioncards = random.choices(create_dec()["Role"]["S"],k=2) + random.choices(create_dec()["Role"]["C"],k=4)
        elif((num_ply==6)):
            selectioncards = random.choices(create_dec()["Role"]["S"],k=2) + random.choices(create_dec()["Role"]["C"],k=5)
        elif((num_ply==7)):
            selectioncards = random.choices(create_dec()["Role"]["S"],k=3) + random.choices(create_dec()["Role"]["C"],k=5)
        elif((num_ply==8)):
            selectioncards = random.choices(create_dec()["Role"]["S"],k=3) + random.choices(create_dec()["Role"]["C"],k=6)
        elif((num_ply==9)):
            selectioncards = random.choices(create_dec()["Role"]["S"],k=3) + random.choices(create_dec()["Role"]["C"],k=7)
        elif((num_ply==10)):
            selectioncards = random.choices(create_dec()["Role"]["S"],k=4) + random.choices(create_dec()["Role"]["C"],k=7)
        else :
            print("Number of players is not valid")
            
        random.shuffle(selectioncards)
        for i in range(len(Game.players)) : 
            rand_role = selectioncards.pop(random.randrange(len(selectioncards)))
            Game.players[i].role = rand_role.name
            
    def showRoles (self,Game):
        for i in range (len(Game.players)):
            input(f"player {Game.players[i].name} press a Key ") 
            print(f"Your Role is {Game.players[i].role} \n")
            
    def DistributeCards(self,Game):
        num_ply = len(Game.players)
        avcards = Game.AvailableCards
        if (num_ply>=3 and num_ply<=5 ) :
            nm_cr = 6
        elif( (num_ply>=6 and num_ply<=7 )):
            nm_cr = 5
        elif( (num_ply>=8 and num_ply<=10 )):
            nm_cr = 4 
        else :
            print("Number of players is not valid")
            
        for i in range(len(Game.players)) : 
            Game.players[i].hand = hand(random_cards(avcards,nm_cr),nm_cr)
        self.stockpile = avcards
def random_cards(avcards,num_cr) :
    cards = []
    for i in range(num_cr) : 
        cards.append(avcards.pop(random.randrange(len(avcards))))      
    return cards



class Tour():
    def __init__(self,current_player):
        self.current_player = current_player
    def nextplayer (self,next_player):
        self.current_player = next_player

    def action_on_player(self,target_player,IdxCard,idxCardtoRem = None):
        if (self.current_player.hand.handCards[IdxCard].function == "Nx") : 
            if ( ( self.current_player.hand.handCards[IdxCard] in target_player.actions) or (len(target_player.actions))==3 ) :
                print("Cannot play this card") #Go back to choice 
            elif(len(target_player.actions)<3):
                target_player.actions.append(self.current_player.hand.handCards[IdxCard])
            else : 
                print("error")
        elif (self.current_player.hand.handCards[IdxCard].function == "N+"):
            if (len(target_player.actions)==0) : 
                print("No action cards in the player's hand")
            else :
                if (target_player.actions[idxCardtoRem].name in self.current_player.hand.handCards[IdxCard].name):
                    target_player.actions.pop(idxCardtoRem) # case where the player have to chose
                print("The action card cannot be played for the target_player")

    def action_on_map (self,IdxCard,Map,x,y):
        x0 = Map.start_coord[0]
        y0 = Map.start_coord[1]
        if (self.current_player.hand.handCards[IdxCard].name == "RoF") :
            print("raa3333")
            Map.update_map(self.current_player.hand.handCards[IdxCard],x,y)
        elif (self.current_player.hand.handCards[IdxCard].name == "MAP") :
            print("Which card do you want to see")
            print("Up : U | Down : D | Middle : M")
            choice = input()
            while not(choice == 'U' or choice == 'D' or choice == 'M'):
                print("please enter Up : 'U' | Down : D | Middle : M" )
                choice = input()
            if (choice == 'U') : 
                print(Map.grid[x0-2][y0+8].show_card())
            elif(choice == 'D'):
                print(Map.grid[x0+2][y0+8].show_card())
            elif (choice == 'M'):
                print(Map.grid[x0][y0+8].show_card())
            else :
                print("Error Up Down Middle ")
        else :
            print("Error")
    def show_actions(self,Game) :
        for i in range(len(Game.players)):
            print(f"Action cards played on {Game.players[i].name}")
            for crd in Game.players[i].actions:
                print(crd,end="\t")
            print("")
    
    def check_path(self,carda,x_pos,y_pos,MAP=None,not_check=None):
        a=False
        for chr in carda.name:
            print(chr)
            if chr == not_check :
                print("passi",chr)
                continue
            if chr=='R':
                print("We check",chr)
                a=self.check_card(x_pos,y_pos+1,MAP,not_check='L')
                if a :
                    return True
            #print("there is no right")
            if chr=='L':
                print("We check",chr)
                a=self.check_card(x_pos,y_pos-1,MAP,not_check='R')
                if a :
                    return True
            #print("there is no left")
            if chr=='U':
                print("We check",chr)
                a=self.check_card(x_pos-1,y_pos,MAP,not_check='D')
                if a :
                    return True
            #1print("there is no up")
            if chr=='D':
                print("We check",chr)
                a=self.check_card(x_pos+1,y_pos,MAP,not_check='U')
                if a :
                    return True
            #print("there is no down")$
        print(a)
        return False

    def check_card(self,x_pos,y_pos,MAP,not_check=None):
        #print (MAP.grid[x_pos][y_pos])
        if x_pos >=MAP.m or x_pos < 0:
            print("Out Of big X")
            return False
        elif y_pos >= MAP.n or y_pos < 0 :
            print("Out Of Y")
            return False
        elif MAP.grid[x_pos][y_pos].name=="UDRL":
            return True 
        elif MAP.grid[x_pos][y_pos].name=="void":
            print("Void")
            return False
        else:
            return self.check_path(MAP.grid[x_pos][y_pos],x_pos,y_pos,MAP,not_check)


    def play_path(self,IdxCard,x_pos,y_pos,MAP):
        m = MAP.m #5
        n=MAP.n #9
        cord=[[x_pos-1,y_pos,'U','D'],[x_pos,y_pos-1,'L','R'],[x_pos+1,y_pos,'D','U'],[x_pos,y_pos+1,'R','L']]
      #  cord = [[x_pos - 1, y_pos, 'U'], [x_pos, y_pos - 1, 'L'], [x_pos + 1, y_pos, 'D'], [x_pos, y_pos + 1, 'R']]
        cx=[]
        cy=[]
        if (x_pos == 0):

            cx.append(cord[1])
            cx.append(cord[2])
            cx.append(cord[3])
        elif (x_pos == m - 1):
            cx.append(cord[0])
            cx.append(cord[1])
            cx.append(cord[3])
        elif (x_pos == -1):
            cx.append(cord[2])
        elif (x_pos == m):
            cx.append(cord[0])
        else:
            cx=cord


        if (y_pos == 0):
            cy.append(cord[0])
            cy.append(cord[2])
            cy.append(cord[3])
        elif (y_pos == n - 1):
            cy.append(cord[0])
            cy.append(cord[1])
            cy.append(cord[2])
        elif (y_pos == -1):
            cy.append(cord[3])
        elif (y_pos == n):
            cy.append(cord[1])
        else:
            cy = cord
        c=[]
        for elem in cy:
            if elem in cx:
                c.append(elem)


            


        cord=c
        print(cord) 
        print(x_pos,y_pos) 
        print(MAP.n,MAP.m)

        if x_pos==MAP.m or x_pos==-1 or y_pos==MAP.n or y_pos==-1:
            print('we gonna void it on')
            vide=VoidCard()
            MAP.update_map(vide,x_pos,y_pos)
            if x_pos==-1:
                x_pos=0
                cord=[[x_pos+1,y_pos,'D','U']]
            if y_pos==-1:
                y_pos=0 
                cord=[[x_pos,y_pos+1,'R','L']]

        go=False
        #condition_on_sides=MAP.grid[x_pos-1][y_pos].name!="void" or MAP.grid[x_pos][y_pos-1].name!="void" or MAP.grid[x_pos][y_pos+1].name!="void" or MAP.grid[x_pos+1][y_pos].name!="void"
       
        if(MAP.grid[x_pos][y_pos].name=="void"):
            print("Void place, A card can be played here")
            for crd in cord:
                print(crd)
                cond_on_crd = crd[3] in MAP.grid[crd[0]][crd[1]].name 
                cond_on_ncrd = crd[2] in self.current_player.hand.handCards[IdxCard].name
                print(cond_on_crd,cond_on_ncrd)
            
                if (MAP.grid[crd[0]][crd[1]].name=="void"):
                    print("void")
                    pass
                elif  isinstance (MAP.grid[crd[0]][crd[1]],GoalCard) :   #Goal card
                    
                    if ( cond_on_ncrd == True ) and ( MAP.grid[crd[0]][crd[1]].revealed==False ):
                        print('we show the card')
                        MAP.grid[crd[0]][crd[1]].revealed=True
                        if cond_on_crd==False:
                            print('Revere GOAL ')
                            MAP.grid[crd[0]][crd[1]].reverse()
                            go=True
                            
                    elif ((cond_on_ncrd) and (cond_on_crd )) or (not (cond_on_ncrd) and not (cond_on_crd )):
                            go=True
                            print('fixed goal true')
                    else:
                        print('fixed goal false')
                        go= False
                        break
                    print("GOAL true")

                elif ((cond_on_ncrd) and (cond_on_crd )) :
                    
                    go=True
                    print("concored true")
                elif (not (cond_on_ncrd) and not (cond_on_crd )) :
                    
                    go=True
                    print("concored true")
                else:
                    go=False
                    print("brikina")
                    break
            if go:
                if ( self.check_path(self.current_player.hand.handCards[IdxCard],x_pos,y_pos,MAP)) :
                    MAP.update_map(self.current_player.hand.handCards[IdxCard],x_pos,y_pos)
                    print("card played hahaha")
                else : 
                    print("card cannot be played")
            else : 
                print("wlh ghir nqol")
                 
                    




                #MAP.grid[x_pos][y_pos]=self.current_player.hand.handCards[IdxCard]

        
            

        else:
            print("There is a card already played there")


    def play_card(self,IdxCard,x_pos=None,y_pos=None,map=None,target_player=None,idxCardtoRem=None):

        if type(self.current_player.hand.handCards[IdxCard])==type(ActionCard):

            self.play_action(IdxCard=IdxCard,map=map,target_player=target_player,idxCardtoRem=idxCardtoRem)

        elif type(self.current_player.hand.handCards[IdxCard])==type(PathCard):

            self.play_path(IdxCard=IdxCard,map=map,target_player=target_player,idxCardtoRem=idxCardtoRem)
        else:
            print("Error type of card invalid")


        










"""plyr1 = player("Khaled")
plyr2 = player("Feriel")
plyr3 = player("Assil")
Game = game([plyr1,plyr2,plyr3])
manche1 = manche()
manche1.DistributeRoles(Game)
manche1.DistributeCards(Game)
manche1.showRoles(Game)
#print(plyr1.role , plyr2.role , plyr3.role)

hand1 = plyr3.hand 
hand1.DisplayHand ()
tour1 = Tour(plyr3)
idx=int(input("Please play a card \n"))
c = tour1.current_player.hand.handCards[idx]
tour1.play_action(idx,target_player=plyr1)

tour1.nextplayer (plyr2)
plyr2.hand.DisplayHand()
idx=int(input("Please play a card \n"))
tour1.play_action(idx,target_player=plyr3)
tour1.show_actions(Game)"""
class map():
    def __init__(self,dec,n=9,m=5,start_coord=[2,0]):   
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
        self.grid=grid

        
    def display_map(self) :
        first = ''
        for p in range(self.n):
            first+= "  " + f"{p}" + "  "
        first = " |" + first
        second = "-"* 5 * self.n
        second = "-+"+second
        grid_to_print=''
        print(first)
        print(second)
        for i in range (map1.m) :
            for k in range(3):
                line=''
                if (k==1) : line = f"{i}|"
                else : line = f" |"
                for j in range (map1.n):
                    a=map1.grid[i][j].display_card().split("\n")
                    line = line + a[k]
                grid_to_print+=line+'\n'
        print(grid_to_print)

    def update_map(self,Cardplayed,x,y):

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
            if(self.grid[x][y].name == "void"):
                self.grid[x][y]=Cardplayed
            elif (self.grid[x][y].name == "RoF"):
                self.grid[x][y]= VoidCard()
            else :
                print("Error : Card Position")
    
    def check_map (self) :
    
        x0,y0=self.start_coord[0],self.start_coord[1]
        xf1,yf = x0-2,y0+8
        xf2= x0
        xf3= x0+2
        x=[xf1,xf2,xf3]

        #checking expansion from the right on y 
        if (yf<self.n-1): 
            print
            print("expansion from right")
            # top card
            if self.grid[xf1+1][yf].name!= "void" or self.grid[xf1][yf+1].name!= "void" or self.grid[xf1][yf-1].name!= "void":
                self.grid[xf1][yf].revealed=True
            # middle card
            if self.grid[xf2+1][yf].name!= "void" or self.grid[xf2-1][yf].name!= "void" or self.grid[xf2][yf+1].name!= "void" or self.grid[xf2][yf-1].name!="void":
                self.grid[xf2][yf].revealed=True
            # bottom card
            if self.grid[xf3-1][yf].name!= "void" or self.grid[xf3][yf+1].name!= "void" or self.grid[xf3][yf-1].name!= "void":
                self.grid[xf3][yf].revealed=True
        #checking expansion from top
        if (xf1>0):
            print("expansion from top")
            #top card
            if self.grid[xf1-1][yf].name!= "void" or self.grid[xf1+1][yf].name!= "void" or self.grid[xf1][yf-1].name!= "void":
                self.grid[xf1][yf].revealed=True
            #middle card
            if self.grid[xf2+1][yf].name!= "void" or self.grid[xf2-1][yf].name!= "void" or self.grid[xf2][yf-1].name!="void":
                self.grid[xf2][yf].revealed=True
            # bottom card
            if self.grid[xf3-1][yf].name!= "void" or self.grid[xf3][yf-1].name!= "void":
                self.grid[xf3][yf].revealed=True
        #checking expansion from bottom
        if (xf3<self.m-1):
            print("expansion from bottom")
            #top card
            if self.grid[xf1+1][yf].name!= "void" or self.grid[xf1][yf-1].name!= "void":
                self.grid[xf1][yf].revealed=True
            #middle card
            if self.grid[xf2+1][yf].name!= "void" or self.grid[xf2-1][yf].name!= "void" or self.grid[xf2][yf-1].name!="void":
                self.grid[xf2][yf].revealed=True
            # bottom card
            if self.grid[xf3-1][yf].name!= "void" or self.grid[xf3][yf-1].name!= "void" or self.grid[xf3+1][yf].name!= "void":
                self.grid[xf3][yf].revealed=True
        
        #checking for no expansion
        if (xf3==self.m-1 and xf1==0 and yf==self.n-1):
            print("no expansion")
            # top card
            if self.grid[xf1][yf-1].name!= "void" or self.grid[xf1+1][yf].name!= "void":
                self.grid[xf1][yf].revealed=True
            # middle card
            if self.grid[xf2+1][yf].name!= "void" or self.grid[xf2-1][yf].name!= "void" or self.grid[xf2][yf-1].name!="void":
                self.grid[xf2][yf].revealed=True
            # bottom card
            if self.grid[xf3-1][yf].name!= "void" or self.grid[xf3][yf-1].name!= "void" :
                self.grid[xf3][yf].revealed=True




  
decc= create_dec()
map1 = map(decc)
map1.display_map()
plyr1 = player("Khaled")
plyr2 = player("Feriel")
plyr3 = player("Assil")
Game = game([plyr1,plyr2,plyr3])
manche1 = manche()

manche1.DistributeRoles(Game)
manche1.DistributeCards(Game)
manche1.showRoles(Game)
tour1=Tour(plyr3)

hand1 = plyr3.hand 
#hand1.DisplayHand()
#idx = int(input("please enter an action on path "))
#tour1.action_on_map (idx,map1,2,1)
#map1.display_map()

for i in range (100):
    hand1.DisplayHand()
    idx = int(input("please enter a path card "))
    x_corda=int(input("please enter X "))
    y_corda=int(input("please enter y "))
    #rev=input("Do you want to reverse [Y/N]")
    #if rev =='Y':
        #hand1.handCards[idx].reverse()
    #hand1.DisplayHand()
    tour1.play_path(idx,x_corda,y_corda,map1)
    map1.display_map()


