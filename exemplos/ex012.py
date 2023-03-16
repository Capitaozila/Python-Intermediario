while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador: ')

    # numero_1 = '1.0'
    # numero_2 = '2'
    # operador = '+'

    numeros_validos = None

    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)

        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Pelo menos um dos números digitados é inválido')
        continue

    operadores_permitidos = '+-/*'
    operador_valido = operador not in operadores_permitidos or len(
        operador) > 1

    if operador_valido:
        print(
            'Digite um operador válido: +(soma), -(subtração), /(divisão), *(multiplicação)')
        continue

    if operador == '+':
        print(num_1_float + num_2_float)

    elif operador == '-':
        print(num_1_float - num_2_float)

    elif operador == '/':
        print(num_1_float / num_2_float)

    elif operador == '*':
        print(num_1_float * num_2_float)

    else:
        print('Não deveria chegar até aqui')

    # # # # # # # #

    sair = input('Deseja sair? ').lower().startswith('sim')

    if sair:
        break
