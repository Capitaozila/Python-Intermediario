import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    previous_vertices = {vertex: None for vertex in graph}
    distances[start] = 0

    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous_vertices

def shortest_path(graph, start, end):
    distances, previous_vertices = dijkstra(graph, start)
    path = []
    current_vertex = end

    while previous_vertices[current_vertex] is not None:
        path.append(current_vertex)
        current_vertex = previous_vertices[current_vertex]
    path.append(start)

    path = path[::-1]

    return path

# Exemplo de uso:
graph = {
    '1': {'2': 4, '3': 6, '4': 13},
    '2': {'3': 2, '4': 9, '5': 10},
    '3': {'5': 7, '6': 2},
    '4': {'7': 2},
    '5': {'4': 1},
    '6': {'5': 5, '8': 1, '9': 3},
    '7': {'5': 1, '9': 1},
    '8': {'5': 5, '7': 3, '9': 2},
    '9': {}
}

for end in graph:
    if end != '1':
        path = shortest_path(graph, '1', end)
        print(f'O caminho mais curto do vértice 1 até o vértice {end} é: {" -> ".join(path)}')
