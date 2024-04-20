import numpy as np

# Dados fornecidos
data = np.array([
    [0.5, 0.0, 0.0, 0.1],
    [1.2, 1.0, 0.0, 0.5],
    [1.0, 0.0, -0.5, 0.5],
    [1.0, -0.5, 0.0, 0.5],
    [1.2, 0.0, 1.0, 0.5]
])

# Função de fitness
def fitness(x):
    return -np.sum([ai * np.exp(-((x[0] - bi)**2 + (x[1] - ci)**2) / di**2) for ai, bi, ci, di in data])

# Operação de crossover
def crossover(parent1, parent2):
    child = parent1.copy()
    mask = np.random.randint(0, 2, parent1.shape).astype(bool)
    child[mask] = parent2[mask]
    return child

# Operação de mutação
def mutate(x):
    mutation_mask = np.random.randint(0, 2, x.shape).astype(bool)
    x[mutation_mask] = np.random.uniform(-1, 1, mutation_mask.sum())
    return x

# Algoritmo genético
def genetic_algorithm(population_size, num_generations, num_genes):
    # Inicializando a população
    population = np.random.uniform(-1, 1, (population_size, num_genes))

    for generation in range(num_generations):
        # Avaliando a população
        fitness_values = np.apply_along_axis(fitness, 1, population)

        # Selecionando os pais para crossover
        parents = population[np.argsort(fitness_values)[-2:]]

        # Gerando a próxima geração
        for i in range(population_size):
            child = crossover(*parents)
            child = mutate(child)
            population[i, :] = child

    # Retornando o melhor indivíduo da última geração
    fitness_values = np.apply_along_axis(fitness, 1, population)
    best_individual = population[np.argmax(fitness_values)]
    return best_individual

# Executando o algoritmo genético
best_individual = genetic_algorithm(100, 200, 2)
print("Melhor indivíduo: ", best_individual)
