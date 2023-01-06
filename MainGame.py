import random 
from Cards import *
from Player import player
from Game import game
from Map import map 
from Manche import manche

Players=[]
while True : 
    try : 
        Num_players=int(input("Please enter the number of Players: "))
        break 
    except : 
        print("Please enter an integer between 3 and 11 NOT a letter or a symbol ... ")
while Num_players < 3 or Num_players > 11 :
    Num_players=int(input("Please enter a valid number of Players between 3 and 11: "))

Num_boots=int(input("Please enter the number of Boots: "))
while Num_boots < 0 or Num_boots > Num_players :
    Num_boots=int(input(f"Please enter a valid number of Boots between 0 and {Num_players}: "))

for i in range(Num_boots):
    name_player=f"B00T {i+1}"
    plyr=player(name_player)
    Players.append(plyr)
 

for i in range(Num_players-Num_boots):
    name_player=input(f"Please enter the name of the Player {i+Num_boots+1}: ")
    plyr=player(name_player)
    Players.append(plyr)
    
Game = game(Players)

for i in range(3):
    map1 = map(Game.dec)
    manche1 = manche()

    map1.display_map()
    manche1.DistributeRoles(Game)
    manche1.DistributeCards(Game)
    manche1.showRoles(Game) 
    input("Press enter to start the new manche")  
    Game.Play (manche1,map1)
print("\n\n")
print("               Finale score              ")
print("*****************************************")
maxscore = Game.players[0].score
winner_name = Game.players[0].name
for i in range(len(Game.players)) : 
    print (f"The score of the player named {Game.players[i].name} is {Game.players[i].score}")
    if (Game.players[i].score > maxscore) : 
        maxscore = Game.players[i].score
        winner_name = Game.players[i].name
    print("*****************************************\n")

print(f"The winner is {winner_name}")
print("\n")
print("             CONGRATULATIONS !          ")

    
    

