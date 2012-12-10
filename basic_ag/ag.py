#!/usr/bin/python

from random import random, randint

# number of bits of individual representation
INDIVIDUAL_LENGTH = 22

# inferior and superior limits of individual value
LOW_BOUND = -10
HIGH_BOUND = 10

# mutation and crossover rate in %
MUTATION_RATE = 1
CROSSOVER_RATE = 60

# population size
POP_SIZE = 4

def generate_individual():
	return ''.join(str(randint(0,1)) for i  in range(INDIVIDUAL_LENGTH))

def individual_value(individual):
	return LOW_BOUND + (((HIGH_BOUND - LOW_BOUND) * int(individual, 2)) / ((2 ** INDIVIDUAL_LENGTH) - 1.0))
	
# objective func == f(x) = x^2 - 3x + 4
# fitness function (minimization problem) == fa(x) = -f(x))
def objective_func(individual):
	x = individual_value(individual)
	return (x ** 2) - (3 * x) + 4

def fitness(individual):
	return -objective_func(individual)


def random_percent():
	return random() * 100

def crossover():
	pass

def mutation(individual):
	out = ''
	for cromossomo in individual:
		p = random_percent()
		if p < 1.0:
			if cromossomo == '0': out += '<1>'
			else: out += '<0>'
		else: out += cromossomo
	print out
	


if '__name__' == '__main__':
	main()


