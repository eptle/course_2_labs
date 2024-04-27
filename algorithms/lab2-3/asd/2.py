def matrix_to_graph(matrix):
    nodes = list(range(len(matrix)))
    edges = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                edges.append((i, j))

    return (nodes, edges)

def bfs(graph, start, end):
    nodes, edges = graph
    d = [float('inf')] * len(nodes)
    d[start] = 0
    Q = [start]

    while Q:
        u = Q.pop(0)
        for edge in edges:
            if edge[0] == u:
                v = edge[1]
                if d[v] == float('inf'):
                    d[v] = d[u] + 1
                    Q.append(v)

    return d[end]

with open('2.txt') as file:
    matrix = file.readlines()
    matrix = [list(map(int, i.strip().split())) for i in matrix]
    graph = matrix_to_graph(matrix)
    print(bfs(graph, 0, 5))