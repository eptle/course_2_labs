from queue import Queue
import matplotlib.pyplot as plt
import networkx as nx


def bfs(graph, start_node):
    visited = set()
    q = Queue()
    q.put(start_node)
    order = []

    while not q.empty():
        vertex = q.get()
        if vertex not in visited:
            order.append(vertex)
            visited.add(vertex)
            for node in graph[vertex]:
                if node not in visited:
                    q.put(node)
    return order


def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()

    order = []

    if start_node not in visited:
        order.append(start_node)
        visited.add(start_node)
        for node in graph[start_node]:
            if node not in visited:
                order.extend(dfs(graph, node, visited))

    return order


def visualize_search(order, title, G, pos):
    plt.figure()
    plt.title(title)
    for i, node in enumerate(order, start=1):
        plt.clf()
        plt.title(title)
        nx.draw(G, pos, with_labels=True, node_color=['r' if n == node else 'g' for n in G.nodes])
        plt.draw()
        plt.pause(0.01)
    plt.show()


def generate_graph(n, m):
    while True:
        G = nx.gnm_random_graph(n, m)
        if nx.is_connected(G):
            return G


if __name__ == '__main__':
    G = generate_graph(20, 20)
    # G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G')])
    pos = nx.spring_layout(G)

    print(G[0])
    visualize_search(bfs(G, 0), 'bfs', G, pos)
