from functools import reduce 

produtos = [
    {'nome': 'Produto 5', 'preço': 10.0},
    {'nome': 'Produto 2', 'preço': 30.0},
    {'nome': 'Produto 4', 'preço': 20.0},
    {'nome': 'Produto 3', 'preço': 40.0},
    {'nome': 'Produto 1', 'preço': 69.90},
    
]

def funcao_do_reduce(acumulador, produto):
    print('acumulador', acumulador)
    print('produto', produto)
    print()
    return acumulador + produto['preço']

total = reduce(
    funcao_do_reduce,
    produtos,
    0
)

print('O total é: ', total)

# total = 0
# for p in produtos:
#     total += p['preço']
