# -*- coding: utf-8 -*-



from Cards import *
# This class fully describes a player for the game purpose 
class player():

    def __init__(self,name):
        """
        Constructor of a class player
        
        Attributes
        ----------
        name : string
            player's name.
        score : integer
            player's role.The initialisation is 0.
        hand : list
            list of cards in the player's hand.The default is None
        Actions : list
            list of cards in the player's hand.The default is  []

    
        """
        self.name = name
        self.__score = 0
        self.__role = None
        self.__hand =  None
        self.__actions = []
    
    
    @property
    def score( self ) :
        return self.__score
    @score.setter
    def score( self ,score) :
        self.__score = score
        
    @property
    def role( self ) :
        return self.__role
    @role.setter
    def role( self ,role) :
        self.__role= role
            
    @property
    def hand( self ) :
        return self.__hand
    @hand.setter
    def hand( self ,hand) :
        self.__hand= hand
    
    @property
    def actions( self ) :
        return self.__actions
    @actions.setter
    def actions( self ,actions) :
        self.__actions= actions

        
                
            
 