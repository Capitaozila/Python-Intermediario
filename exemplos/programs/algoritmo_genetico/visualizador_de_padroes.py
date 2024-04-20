import pandas as pd

# Caminho para o arquivo CSV
caminho_arquivo = "./programs/meu_banco.csv"

# Carregar o conjunto de dados
meu_banco_data = pd.read_csv(caminho_arquivo)


# Resumo estatístico do conjunto de dados
print("\nResumo estatístico do conjunto de dados:")
print(meu_banco_data.describe())

# Contagem de amostras por coluna
for coluna in meu_banco_data.columns:
    print("\nContagem de amostras por", coluna + ":")
    print(meu_banco_data[coluna].value_counts())
