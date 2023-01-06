# -*- coding: utf-8 -*-
from Cards import *
import random
 
class game(): #Partie

    def __init__(self,players):
        self.players = players
        self.__dec = create_dec()
        avcards = self.dec["Action"] + self.dec["Path"] 
        random.shuffle(avcards)
        self.AvailableCards = avcards
        self.GoldsCards=self.dec["Gold"]
    @property
    def dec( self ) :
        return self.__dec
    @dec.setter
    def dec( self ,dec) :
        self.__dec= dec
                
     
    def __regenerate(self):
        avcards = self.dec["Action"] + self.dec["Path"] 
        random.shuffle(avcards)
        self.AvailableCards = avcards
        for crd in self.dec["Goal"]:
            crd.revealed=False

    def __Display_roles (self):
       roles =  {"CHR" :"Miner/Chercheur",
                   "SAB" :"Saboter/Saboteur" }
       for player in self.players :
           print (f"The player named {player.name} is a {roles[player.role]}")


    def __Display_score (self):
       for player in self.players :
           print (f"The score of the player named {player.name} is {player.score}")
           
    def Play (self,manche,Map):
       while  manche.Endmanche == False:
           # for now the game ends when we reach the G goal card
           tour=Tour(self.players[0])
           manche.play_tour(self,tour,Map)
           if (manche.Endmanche == False) : 
               Sab = manche.DoSabWon (self)
       winner = self.players.index(tour.current_player)
       self.__Scoreupdate(Sab,winner)
       self.__Display_roles()
       self.__Display_score()
       
       for pl_id in range(len(self.players)-1,winner-1,-1):
           A=self.players.pop(pl_id)
           self.players.append(A)



       self.__regenerate()
    def __Scoreupdate(self,Sab = False ,winner = None) :
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
                elif(SabC == 3 or SabC == 2 ) : 
                    self.players[i].score += 3
                    for i in range(len(self.GoldsCards)) : 
                        if (self.GoldsCards[i].gain == 3) : 
                            self.GoldsCards.remove(self.GoldsCards[i])
                            break
                else : 
                    print("GOLD ERROR")
        else :
            GoldC = random.choices(self.GoldsCards,k=len(self.players))
            
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
            for pl in plyrs : 

                if pl.role == 'SAB' :
                    continue
                elif not ("B00T" in pl.name) :
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
                    for h in range(len(self.GoldsCards)) : 
                        if (self.GoldsCards[h]== max(gains)):
                            self.GoldsCards.remove(self.GoldsCards[h])
                    GoldC.pop(ids)   

class Tour():
    def __init__(self,current_player):
        self.__current_player = current_player
        self.__to_throw = True
        self.boot = False
        
        
         
    @property
    def current_player( self ) :
        return self.__current_player
    @current_player.setter
    def current_player( self ,current_player) :
        self.__current_player= current_player
        
        
    @property
    def to_throw( self ) :
        return self.__to_throw
    @to_throw.setter
    def to_throw( self ,to_throw) :
        self.__to_throw= to_throw
    
    def nextplayer (self,next_player):
        self.current_player = next_player

    def action_on_player(self,target_player,IdxCard,Manche,Map,Boot = False):
        maching_cards = 0  
        if (self.current_player.hand.handCards[IdxCard].function == "Nx") : 
            if ( ( self.current_player.hand.handCards[IdxCard].name in target_player.actions) or (len(target_player.actions))==3 ) :
                
                if ("B00T" in self.current_player.name ) : 
                    self.boot = False
                else : 
                    print("Cannot play this card")
                    self.replay_card(Manche,Map)
            elif(len(target_player.actions)<3):
                target_player.actions.append(self.current_player.hand.handCards[IdxCard].name)
                self.boot = True
            else : 
                print("error")
                self.replay_card(Manche,Map)
        elif (self.current_player.hand.handCards[IdxCard].function == "N+"):
            if (len(target_player.actions)==0) : 
                
                
                if ("B00T" in self.current_player.name ) : 
                    self.boot = False
                else : 
                    print("No action cards in the player's hand")
                    self.replay_card(Manche,Map)
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

    def action_on_map (self,IdxCard,Map,x,y,Manche):
        x0 = Map.start_coord[0]
        y0 = Map.start_coord[1]
        if (self.current_player.hand.handCards[IdxCard].name == "RoF") :
            print("Rocks falling watch out !")
            xd = int(input('Please enter X: '))
            yd= int(input('Please enter Y: '))

            if xd>= Map.m or yd>= Map.n or xd< 0 or yd<0 :
                print("Out of Map. Please enter a valid value  of X and Y: ")
                self.replay_card(Manche,Map)
            elif Map.grid[xd][yd].name=="UDRL" or isinstance(Map.grid[xd][yd],VoidCard) or isinstance(Map.grid[xd][yd],GoalCard):
                print("Please enter a valid value  of X and Y:")
                self.replay_card(Manche,Map)
            else:
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
                self.replay_card(Manche,Map)
        else :
            print("Error")
            self.replay_card(Manche,Map)

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


    def play_path(self,IdxCard,x_pos,y_pos,MAP,Manche):
        m = MAP.m #5
        n=MAP.n #9

        if x_pos>MAP.m or y_pos>MAP.n:
            print('no path reaches the position',f'({x_pos},{y_pos})')
            self.replay_card(Manche,MAP)


        cord=[[x_pos-1,y_pos,'U','D'],[x_pos,y_pos-1,'L','R'],[x_pos+1,y_pos,'D','U'],[x_pos,y_pos+1,'R','L']]
     
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
                        Manche.Endmanche = False 
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
                            Manche.Endmanche = True
                            print("Les Chercheurs ont gagnee")

                    MAP.update_map(self.current_player.hand.handCards[IdxCard],x_pos,y_pos)
                    self.boot = True
                   
                else : 
                    #print("card cannot be played")
                    if ("B00T" in self.current_player.name ) : 
                        self.boot = False
                    else : 
                        self.replay_card(Manche,MAP)
            else : 
                
                if ("B00T" in self.current_player.name ) : 
                    self.boot = False
                else : 
                    print("card cannot be played")
                    self.replay_card(Manche,MAP)
                 
                    




                #MAP.grid[x_pos][y_pos]=self.current_player.hand.handCards[IdxCard]

        
            

        else:
            
            if ("B00T" in self.current_player.name ) : 
                self.boot = False
            else : 
                print("There is a card already played there")
                self.replay_card(Manche,MAP)


    def play_card(self,idx,Manche,Map,Game,Boot = False ,x_pos=None,y_pos=None,map=None,target_player=None):
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
                    self.play_path(idx,x_corda,y_corda,Map,Manche)
                    #self.current_player.hand.Throwcard(self.current_player.hand.handCards[idx])
                else:
                    print(f"{self.current_player.name} please fix your material first")
                    self.replay_card(Manche,Map)
            elif isinstance(self.current_player.hand.handCards[idx],ActionCard):
                if self.current_player.hand.handCards[idx].name in ["MAP","RoF"] :
                    self.action_on_map (idx,Map,2,1,Manche)
                    #self.current_player.hand.Throwcard(self.current_player.hand.handCards[idx])
                else:
                    for i in range(len(Game.players)):
                        print(f'-{i}- {Game.players[i].name}')
                    target=int(input('Enter a number :'))
                    self.action_on_player(Game.players[target],idx,Manche,Map)
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
                    self.play_path(idx,x_pos,y_pos,Map,Manche)
                    #self.current_player.hand.Throwcard(self.current_player.hand.handCards[idx])
                else:
                    print(f"{self.current_player.name} please fix your material first")
                    self.replay_card(Manche,Map)
            elif isinstance(self.current_player.hand.handCards[idx],ActionCard):
                if self.current_player.hand.handCards[idx].name in ["MAP","RoF"] :
                    self.action_on_map (idx,Map,2,1,Manche)
                    #self.current_player.hand.Throwcard(self.current_player.hand.handCards[idx])
                else:
                    self.action_on_player(Game.players[target_player],idx,Manche,Map,Boot = True)
                    #self.current_player.hand.Throwcard(self.current_player.hand.handCards[idx])
            #print('to throw raho',self.to_throw)
    def replay_card(self,Manche,Map):
        print(f"Please  {self.current_player.name} replay :")
        self.current_player.hand.DisplayHand()
        idx=int(input('Select a Card: '))
        self.play_card(idx,Manche,Map)
