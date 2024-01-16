grupos = groupby(alunos)

for chave, grupo in grupos:
    print(chave)
    print(list(grupo))