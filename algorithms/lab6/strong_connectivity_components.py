def matrix_to_graph(matrix):
    graph = dict()
    for i in range(len(matrix)):
        graph[i] = [v for v in range(len(matrix[i])) if matrix[i][v] != 0]

    return graph


def transpose_matrix(matrix):
    return list(zip(*matrix))


def reverse_graph(graph):
    matrix = [[0] * len(graph) for _ in range(len(graph))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j in graph[i]:
                matrix[i][j] = 1

    print(*matrix, sep='\n')


if __name__ == '__main__':
    with open('matrix.txt', 'r') as file:
        M = [list(map(int, s.strip().split())) for s in file.readlines()]

    G = matrix_to_graph(M)

    print(*G.items(), sep='\n')

    reverse_graph(G)
    print()
