primeiro_valor = input("Digite o primeiro valor: ")
segundo_valor = input("Digite o segundo valor: ")

primeiro_valor_int = int(primeiro_valor)
segundo_valor_int = int(segundo_valor)

if (primeiro_valor_int > segundo_valor_int):
    print(
        f'O primeiro valor: "{primeiro_valor_int}" é maior que "{segundo_valor_int}"')
elif (segundo_valor_int > primeiro_valor_int):
    print(
        f'O segundo valor "{segundo_valor_int}" é maior que "{primeiro_valor_int}"')
else:
    print(
        f'Os dois valores "{primeiro_valor_int}" e "{segundo_valor_int}" são iguais')
