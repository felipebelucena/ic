#!/usr/bin/python

# User-defined objective and fitness functions.

# objective func == f(x) = x^2 - 3x + 4
# fitness function (minimization problem) == fa(x) = -f(x))
def objective_func(x):
        return (x ** 2) - (3 * x) + 4

def fitness(x):
        return -objective_func(x)

