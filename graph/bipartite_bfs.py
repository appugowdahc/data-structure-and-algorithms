from collections import deque

def is_bipartite_bfs(graph):
    n = len(graph)
    color = [-1] * n  # -1 means uncolored, 0 and 1 are the two colors
    
    for i in range(n):
        if color[i] == -1:  # If the node is not yet colored, start BFS
            queue = deque([i])
            color[i] = 0  # Assign the first color (0)
            
            while queue:
                node = queue.popleft()
                
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        # Color with the opposite color
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        # If a neighbor has the same color, graph is not bipartite
                        return False
    return True

# Example of a bipartite graph adjacency list:
graph = [
    [1, 3],  # Node 0 is connected to nodes 1 and 3
    [0, 2],  # Node 1 is connected to nodes 0 and 2
    [1, 3],  # Node 2 is connected to nodes 1 and 3
    [0, 2]   # Node 3 is connected to nodes 0 and 2
]

print("Is Bipartite (BFS):", is_bipartite_bfs(graph))
