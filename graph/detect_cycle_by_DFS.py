def dfs(node, parent, visited, adj_list):
    visited[node] = True
    
    # Visit all neighbors of the current node
    for neighbor in adj_list[node]:
        if not visited[neighbor]:
            if dfs(neighbor, node, visited, adj_list):
                return True  # Cycle found
        elif neighbor != parent:
            return True  # If neighbor is visited and not parent, cycle detected
    
    return False

def has_cycle(graph):
    n = len(graph)
    visited = [False] * n
    
    # Convert adjacency matrix to adjacency list
    adj_list = adjacency_matrix_to_list(graph)
    
    # Check for cycles in each component of the graph
    for node in range(n):
        if not visited[node]:
            if dfs(node, -1, visited, adj_list):  # Start DFS, parent is -1 for root
                return True
    
    return False

def adjacency_matrix_to_list(matrix):
    adj_list = {}
    for i in range(len(matrix)):
        adj_list[i] = []
    for i in range(len(matrix)):
        for j in range(i, len(matrix[i])):
            if matrix[i][j] == 1 and i != j:
                adj_list[i].append(j)
                adj_list[j].append(i)
    return adj_list

# Example adjacency matrix (undirected graph)
graph = [
    [0, 1, 0, 1],
    [1, 0, 1, 1],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

# Check if the graph contains a cycle
if has_cycle(graph):
    print("Graph contains a cycle")
else:
    print("Graph does not contain a cycle")
