def matrix_to_graph(matrix):
    graph = dict()
    for i in range(len(matrix)):
        graph[i] = [v for v in range(len(matrix[i])) if matrix[i][v] != 0]

    return graph


def greedy_graph_coloring(graph):
    n = len(graph)
    colors = [-1] * n
    colors[0] = 0
    available_colors = [False] * n

    for u in range(1, n):
        for i in graph[u]:
            if colors[i] != -1:
                available_colors[colors[i]] = True

        cr = 0
        while cr < n and available_colors[cr]:
            cr += 1
        colors[u] = cr

        for i in graph[u]:
            if colors[i] != -1:
                available_colors[colors[i]] = False
    return colors


if __name__ == '__main__':
    with open('matrix.txt', 'r') as file:
        matrix = [list(map(int, s.strip().split())) for s in file.readlines()]

    graph = matrix_to_graph(matrix)

    for k, v in graph.items():
        print(k, v, sep=': ')
    print('\n')

    print(greedy_graph_coloring(graph))