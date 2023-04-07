numero = input('Digite um número inteiro: ')
try:
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print(f'{numero_int} é par')
    else:
        print(f'{numero_int} é ímpar')
except ValueError:
    print(f'"{numero}" não é um número inteiro')
