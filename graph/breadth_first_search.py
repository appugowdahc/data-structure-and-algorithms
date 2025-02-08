from collections import deque

def bfs(graph, start):
    import pdb;pdb.set_trace()
    visited = set()  # Track visited nodes
    queue = deque([start])  # Queue for BFS
    visited.add(start)
    
    while queue:
        node = queue.popleft()  # Dequeue a node
        print(node, end=" ")  # Visit the node
        
        # Enqueue all unvisited neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
# Representation of an undirected graph


def  breadth_first_search(nodes,starting_node):
    visited = set()
    queue = deque([starting_node])
    visited.add(starting_node)
    
    while queue:
        node = queue.popleft()
        print(node,end=", ")
        
        for neighbor in nodes[node]:
            if neighbor  not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Print the adjacency list
for node in graph:
    print(f"{node} -> {', '.join(graph[node])}")


# Call BFS
breadth_first_search(graph, 'A')
print("\n")
