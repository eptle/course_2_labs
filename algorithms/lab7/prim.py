import math


def matrix_to_graph(matrix):
    V = tuple(range(len(matrix)))
    E = list()
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i < j and matrix[i][j] != 0:
                E.append((i, j, matrix[i][j]))

    return V, E


def get_min(E, united):
    edge = (-1, -1, math.inf)
    min_edge = min(E, key=lambda x: x[2] if (x[0] in united) != (x[1] in united) else math.inf)
    if min_edge[2] < edge[2]:
        edge = min_edge

    return edge


def prim(graph):
    V, E = graph
    united = {1}
    mst = []

    while len(united) < len(V):
        min_edge = get_min(E, united)

        if min_edge[2] == math.inf:
            break

        mst.append(min_edge)
        united.add(min_edge[1]) if (min_edge[1] not in united) else united.add(min_edge[0])

    return mst



if __name__ == '__main__':
    with open('matrix.txt', 'r') as file:
        M = [list(map(int, s.strip().split())) for s in file.readlines()]

    G = matrix_to_graph(M)
    print(G)
    print(prim(G))
