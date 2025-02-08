class Solution:
    def isNegativeWeightCycle(self, n, edges):
        # Initialize distances to all nodes as infinity
        dist = [float('inf')] * n
        
        # Perform Bellman-Ford for each node
        for i in range(n):
            dist[i] = 0  # Assume this node as the starting point
            
            # Relax edges n-1 times
            for _ in range(n - 1):
                for u, v, w in edges:
                    if dist[u] != float('inf') and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
            
            # Check for negative weight cycle by trying to relax one more time
            for u, v, w in edges:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    return 1  # Negative weight cycle found
            
            # Reset distances for the next iteration
            dist = [float('inf')] * n
        
        return 0  # No negative weight cycle
