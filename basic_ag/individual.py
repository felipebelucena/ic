#!/usr/bin/python

from random import random, randint
import ag_aux

def random_percent():
    return random() * 100

class Individual(object):

    def __init__(self, individual_length, low_bound, high_bound, mutation_rate):
        self.individual_length = individual_length
        self.low_bound = low_bound
        self.high_bound = high_bound
        self.mutation_rate = mutation_rate
        self.chromosome = Individual.generate_individual(individual_length)

    def __str__(self):
        return "Chromosome: {0}\tValue: {1}\tFitness: {2}".format(self.chromosome,  self.individual_value(), self.fitness())

    @staticmethod
    def generate_individual(individual_length):
        return ''.join(str(randint(0,1)) for i  in range(individual_length))
    
    @staticmethod
    def generate_pop(pop_size, il, lb, hb, mr):
        return [Individual(il, lb, hb, mr) for i in range(pop_size)]

    def individual_value(self):
        return self.low_bound + (((self.high_bound - self.low_bound) * int(self.chromosome, 2)) /
        ((2 ** self.individual_length) - 1.0))

    def fitness(self):
        return ag_aux.fitness(self.individual_value())

    @staticmethod
    def crossover(ind1, ind2, crossover_rate):
        if ind1.individual_length != ind2.individual_length:
            raise Exception("Crossover error: individuals have not equal chromosome length")

        if random_percent() < crossover_rate:
            cut_point = randint(0,ind1.individual_length)
            ind1_tmp = ind1.chromosome
            ind2_tmp = ind2.chromosome
            ind1.chromosome = ind1_tmp[0:cut_point] + ind2_tmp[cut_point:]
            ind2.chromosome = ind2_tmp[0:cut_point] + ind1_tmp[cut_point:]          
            
    def mutation(self):
        for i in range(len(self.chromosome)):       
            if random_percent() < self.mutation_rate:
                _list = list(self.chromosome)
                if _list[i] == '0':
                    _list[i] = '1'
                else:
                    _list[i] = '0'
                self.chromosome = "".join(_list)


def main():
    pass

if __name__ == '__main__':
    main()
