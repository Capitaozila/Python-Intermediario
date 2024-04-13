import pandas as pd
import random
import os

# Ler o arquivo CSV
df = pd.read_csv('./exemplos/programs/personagens.csv')

# Definir pesos para as características
pesos = {'Arma': {'Lâmina': 10, 'Outra': 5},
         'Sofre Transformação': {'Sim': 10, 'Não': 5},
         'Idade': {'Adulto': 10, 'Outra': 5},
         'Classe': {'Herói': 10, 'Outra': 5}}

# Calcular a força de um personagem
def calcular_forca(personagem):
    forca = 0
    for caracteristica, valor in personagem.items():
        if caracteristica in pesos:
            forca += pesos[caracteristica].get(valor, 0)
    return forca

# Realizar uma batalha entre dois personagens
def batalha(personagem1, personagem2, registro_batalhas):
    # Verificar se os personagens já lutaram duas vezes
    if registro_batalhas.get((personagem1['Personagem'], personagem2['Personagem']), 0) >= 2:
        return None, None, None

    forca1 = calcular_forca(personagem1)
    forca2 = calcular_forca(personagem2)
    if forca1 > forca2:
        vencedor = personagem1
        perdedor = personagem2
    else:
        vencedor = personagem2
        perdedor = personagem1

    # Encontrar a característica que fez a diferença
    diferenca = [caracteristica for caracteristica in pesos if personagem1[caracteristica] != personagem2[caracteristica]]
    
    # Atualizar o registro de batalhas
    registro_batalhas[(personagem1['Personagem'], personagem2['Personagem'])] = registro_batalhas.get((personagem1['Personagem'], personagem2['Personagem']), 0) + 1

    return vencedor, perdedor, diferenca

# Realizar várias batalhas
def varias_batalhas(df):
    registro_batalhas = {}
    while len(df) > 1:
        personagem1 = df.iloc[random.randint(0, len(df)-1)]
        personagem2 = df.iloc[random.randint(0, len(df)-1)]
        if personagem1['Personagem'] == personagem2['Personagem']:
            continue
        vencedor, perdedor, diferenca = batalha(personagem1, personagem2, registro_batalhas)
        if vencedor is None:
            continue
        if perdedor is not None:  # Check if perdedor is not None
            df = df[df['Personagem'] != perdedor['Personagem']]
        if vencedor is not None and perdedor is not None and diferenca is not None:
            print(f"{vencedor['Personagem']} venceu a batalha contra {perdedor['Personagem']} devido à diferença em {diferenca}")
    return df.iloc[0]

# Realizar a evolução genética
def evolucao_genetica(df, geracoes):
    for i in range(geracoes):
        os.system('cls')  # Limpar a saída do console
        print(f"Geração {i+1}")
        vencedor = varias_batalhas(df)
        print(f"O vencedor da geração {i+1} é {vencedor['Personagem']}")
        # Aqui você pode adicionar o código para a reprodução (crossover) e mutação

        # Perguntar ao usuário se ele deseja continuar para a próxima geração
        continuar = input("Quer continuar para a próxima geração? (sim ou não): ")
        if continuar.lower() != "sim":
            break

    return vencedor

# Executar o algoritmo genético
vencedor_final = evolucao_genetica(df, 10)
print(f"O vencedor final é {vencedor_final['Personagem']}")