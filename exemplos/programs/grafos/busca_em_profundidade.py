def dfs(grafo, raiz):
    # Cria um conjunto para armazenar os vértices visitados
    visitado = {raiz}
    
    # Cria uma pilha e adiciona o vértice raiz
    pilha = [raiz]

    while pilha:
        # Remove o próximo vértice da pilha
        vertice = pilha.pop()
        
        # Imprime o vértice atual
        print(f"Visitando o vértice: {vertice}")

        # Percorre todos os vizinhos do vértice atual
        for vizinho in grafo[vertice]:
            # Se o vizinho ainda não foi visitado...
            if vizinho not in visitado:
                # Marca o vizinho como visitado
                visitado.add(vizinho)
                
                # Adiciona o vizinho à pilha
                pilha.append(vizinho)
                print(f"Adicionando {vizinho} à pilha")

# Exemplo de uso:
grafo = {
    '1': ['2', '4'],
    '2': ['3', '1'],
    '3': ['2', '6'],
    '4': ['5', '1'],
    '5': ['4'],
    '6': ['3']
}

print("Iniciando a busca em profundidade a partir do vértice 1")
dfs(grafo, '1')  # Saída: Visitando o vértice: 1, Adicionando 4 à pilha, Adicionando 2 à pilha, ...
