"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto

texto_1 = 'Luiz'  # iterável

iteratador = iter(texto_1)  # iterator

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break


texto_2 = 'Luiz'

novo_texto_2 = ''

for letra in texto_2:
    novo_texto_2 += letra

print(novo_texto_2)
