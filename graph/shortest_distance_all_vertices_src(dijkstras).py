from collections import deque

class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex src.
    def dijkstra(self, adj=[[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]], src=2) -> list[int]:
        
        
        dist = [float('inf')]*len(adj)
        
        dist[src] = 0
        
        queue = deque([(src,0)])
        
        while queue:
            
            node, dis = queue.popleft()
            
            if dis > dist[node]:
                continue
            
            for neighbor,dx in adj[node]:
                
                if dis+dx < dist[neighbor]:
                    dist[neighbor] = dis+dx
                    queue.append((neighbor,dis+dx))
                    
        
        return dist
    
    
############### using priority min heap
import heapq
from typing import List, Tuple

class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex src using Dijkstra's algorithm.
    def dijkstra(self, adj: List[List[Tuple[int, int]]], src: int) -> List[int]:
        
        dist = [float('inf')] * len(adj)
        dist[src] = 0
        
        # Priority queue (min-heap)
        queue = [(0, src)]  # (distance, node)
        
        while queue:
            dis, node = heapq.heappop(queue)
            
            # If the distance is greater than the recorded distance, skip processing
            if dis > dist[node]:
                continue
            
            # Explore neighbors
            for neighbor, weight in adj[node]:
                new_dist = dis + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(queue, (new_dist, neighbor))
        
        return dist
