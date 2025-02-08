
from collections import deque
graph = [
    [0,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,0],
    [0,0,0,0,1],
    [0,0,0,0,0],    
]

adj_list = [[] for i in range(len(graph))]


for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] ==1:
            
            adj_list[i].append(j)
            
print(f"adj_list is: {adj_list}")

in_degree = [0]*len(graph)
for i in range(len(adj_list)):
    for node in adj_list[i]:
        in_degree[node] += 1
        
print(f"in_Degree list is: {in_degree}")

queue = deque([])
for node in in_degree:
    if node == 0:
        queue.append(node)
        
topological_ord = []
while  queue:
    node = queue.popleft()
    topological_ord.append(node)
    for neighbor in adj_list[node]:
        in_degree[neighbor] -=1 
        if in_degree[neighbor] == 0:
            queue.append(neighbor)    

if len(in_degree) != len(topological_ord):
    print("This is cyclic graph or cycle exists in the graph..")
else:
    print(f"Topological sort can be done on this graph: {topological_ord}")