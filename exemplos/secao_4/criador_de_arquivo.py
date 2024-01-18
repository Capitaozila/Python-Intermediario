caminho_arquivo = 'C:\\Users\\Fabin\\Documents\\Python-Intermediary\\exemplos\\arquivos'
caminho_arquivo += '\\aula116.txt'

# arquivo = open(caminho_arquivo, 'w')

# arquivo.close()

with open (caminho_arquivo, 'w+') as arquivo:
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\n')
    arquivo.writelines(('linha 3\n', 'linha 4\n'))
    arquivo.seek(0, 0)
    print(arquivo.read())

print('##' * 10)

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())