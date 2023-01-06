# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 11:16:49 2023

@author: khale
"""
from Cards import *
class player():

    def __init__(self,name):
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

        
                
            
 