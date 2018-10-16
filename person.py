import random
from virus import * 
from simulation import *
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

    def did_survive_infection(self, mortality_rate):
        if self.infected != None:
            if random.random() <= mortality_rate:
                self.is_alive = False
                self.infected = None
                #print(self._id, "died")
                return False
            else:
                self.is_vaccinated = True
                self.infected = None
                #print(self._id, "survived and is vaccinated")
                return True
        
        




