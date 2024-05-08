def matrix_to_graph(matrix):
    V = tuple(range(len(matrix)))
    E = list()
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i < j and matrix[i][j] != 0:
                E.append((i, j, matrix[i][j]))

    return V, E


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

        return True


def kruskal(graph):
    V, E = graph
    E.sort(key=lambda x: x[2])
    uf = DSU(len(E))
    min_spanning_tree = list()

    for edge in E:
        u, v, weight = edge
        if uf.union(u, v):
            min_spanning_tree.append(edge)

    return min_spanning_tree



if __name__ == '__main__':
    with open('matrix.txt', 'r') as file:
        M = [list(map(int, s.strip().split())) for s in file.readlines()]

    G = matrix_to_graph(M)
    print(G)
    print(kruskal(G))
