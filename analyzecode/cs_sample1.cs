using System;
using System.Collections.Generic;

class Graph
{
    private Dictionary<string, List<string>> adjList;

    public Graph()
    {
        adjList = new Dictionary<string, List<string>>();
    }

    // Method to add a vertex to the graph
    public void AddVertex(string vertex)
    {
        if (!adjList.ContainsKey(vertex))
        {
            adjList[vertex] = new List<string>();
            Console.WriteLine($"Vertex {vertex} added.");
        }
        else
        {
            Console.WriteLine($"Vertex {vertex} already exists.");
        }
    }

    // Method to add an edge to the graph
    public void AddEdge(string vertex1, string vertex2)
    {
        if (adjList.ContainsKey(vertex1) && adjList.ContainsKey(vertex2))
        {
            adjList[vertex1].Add(vertex2);
            adjList[vertex2].Add(vertex1); // For undirected graph
            Console.WriteLine($"Edge added between {vertex1} and {vertex2}.");
        }
        else
        {
            Console.WriteLine("One or both vertices not found.");
        }
    }

    // Method to remove an edge from the graph
    public void RemoveEdge(string vertex1, string vertex2)
    {
        if (adjList.ContainsKey(vertex1) && adjList.ContainsKey(vertex2))
        {
            adjList[vertex1].Remove(vertex2);
            adjList[vertex2].Remove(vertex1); // For undirected graph
            Console.WriteLine($"Edge removed between {vertex1} and {vertex2}.");
        }
        else
        {
            Console.WriteLine("One or both vertices not found.");
        }
    }

    // Method for DFS traversal
    public void DFS(string start)
    {
        HashSet<string> visited = new HashSet<string>();
        Console.WriteLine("Depth-First Search starting from vertex: " + start);
        DFSUtil(start, visited);
        Console.WriteLine(); // For a new line
    }

    private void DFSUtil(string vertex, HashSet<string> visited)
    {
        visited.Add(vertex);
        Console.Write(vertex + " ");

        foreach (var neighbor in adjList[vertex])
        {
            if (!visited.Contains(neighbor))
            {
                DFSUtil(neighbor, visited);
            }
        }
    }

    // Method for BFS traversal
    public void BFS(string start)
    {
        HashSet<string> visited = new HashSet<string>();
        Queue<string> queue = new Queue<string>();
        visited.Add(start);
        queue.Enqueue(start);

        Console.WriteLine("Breadth-First Search starting from vertex: " + start);
        
        while (queue.Count > 0)
        {
            string vertex = queue.Dequeue();
            Console.Write(vertex + " ");

            foreach (var neighbor in adjList[vertex])
            {
                if (!visited.Contains(neighbor))
                {
                    visited.Add(neighbor);
                    queue.Enqueue(neighbor);
                }
            }
        }
        Console.WriteLine(); // For a new line
    }

    // Method to display the graph
    public void Display()
    {
        Console.WriteLine("Graph adjacency list:");
        foreach (var vertex in adjList)
        {
            Console.Write(vertex.Key + ": ");
            foreach (var neighbor in vertex.Value)
            {
                Console.Write(neighbor + " ");
            }
            Console.WriteLine();
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        Graph g = new Graph();

        // Adding vertices
        g.AddVertex("A");
        g.AddVertex("B");
        g.AddVertex("C");
        g.AddVertex("D");
        g.AddVertex("E");

        // Adding edges
        g.AddEdge("A", "B");
        g.AddEdge("A", "C");
        g.AddEdge("B", "D");
        g.AddEdge("C", "D");
        g.AddEdge("D", "E");

        // Display the graph
        g.Display();

        // Perform DFS and BFS
        g.DFS("A");
        g.BFS("A");

        // Remove an edge and display the graph again
        g.RemoveEdge("A", "C");
        g.Display();
    }
}
