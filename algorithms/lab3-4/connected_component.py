from queue import Queue


def matrix_to_graph(matrix):
    graph = dict()
    for i in range(len(matrix)):
        graph[i] = [v for v in range(len(matrix[i])) if matrix[i][v] == 1]

    return graph


def bfs(graph, start, visited, components):
    component = list()
    queue = Queue()

    component.append(start)
    queue.put(start)
    visited.add(start)

    while not queue.empty():
        node = queue.get()

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.put(neighbour)
                visited.add(neighbour)
                component.append(neighbour)

    components.append(component)


def connected_components(graph):
    components = list()
    visited = set()

    for node in graph.keys():
        if node not in visited:
            bfs(graph, node, visited, components)

    return max(components, key=len)


if __name__ == '__main__':
    with open('matrix.txt', 'r') as file:
        M = [list(map(int, s.strip().split())) for s in file.readlines()]

    G = matrix_to_graph(M)

    for k, v in G.items():
        print(k, v, sep=': ')
    print('\n')

    connected_component = connected_components(G)
    print(connected_component, len(connected_component))
