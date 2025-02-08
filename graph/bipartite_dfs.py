def is_bipartite_dfs(graph):
    n = len(graph)
    color = [-1] * n  # -1 means uncolored, 0 and 1 are the two colors

    def dfs(node, col):
        color[node] = col
        for neighbor in graph[node]:
            if color[neighbor] == -1:
                if not dfs(neighbor, 1 - col):
                    return False
            elif color[neighbor] == color[node]:
                return False
        return True

    for i in range(n):
        if color[i] == -1:  # If the node is not yet colored, start DFS
            if not dfs(i, 0):  # Start coloring with color 0
                return False
    return True

# Example of a bipartite graph adjacency list:
graph = [
    [1, 3],  # Node 0 is connected to nodes 1 and 3
    [0, 2],  # Node 1 is connected to nodes 0 and 2
    [1, 3],  # Node 2 is connected to nodes 1 and 3
    [0, 2]   # Node 3 is connected to nodes 0 and 2
]

print("Is Bipartite (DFS):", is_bipartite_dfs(graph))
