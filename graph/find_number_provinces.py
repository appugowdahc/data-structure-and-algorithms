############################ BFS ###############################33
from collections import deque
class Solution1:
    def numProvinces(self, adj, V):
        # code here 
        adj1 ={i:[] for i in range(1,V+1)}
        
        for i in range(len(adj)):
            for j in range(len(adj[0])):
                if adj[i][j] == 1 and   j+1 not in adj1[i+1]:
                    adj1[i+1].append(j+1)
                if adj[i][j] == 1 and i+1 not in adj1[j+1]:
                    adj1[j+1].append(i+1)
                    
        def dfs(node,vis,adj):
            queue = deque([node])
            vis[node] = 1
            while queue:
                parent = queue.popleft()
                for neighbor in adj[parent]:
                    if not vis[neighbor]:
                        queue.append(neighbor)
                        vis[neighbor] =1
           
        vis = [0] * (V + 1)
        provinces_count = 0
        for node in range(1,V+1):
            
            if not vis[node]:
                dfs(node,vis,adj1)
                provinces_count += 1
                
        return provinces_count



############################ DFS##################33333333
class Solution:
    def numProvinces(self, adj, V):
        # code here 
        adj1 ={i:[] for i in range(1,V+1)}
        
        for i in range(len(adj)):
            for j in range(len(adj[0])):
                if adj[i][j] == 1 and   j+1 not in adj1[i+1]:
                    adj1[i+1].append(j+1)
                if adj[i][j] == 1 and i+1 not in adj1[j+1]:
                    adj1[j+1].append(i+1)
                    
        def dfs(node,vis,adj):
            vis[node] = 1
            for neighbor in adj[node]:
                if not vis[neighbor]:
                    dfs(neighbor,vis,adj)
           
        vis = [0] * (V + 1)
        provinces_count = 0
        for node in range(1,V+1):
            
            if not vis[node]:
                dfs(node,vis,adj1)
                provinces_count += 1
                
        return provinces_count


adj = [
 [1, 0, 1],
 [0, 1, 0],
 [1, 0, 1]
]
V= 3

s = Solution()
print(s.numProvinces(adj,V))