graph = []
with open('lab2-3/graph.txt') as file:
    for line in file:
        graph.append(tuple(map(int, line.split())))

assert graph == list(zip(*graph)), 'матрица составлена неверно'
