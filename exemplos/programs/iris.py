import pandas as pd
import requests
import matplotlib.pyplot as plt

# URL do conjunto de dados Iris
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Colunas do conjunto de dados
colunas = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# Carregar o conjunto de dados
iris_data = pd.read_csv(url, names=colunas)

# Exibindo as primeiras linhas do conjunto de dados
print("Primeiras linhas do conjunto de dados Iris:")
print(iris_data.head())

# Resumo estatístico do conjunto de dados
print("\nResumo estatístico do conjunto de dados Iris:")
print(iris_data.describe())

# Contagem de amostras por espécie
print("\nContagem de amostras por espécie:")
print(iris_data['species'].value_counts())

# Visualização de dispersão por espécie
plt.figure(figsize=(10, 6))
for species in iris_data['species'].unique():
    subset = iris_data[iris_data['species'] == species]
    plt.scatter(subset['sepal_length'], subset['sepal_width'], label=species)
plt.xlabel('Comprimento da Sépala')
plt.ylabel('Largura da Sépala')
plt.title('Dispersão de Comprimento x Largura da Sépala por Espécie')
plt.legend()
plt.show()
