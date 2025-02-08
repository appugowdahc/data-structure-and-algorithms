from collections import defaultdict
import heapq

def find_eventual_safe_nodes(graph):
    n = len(graph)
    reverse_graph = defaultdict(list)
    in_degree = [0]*n
    
    #build reverse graph and in_degree
    for u in range(n):
        for v in graph[u]:
            reverse_graph[v].append(u)
            
        in_degree[u] = len(graph[u])
        
        
    queue = [i for i in range(n) if in_degree[i] == 0]
    heapq.heapify(queue)
    safe_nodes = []
    
    while queue:
        node = heapq.heappop(queue)
        safe_nodes.append(node)
        
        for neighbor in reverse_graph[node]:
            in_degree[neighbor] -= 1
            
            if in_degree[neighbor] == 0:
                heapq.heappush(queue,neighbor)
                
    return sorted(safe_nodes)

graph = [
    [1,2],
    [2,3],
    [5],
    [0],
    [5],
    [],
    []
]
print(find_eventual_safe_nodes(graph))
