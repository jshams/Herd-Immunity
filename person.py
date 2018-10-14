import random
from simulation import *
from virus import *
# TODO: Import the virus clase

class Person(object):
    # before u passed in a 'virus; 
    def __init__(self, _id, is_vaccinated = bool, infected = None):
        # TODO:  Finish this method.  Follow the instructions in the class documentation
        # to set the corret values for the following attributes.
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.is_alive = True
        self.infected = infected
        #self.virus = virus
'''
    def interactions(self, friend):
        if friend.infected:
            return(False)
        else:
            return self.virus.attack(friend)
            
    def is_dead(self):
        if self.virus.mortality >= random.random():
            self.is_alive = False
        else:
            self.is_vaccinated = True
            self.infected = False
'''
    def did_survive_infection(self):
        if self.infected != None:
            if random.random() <= self.morality:
                self.is_alive = False
                self.infected = True
                return False
            else:
                self.is_vaccinated = True
                self.infected = None
                return True
        
        




