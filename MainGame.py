import random 
from Cards import *
from Player import player
from Game import game
from Map import map 
from Manche import manche

# Initialization of the list of players 
Players=[]
# Inputing the number of players as well as the number of B00Ts
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
 
# Input the names of real players
for i in range(Num_players-Num_boots):
    name_player=input(f"Please enter the name of the Player {i+Num_boots+1}: ")
    plyr=player(name_player)
    Players.append(plyr)
    
# Creation a class game 
Game = game(Players)

# Main loop of the game for 3 rounds
for i in range(3):    
    # Creation a map each round 
    map1 = map(Game.dec)
    # Creation a class manche (round)
    manche1 = manche()
    # Display the Map at the start (Void map with only the start and end cards)
    map1.display_map()
    # Distribute roles for the players
    manche1.DistributeRoles(Game)
    # Distribute cards for the players
    manche1.DistributeCards(Game)
    # Show the roles of the real players
    manche1.showRoles(Game) 
    input("Press enter to start the new manche")  
    # Starting the round
    Game.Play (manche1,map1)
print("\n\n")
print("               Finale score              ")
print("*****************************************")
# Designing the Winner
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
input("")
    
    

