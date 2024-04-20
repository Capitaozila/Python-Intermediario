import numpy as np

# Função de Goldstein-Price
def goldstein_price(x):
    return (1 + (x[0] + x[1] + 1)**2 * (19 - 14*x[0] + 3*x[0]**2 - 14*x[1] + 6*x[0]*x[1] + 3*x[1]**2)) * (30 + (2*x[0] - 3*x[1])**2 * (18 - 32*x[0] + 12*x[0]**2 + 48*x[1] - 36*x[0]*x[1] + 27*x[1]**2))

# Inicialização da população
def initialize_population(pop_size, dimensions, bounds):
    population = []
    for _ in range(pop_size):
        individual = [np.random.uniform(bounds[i][0], bounds[i][1]) for i in range(dimensions)]
        population.append(individual)
    return population

# Seleção de roleta
def roulette_selection(population, fitnesses):
    total_fitness = np.sum(fitnesses)
    r = np.random.uniform(0, total_fitness)
    accumulated_fitness = 0
    for i in range(len(population)):
        accumulated_fitness += fitnesses[i]
        if accumulated_fitness >= r:
            return population[i]

# Crossover de um ponto
def one_point_crossover(parent1, parent2):
    crossover_point = np.random.randint(1, len(parent1))
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutação de um ponto
def one_point_mutation(individual, bounds, mutation_rate):
    for i in range(len(individual)):
        if np.random.rand() < mutation_rate:
            individual[i] = np.random.uniform(bounds[i][0], bounds[i][1])
    return individual

# Algoritmo genético
def genetic_algorithm(pop_size, dimensions, bounds, generations, crossover_rate, mutation_rate):
    # Inicializar população
    population = initialize_population(pop_size, dimensions, bounds)
    
    for _ in range(generations):
        # Avaliar fitness
        fitnesses = [1 / goldstein_price(individual) for individual in population]
        
        new_population = []
        for _ in range(pop_size // 2):
            # Seleção
            parent1 = roulette_selection(population, fitnesses)
            parent2 = roulette_selection(population, fitnesses)
            
            # Crossover
            if np.random.rand() < crossover_rate:
                child1, child2 = one_point_crossover(parent1, parent2)
            else:
                child1, child2 = parent1, parent2
            
            # Mutação
            child1 = one_point_mutation(child1, bounds, mutation_rate)
            child2 = one_point_mutation(child2, bounds, mutation_rate)
            
            new_population.extend([child1, child2])
        
        population = new_population
    
    # Retornar o melhor indivíduo da última geração
    fitnesses = [1 / goldstein_price(individual) for individual in population]
    best_individual = population[np.argmax(fitnesses)]
    return best_individual

# Parâmetros
pop_size = 200
dimensions = 2
bounds = [(-2, 2), (-2, 2)]
generations = 100
crossover_rate = 0.8
mutation_rate = 0.02

# Executar o algoritmo genético
best_individual = genetic_algorithm(pop_size, dimensions, bounds, generations, crossover_rate, mutation_rate)
print("Melhor indivíduo:", best_individual)
