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