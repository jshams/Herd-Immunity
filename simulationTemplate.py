import random, sys
random.seed(42)
from person import Person
from logger import Logger

class Simulation(object):

    def __init__(self, pop_size, vacc_percentage, virus_name,
                 mortality_rate, basic_repro_num, initial_infected=1):
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.virus_name = virus_name    
        self.mortality_rate = mortality_rate
        self.basic_repro_num = basic_repro_num
        self.total_infected = initial_infected
        self.current_infected = initial_infected
        self.next_person_id = 0
        self.initial_infected = initial_infected
        self.total_dead = 0
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, pop_size, vacc_percentage, initial_infected)
        print("running init...")
        # TODO: Create a Logger object and bind it to self.logger.  You should use this
        # logger object to log all events of any importance during the simulation.  Don't forget
        # to call these logger methods in the corresponding parts of the simulation!
        self.logger = Logger(self.file_name)

        # self.logger.write_metadata(self.pop_size, vacc_percentage,
        # self.virus_name, self.mortality_rate, self.basic_repro_num)
        # This attribute will be used to keep track of all the people that catch
        # the infection during a given time step. We'll store each newly infected
        # person's .ID attribute in here.  At the end of each time step, we'll call
        # self._infect_newly_infected() and then reset .newly_infected back to an empty
        # list.
        self.newly_infected = []
        # TODO: Call self._create_population() and pass in the correct parameters.
        # what parameters are required to pass into self._create_population()?
        # Store the array that this method will return in the self.population attribute.
        self.population = self._create_population(self.current_infected)
       

    def _create_population(self, initial_infected):
        # TODO: Finish this method!  This method should be called when the simulation
        # begins, to create the population that will be used. This method should return
        # an array filled with Person objects that matches the specifications of the
        # simulation (correct number of people in the population, correct percentage of
        # people vaccinated, correct number of initially infected people).
        population = []
        infected_count = 0
        self.next_person_id+=1
        while len(population) != self.pop_size:
            if infected_count !=  initial_infected:
                '''
                print("running create population")
                instantiate virus object (varname = name of class(pararameters with self))
                instantiate person object(id, is vaccinated bool, )

                '''
                print("running create population")
                virus_object = Virus(self.virus_name, self.basic_repro_num, self.mortality_rate)
                person_object = Person(self.next_person_id, False, virus_object)

                population.append(person_object)
                infected_count+=1
                self.next_person_id+=1
                # TODO: Create all the infected people first, and then worry about the rest.
                # Don't forget to increment infected_count every time you create a
                # new infected person!
            else:
                # Now create all the rest of the people.
                # Every time a new person will be created, generate a random number between
                # 0 and 1.  If this number is smaller than vacc_percentage, this person
                # should be created as a vaccinated person. If not, the person should be
                # created as an unvaccinated person.
                pass
            # TODO: After any Person object is created, whether sick or healthy,
            # you will need to increment self.next_person_id by 1. Each Person object's
            # ID has to be unique!
        return population

    def _simulation_should_continue(self):
        # TODO: Complete this method!  This method should return True if the simulation
        # should continue, or False if it should not.  The simulation should end under
        # any of the following circumstances:
        #     - The entire population is dead.
        #     - There are no infected people left in the population.
        # In all other instances, the simulation should continue.
        pass

    def run(self):
        # TODO: Finish this method.  This method should run the simulation until
        # everyone in the simulation is dead, or the disease no longer exists in the
        # population. To simplify the logic here, we will use the helper method
        # _simulation_should_continue() to tell us whether or not we should continue
        # the simulation and run at least 1 more time_step.

        # This method should keep track of the number of time steps that
        # have passed using the time_step_counter variable.  Make sure you remember to
        # the logger's log_time_step() method at the end of each time step, pass in the
        # time_step_counter variable!
        time_step_counter = 0
        # TODO: Remember to set this variable to an intial call of
        # self._simulation_should_continue()!
        should_continue = None
        while should_continue:
        # TODO: for every iteration of this loop, call self.time_step() to compute another
        # round of this simulation.  At the end of each iteration of this loop, remember
        # to rebind should_continue to another call of self._simulation_should_continue()!
            pass
        print('The simulation has ended after {time_step_counter} turns.'.format(time_step_counter))

    def time_step(self):
        # TODO: Finish this method!  This method should contain all the basic logic
        # for computing one time step in the simulation.  This includes:
            # - For each infected person in the population:
            #        - Repeat for 100 total interactions:
            #             - Grab a random person from the population.
            #           - If the person is dead, continue and grab another new
            #                 person from the population. Since we don't interact
            #                 with dead people, this does not count as an interaction.
            #           - Else:
            #               - Call simulation.interaction(person, random_person)
            #               - Increment interaction counter by 1.
            pass

    def interaction(self, person, random_person):
        # TODO: Finish this method! This method should be called any time two living
        # people are selected for an interaction.  That means that only living people
        # should be passed into this method.  Assert statements are included to make sure
        # that this doesn't happen.
        assert person1.is_alive == True
        assert random_person.is_alive == True

        # The possible cases you'll need to cover are listed below:
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0 and 1.  If that number is smaller
            #     than basic_repro_num, random_person's ID should be appended to
            #     Simulation object's newly_infected array, so that their .infected
            #     attribute can be changed to True at the end of the time step.
        # TODO: Remember to call self.logger.log_interaction() during this method!
        pass

    def _infect_newly_infected(self):
        # TODO: Finish this method! This method should be called at the end of
        # every time step.  This method should iterate through the list stored in
        # self.newly_infected, which should be filled with the IDs of every person
        # created.  Iterate though this list.
        # For every person id in self.newly_infected:
        #   - Find the Person object in self.population that has this corresponding ID.
        #   - Set this Person's .infected attribute to True.
        # NOTE: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list!

if __name__ == "__main__":
    params = sys.argv[1:]
    pop_size = int(params[0])
    vacc_percentage = float(params[1])
    virus_name = str(params[2])
    mortality_rate = float(params[3])
    basic_repro_num = float(params[4])
    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1
    simulation = Simulation(pop_size, vacc_percentage, virus_name, mortality_rate,
                            basic_repro_num, initial_infected)
    simulation.run()