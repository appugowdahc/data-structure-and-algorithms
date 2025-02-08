from typing import List
from collections import deque

class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        # Helper function to perform BFS
        def bfs(node, visited, adj):
            queue = deque([(node, -1)])  # Start with (node, parent)
            visited[node] = True
            
            while queue:
                element, parent = queue.popleft()
                
                for vertex in adj[element]:
                    if not visited[vertex]:
                        visited[vertex] = True
                        queue.append((vertex, element))  # Add neighbor with its parent
                    elif parent != vertex:
                        return True  # Cycle found
                        
            return False
        
        visited = [False] * V  # Initialize visited array
        
        # Check each component of the graph
        for node in range(V):
            if not visited[node]:
                if bfs(node, visited, adj):
                    return True  # Cycle found
        
        return False  # No cycle found
adj2 = [[],[2],[1, 3],[2]]

obj = Solution()

ans = obj.isCycle(5, adj2)
#{ 
 # Driver Code Starts

# if __name__ == '__main__':

#     T=int(input("enter test cases count: "))
#     for i in range(T):
#         V, E = map(int, input("enter the number of  vertices and number of edges: ").split())
#         adj = [[] for i in range(V)]
#         for _ in range(E):
#             u, v = map(int, input("enter edge connection value:").split())
#             adj[u].append(v)
#             adj[v].append(u)
#         obj = Solution()
#         adj2 = [[1, 2], [0, 4], [0, 3], [2, 4], [1, 3]]
#         # ans = obj.isCycle(V, adj)
#         ans = obj.isCycle(V, adj2)
#         if(ans):
#             print("1")
#         else:
#             print("0")

