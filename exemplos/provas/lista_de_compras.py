import os

# lista_de_compras = ['Feijão', 'Arroz', 'Ovo']

# tentativa
# while True:
#     print('Selecione uma opção')
#     opcao = input('[i]nserir [a]pagar [l]istar: ').lower()
#     print(opcao)

#     try:
#       valores_validos = 'ial'
#       if valores_validos in opcao:
#         print('deu certo')
#       else:
#         print('Digite uma opção válida')

#       # os.system('cls' if os.name == 'nt' else 'clear')

#     except:
#       print('deu errado')


lista = ['Feijão', 'Arroz', 'Ovo']

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls' if os.name == 'nt' else 'clear')
        valor = input('O que deseja adicionar na lista? ')
        lista.append(valor)
    elif opcao == 'a':

        indice_str = input('Escolha o index do item para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor, digite um número inteiro')
        except IndexError:
            print('Esse index de item não existe na lista')

    elif opcao == 'l':
        os.system('cls' if os.name == 'nt' else 'clear')

        if len(lista) == 0:

            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)

    else:
        os.system('cls' if os.name == 'nt' else 'clear')

        print('Digite uma opção correta')
        print('(i) de Inserir, (a) de apagar e (l) de listar')
