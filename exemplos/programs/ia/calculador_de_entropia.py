import math

# def info_time(data):
#     total = sum(data)
#     entropy = sum([- (x / total) * math.log2(x / total) if x > 0 else 0 for x in data])
#     return entropy

# # Cálculo da entropia para cada valor do atributo 'Time'
# entropy_um = (13/16) * info_time([9,4])
# entropy_dois = (3/16) * info_time([2,1])

# # Soma das entropias
# total_entropy = entropy_um + entropy_dois

# print(f"Entropia total para o atributo 'Time': {round(total_entropy, 4)}")


# def info_time(data):
#     total = sum(data)
#     entropy = sum([- (x / total) * math.log2(x / total)
#                   if x > 0 else 0 for x in data])
#     return entropy


# Cálculo da entropia para o conjunto de dados [v,f]
# entropy = info_time([6, 1])

resultado = - (2/16) * math.log2(2/16) - (1/16) * math.log2(1/16)
teste1 = (2/16)*math.log2(2/16)
teste2 = (1/16)*math.log2(1/16)
resultado2 = -teste1 - teste2

ai_papai_total = - (11/16) * math.log2(11/16) - (5/16) * math.log2(5/16)

if resultado2 == resultado:
    print("Resultado correto")
else:
    print("Resultado incorreto")

# print(f"Entropia para o conjunto de dados [v,f]: {entropy}")

print(f"Testes deram {teste1} e {teste2}")

print(f"Resultado esperado: {resultado}")

print(f"ai_papai: {ai_papai_total}")
