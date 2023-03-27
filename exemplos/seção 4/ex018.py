def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


multiplicacao = multiplica(1, 2, 3, 4, 5)

print('A multiplicação de todos os números é: ', multiplicacao)

print('-----------------')
print('-----------------')


def parImpar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é impar'


print(parImpar(1))
print(parImpar(2))
print(parImpar(16))
print(parImpar(0))
print(parImpar(-20))
