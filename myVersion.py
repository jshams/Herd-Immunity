import random
random.seed(42)

name = input("Please enter virus name: ")
initial_pop_size = float(input("Please enter population size: "))
vac = float(input("Please enter vaccination percentage in decimal form: "))
mortality = float(input("Please enter mortality rate in decimal form: "))
trans = float(input("Please enter transmission rate in decimal form: "))
init_pop_infected = float(input("Please enter initial infected population: "))
'''while init_pop_infected > initial_pop_size:
    print("Initial infected population cannot be greater than population size.")
    init_pop_infected = input("Please enter initial infected population: ")
'''

pop_size = initial_pop_size
total_dead = 0
iterations = 0
possibly_infected = 0

#def randd(x , y):
    # enter veriable vac, mortality, or transmition
    #

while init_pop_infected != 0 or total_dead != initial_pop_size or iterations == 10:
    possibly_infected = pop_size*(1 - vac)
        #round above
    currently_infected = init_pop_infected*(1 - vac)
        #round above
    dead = currently_infected * mortality
    total_dead += dead
    pop_size = pop_size - total_dead
    init_pop_infected = (currently_infected - dead)*trans
        #REMEMBER TO ADD THAT WITH EACH PERSON INFECTED COMES 100 PERSON LOOPS OF INFECTION...
    iterations += 1
    print("After " + str(iterations) + "iterations of " + name + ":")
    print(str(currently_infected) + " got infected.")
    print(str(dead) + " of the infected people died.")
    print(str(pop_size) + "people remain.")
