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
        self.dec = create_dec()
        avcards = self.dec["Action"] + self.dec["Path"] 
        random.shuffle(avcards)
        self.AvailableCards = avcards
        self.GoldsCards=self.dec["Gold"]
        
                
     
    def regenerate(self):
        avcards = self.dec["Action"] + self.dec["Path"] 
        random.shuffle(avcards)
        self.AvailableCards = avcards
        for crd in self.dec["Goal"]:
            crd.revealed=False



    def Display_score (self):
       for player in self.players :
           print (f"The score of the player named {player.name} is {player.score}")
           
    def Play (self,manche):
       while  manche.Inprogess == False:
           # for now the game ends when we reach the G goal card
           tour=Tour(self.players[0])
           manche.play_tour(tour,map1,manche)
           Sab = manche.DoSabWon (self)
       winner = self.players.index(tour.current_player)
       self.Scoreupdate(Sab,winner)
       self.Display_score()
  
    def Scoreupdate(self,Sab = False ,winner = None) :
        plyrs = list(self.players)
        idxS = []
        if (Sab) : 
            for i in range(len(self.players)) : 
                if (self.players[i].role == 'SAB') :
                    idxS.append(i) 
            SabC = len(idxS)
            for i in idxS : 
                if (SabC == 1 ) : 
                    # We have to POP from the gold cards 4 worth of gold
                    self.players[i].score += 4
                    s = 0 
                    for i in range(len(self.GoldsCards)) : 
                        s += self.GoldsCards[i].gain
                        if ( s == 4) : 
                            self.GoldsCards.remove(self.GoldsCards[i])
                            self.GoldsCards.remove(self.GoldsCards[i-1])
                            break
                elif(SabC == 4) : 
                    self.players[i].score += 2
                    for i in range(len(self.GoldsCards)) : 
                        if (self.GoldsCards[i].gain == 2) : 
                            self.GoldsCards.remove(self.GoldsCards[i])
                            break
                elif(SabC == 3) : 
                    self.players[i].score += 3
                    for i in range(len(self.GoldsCards)) : 
                        if (self.GoldsCards[i].gain == 3) : 
                            self.GoldsCards.remove(self.GoldsCards[i])
                            break
                else : 
                    print("GOLD ERROR")
        else :
            
            GoldC = random.choices(self.GoldsCards,k=len(self.players))
            print(len(GoldC))
            if not ( "B00T" in self.players[winner].name ) : 
                if self.players[winner].role == 'SAB':
                    print(f"player {self.players[winner].name} you were not supposed to do this ... ")
                else:
                    print(f"player {self.players[winner].name} please chose a gold card ")
                    for i in range(len(GoldC)) : 
                        print(f"{i} : {GoldC [i].name} == {GoldC [i].gain}\n")
                    choice = int(input())
                    plyrs[winner].score += GoldC[choice].gain
                    self.GoldsCards.remove(GoldC[choice])
                    GoldC.pop(choice)
            else : 
                gains = []
                for i in range(len(GoldC)) : 
                    gains.append(GoldC[i].gain)
                    
                plyrs[winner].score += max(gains)
                ids = gains.index(max(gains))
                self.GoldsCards.remove(GoldC[ids])
                GoldC.pop(ids)
                
            plyrs.pop(winner)
            print(len(GoldC))
            print(len(plyrs))
            for pl in plyrs : 

                if pl.role == 'SAB' :
                    continue
                if not ("B00T" in pl.name) :
                    print(f"player {pl.name} please chose a gold card ")
                    for i in range(len(GoldC)) : 
                        print(f"{i} : {GoldC [i].name} == {GoldC [i].gain}\n")
                        
                    choice =int(input())
                    pl.score += GoldC[choice].gain
                    self.GoldsCards.remove(GoldC[choice])
                    GoldC.pop(choice)
                else : 
                    gains = []
                    for i in range(len(GoldC)) : 
                        gains.append(GoldC[i].gain)
                        
                    pl.score += max(gains)
                    ids = gains.index(max(gains))
                    self.GoldsCards.remove(GoldC[ids])
                    GoldC.pop(ids)
        #print(len(self.GoldsCards))
                
            
  
    
class hand () :
    def __init__(self,handCards,number_cards):
        self.handCards = handCards
        self.number_cards = number_cards 
    def Throwcard (self,CardtoThrow):
        for i in range(len(self.handCards)) : 
            if  self.handCards[i] == CardtoThrow : 
                self.handCards.pop(i)
                break
            #else : print("don't throw this")
        
    def AddCard (self,CardtoAdd):
        if len(self.handCards) < self.number_cards :
            self.handCards.append(CardtoAdd)
            # print(CardtoAdd,'Is the Added Card')
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
            selectioncards = random.choices(Game.dec["Role"]["S"],k=1) + random.choices(Game.dec["Role"]["C"],k=3)
        elif((num_ply==4)):
            selectioncards = random.choices(Game.dec["Role"]["S"],k=1) + random.choices(Game.dec["Role"]["C"],k=4)
        elif((num_ply==5)):
            selectioncards = random.choices(Game.dec["Role"]["S"],k=2) + random.choices(Game.dec["Role"]["C"],k=4)
        elif((num_ply==6)):
            selectioncards = random.choices(Game.dec["Role"]["S"],k=2) + random.choices(Game.dec["Role"]["C"],k=5)
        elif((num_ply==7)):
            selectioncards = random.choices(Game.dec["Role"]["S"],k=3) + random.choices(Game.dec["Role"]["C"],k=5)
        elif((num_ply==8)):
            selectioncards = random.choices(Game.dec["Role"]["S"],k=3) + random.choices(Game.dec["Role"]["C"],k=6)
        elif((num_ply==9)):
            selectioncards = random.choices(Game.dec["Role"]["S"],k=3) + random.choices(Game.dec["Role"]["C"],k=7)
        elif((num_ply==10)):
            selectioncards = random.choices(Game.dec["Role"]["S"],k=4) + random.choices(Game.dec["Role"]["C"],k=7)
        else :
            print("Number of players is not valid")
            
        random.shuffle(selectioncards)
        for i in range(len(Game.players)) : 
            rand_role = selectioncards.pop(random.randrange(len(selectioncards)))
            Game.players[i].role = rand_role.name
   
            
    def DoSabWon (self,Game):
        Wc = 0
        if (len(self.stockpile)==0):
            for i in range(len(Game.players)) : 
                if (len(Game.players[i].hand.handCards)) == 0 :
                    Wc += 1
                else : 
                    continue
            print(Wc,len(Game.players))
            if (Wc == len(Game.players)):
                self.Inprogess = True
                print("Les saboteurs ont gagné")
                return True
            else : 
                self.Inprogess = False
                print("Partie continue")
                return False
                #for j in range(len(Game.players[i].hand.handCards)):  
                #    if (isinstance(Game.players[i].hand.handCards[j],PathCard)) :
                #        pathC = True
                #        break 
                #    else : continue 
                #if (pathC == True) : break 
                #else : continue 
            #if (pathC == False) : 
               #   self.Inprogess = True
              #    print("Les saboteurs ont gagné")
              #    return True
             # else : 
             #     self.Inprogess = False
             #     print("Partie continue")
             #    return False
        
        
       
    def showRoles (self,Game):
        for i in range (len(Game.players)):
            input(f"player {Game.players[i].name} press a Key ") 
            print(f"Your Role is {Game.players[i].role} \n")
            
    def DistributeCards(self,Game):
        num_ply = len(Game.players)
        avcards = list(Game.AvailableCards)
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
    

        
    def play_tour(self,tour,map,manche):
        tour.boot = False
        #listpl = list(Game.players)
        for pl in Game.players:
            tour.nextplayer(pl) 
            hand1=tour.current_player.hand
            hand1.DisplayHand() 
            if not ("B00T" in pl.name ) : 
                
                print(f"{tour.current_player.name}'s turn to play ")
                idx = int(input("please enter a card or '-1' if you want to throw a card:  "))
    
                if idx == -1:
                     idx = int(input("please select a card to throw: "))
                     print(hand1.handCards[idx],'thrown' )
                     hand1.Throwcard(hand1.handCards[idx])
                     tour.to_throw=False
                        
    
                else :
                    tour.play_card(idx)
    
                if tour.to_throw==True:
                    hand1.Throwcard(hand1.handCards[idx])
            else : 
                if (pl.role == "SAB") : 
                        idxtothrow = 0 
                        for c in range(len(pl.hand.handCards)) : 
                            print(pl.hand.handCards[c])
                            if(isinstance(pl.hand.handCards[c],ActionCard) and pl.hand.handCards[c].function == "Nx" ) :
                                listpl = list(Game.players)
                                listpl.remove(pl) 
                                choice = random.choice(listpl)
                                idxvic = (Game.players).index(choice)
                                tour.play_card(c,Boot = True ,x_pos=None,y_pos=None,map=None,target_player=idxvic)
                                if (tour.boot) :
                                    idxtothrow = c
                                    break 
                                
                            elif( isinstance( pl.hand.handCards[c], PathCard) and pl.hand.handCards[c].function == "Nx"  and len(pl.actions) == 0 ) :
                                error = False 
                                for i in range(map.m) : 
                                     for j in range(map.n) : 
                                         if not (tour.boot) : 
                                            try : 
                                                 tour.play_card(c,Boot = True ,x_pos=i,y_pos=j,map=None,target_player=None)
                                            except : 
                                                error = True
                                                break
                                             #if not (tour.boot) : 
                                             #    pl.hand.handCards[c].reversed = True
                                             #    tour.play_card(c,Boot = True ,x_pos=i,y_pos=j,map=None,target_player=None)
                                         else : 
                                             idxtothrow = c
                                             break
                                     if (tour.boot) : break
                                     if (error) : break
                                if (tour.boot) : break
                                if (error) : continue
                                if (j == (map.n-1) and i == (map.m-1) and not (tour.boot)) :
                                     continue 
                                 #tour.boot = True 
                            elif(len(pl.actions) != 0 ) : 
                                for a in pl.actions :
                                    if a in pl.hand.handCards[c].name and pl.hand.handCards[c].function == "N+" : 
                                        tour.play_card(c,Boot = True ,x_pos=None,y_pos=None,map=None,target_player=(Game.players).index(pl)) 
                                        tour.boot = True 
                                        idxtothrow = c
                                        break
                                if (tour.boot): break 
                                
                            elif (isinstance( pl.hand.handCards[c], ActionCard) and pl.hand.handCards[c].name == "RoF" ) : 
                                x0,y0=map.start_coord[0],map.start_coord[1]
                                if(map.grid[x0+1][y0+1].name != "void") and (map.grid[x0+1][y0+1].function != "Nx"): 
                                    map.grid[x0+1][y0+1] = VoidCard() 
                                    tour.boot = True 
                                    idxtothrow = c
                                    break 
                                elif(map.grid[x0+1][y0].name != "void") and (map.grid[x0+1][y0].function != "Nx") : 
                                    map.grid[x0+1][y0] = VoidCard() 
                                    tour.boot = True 
                                    idxtothrow = c
                                    break
                                elif (map.grid[x0-1][y0].name != "void") and (map.grid[x0-1][y0].function != "Nx") : 
                                    map.grid[x0-1][y0] = VoidCard() 
                                    tour.boot = True 
                                    idxtothrow = c
                                    break 
                                else :
                                   
                                    tour.boot = False
                                    continue 
                            else : 
                                continue
                    
                
                #    else : 
                #        for card in range(len(pl.hand.handCards))  : 
                            
                        
                #            if(isinstance(pl.hand.handCards[c],ActionCard) and pl.hand.handCards[c].function == "Nx" ) :
                #                listpl.remove(pl) 
                #                choice = random.choice(listpl)
                #                idxvic = (Game.players).index(choice)
                #                tour.play_card(c,Boot = True ,x_pos=None,y_pos=None,map=None,target_player=idxvic)
                #                tour.boot = True 
                #                break 
                
                                    
                        if (not tour.boot ) :
                                thrown = False
                                for card in range(len(pl.hand.handCards)) : 
                                    if (pl.hand.handCards[card].function == 'N+') : 
                                        hand1.Throwcard(hand1.handCards[card]) 
                                        break
                                if not thrown and len(pl.hand.handCards) > 0 : 
                                    hand1.Throwcard(hand1.handCards[hand1.handCards.index(random.choice(hand1.handCards))])
                        else : 
                               
                                hand1.Throwcard(hand1.handCards[idxtothrow])
                                    
                else : 
                        
                        idxtothrow = 0 
                        
                        for c in range(len(pl.hand.handCards)) : 
                            # First thing to do :  check if action card are played against the BOOT
                            
                            if(len(pl.actions) != 0 ) : 
                                
                                for a in pl.actions :
                                    if a in pl.hand.handCards[c].name and pl.hand.handCards[c].function == "N+" : 
                                        tour.play_card(c,Boot = True ,x_pos=None,y_pos=None,map=None,target_player=(Game.players).index(pl)) 
                                        tour.boot = True 
                                        idxtothrow = c
                                        break
                                if (tour.boot): break 
                            
                            elif(isinstance(pl.hand.handCards[c],ActionCard) and pl.hand.handCards[c].function == "N+" ) :
                                
                                listpl = list(Game.players)
                                listpl.remove(pl) 
                                choice = random.choice(listpl)
                                idxvic = (Game.players).index(choice)
                                tour.play_card(c,Boot = True ,x_pos=None,y_pos=None,map=None,target_player=idxvic)
                                
                                if (tour.boot) :
                                    idxtothrow = c
                                    
                                    break 
                                
                            elif( isinstance( pl.hand.handCards[c], PathCard) and pl.hand.handCards[c].function == "N+"  and len(pl.actions) == 0 ) :
                                 error=  False 
                                 checkingCoor = [map.start_coord[0],map.start_coord[0]-1,map.start_coord[0]+1,map.start_coord[0]-2,map.start_coord[0]+2]
                                 for i in checkingCoor : 
                                     for j in range(map.n) : 
                                         if not (tour.boot) : 
                                            try : 
                                                tour.play_card(c,Boot = True ,x_pos=i,y_pos=j,map=None,target_player=None)
                                            except : 
                                                error = True
                                                break
                                           #  if not (tour.boot) : 
                                           #      pl.hand.handCards[c].reversed = True
                                           #      tour.play_card(c,Boot = True ,x_pos=i,y_pos=j,map=None,target_player=None)
                                         else : 
                                             idxtothrow = c
                                           
                                             break
                                     if (tour.boot) : 
                                         break
                                     if (error) : break  
                                 if (tour.boot) : 
                                    
                                     break
                                 if (error) : continue 
                                 if (j == (map.n-1) and i == (map.m-1) and not (tour.boot)) :
                                     continue 
                                
                            elif (isinstance( pl.hand.handCards[c], ActionCard) and pl.hand.handCards[c].name == "RoF" ) : 
                                x0,y0=map.start_coord[0],map.start_coord[1]
                                for x in range(map.m) : 
                                    for y in range(map.n) : 
                                        if (map.grid[x][y].name != "void") and (map.grid[x][y].function == "Nx")  : 
                                            map.grid[x][y] = VoidCard() 
                                            tour.boot = True 
                                            idxtothrow = c
                                            break
                                    if (tour.boot) : break 
                                if (tour.boot) : break 

                                if (y == (map.n-1) and x == (map.m-1) and not (tour.boot)) :
                                    continue 
                               
                            else : 
                                continue

                        if (not tour.boot ) :
                                thrown = False
                                for card in range(len(pl.hand.handCards)) : 
                                    if (pl.hand.handCards[card].function == 'Nx') : 
                                        hand1.Throwcard(hand1.handCards[card]) 
                                        thrown = True
                                        break
                                if not thrown and len(pl.hand.handCards) > 0 : 
                                    hand1.Throwcard(hand1.handCards[hand1.handCards.index(random.choice(hand1.handCards))])
                        else : 
                                
                                hand1.Throwcard(hand1.handCards[idxtothrow])
                                    
                                    
                            
            
                        

           
            if len(manche.stockpile)>0 :
                hand1.AddCard(manche.stockpile.pop())
                hand1.DisplayHand()
              
            map.display_map()
            tour.show_actions(Game)
            
            if self.Inprogess:
                print('Partie terminé')
                break 

def random_cards(avcards,num_cr) :
    cards = []
    for i in range(num_cr) : 
        cards.append(avcards.pop(random.randrange(len(avcards))))  
    print("avcard dans la fonction ",len(avcards))
    return cards





class Tour():
    def __init__(self,current_player):
        self.current_player = current_player
        self.to_throw = True
        self.boot = False
    def nextplayer (self,next_player):
        self.current_player = next_player

    def action_on_player(self,target_player,IdxCard,Boot = False):
        maching_cards = 0  
        if (self.current_player.hand.handCards[IdxCard].function == "Nx") : 
            if ( ( self.current_player.hand.handCards[IdxCard].name in target_player.actions) or (len(target_player.actions))==3 ) :
                
                if ("B00T" in self.current_player.name ) : 
                    self.boot = False
                else : 
                    print("Cannot play this card")
                    self.replay_card()
            elif(len(target_player.actions)<3):
                target_player.actions.append(self.current_player.hand.handCards[IdxCard].name)
                self.boot = True
            else : 
                print("error")
                self.replay_card()
        elif (self.current_player.hand.handCards[IdxCard].function == "N+"):
            if (len(target_player.actions)==0) : 
                
                
                if ("B00T" in self.current_player.name ) : 
                    self.boot = False
                else : 
                    print("No action cards in the player's hand")
                    self.replay_card()
            else :
                for idxCardtoRem in range(len(target_player.actions)):
                    #print(target_player.actions[idxCardtoRem])
                    #print(self.current_player.hand.handCards[IdxCard].name)
                    if (target_player.actions[idxCardtoRem][1] in self.current_player.hand.handCards[IdxCard].name):
                        #target_player.actions.pop(idxCardtoRem)
                        maching_cards += 1 
                        idxx =  idxCardtoRem;
                        #print('we took it off') # case where the player have to chose
                        #break
                if (maching_cards == 1) :
                    target_player.actions.pop(idxx)
                    self.boot = True
                else : 
                    if (Boot == False) : 
                        print("Which action would you want to remove : ")
                        for idxCardtoRem in range(len(target_player.actions)) : 
                            print(f"{idxCardtoRem} : {target_player.actions[idxCardtoRem]}\n")
                        idxx = int(input())  
                        target_player.actions.pop(idxx)
                    else : 
                        idxx = 0
                        target_player.actions.pop(idxx)
                        self.boot = True
        else:
            print("The action card cannot be played for the target_player")
            self.boot = False

    def action_on_map (self,IdxCard,Map,x,y):
        x0 = Map.start_coord[0]
        y0 = Map.start_coord[1]
        if (self.current_player.hand.handCards[IdxCard].name == "RoF") :
            print("Rocks falling watch out !")
            xd = int(input('Please enter X: '))
            yd= int(input('Please enter Y: '))
            Map.update_map(self.current_player.hand.handCards[IdxCard],xd,yd)
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
                self.replay_card()
        else :
            print("Error")
            self.replay_card()

    def show_actions(self,Game) :
        for i in range(len(Game.players)):
            print(f"Action cards played on {Game.players[i].name}")
            for crd in Game.players[i].actions:
                print(crd,end="\t")
            print("")
    
    def check_path(self,carda,x_pos,y_pos,MAP=None,not_check=None):
        a=False
        for chr in carda.name:
            
            if chr == not_check :
                
                continue
            if chr=='R':
                
                a=self.check_card(x_pos,y_pos+1,MAP,not_check='L')
                if a :
                    return True
            #print("there is no right")
            if chr=='L':
                
                a=self.check_card(x_pos,y_pos-1,MAP,not_check='R')
                if a :
                    return True
            #print("there is no left")
            if chr=='U':
                
                a=self.check_card(x_pos-1,y_pos,MAP,not_check='D')
                if a :
                    return True
            #1print("there is no up")
            if chr=='D':
                
                a=self.check_card(x_pos+1,y_pos,MAP,not_check='U')
                if a :
                    return True
            #print("there is no down")$
        
        return False

    def check_card(self,x_pos,y_pos,MAP,not_check=None):
        #print (MAP.grid[x_pos][y_pos])
        
        if x_pos >=MAP.m or x_pos < 0:
            
            return False
        elif y_pos >= MAP.n or y_pos < 0 :
            
            return False
        elif MAP.grid[x_pos][y_pos].function == "Nx":
            
            return False
        elif MAP.grid[x_pos][y_pos].name=="UDRL":
            return True 
        elif MAP.grid[x_pos][y_pos].name=="void":
            
            return False
        else:
            return self.check_path(MAP.grid[x_pos][y_pos],x_pos,y_pos,MAP,not_check)


    def play_path(self,IdxCard,x_pos,y_pos,MAP):
        m = MAP.m #5
        n=MAP.n #9

        if x_pos>MAP.m or y_pos>MAP.n:
            print('no path reaches the position',f'({x_pos},{y_pos})')
            self.replay_card()


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
       

        if x_pos>=MAP.m or x_pos==-1 or y_pos>=MAP.n or y_pos==-1:
            
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
            
            reveal_goal=False
            for crd in cord:
                
                
                cond_on_crd = crd[3] in MAP.grid[crd[0]][crd[1]].name 
                cond_on_ncrd = crd[2] in self.current_player.hand.handCards[IdxCard].name
                
            
                if (MAP.grid[crd[0]][crd[1]].name=="void"):
                    
                    pass
                elif  isinstance (MAP.grid[crd[0]][crd[1]],GoalCard) :   #Goal card
                    
                    if ( cond_on_ncrd == True ) and ( MAP.grid[crd[0]][crd[1]].revealed==False and self.current_player.hand.handCards[IdxCard].function == 'N+'):
                       
                        reveal_goal=True  # the goal card will be revealed in condition that it satisfies the path to the Start
                        x_rev=crd[0]    # cooredinated of the card to be reveald if the condition is statisfied
                        y_rev=crd[1]

                        if cond_on_crd==False:
                            
                            MAP.grid[crd[0]][crd[1]].reverse()
                        
                        go=True

                        
                            
                    elif ((cond_on_ncrd) and (cond_on_crd )) or (not (cond_on_ncrd) and not (cond_on_crd )):
                            go=True
                            
                    else:
                        
                        go= False
                        manche1.Inprogess = False 
                        break
                    

                elif ((cond_on_ncrd) and (cond_on_crd)) :
                    
                    go=True
                    
                elif (not (cond_on_ncrd) and not (cond_on_crd )) :
                    
                    go=True
                    
                else:
                    go=False
                    
                    break
            if go:
                if ( self.check_path(self.current_player.hand.handCards[IdxCard],x_pos,y_pos,MAP)) :

                    if reveal_goal:
                        
                        MAP.grid[x_rev][y_rev].revealed=True
                        if 'G' in MAP.grid[x_rev][y_rev].value  :
                            manche1.Inprogess = True

                    MAP.update_map(self.current_player.hand.handCards[IdxCard],x_pos,y_pos)
                    self.boot = True
                   
                else : 
                    #print("card cannot be played")
                    if ("B00T" in self.current_player.name ) : 
                        self.boot = False
                    else : 
                        self.replay_card()
            else : 
                
                if ("B00T" in self.current_player.name ) : 
                    self.boot = False
                else : 
                    print("card cannot be played")
                    self.replay_card()
                 
                    




                #MAP.grid[x_pos][y_pos]=self.current_player.hand.handCards[IdxCard]

        
            

        else:
            
            if ("B00T" in self.current_player.name ) : 
                self.boot = False
            else : 
                print("There is a card already played there")
                self.replay_card()


    def play_card(self,idx,Boot = False ,x_pos=None,y_pos=None,map=None,target_player=None,idxCardtoRem=None):
        if (Boot == False) : 
            self.to_throw=True
            if idx == -1:
                idx = int(input("please select a card to throw: "))
                print(self.current_player.hand.handCards[idx],'thrown' )   
                self.current_player.hand.Throwcard(self.current_player.hand.handCards[idx])
                self.to_throw=False
                #return to_throw
                print(self.to_throw)
            elif isinstance(self.current_player.hand.handCards[idx],PathCard):
                if len(self.current_player.actions)==0:
                    x_corda=int(input("please enter X "))
                    y_corda=int(input("please enter y "))
                    rev=input("Do you want to reverse [Y/N]")
                    if rev =='Y':
                        self.current_player.hand.handCards[idx].reverse()
                    self.play_path(idx,x_corda,y_corda,map1)
                    #self.current_player.hand.Throwcard(self.current_player.hand.handCards[idx])
                else:
                    print(f"{self.current_player.name} please fix your material first")
                    self.replay_card()
            elif isinstance(self.current_player.hand.handCards[idx],ActionCard):
                if self.current_player.hand.handCards[idx].name in ["MAP","RoF"] :
                    self.action_on_map (idx,map1,2,1)
                    #self.current_player.hand.Throwcard(self.current_player.hand.handCards[idx])
                else:
                    for i in range(len(Game.players)):
                        print(f'-{i}- {Game.players[i].name}')
                    target=int(input('Enter a number :'))
                    self.action_on_player(Game.players[target],idx)
                    #self.current_player.hand.Throwcard(self.current_player.hand.handCards[idx])
            #print('to throw raho',self.to_throw)
        else : 
            self.to_throw=True
            if idx == -1:
                print(self.current_player.hand.handCards[idx],'thrown' )   
                self.current_player.hand.Throwcard(self.current_player.hand.handCards[idx])
                self.to_throw=False
                #return to_throw
                print(self.to_throw)
            elif isinstance(self.current_player.hand.handCards[idx],PathCard):
                if len(self.current_player.actions)==0:
                    self.play_path(idx,x_pos,y_pos,map1)
                    #self.current_player.hand.Throwcard(self.current_player.hand.handCards[idx])
                else:
                    print(f"{self.current_player.name} please fix your material first")
                    self.replay_card()
            elif isinstance(self.current_player.hand.handCards[idx],ActionCard):
                if self.current_player.hand.handCards[idx].name in ["MAP","RoF"] :
                    self.action_on_map (idx,map1,2,1)
                    #self.current_player.hand.Throwcard(self.current_player.hand.handCards[idx])
                else:
                    self.action_on_player(Game.players[target_player],idx,Boot = True)
                    #self.current_player.hand.Throwcard(self.current_player.hand.handCards[idx])
            #print('to throw raho',self.to_throw)
        
        

    def replay_card(self):
        print(f"Please  {self.current_player.name} replay :")
        self.current_player.hand.DisplayHand()
        idx=int(input('Select a Card: '))
        self.play_card(idx)


        """"
        if type(self.current_player.hand.handCards[IdxCard])==type(ActionCard):

            self.play_action(IdxCard=IdxCard,map=map,target_player=target_player,idxCardtoRem=idxCardtoRem)

        elif type(self.current_player.hand.handCards[IdxCard])==type(PathCard):

            self.play_path(IdxCard=IdxCard,map=map,target_player=target_player,idxCardtoRem=idxCardtoRem)
        else:
            print("Error type of card invalid")
""" 

        










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
            if (Cardplayed.name == "RoF"):
                self.grid[x][y]= VoidCard()
            elif(self.grid[x][y].name == "void"):
                self.grid[x][y]=Cardplayed
            else :
                print("Error : Card Position")
"""    
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


"""

  

plyr1 = player("B00T 1")
plyr2 = player("B00T 2")
plyr3 = player("B00T 3")

Game = game([plyr1,plyr2,plyr3])
#decc= create_dec()
        #map1 = map(Game.dec)

        #manche1 = manche()

        #map1.display_map()
        #manche1.DistributeRoles(Game)
        #manche1.DistributeCards(Game)
        #manche1.showRoles(Game)

#tour1=Tour(plyr3) 
#hand1=tour1.current_player.hand
#hand1.DisplayHand()
#idx = int(input("please enter an action on path "))
#tour1.action_on_map (idx,map1,2,1)
#map1.display_map()

#Game.Play (manche1)

for i in range(3):
    map1 = map(Game.dec)
    manche1 = manche()

    map1.display_map()
    manche1.DistributeRoles(Game)
    plyr1.role = "CHR"
    plyr2.role = "CHR"
    plyr3.role = "CHR"
    manche1.DistributeCards(Game)
    manche1.showRoles(Game)

    Game.Play (manche1)
    Game.regenerate()
    



"""
while  manche1.Inprogess == False:

    # for now the game ends when we reach the G goal card

    tour1=Tour(Game.players[0])
    manche1.play_tour(tour1,map1)

"""
'''
for pl in Game.players:
    tour1.nextplayer(pl) 
    hand1=tour1.current_player.hand
    hand1.DisplayHand()
    idx = int(input("please enter a card "))
    tour1.play_card(idx)
    hand1.Throwcard(hand1.handCards[idx])
    hand1.AddCard(manche1.stockpile.pop())
    
    map1.display_map()
    tour1.show_actions(Game)
'''    



"""
    for i in range (100):
    hand1.DisplayHand()
    idx = int(input("please enter a card "))
    tour1.play_card(idx)
    
    
    if isinstance(hand1.handCards[idx],PathCard):
        x_corda=int(input("please enter X "))
        y_corda=int(input("please enter y "))
        rev=input("Do you want to reverse [Y/N]")
        if rev =='Y':
            hand1.handCards[idx].reverse()
        tour1.play_path(idx,x_corda,y_corda,map1)
    elif isinstance(hand1.handCards[idx],ActionCard):
        if hand1.handCards[idx].name in ["MAP","RoF"] :
            tour1.action_on_map (idx,map1,2,1)
        else:
            for i in range(len(Game.players)):
                print(f'-{i}- {Game.players[i].name}')
            target=int(input('Enter a number :'))
            tour1.action_on_player(Game.players[target],idx)
    
    #rev=input("Do you want to reverse [Y/N]")
    #if rev =='Y':
        #hand1.handCards[idx].reverse()
    #hand1.DisplayHand()
"""
"""
    hand1.Throwcard(hand1.handCards[idx])
    hand1.AddCard(manche1.stockpile.pop())
    
    map1.display_map()
    tour1.show_actions(Game)
"""


