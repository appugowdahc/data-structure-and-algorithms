# User function Template for python3
from typing import List
from heapq import heappop, heappush
from collections import defaultdict, deque

class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        # Build adjacency list
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # Priority queue for Dijkstra's algorithm
        pq = []
        heappush(pq, (0, 1))  # (distance, node)
        
        dist = [float('inf')] * (n + 1)
        dist[1] = 0
        parent = [-1] * (n + 1)  # To track the path
        
        while pq:
            d, node = heappop(pq)
            
            # Skip if the distance is already processed
            if d > dist[node]:
                continue
            
            for neighbor, weight in graph[node]:
                new_dist = d + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    parent[neighbor] = node
                    heappush(pq, (new_dist, neighbor))
        
        # Reconstruct the path from 1 to n
        if dist[n] == float('inf'):
            return [-1]  # No path exists
        
        path = deque()
        current = n
        while current != -1:
            path.appendleft(current)
            current = parent[current]
        
        return [dist[n]] + list(path)