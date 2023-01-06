# -*- coding: utf-8 -*-

# This class provides utility functions for managing the cards in the hand of a single player
class hand () :
    def __init__(self,handCards,number_cards):
        """
        Constructor of a class Hand

        Attributes
        ----------
        handCards : list
            a list of all the cards in the hand .
        number_cards : integer
            The number of card in each player's hand.

       

        """
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
        """
        Throwcard makes sure to ommit the played/thrown card from the players's hand 

        Parameters
        ----------
        CardtoThrow : card
            The potential a player may throw/Play 

        Returns
        -------
        None.

        """
        for i in range(len(self.handCards)) : 
            if  self.handCards[i] == CardtoThrow : 
                self.handCards.pop(i)
                break
            #else : print("don't throw this")
        
    def AddCard (self,CardtoAdd):
        """
        AddCard makes sure to add a card to the player's hand  in the cas where 
        the playerd plays/thows a card and the stockpile is not empty 

        Parameters
        ----------
        CardtoAdd : card
            The card to be added 

        Returns
        -------
        None.

        """
        if len(self.handCards) < self.number_cards :
            self.handCards.append(CardtoAdd)
            # print(CardtoAdd,'Is the Added Card')
        else : print("You have Max Number of cards Already")
        
    def DisplayHand (self):
        """
        DisplayHand displays the player hand to see his/her/its options 

        Returns
        -------
        None.

        """
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
        