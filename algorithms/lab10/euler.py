def is_eulerian(graph):
    odd = 0
    for row in graph:
        degree = sum(row)
        if degree % 2 == 1:
            odd += 1
    return odd == 0


def find_eulerian_cycle(graph):
    if not is_eulerian(graph):
        return None

    n = len(graph)
    stack = [0]
    cycle = []
    while stack:
        v = stack[-1]
        if any(graph[v]):
            for u in range(n):
                if graph[v][u] == 1:
                    graph[v][u] = 0
                    graph[u][v] = 0
                    stack.append(u)
                    break
        else:
            cycle.append(stack.pop())
    return cycle[::-1]


if __name__ == '__main__':
    with open('matrix.txt', 'r') as file:
        graph = [list(map(int, s.strip().split())) for s in file.readlines()]

    path = find_eulerian_cycle(graph)
    if path:
        print("Эйлеров цикл:", path)
    else:
        print("Граф не является эйлеровым")