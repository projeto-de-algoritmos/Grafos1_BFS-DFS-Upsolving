from math import pi, sin, cos
# macros


def ri():
    return int(input())


def mi():
    return map(int, input().split())


def mf():
    return map(float, input().split())


def lis():
    return list(map(int, input().split()))

# create a graph class that can be used to represent a graph and has the following methods:
# dfs(start) - returns a list of nodes in a depth first search starting from start
# bfs(start) - returns a list of nodes in a breadth first search starting from start
# add_edge(node1, node2) - adds an edge between node1 and node2
# add_node(node) - adds a node to the graph
# remove_edge(node1, node2) - removes an edge between node1 and node2
# remove_node(node) - removes a node from the graph
# get_neighbors(node) - returns a list of neighbors for the given node
# get_edges() - returns a list of all edges in the graph
# get_nodes() - returns a list of all nodes in the graph
# get_degree(node) - returns the degree of the given node
# get_degree_sequence() - returns a list of degrees for all nodes
# is_connected() - returns True if the graph is connected, False otherwise
# is_bipartite() - returns True if the graph is bipartite, False otherwise
# is_eulerian() - returns True if the graph is eulerian, False otherwise
# is_tree() - returns True if the graph is a tree, False otherwise


class Graph:
    def __init__(self, nNodes, edges):
        self.numNodes = nNodes
        self.edges = edges
        # self.nodes = list(range(1, nNodes + 1))
        self.graph = {node: [] for node in range(1, self.numNodes+1)}
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])

    # dfs
    def dfs(self, start):
        visited = []
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                stack.extend(self.graph[node])
        return visited

    # bfs
    def bfs(self, start):
        visited = []
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                queue.extend(self.graph[node])
        return visited

    def add_edge(self, node1, node2):
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def add_node(self, node):
        self.graph[node] = []

    def remove_edge(self, node1, node2):
        self.graph[node1].remove(node2)
        self.graph[node2].remove(node1)

    def remove_node(self, node):
        for neighbor in self.graph[node]:
            self.graph[neighbor].remove(node)
        del self.graph[node]

    def get_neighbors(self, node):
        return self.graph[node]

    def get_edges(self):
        return self.edges

    def get_graph(self):
        return self.graph

    def get_nodes(self):
        return list(range(self.numNodes))

    def get_degree(self, node):
        return len(self.graph[node])

    def get_degree_sequence(self):
        return [len(self.graph[node]) for node in range(1, self.numNodes)]

    # check if is connected using bfs
    def is_connected(self):
        visited = self.bfs(1)
        return len(visited) == self.numNodes

    # check number of connected components
    def num_connected_components(self):
        visited = self.bfs(1)
        return len(visited)

    # check number of groups of connected components
    def num_groups(self):
        visited = self.bfs(1)
        chunks = 1
        # check if node is in visited
        for node in range(1, self.numNodes+1):
            if node not in visited:
                new_visited = self.bfs(node)
                # add difference to visited
                visited.extend(new_visited)
                chunks += 1
        return chunks


# main
t = int(input())

for i in range(t):
    nNodes = ri()
    nEdges = ri()
    edges = []
    for j in range(nEdges):
        x, y = mi()
        edges.append((x, y))

    # instantiate the graph
    graph = Graph(nNodes, edges)
    # print(graph.get_edges())
    print(graph.get_graph())

    # do bfs and dfs
    print(graph.bfs(1))
    # print(len(graph.bfs(1)))
    # print(nNodes)
    # print(graph.dfs(1))

    # check if the graph is connected
    print("grupo eh conectado: ", graph.is_connected())
    print("numero de chunks conectados: ", graph.num_groups())
