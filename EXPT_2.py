from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

    def bfs(self, start):
        queue = deque()
        visited = set()

        queue.append(start)
        visited.add(start)

        while queue:
            node = queue.popleft()
            print(node, end=' ')

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

# Sample graph
graph = Graph()
graph.add_edge(0, [1, 3 , 8])
graph.add_edge(1, [0, 7])
graph.add_edge(2, [3, 5 , 7])
graph.add_edge(3, [0 ,2, 4])
graph.add_edge(4, [3, 8])
graph.add_edge(5, [2 ,6])
graph.add_edge(6, [5])
graph.add_edge(7, [1 ,2])
graph.add_edge(8, [0 ,4])

print("BFS:")
graph.bfs(0)