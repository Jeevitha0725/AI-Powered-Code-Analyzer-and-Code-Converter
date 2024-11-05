class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            print(f"Vertex {vertex} added.")

    def add_edge(self, u, v):
        if u in self.graph and v in self.graph:
            self.graph[u].append(v)
            self.graph[v].append(u)  # For undirected graph
            print(f"Edge added between {u} and {v}.")
        else:
            print("One or both vertices not found.")

    def remove_edge(self, u, v):
        if u in self.graph and v in self.graph:
            self.graph[u].remove(v)
            self.graph[v].remove(u)  # For undirected graph
            print(f"Edge removed between {u} and {v}.")
        else:
            print("One or both vertices not found.")

    def display(self):
        print("Graph adjacency list:")
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {edges}")

    def dfs(self, start):
        visited = set()
        print("Depth-First Search starting from vertex:", start)
        self._dfs_util(start, visited)
        print()  # for a new line

    def _dfs_util(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")

        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_util(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)
        print("Breadth-First Search starting from vertex:", start)

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()  # for a new line


# Example usage
if __name__ == "__main__":
    g = Graph()

    # Adding vertices
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")

    # Adding edges
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")
    g.add_edge("D", "E")

    # Display graph
    g.display()

    # Perform DFS and BFS
    g.dfs("A")
    g.bfs("A")

    # Remove an edge and display the graph again
    g.remove_edge("A", "C")
    g.display()
