def matrix_to_graph(matrix):
    graph = dict()
    for i in range(len(matrix)):
        graph[i] = [v for v in range(len(matrix[i])) if matrix[i][v] != 0]

    return graph


def transpose_matrix(matrix):
    return list(zip(*matrix))


def dfs(graph, start, visited, component):
    visited.add(start)
    for node in graph[start]:
        if node not in visited:
            visited.add(node)
            dfs(graph, node, visited, component)


def strong_connectivity(matrix):
    graph = matrix_to_graph(matrix)
    reversed_graph = matrix_to_graph(transpose_matrix(matrix))

    visited = set()
    strong_connectivities = list()

    for node in graph.keys():
        if node not in visited:
            vis1 = set()
            dfs(graph, node, vis1, strong_connectivities)
            vis2 = set()
            dfs(reversed_graph, node, vis2, strong_connectivities)

            strong_connectivities.append(list(vis1 & vis2))
            visited |= vis1 & vis2

    return strong_connectivities


if __name__ == '__main__':
    with open('matrix.txt', 'r') as file:
        M = [list(map(int, s.strip().split())) for s in file.readlines()]

    print(strong_connectivity(M))
