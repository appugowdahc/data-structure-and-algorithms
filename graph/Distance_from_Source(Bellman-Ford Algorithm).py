#User function Template for python3
from collections import deque
class Solution:
    '''
    Function to implement Bellman Ford
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    
    '''
    def bellmanFord(self,V, edges, src):
    # Step 1: Initialize distances from src to all other vertices as infinity
        dist = [float('inf')] * V
        dist[src] = 0
        
        # Step 2: Relax all edges V - 1 times
        for _ in range(V - 1):
            for u, v, w in edges:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        
        # Step 3: Check for negative-weight cycles
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                return [-1]  # Negative cycle detected
        
        # Step 4: Replace 'inf' with 108 for unreachable vertices
        for i in range(V):
            if dist[i] == float('inf'):
                dist[i] = 10**8
        
        return dist
         