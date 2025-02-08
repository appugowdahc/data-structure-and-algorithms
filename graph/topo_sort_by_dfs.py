

graph = [
    [0,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,0],
    [0,0,0,0,1],
    [0,0,0,0,0],    
]

adj_list = {i:[] for i in range(len(graph))}




for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] ==1:
            
            adj_list[i].append(j)
            
print(adj_list)
adj_list = {
    0:[1],
    1:[3],
    2:[3],
    3:[],
    4:[0,2],
    5:[4],
    6:[4,5]  
}

def dfs(node,visited,adj_list,stack):
    visited[node] = 1
    for neighbor in adj_list[node]:
        if not visited[neighbor]:
            dfs(neighbor,visited,adj_list,stack)
        
    stack.append(node)
stack = []
visited = [0]*7
for node in adj_list:
    if not visited[node]:
        dfs(node,visited,adj_list,stack)
print(stack[::-1])