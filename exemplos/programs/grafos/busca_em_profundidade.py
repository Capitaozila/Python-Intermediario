def dfs(grafo, raiz):
    visitado = set()  # Cria um conjunto vazio para armazenar os vértices visitados
    pilha = [raiz]  # Cria uma pilha e adiciona o vértice raiz

    while pilha:
        vertice = pilha.pop()  # Remove o último vértice da pilha
        if vertice not in visitado:
            visitado.add(vertice)  # Marca o vértice como visitado
            print(f"Visitando o vértice: {vertice}")

            for vizinho in reversed(grafo[vertice]):
                if vizinho not in visitado:
                    pilha.append(vizinho)  # Adiciona o vizinho à pilha
                    print(f"Adicionando {vizinho} à pilha")

# Exemplo de uso:
grafo = {
    '1': ['2', '4'],
    '2': ['3', '1'],
    '3': ['2', '4','6'],
    '4': ['5', '1'],
    '5': ['4'],
    '6': ['3']
}

print("Iniciando a busca em profundidade a partir do vértice 1")
dfs(grafo, '1')  # Saída: Visitando o vértice: 1, Adicionando 4 à pilha, Adicionando 2 à pilha, ...
