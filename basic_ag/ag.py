#!/usr/bin/python

from random import random, randint
import ag_aux

# number of bits of individual representation
INDIVIDUAL_LENGTH = 22

# inferior and superior limits of individual value
LOW_BOUND = -10
HIGH_BOUND = 10

# mutation and crossover rate in %
MUTATION_RATE = 1
CROSSOVER_RATE = 60

# population size
POP_SIZE = 10

# Number of generations
GENERATION_NUMBER = 1

def generate_individual():
    return ''.join(str(randint(0,1)) for i  in range(INDIVIDUAL_LENGTH))

def generate_pop():
    return [generate_individual() for i in range(POP_SIZE)] 

def individual_value(individual):
    return LOW_BOUND + (((HIGH_BOUND - LOW_BOUND) * int(individual, 2)) / ((2 ** INDIVIDUAL_LENGTH) - 1.0))
	
def random_percent():
    return random() * 100

def crossover(individual1, individual2):
    if random_percent() < CROSSOVER_RATE:
        pass

def mutation(individual):
    for i in range(len(individual)):
        if random_percent() < MUTATION_RATE:
            if individual[i] == '0':
                individual[i] = '1'
            else:
                individual[i] = '1'

def main():
    pass
    
if __name__ == '__main__':
	main()

