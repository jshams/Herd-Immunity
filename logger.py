class Logger(object):

    def __init__(self, file_name):
        # TODO:  Finish this initialization method.  The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.log_file = open(file_name, 'w')

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        # TODO: Finish this method.  The simulation class should use this method
        # immediately upon creation,(Q: when is this...?) to log the specific parameters of the simulation
        # as the first line of the file.  This line of metadata should be tab-delimited
        # (each item separated by a '\t' character).
        # NOTE: Since this is the first method called, it will create the text file
        # that we will store all logs in.  Be sure to use 'w' mode when you open the file.
        # For all other methods, we'll want to use the 'a' mode to append our new log to the end,
        # since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!

        first_line = str(("{} {} {} {} {}\n".format(pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num))).replace(" ", " ")
        
        # outputString =  'Population Size: ' + str(pop_size) + '\n'
        # outputString += "% of people vaccinated: " + str(vacc_percentage) + '\n'
        # outputString += "Virus: " + virus_name + '\n'
        # outputString += 'Mortality Rate: ' + str(mortality_rate) + '\n'
        self.log_file.write(first_line)

        # with open(self.file_name, "w") as file:
        #     file.write(first_line)
        #     file.close()

    def log_interaction(self, person1, person2, did_infect=None, person2_vacc=None):
        # TODO: Finish this method. The Simulation object should use this method to
        # log every interaction a sick individual has during each time step. This method
        # should accomplish this by using the information from person1 (the infected person),
        # person2 (the person randomly chosen for the interaction), and the optional
        # keyword arguments passed into the method.  See documentation for more info
        # on the format of the logs that this method should write.
        # NOTE:  You'll need to think
        # about how the booleans passed (or not passed) represent
        # all the possible edge cases!
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        data = (person1._id, 'infected' if did_infect else 'did not infect', person2._id, person2._id, did_infect)
        
        log = '%s %s %s because %s %s' % data
        self.log_file.write(log + '\n')

        # with open(self.file_name, "a") as file:
        #     if did_infect:
        #         file.write("{} has infected {}\n".format(person1._id, person2._id))
        #     else:
        #         if person2_sick:
        #             file.write("{} is already sick\n". format(person2._id))
        #         elif person2_vacc:
        #             file.write("{} is vaccinated\n".format(person2._id))
        #         else:
        #             file.write("{} fails to infect {}\n".format(person1._id, person2._id))
    def log_infection_survival(self, person, did_die_from_infection):
        # TODO: Finish this method.  The Simulation object should use this method to log
        # the results of every call of a Person object's .resolve_infection() method.
        # If the person survives, did_die_from_infection should be False.  Otherwise,
        # did_die_from_infection should be True.  See the documentation for more details
        # on the format of the log.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        data = (person._id, 'died' if did_die_from_infection else 'did not die')
        log = '%s %s from the infection.' % data
        self.log_file.write(log + '\n')


    def log_time_step(self, number_of_dead, time_step_number):
        # TODO: Finish this method.  This method should log when a time step ends, and a
        # new one begins.  See the documentation for more information on the format of the log.
        # NOTE: Stretch challenge opportunity! Modify this method so that at the end of each time
        # step, it also logs a summary of what happened in that time step, including the number of
        # people infected, the number of people dead, etc.  You may want to create a helper class
        # to compute these statistics for you, as a Logger's job is just to write logs!
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        log = 'End of itteration %i. Number of people who died: %d' % (time_step_number, number_of_dead)
        self.log_file.write(log + '\n')
