# -*- coding: utf-8 -*-
import random 
from Hand import hand
from Cards import * 

# This class provides utility functions for the good functioning of a round in the game
class manche () : 
    def __init__(self):
        """
         Constructor of a class manche

         Attributes
         ----------
         stockpile : list
             a list of all the cards in the stockpile .
         Endmanche : integer
             The number of card in each player's hand.

        """
        self.__stockpile = []
        self.__Endmanche = False
        
         
    @property
    def stockpile( self ) :
        return self.__stockpile
    @stockpile.setter
    def stockpile( self ,stockpile) :
        self.__stockpile= stockpile
        
    @property
    def Endmanche( self ) :
        return self.__Endmanche
    @Endmanche.setter
    def Endmanche( self ,Endmanche) :
        self.__Endmanche= Endmanche
    
    def DistributeRoles(self,Game):
        """
        DistributeRoles takes care of distributing the roles of miners and saboters 
        to the players depending on their number

        Parameters
        ----------
        Game : game class
            it containes the players and the available card in the game.

        Returns
        -------
        None.

        """
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
        """
        DoSabWon takes care of checking if the saboters won of the round is still running

        Parameters
        ----------
        Game : game class
            it containes the players and the available card in the game.

        Returns
        -------
        bool
            True : if the saboters won the round / False : if the saboters did not won and the round is still in progress.

        """
        Wc = 0
        if (len(self.stockpile)==0):
            for i in range(len(Game.players)) : 
                if (len(Game.players[i].hand.handCards)== 0 and self.Endmanche == False ) :
                    Wc += 1
                else : 
                    continue
            if (Wc == len(Game.players)):
                self.Endmanche = True
                print("Les saboteurs ont gagné")
                return True
            else : 
                self.Endmanche = False
                print("Partie continue")
                return False
        
        
       
    def showRoles (self,Game):
        """
        showRoles Displays the players and their role (Miner/Chercheurs or Saboter/Saboteur)
        if the player is a B00T the role is not displayed

        Parameters
        ----------
        Game : game class
            it containes the players and the available card in the game.

        Returns
        -------
        None.

        """
        for i in range (len(Game.players)):
            if "B00T" in Game.players[i].name :
                continue
            input(f"player {Game.players[i].name} press a Key ") 
            print(f"Your Role is {Game.players[i].role} \n")
            
    def DistributeCards(self,Game):
        """
        DistributeCards takes care of sitributing shuffled card to the players 
        and stores the rest of the cards in a pile (Stockpile)

        Parameters
        ----------
        Game : game class
            it containes the players and the available card in the game.

        Returns
        -------
        None.

        """
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
    

        
    def play_tour(self,Game,tour,map):
        """
        play_tour goes through all the players (one tour) for them to play and 
        manages the progress of the game depending on wether the player is a B00T 
        or a real person.
        The AI simulating the BOOT is also contained in this function 

        Parameters
        ----------
        Game : game class
            It containes the players and the available card in the game.
        tour : Tour class
            It Contains the current player who's playing , a boolean to keep track 
            if the current player has thronw a card and another boolean to indicate if the player has 
            played in the case if he is a B00T
        map : map Class
            It contains the grid representing the map and the coordinates of the start card.

        Returns
        -------
        None.

        """
        tour.boot = False
        #listpl = list(Game.players)
        for pl in Game.players:
            tour.nextplayer(pl) 
            hand1=tour.current_player.hand
            hand1.DisplayHand() 
            if len(hand1.handCards )== 0 :
                continue
            if not ("B00T" in pl.name ) : 
                
                print(f"{tour.current_player.name}'s turn to play ")
                idx = int(input(f"please enter a card or [0:{len(tour.current_player.hand.handCards)-1}] '-1' if you want to throw a card:  "))
                condition=len(tour.current_player.hand.handCards)
                #print(condition)
                while ( idx!=-1 and  idx<0 ) or idx>=condition :
                    idx = int(input(f"please enter a valid Number [0:{len(tour.current_player.hand.handCards)-1}] card or '-1' if you want to throw a card:  "))

    
                if idx == -1:
                     idx = int(input("please select a card to throw: "))
                     while   idx<0  or idx >= len(tour.current_player.hand.handCards):
                        idx = int(input(f"please enter a valid Number [0:{len(tour.current_player.hand.handCards)-1}] : "))
                     print(hand1.handCards[idx],'thrown' )
                     hand1.Throwcard(hand1.handCards[idx])
                     tour.to_throw=False
                        
    
                else :
                    try : 
                        tour.play_card(idx,self,map,Game)
                    except : 
                        print("Please select another card ...")
                        self.replay_card(self)
    
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
                                tour.play_card(c,self,map,Game,Boot = True ,x_pos=None,y_pos=None,map=None,target_player=idxvic)
                                if (tour.boot) :
                                    idxtothrow = c
                                    break 
                                
                            elif( isinstance( pl.hand.handCards[c], PathCard) and pl.hand.handCards[c].function == "Nx"  and len(pl.actions) == 0 ) :
                                error = False 
                                for i in range(map.m) : 
                                     for j in range(map.n) : 
                                         if not (tour.boot) : 
                                            try : 
                                                 tour.play_card(c,self,map,Game,Boot = True ,x_pos=i,y_pos=j,map=None,target_player=None)
                                            except : 
                                                error = True
                                                tour.boot = False
                                                break
                                             #if not (tour.boot) : 
                                             #    pl.hand.handCards[c].reversed = True
                                             #    tour.play_card(c,self,map,Game,Boot = True ,x_pos=i,y_pos=j,map=None,target_player=None)
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
                                        tour.play_card(c,self,map,Game,Boot = True ,x_pos=None,y_pos=None,map=None,target_player=(Game.players).index(pl)) 
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
                    
                
              
                
                                    
                        if (not tour.boot ) :
                                thrown = False
                                for card in range(len(pl.hand.handCards)) : 
                                    if (pl.hand.handCards[card].function == 'N+') : 
                                        hand1.Throwcard(hand1.handCards[card]) 
                                        break
                                if not thrown and len(pl.hand.handCards) > 0 : 
                                    hand1.Throwcard(hand1.handCards[hand1.handCards.index(random.choice(hand1.handCards))])
                        else : 
                               if (len(pl.hand.handCards) > 0) : 
                                   hand1.Throwcard(hand1.handCards[idxtothrow])
                                    
                else : 
                        
                        idxtothrow = 0 
                        
                        for c in range(len(pl.hand.handCards)) : 
                            # First thing to do :  check if action card are played against the BOOT
                            if(len(pl.actions) != 0 ) : 
                                
                                for a in pl.actions :
                                    if a in pl.hand.handCards[c].name and pl.hand.handCards[c].function == "N+" : 
                                        tour.play_card(c,self,map,Game,Boot = True ,x_pos=None,y_pos=None,map=None,target_player=(Game.players).index(pl)) 
                                        tour.boot = True 
                                        idxtothrow = c
                                        break
                                if (tour.boot): break 
                            
                            elif(isinstance(pl.hand.handCards[c],ActionCard) and pl.hand.handCards[c].function == "N+" ) :
                                
                                listpl = list(Game.players)
                                listpl.remove(pl) 
                                choice = random.choice(listpl)
                                idxvic = (Game.players).index(choice)
                                tour.play_card(c,self,map,Game,Boot = True ,x_pos=None,y_pos=None,map=None,target_player=idxvic)
                                
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
                                                tour.play_card(c,self,map,Game,Boot = True ,x_pos=i,y_pos=j,map=None,target_player=None)
                                            except : 
                                                error = True
                                                break
                                           #  if not (tour.boot) : 
                                           #      pl.hand.handCards[c].reversed = True
                                           #      tour.play_card(c,self,map,Game,Boot = True ,x_pos=i,y_pos=j,map=None,target_player=None)
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
                                if (len(pl.hand.handCards) > 0) : 
                                    hand1.Throwcard(hand1.handCards[idxtothrow])

            if len(self.stockpile)>0 :
                hand1.AddCard(self.stockpile.pop())
                hand1.DisplayHand()
              
            map.display_map()
            tour.show_actions(Game)
            
            if self.Endmanche:
                print('Partie terminé')
                break 
