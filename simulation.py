import random, sys
random.seed(42)
from person2 import Person
from logger import Logger
from virus import Virus

class Simulation(object):
    def __init__(self, population_size, vac, virus, people_initially_infected = 1):
        self.population = []
        self.logger = Logger('log.txt')
        self.is_alive = population_size
        self.infected_list = []
        self.dead_list = []
        self.virus = Virus
        self.population_size = population_size
        self.vac = vac
        self.people_initially_infected = people_initially_infected
        self.initialize(people_initially_infected)    

    def initialize(self, people_initially_infected):
        for i in range(self.population_size):
            _id = i
            vaccinated = None
            infected = None
            

        
        
        
        uid = 0
        while x < self.population_size:
            self.person = uid
            uid +=1
    def initial_vaccination(self, ):
        for person in self.population[:int(vac*self.population_size)]:
            self.person.is_vaccinated = True
    def set_people_initially_infected():
        if int(self.mortality*self.population_size) < int(vac*self.population_size):
            person = int(vac*self.population_size)
            while person < self.population_size - self.people_initially_infected:
                self.myguy.person.infected = True
                infected_list.append(self.myguy.person)
                person +=1
        else:
            person = int(self.population_size - people_initially_infected)
            while person <= self.population_size:
                self.myguy.person.infected = True
                person +=1
    def interaction():
        this_functions_list = []
        for person in self.infected_list[0:len(self.infected_list)-1]:
            x = 0
            while x < 100:
                        #crucial line below
                z = self.population[random.randint(0, self.population_size-1)]
                if z.vac == True:
                    print("hello")
                    #log it (was hit by guy but already vaccinated)
                else:
                    if random.random() <= self.transmission:
                        if z.infected != True:
                            z.infected = True
                            this_functions_list.append(z)
                            #log it (was hit by guy and got it)
                        else:
                            print("hello")
                            #log it (was hit by guy but already had it)
                    else:
                            #log it (Was hit by guy but didn't get it)
                            print("hello")
                x += 1
            person += 1
        self.infected_list.append(this_functions_list)

    def survived():
        for person in self.population[0:len(self.population)-1]:
            z = 0
            while z == 0:
                if self.population(z).infected == True:
                    if random.random() <= self.transmission:
                        dead_list.append(self.person.z)
                        population.pop(int(self.person.z))
                        #log it
                    else:
                        #log it
                        print("Hello")
                z+=1
    call()
    namer()
    initial_vaccination()
    set_people_initially_infected()
    while len(infected_list) != 0 or population != 0:
        interaction()
        survived()

    
            


        
            



            #log person interacted with person
            





