# exemplo de entrada com uma matriz

V = [0, 1, 2, 3, 4]
A = [(0, 1), (0, 2), (1, 2), (1, 3), (1, 2), (2, 3), (2, 4)]

matrix = [[0, 1, 1, 0, 0],
          [1, 0, 1, 1, 0],
          [1, 1, 0, 1, 1],
          [0, 1, 1, 0, 0],
          [0, 0, 1, 0, 0]]

graph = dict()
graph[0] = [1, 2]
graph[1] = [0, 2, 3]
graph[2] = [0, 1, 3, 4]
graph[3] = [1, 2]
graph[4] = [2]

matrix_elements = sorted(graph.keys())
cols = rows = len(matrix_elements)

adjacency_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        if matrix_elements[j] in graph[matrix_elements[i]]:
            adjacency_matrix[i][j] = 1

for row in matrix:
    print(row)

# edges_list = []