from collections import deque

class Solution:
    
    # Function to find a Mother Vertex in the Graph.
    def findMotherVertex(self, V, adj):
        def dfs(v, visited):
            visited[v] = True
            for neighbor in adj[v]:
                if not visited[neighbor]:
                    dfs(neighbor, visited)
        
        # Step 1: Find the last finished vertex in DFS
        visited = [False] * V
        last_finished_vertex = 0
        for i in range(V):
            if not visited[i]:
                dfs(i, visited)
                last_finished_vertex = i

        # Step 2: Check if this last finished vertex is a mother vertex
        visited = [False] * V
        dfs(last_finished_vertex, visited)
        
        # If all vertices are visited, last_finished_vertex is a mother vertex
        if all(visited):
            return last_finished_vertex
        else:
            return -1