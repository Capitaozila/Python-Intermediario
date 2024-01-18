def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


v = executa(saudacao, 'Bom dia', 'Luis')

for i in {'Luis', 'Maria', 'João', 'Ana', 'Leonardor', 'Pedro', 'Paulo', 'Joana'}:
    print(executa(saudacao, 'Bom dia', i))
