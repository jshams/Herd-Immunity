from simulation import Simulation
from person import Person
from virus import Virus
from logger import Logger
#import unittest
import random
#import pytest
random.seed(42)

# create the simulation
def create_simulation():
    # simulation =  Simulation(100, 0.90, "Ebola" 0.70, 0.25, 10)
    population_size = 10000
    vacc_percentage = 0.50
    virus_name = 'Ebola'
    mortality_rate = 0.50
    basic_repro_num = 0.25
    initial_infected = 100
    simulation = Simulation(population_size, vacc_percentage, virus_name,
                            mortality_rate,basic_repro_num,
                            initial_infected)
    return simulation

# test the created simulation
def test_create_simulation():
    # * Check to make the virus instantiator is working
    simulation = create_simulation()
    assert simulation.population_size == 10000
    assert simulation.vacc_percentage == 0.50
    assert simulation.virus_name == "Ebola"
    assert simulation.mortality_rate ==  0.50
    assert simulation.basic_repro_num == 0.25
    assert simulation.initial_infected == 100

def test_should_continue_method():
    simulation = create_simulation()
    test_create_population()
    assert simulation._simulation_should_continue() is True

def test_create_population():
    simulation = create_simulation()
    simulation._create_population(simulation.initial_infected)
    assert simulation.population_size == 10000
    assert simulation.vacc_percentage == 0.50
    infected_count = 0
    assert len(simulation.population) == 10000
    for person in simulation.population:
        if person.infected is not None:
            infected_count += 1
    assert infected_count == 101

def test_run():
    simulation = create_simulation()
    test_create_population()
    simulation._create_population(simulation.initial_infected)

    time_step_counter = 0
    assert time_step_counter == 0
    should_continue = 0
    assert time_step_counter == 0
    
    while should_continue:
        simulation.time_step()
        time_step_counter+=1
        assert time_step_counter == time_step_counter
        should_continue = simulation._simulation_should_continue()
        assert should_continue == simulation._simulation_should_continue()