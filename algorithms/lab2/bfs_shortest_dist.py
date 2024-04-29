from queue import Queue


def matrix_to_graph(matrix):
    graph = dict()
    for i in range(len(matrix)):
        graph[i] = [v for v in range(len(matrix[i])) if matrix[i][v] == 1]

    return graph


def bfs_shortest_distance(graph, start, end):
    visited = set()
    queue = Queue()
    queue.put((start, 0))

    while not queue.empty():
        node, distance = queue.get()

        if node == end:
            return distance

        visited.add(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.put((neighbour, distance + 1))

    return -1


if __name__ == '__main__':
    with open('matrix.txt', 'r') as file:
        matrix = [list(map(int, s.strip().split())) for s in file.readlines()]

    graph = matrix_to_graph(matrix)

    for k, v in graph.items():
        print(k, v, sep=': ')
    print('\n')

    print(bfs_shortest_distance(graph, 0, 5))
