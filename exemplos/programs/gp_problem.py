import numpy as np
import pandas as pd

# Função Goldstein-Price
def goldstein_price(x):
    return (1 + (x[0] + x[1] + 1)**2 * (19 - 14*x[0] + 3*x[0]**2 - 14*x[1] + 6*x[0]*x[1] + 3*x[1]**2)) * (30 + (2*x[0] - 3*x[1])**2 * (18 - 32*x[0] + 12*x[0]**2 + 48*x[1] - 36*x[0]*x[1] + 27*x[1]**2))

# Inicialização da população
def init_population(pop_size, dimensions, bounds):
    population = []
    for i in range(pop_size):
        individual = []
        for j in range(dimensions):
            individual.append(np.random.uniform(bounds[j][0], bounds[j][1]))
        population.append(individual)
    return np.array(population)

# Função de fitness
def fitness(population):
    return np.array([1 / (1 + goldstein_price(individual)) for individual in population])

# Seleção de roleta
def roulette_selection(population, fitness):
    total_fitness = np.sum(fitness)
    probs = fitness / total_fitness
    return population[np.random.choice(len(population), p=probs)]

# Crossover de um ponto
def one_point_crossover(parent1, parent2):
    point = np.random.randint(len(parent1))
    child1 = np.concatenate((parent1[:point], parent2[point:]))
    child2 = np.concatenate((parent2[:point], parent1[point:]))
    return child1, child2

# Mutação
def bit_flip_mutation(individual, mutation_rate):
    for i in range(len(individual)):
        if np.random.rand() < mutation_rate:
            individual[i] = np.random.uniform(bounds[i][0], bounds[i][1])
    return individual

# Algoritmo Genético
def genetic_algorithm(pop_size, dimensions, bounds, generations, crossover_rate, mutation_rate):
    # Inicializar população
    population = init_population(pop_size, dimensions, bounds)
    data = []
    for generation in range(generations):
        new_population = []
        for i in range(int(pop_size/2)):
            # Seleção
            parent1 = roulette_selection(population, fitness(population))
            parent2 = roulette_selection(population, fitness(population))
            # Crossover
            if np.random.rand() < crossover_rate:
                child1, child2 = one_point_crossover(parent1, parent2)
            else:
                child1, child2 = parent1, parent2
            # Mutação
            child1 = bit_flip_mutation(child1, mutation_rate)
            child2 = bit_flip_mutation(child2, mutation_rate)
            new_population.append(child1)
            new_population.append(child2)
        population = np.array(new_population)
        # Armazenar dados para impressão
        data.append([generation, np.max(fitness(population)), np.mean(fitness(population)), np.min(fitness(population))])
    # Imprimir tabela
    df = pd.DataFrame(data, columns=['Geração', 'Fitness Máximo', 'Fitness Médio', 'Fitness Mínimo'])
    print(df)

# Parâmetros
pop_size = 200
dimensions = 2
bounds = [(-1, 1), (-1, 1)]
generations = 100
crossover_rate = 0.8
mutation_rate = 0.02

# Executar AG
genetic_algorithm(pop_size, dimensions, bounds, generations, crossover_rate, mutation_rate)
