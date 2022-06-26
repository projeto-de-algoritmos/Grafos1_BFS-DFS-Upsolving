from collections import defaultdict
from queue import Queue as Fila

class Graph:
    def __init__(self, nNodes, edges):
        self.numNodes = nNodes
        self.edges = edges
        # self.nodes = list(range(1, nNodes + 1))
        self.graph = defaultdict(list)
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])

    # bfs
    def bfs(self, start):
        visited = defaultdict(int)
        
        fila = Fila()
        fila.put(start)
        
        visited[start] = 1
        while not fila.empty():
            node = fila.get()
            for i in self.get_neighbors(node): 
                if visited[i] == 0:
                    visited[i] = visited[node]*(-1)
                    fila.put(i)
        return sum(value == 1 for value in visited.values())

    def get_neighbors(self, node):
        return self.graph[node]

    def get_edges(self):
        return self.edges

    def get_graph(self):
        return self.graph

    def get_nodes(self):
        return list(range(self.numNodes))

        
#main
nNodes = int(input())

edges = []
for i in range(nNodes-1):
    x, y = tuple(map(int, input().split()))
    edges.append((x, y))
    
graph = Graph(nNodes, edges)
# print(graph.get_edges())
# print(graph.get_graph())
# print(graph.get_neighbors(3))

solution = graph.bfs(1)
# print(solution)
print(solution*(nNodes-solution)-(nNodes-1))
