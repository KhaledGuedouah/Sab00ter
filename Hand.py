# -*- coding: utf-8 -*-

class hand () :
    def __init__(self,handCards,number_cards):
        self.__handCards = handCards
        self.__number_cards = number_cards 
        
        
    @property
    def handCards( self ) :
        return self.__handCards
    @handCards.setter
    def handCards( self ,handCards) :
        self.__handCards= handCards
    
    @property
    def number_cards( self ) :
        return self.__number_cards
    
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
        for i in range(len(self.handCards)):
            print(f" [{i}]     ",end="")
        print("")
        