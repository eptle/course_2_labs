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
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            print(self.parent)
            print(self.rank, end='\n\n')
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


def kruskal(graph):
    V, E = graph
    dsu = DSU(len(V))
    mst = []

    E.sort(key=lambda x: x[-1])

    for u, v, weight in E:
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            mst.append((u, v, weight))

    return mst


if __name__ == '__main__':
    with open('matrix.txt', 'r') as file:
        M = [list(map(int, s.strip().split())) for s in file.readlines()]

    G = matrix_to_graph(M)
    print(G)
    print(kruskal(G))
