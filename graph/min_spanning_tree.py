#User function Template for python3
from typing import List
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V=3, adj=[[[1, 5], [2, 1]], [[0, 5], [2, 3]], [[1, 3], [0, 1]]]) -> int:
        # Initialize the min-heap
        min_heap = []
        # Add the starting node (node 0) with edge weight 0
        heapq.heappush(min_heap, (0, 0))  # (weight, node)
        
        # Array to track visited nodes
        visited = [False] * V
        # Total weight of the MST
        mst_weight = 0
        
        # Number of edges added to the MST
        edges_in_mst = 0
        
        while min_heap and edges_in_mst < V:
            # Pop the edge with the smallest weight
            weight, node = heapq.heappop(min_heap)
            
            # Skip if the node is already in the MST
            if visited[node]:
                continue
            
            # Mark the node as visited
            visited[node] = True
            # Add the edge weight to the MST total weight
            mst_weight += weight
            # Increment the count of edges in the MST
            edges_in_mst += 1
            
            # Push all edges from the current node to the min-heap
            for neighbor, edge_weight in adj[node]:
                if not visited[neighbor]:
                    heapq.heappush(min_heap, (edge_weight, neighbor))
        
        return mst_weight