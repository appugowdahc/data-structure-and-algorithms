def is_cyclic_dfs(graph):
    def dfs(node):
        if visiting[node]:  # The node is already in the recursion stack (cycle detected)
            return True
        if visited[node]:  # The node has been fully explored, no cycle found from this node
            return False
        
        # Mark the node as visiting (part of current DFS path)
        visiting[node] = True
        
        # Explore all the neighbors (children) of the current node
        for neighbor in graph[node]:
            if dfs(neighbor):  # If any neighbor leads to a cycle, return True
                return True
        
        # Mark the node as visited (fully explored) and remove from visiting
        visiting[node] = False
        visited[node] = True
        
        return False

    n = len(graph)
    visited = [False] * n  # Tracks fully visited nodes
    visiting = [False] * n  # Tracks nodes in the current DFS recursion stack
    
    # Check for cycles starting from each node
    for i in range(n):
        if not visited[i]:  # If the node hasn't been visited, start a DFS from it
            if dfs(i):  # If a cycle is found during the DFS
                return True
    
    return False  # No cycle found

# Example of a directed graph using an adjacency list:
graph = [
    [1],        # Node 0 has an edge to node 1
    [2],        # Node 1 has an edge to node 2
    [0, 3],     # Node 2 has edges to nodes 0 (back edge, forms a cycle) and 3
    [4],        # Node 3 has an edge to node 4
    []          # Node 4 has no outgoing edges
]

print("Cycle Detected:", is_cyclic_dfs(graph))  # Output: True (cycle exists)
