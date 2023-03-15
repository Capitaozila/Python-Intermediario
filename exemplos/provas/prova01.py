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
Faça um programa que pergunte a horario ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# entrada = input('Em números inteiros: que horas tem? ')

# entrada = '25'

# try:
#     horario = int(entrada)

#     madrugada = horario >= 0 and horario <= 6 or horario == 24
#     dia = horario >= 7 and horario <= 12
#     tarde = horario >= 13 and horario <= 17
#     noite = horario >= 18 and horario <= 23

#     if madrugada:
#         print('Boa madrugada!')

#     elif dia:
#         print('Bom dia!')

#     elif tarde:
#         print('Boa tarde!')

#     elif noite:
#         print('Boa noite!')

#     else:
#         print('Não reconheço esse hórario')

# except:
#     print(f'"{entrada}" não é um número inteiro válido')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# primeiro_nome = input("Digite seu primeiro nome: ")

# nome = str(primeiro_nome)
# tamanho_nome = len(nome)

# nome_curto = tamanho_nome > 1 and tamanho_nome <= 4
# nome_normal = tamanho_nome >= 5 and tamanho_nome <= 6
# nome_grande = tamanho_nome >= 7

# if nome_curto:
#     print("Seu nome é curto")

# elif nome_normal:
#     print('Seu nome é normal')

# elif nome_grande:
#     print('Seu nome é muito grande')

# else:
#     print('Digite um nome válido')


# ate a aula 196 modulo 4
