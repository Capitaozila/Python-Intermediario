import random

# Parâmetros
target = "FORTE"
population_size = 100
mutation_rate = 0.01
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,!"

# Inicialização
population = [''.join(random.choices(characters, k=len(target))) for _ in range(population_size)]

# Função de fitness
def fitness(individual):
    return sum(ind_char == tar_char for ind_char, tar_char in zip(individual, target))

# Seleção
def selection(population):
    fitnesses = [fitness(individual) for individual in population]
    parent1 = random.choices(population, weights=fitnesses)[0]
    parent2 = random.choices(population, weights=fitnesses)[0]
    return parent1, parent2

# Crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(target))
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

# Mutação
def mutate(individual):
    return ''.join(char if random.random() > mutation_rate else random.choice(characters) for char in individual)

# Algoritmo genético
for generation in range(100):
    new_population = []
    for _ in range(population_size):
        parent1, parent2 = selection(population)
        child = crossover(parent1, parent2)
        child = mutate(child)
        new_population.append(child)
    population = new_population
    # Imprime o melhor indivíduo de cada geração
    print(max(population, key=fitness))

# Imprime o melhor indivíduo final
print("Final:", max(population, key=fitness))