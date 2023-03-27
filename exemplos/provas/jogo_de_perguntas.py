perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': 'c',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': 'a',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': 'b',
    },

    {
        'Pergunta': 'Quem descobriu o Brasil?',
        'Opções': ['Pedro Álvares Cabral', 'Cristóvão Colombo', 'Américo Vespúcio', 'Navegantes'],
        'Resposta': 'a',
    },

    {
        'Pergunta': 'Me diga um animal que voa?',
        'Opções': ['Gato', 'Mamute', 'Cachorro', 'Papagaio'],
        'Resposta': 'd',
    },
    {
        'Pergunta': 'Me diga um animal que não voa?',
        'Opções': ['Papagaio', 'bem-te-vi', 'pardal', 'pinguim'],
        'Resposta': 'd',

    }
]

quantidade_de_acertos = 0

letras = ['a', 'b', 'c', 'd']

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    print()
    for i in range(len(pergunta['Opções'])):
        print(f'{letras[i]}) {pergunta["Opções"][i]}')
    print()
    resposta = input('A letra correta é: ')
    if resposta == pergunta['Resposta']:
        print('Resposta correta!')
        quantidade_de_acertos += 1
    else:
        print('Resposta incorreta!')
    print()

print(
    f'Você acertou {quantidade_de_acertos} perguntas de um total de {len(perguntas)} perguntas.')
