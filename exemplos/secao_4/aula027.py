from itertools import groupby


alunos = [
    # nome, nome da pessoa, nota, nota da pessoa (A, B, C, D, E, F)
    {'nome': 'Luis', 'nota': 'A'},
    {'nome': 'João', 'nota': 'B'},
    {'nome': 'Maria', 'nota': 'C'},
    {'nome': 'Pedro', 'nota': 'D'},
    {'nome': 'Thaissa', 'nota': 'E'},
    {'nome': 'Helena', 'nota': 'F'},
    {'nome': 'Karla', 'nota': 'C'},
]

def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)


for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)