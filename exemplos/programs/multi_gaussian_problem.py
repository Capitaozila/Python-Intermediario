
import numpy as np
import random

# Função gaussiana


def gaussian(x, amp, cen, wid):
    return amp * np.exp(-(x-cen)**2 / wid)

# Função de fitness


def fitness(individual, x, data):
    amp1, cen1, wid1, amp2, cen2, wid2 = individual
    model = gaussian(x, amp1, cen1, wid1) + gaussian(x, amp2, cen2, wid2)
    return np.sum((data - model)**2)

# Operações genéticas


def mutate(individual):
    index = random.randint(0, len(individual) - 1)
    individual[index] += random.uniform(-0.1, 0.1)
    return individual


def crossover(individual1, individual2):
    index = random.randint(1, len(individual1) - 2)
    return individual1[:index] + individual2[index:]

# Algoritmo genético


def genetic_algorithm(x, data, population_size, generations):
    # Inicializar população
    population = [np.random.uniform(0, 2, 6) for _ in range(population_size)]

    for _ in range(generations):
        # Avaliar fitness
        scores = [fitness(ind, x, data) for ind in population]

        # Selecionar pais
        parents = [population[i] for i in np.argsort(scores)[:2]]

        # Crossover e mutação
        population = [mutate(crossover(parents[0], parents[1]))
                      for _ in range(population_size)]

    # Retornar o melhor indivíduo
    return min(population, key=lambda ind: fitness(ind, x, data))
