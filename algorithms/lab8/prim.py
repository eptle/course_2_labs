import math


def matrix_to_graph(matrix):
    graph = dict()
    for i in range(len(matrix)):
        graph[i] = [(v, matrix[i][v]) for v in range(len(matrix[i])) if matrix[i][v] != 0]

    return graph


def dijkstra(graph, start):
    dist = {vertex: math.inf for vertex in graph}
    dist[start] = 0
    visited = set()
    priority_queue = [(start, 0)]

    while priority_queue:
        u, current_distance = min(priority_queue, key=lambda x: x[1])
        priority_queue.remove((u, current_distance))

        if u in visited:
            continue

        visited.add(u)

        for v, weight in graph[u]:
            if (v not in visited) and (dist[u] + weight < dist[v]):
                dist[v] = dist[u] + weight
                priority_queue.append((v, dist[v]))

    return dist


if __name__ == '__main__':
    with open('matrix.txt', 'r') as file:
        M = [list(map(int, s.strip().split())) for s in file.readlines()]

    G = matrix_to_graph(M)
    print(G)
    print(dijkstra(G, 0))
