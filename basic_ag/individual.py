#!/usr/bin/python

from random import random, randint

class Individual(object):

    def __init__(self, individual_length, low_bound, high_bound):
        self.individual_length = individual_length
        self.low_bound = low_bound
        self.high_bound = high_bound
        self.individual = Individual.generate_individual(individual_length)


    @staticmethod
    def generate_individual(individual_length):
        return ''.join(str(randint(0,1)) for i  in range(individual_length))
    
    @staticmethod
    def generate_pop(pop_size, individual_length):
        return [Individual.generate_individual(individual_length) for i in range(pop_size)]


# just some tests...
def main():
    i = Individual(10, 4, 5)
    print i.individual_length, " ", i.low_bound, " ", i.high_bound

    j = Individual.generate_pop(5, 10)
    print j

if __name__ == '__main__':
    main()
