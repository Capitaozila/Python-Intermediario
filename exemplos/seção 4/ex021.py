letras = set()

while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('parabens voce digitou a letra secreta')
        break

    print(letras)
