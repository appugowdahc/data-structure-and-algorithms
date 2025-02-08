from collections import deque

def is_cyclic_bfs(graph):
    n = len(graph)
    in_degree = [0] * n  # In-degree of each node
    
    # Calculate in-degree of each node
    for node in range(n):
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    # Collect all nodes with 0 in-degree
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    
    visited_count = 0  # Number of nodes visited
    print(queue)
    while queue:
        node = queue.popleft()
        visited_count += 1
        
        # Decrease in-degree of all its neighbors
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:  # If in-degree becomes 0, add to queue
                queue.append(neighbor)
    
    # If the number of visited nodes is less than total nodes, there is a cycle
    return visited_count != n

# Example of a directed graph using an adjacency list:
graph = [
    [1],        # Node 0 has an edge to node 1
    [2],        # Node 1 has an edge to node 2
    [0, 3],     # Node 2 has edges to nodes 0 (back edge, forms a cycle) and 3
    [4],        # Node 3 has an edge to node 4
    []          # Node 4 has no outgoing edges
]

print("Cycle Detected (BFS):", is_cyclic_bfs(graph))  # Output: True (cycle exists)
