"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero = input('Digite um número inteiro: ')
# try:
#     numero_int = int(numero)
#     if numero_int % 2 == 0:
#         print(f'{numero} é par')
#     else:
#         print(f'{numero} é impar')
# except:
#     print(f'"{numero}" não é um numero inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = input('Que horas são? ')
horario = str(horario)
print(f'Bom dia! Ja são {horario} horas')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# ate a aula 196 modulo 4