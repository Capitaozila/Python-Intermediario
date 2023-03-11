string_digitada = input(str("Digite uma frase: "))
newstring = ''
count1 = 0
count2 = 0
count3 = 0

for a in string_digitada:
    if a.isupper():
        count1 += 1
        newstring += (a.lower())
    elif a.islower():
        count2 += 1
        newstring += (a.upper())
    elif a.isspace():
        count3 += 1
        newstring += a
tamanho = ((len(string_digitada))-count3)
print(f'Na sua frase original: "{string_digitada}"')
print("Palavras em maiscula:", count1)
print("Palavras em minusculo:", count2)
print("Número de espaços em branco:", count3)

print(f"O seu tamanho é de: {tamanho}")

print("Sua frase apos a troca:")
print(newstring)
