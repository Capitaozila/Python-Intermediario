pessoa = {
    'nome': 'Luis Eduardo',
    'sobrenome' : 'Miranda',
    'idade' : 18,
    'altura' : 1.67,
    'peso' : 50,
    'endereços' : [
        {'rua': 'rua das flores', 'número': 123 },
        {'rua': 'rua dos boi', 'número': 321 },
    ]
}

print(pessoa['nome'])
print(pessoa['sobrenome'])
print(pessoa['altura'])
print(pessoa['peso'])
print()

for chave in pessoa:
    print(chave,':', pessoa[chave])