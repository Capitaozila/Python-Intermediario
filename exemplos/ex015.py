lista = ['Maria', 'Luis', 'Rayana', 'Caio', 'João', 'Pedro',
         'Paulo', 'José', 'Ana', 'Luisa', 'Manoel', 'Joana']

lista.append('Pedro')

lista.append('Paulo')

# index = 0

# for nome in lista:
#     print(nome, index)
#     index += 1

# for x in range(0, 3):
#     print('-----------------')

# while index < tamanho_lista:
#     print(lista[index], index)
#     print('rabo')
#     index += 1

for indice, nome in enumerate(lista):
    print(f'{nome} [{indice}]')

# antigamente era assim

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)