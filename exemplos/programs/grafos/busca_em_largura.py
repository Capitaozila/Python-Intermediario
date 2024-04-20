from collections import deque

def bfs(grafo, raiz):
    # Cria um conjunto para armazenar os vértices visitados
    visitado = {raiz}
    
    # Cria uma fila e adiciona o vértice raiz
    fila = deque([raiz])

    while fila:
        # Remove o próximo vértice da fila
        vertice = fila.popleft()
        
        # Imprime o vértice atual
        print(f"Visitando o vértice: {vertice}")

        # Percorre todos os vizinhos do vértice atual
        for vizinho in grafo[vertice]:
            # Se o vizinho ainda não foi visitado...
            if vizinho not in visitado:
                # Marca o vizinho como visitado
                visitado.add(vizinho)
                
                # Adiciona o vizinho à fila
                fila.append(vizinho)
                print(f"Adicionando {vizinho} à fila")

# Exemplo de uso:
grafo = {
    '1': ['2', '4'],
    '2': ['3', '1'],
    '3': ['2', '6'],
    '4': ['5', '1'],
    '5': ['4'],
    '6': ['3']
}

print("Iniciando a busca em largura a partir do vértice 0")
bfs(grafo, '1')  # Saída: Visitando o vértice: 0, Adicionando 2 à fila, Adicionando 3 à fila, Adicionando 4 à fila, ...
