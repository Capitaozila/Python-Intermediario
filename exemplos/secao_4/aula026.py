from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print('------------------------')
    print()

pessoas = ['João', 'Joana', 'Luiz', 'Leticia']

camisetas = [
    ['preta', 'branca'],
    ['p','m'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'polister']
]

# print(*list(combinations(pessoas, 2)), sep='\n')
print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))
# print_iter(combinations(pessoas, 2))