import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

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

print(dijkstra(graph, '1'))
