import math


def matrix_to_graph(matrix):
    V = tuple(i for i in range(len(matrix)))
    E = list()
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i < j and matrix[i][j] != 0:
                E.append((i, j, matrix[i][j]))

    return V, E


def get_min_edge(E, U):
    shortest_edge = (-1, -1, math.inf)
    for mst_edges in U:
        edges = list()
        for vertex in E:
            if (vertex[0] == mst_edges or vertex[1] == mst_edges) and (vertex[0] not in U or vertex[1] not in U):
                edges.append(vertex)
        shortest_edge = min(edges)

    return shortest_edge


def prim_MST(graph):
    V, E = graph
    united = {V[0]}
    MST = list()

    while len(united) < len(V):
        min_edge = get_min_edge(E, united)
        if min_edge[2] == math.inf:
            break

        MST.append(min_edge)
        united.add(min_edge[0])
        united.add(min_edge[1])
    return MST



if __name__ == '__main__':
    with open('matrix.txt', 'r') as file:
        M = [list(map(int, s.strip().split())) for s in file.readlines()]

    G = matrix_to_graph(M)
    print(G)
    print(prim_MST(G))
