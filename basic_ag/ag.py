#!/usr/bin/python

from random import random, randint
import sys
import ag_aux


# number of bits of individual representation
INDIVIDUAL_LENGTH = 0

# inferior and superior limits of individual value
LOW_BOUND = -10
HIGH_BOUND = 10

# mutation and crossover rate in %
MUTATION_RATE = 0
CROSSOVER_RATE = 0

# population size
POP_SIZE = 0

# Population's collection
POPS = []

# Number of generations
GENERATION_NUMBER = 0


def get_args():
    global INDIVIDUAL_LENGTH

    if len(sys.argv) < 6:
        show_help()
        sys.exit(0)

    print "sys.argv[1]: ", sys.argv[1]
    INDIVIDUAL_LENGTH = sys.argv[1]
    
def show_help():
    pass 

# round selection
def selection():
    pass

def avaliation():
    pass
    
def main():
    populations = []
    get_args()
    print "I.L. >> ", INDIVIDUAL_LENGTH
    #initialize()

    for i in range(GENERATION_NUMBER):
        avaliation()
        selection()
        # todo: implement Genetic Algorithm
        # fitness
        # selection
        # crossover and mutation
        pass
    
if __name__ == '__main__':
	main()

