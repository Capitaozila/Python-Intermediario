from collections import Counter
import itertools
import csv
import sys

# Parâmetros de suporte e confiança
sup = 0.50
conf = 0.80

# Função para ler transações de um arquivo CSV
def ler_transacoes_de_csv(nome_arquivo):
    transacoes = {}
    with open(nome_arquivo, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for idx, row in enumerate(reader):
            transacoes[idx+1] = set(row)
    return transacoes

# Função para criar regras de associação
def frequentItems(items, trans, n, s):
    itemsets = set(itertools.combinations(items, n))
    itemTransactions = []
    for i in itemsets:
        for k, v in transacoes.items():
            if set(v).intersection(set(i)) == set(i):
                itemTransactions.append(i)
    ret = []
    for k, v in sorted(Counter(itemTransactions).items()):
        if v >= s * len(trans):
            ret.append([k, v])
    return dict(ret)

# Lê transações do arquivo CSV
transacoes = ler_transacoes_de_csv('./compras.csv')

# Extrai os items únicos
items = set()
for itemset in transacoes.values():
    for item in itemset:
        items.add(item)

# Mostra os resultados
print("1-itemsets mais frequentes:")
print(frequentItems(items, transacoes, 1, sup))
print()
print("2-itemsets mais frequentes:")
print(frequentItems(items, transacoes, 2, sup))
print()
print("3-itemsets mais frequentes:")
print(frequentItems(items, transacoes, 3, sup))
print()
print("4-itemsets mais frequentes:")
print(frequentItems(items, transacoes, 4, sup))
print()
print("5-itemsets mais frequentes:")
print(frequentItems(items, transacoes, 5, sup))
print()

# Imprime as regras de associação
# De acordo com o suporte e confiança
print("Regras de associacao com suporte")
print("e confianca maiores que 50%")
f2 = frequentItems(items, transacoes, 2, sup)
k2 = [k for k in f2.keys()]
v2 = [v for v in f2.values()]
f1 = frequentItems(items, transacoes, 1, sup)
k1 = [k[0] for k in f1.keys()]
v1 = [v for v in f1.values()]
for i in range(len(k2)):
    i1 = k2[i][0]
    i2 = k2[i][1]
    for j in range(len(k1)):
        if k1[j] == i1:
            confidence = v2[i] / v1[j]
    if v2[i] >= sup * len(transacoes) and confidence >= conf:
        print("{0:<6} -> {1:<6}: ({2},{3})".format(i1, i2, str(v2[i]), confidence))
    i1 = k2[i][1]
    i2 = k2[i][0]
    for j in range(len(k1)):
        if k1[j] == i1:
            confidence = v2[i] / v1[j]
    if v2[i] >= sup * len(transacoes) and confidence >= conf:
        print("{0:<6} -> {1:<6}: ({2},{3})".format(i1, i2, str(v2[i]), confidence))
        print()

# from prefixspan import PrefixSpan

# # Definindo as transações
# transactions = [
#     ["A", "B"],
#     ["A", "C"],
#     ["A"],
#     ["B", "C"],
#     ["E"],
#     ["D"],
#     ["E"],
#     ["C", "E"],
#     ["E", "F"],
#     ["A", "B"],
#     ["A", "B", "C"],
#     ["D"],
#     ["D"]
# ]

# # Executando o algoritmo PrefixSpan
# ps = PrefixSpan(transactions)

# # Encontrando os padrões sequenciais com suporte mínimo de 0.5
# patterns = ps.frequent(0.5)

# # Exibindo os padrões encontrados
# for pattern in patterns:
#     print("Padrão:", pattern[1], "Suporte:", pattern[0])
