import math


def matrix_to_graph(matrix):
    graph = dict()
    for i in range(len(matrix)):
        graph[i] = [(v, matrix[i][v]) for v in range(len(matrix[i])) if matrix[i][v] != 0]

    return graph


def bellman_ford(graph, start):
    dist = {vertex: math.inf for vertex in graph}
    dist[start] = 0

    # расслабляем ребра n-1 раз
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if dist[u] != math.inf and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

    # проверка на отрицательные петли:
    for u in graph:
        for v, weight in graph[u]:
            if dist[u] != math.inf and dist[u] + weight < dist[v]:
                raise ValueError("граф содержит отрицательные петли")

    return dist


if __name__ == '__main__':
    with open('matrix.txt', 'r') as file:
        M = [list(map(int, s.strip().split())) for s in file.readlines()]

    G = matrix_to_graph(M)
    print(bellman_ford(G, 0))
