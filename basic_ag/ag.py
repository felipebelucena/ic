#!/usr/bin/python

from random import random, randint
from itertools import izip_longest
from individual import *
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

# best individual
best_ind = None


def get_args():
    global INDIVIDUAL_LENGTH
    global POP_SIZE
    global MUTATION_RATE
    global CROSSOVER_RATE
    global GENERATION_NUMBER

    if len(sys.argv) < 6:
        show_help()
        sys.exit(1)

    INDIVIDUAL_LENGTH = int(sys.argv[1])
    POP_SIZE = int(sys.argv[2])
    MUTATION_RATE = int(sys.argv[3])
    CROSSOVER_RATE = int(sys.argv[4])
    GENERATION_NUMBER = int(sys.argv[5])
    
def show_help():
    print "Passe os seguintes argumentos para executar o algoritmo genetico:\n"
    print "python ag.py <TAM_IND> <TAM_POP> <TAX_MUT> <TAX_CROSS> <N_GEN>\n"
    print "Em que:\n"
    print "<TAM_IND>   - Tamanho do individuo"
    print "<TAM_POP>   - Tamanho da populacao"
    print "<TAX_MUT>   - Taxa de mutacao"
    print "<TAX_CROSS> - Taxa de crossover"
    print "<N_GEN>     - Numero de geracoes"

  
def avaliation(pop):
    print "Avaliacao da populacao...\n"
    global best_ind
    cont = 0
    for i in pop:
        cont += 1
        print cont,
        print i
        if best_ind == None:
            best_ind = i
        else:
            if i.fitness() > best_ind.fitness():
                best_ind = i

def selection(pop):
    print "Selecao..."
    tmp_pop = []
    sel = [(randint(0, POP_SIZE-1), randint(0, POP_SIZE-1)) for i in range(POP_SIZE)]

    print "Selecao por torneio:"
    for index1, index2 in sel:
        print "Individuo ", index1+1, " e Individuo ", index2+1,
        print " Selecionado >> Individuo ",
        
        if pop[index1].fitness() >= pop[index2].fitness():
            print index1+1
            tmp_pop.append(pop[index1])
        else:
            print index2+1
            tmp_pop.append(pop[index2])
    return tmp_pop

def grouper(n, iterable, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

def crossover(pop):
    for i,j in grouper(2, pop):
        Individual.crossover(i,j,CROSSOVER_RATE)

def mutation(pop):
    for i in pop: i.mutation()
    
def main():
    populations = []
    get_args()
    cur_pop = Individual.generate_pop(POP_SIZE, INDIVIDUAL_LENGTH, LOW_BOUND,
    HIGH_BOUND, MUTATION_RATE)

    for i in range(GENERATION_NUMBER):
        print "\n########### Geracao ", i+1, "###############\n"
        populations.append(cur_pop)
        avaliation(cur_pop)
        cur_pop = selection(cur_pop)
        crossover(cur_pop)
        mutation(cur_pop)
        print "\nAvaliacao da populacao apos operadores geneticos..."
        avaliation(cur_pop)

    print "Melhor Invididuo apos {0} geracoes: {1}".format(GENERATION_NUMBER, best_ind)
    
if __name__ == '__main__':
	main()

