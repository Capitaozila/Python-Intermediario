import math
import pandas as pd

def calculate_entropy(f, n):
    total = f + n
    p_f = f / total if f > 0 else 0
    p_n = n / total if n > 0 else 0
    entropy = 0
    if p_f > 0:
        entropy -= p_f * math.log2(p_f)
    if p_n > 0:
        entropy -= p_n * math.log2(p_n)
    return round(entropy, 5)

def main():
    # Proporções
    p_F = round(11/16, 5)
    p_N = round(5/16, 5)

    # Cálculo da entropia
    info_D = round(-p_F * math.log2(p_F) - p_N * math.log2(p_N), 5)

    print(f"info(D) = {info_D}")

    # Contagem de 'F' (vitórias) e 'N' (derrotas) para cada valor de cada atributo
    attributes = {
        'Time': {
            'Morning': {'F': 2, 'N': 0},
            'Afternoon': {'F': 7, 'N': 4},
            'Night': {'F': 2, 'N': 1},
        },
        'Match type': {
            'Master': {'F': 3, 'N': 3},
            'Grand slam': {'F': 6, 'N': 1},
            'Friendly': {'F': 2, 'N': 1},
        },
        'Court surface': {
            'Grass': {'F': 4, 'N': 0},
            'Clay': {'F': 2, 'N': 3},
            'Hard': {'F': 5, 'N': 0},
            'Mixed': {'F': 0, 'N': 2},
        },
        'Best Effort': {
            '1': {'F': 9, 'N': 4},
            '0': {'F': 2, 'N': 1},
        },
    }

    # Cálculo da entropia para cada valor de cada atributo
    entropies = {}
    data = []
    for attribute, counts in attributes.items():
        total_instances = sum(sum(count.values()) for count in counts.values())
        total_entropy = 0
        print(f"\nEntropias para '{attribute}':")
        for value, count in counts.items():
            entropy = calculate_entropy(count['F'], count['N'])
            print(f"  {attribute}-{value}: {round(entropy, 5)}")
            proportion = round((count['F'] + count['N']) / total_instances, 5)
            total_entropy += proportion * entropy
            data.append([attribute, value, entropy, proportion])
        entropies[attribute] = round(total_entropy, 5)

    # Ordenar e imprimir as entropias
    print("\nEntropias totais:")
    for attribute, entropy in sorted(entropies.items(), key=lambda item: item[1], reverse=True):
        print(f"  {attribute}: {round(entropy, 5)}")

    # Cálculo da diferença entre a entropia total e a entropia específica
    print("\nDiferença entre a entropia total e a entropia específica:")
    for attribute, entropy in entropies.items():
        difference = round(info_D - entropy, 5)
        print(f"  {attribute}: {difference}")

    # Criar um DataFrame e salvar como CSV
    df = pd.DataFrame(data, columns=['Attribute', 'Value', 'Entropy', 'Proportion'])
    df = df.round(4)
    df.to_csv('banco_de_dados.csv', index=False)

if __name__ == "__main__":
    main()