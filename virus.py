# import random
from person import *

class Virus:
    def __init__(self, name, transmission, mortality):
        self.name = name
        self.transmission = transmission
        self.mortality = mortality

'''import random
from Person import *

class Virus:
    def __init__(self, name, transmission, mortality):
        self.name = name
        self.transmission = transmission
        self.mortality = mortality
        
    def interactions(self, person):
        if person.is_vaccinated:
            return(False, "was vaccinated")
        if self.transmission >= random.random():
            person.infected = True
            person.virus = self
            return (True, "is weak")
        return (False, "survived")'''