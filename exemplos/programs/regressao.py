from collections import Counter
import itertools
import sys

# Parâmetros de suporte e confiança
sup = 0.5
conf = 0.5

# Em seguida, criamos um dicionário de transações para servir como exemplo em nossa aplicação:


# Conjunto de transações
transacoes = {
    1: {"Cerveja", "Amendoim", "Laranja"},
    2: {"Cerveja", "Cafe", "Laranja", "Amendoim"},
    3: {"Cerveja", "Laranja", "Ovos"},
    4: {"Cerveja", "Amendoim", "Ovos", "Leite"},
    5: {"Cafe", "Laranja", "Ovos", "Leite"},
    6: {"Cafe", "Laranja", "Ovos", "Leite"},
    7: {"Laranja", "Cafe", "Cerveja", "Ovos"},
    8: {"Amendoim", "Cafe", "Cerveja", "Ovos"},
    9: {"Amendoim", "Laranja", "Cerveja", "Ovos"},
    10: {"Amendoim", "Cafe", "Cerveja", "Ovos"},
}

# Agora, "quebramos" cada transação item por item, lendo os valores dos pares "chave-valor" do dicionário de transações. Iteramos cada itemset presente em transacoes.values().

# Faz a leitura do dicionário de transações
# Armazena cada item no vetor items

items = []
for itemset in transacoes.values():
    for item in itemset:
        items.append(item)

items = set(items)


# No trecho de código a seguir temos algoritmo que cria as regras de associação. A função frequentItems receberá como parâmetros nosso vetor de items (items), o dicionário de transações (trans), a quantidade de items por conjunto (n) e o suporte (s). O módulo itertools é utilizado para realizar todas a n-combinações (n) dos items.

### Cria as regras de associação ##############################
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


###############################################################

# Na sequência, vamos imprimir os conjuntos de items (1 a 1, 2 a 2 e 3 a 3) mais frequentes das transações do exemplo.

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
