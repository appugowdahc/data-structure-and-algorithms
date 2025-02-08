#User function Template for python3

from typing import List
from collections import defaultdict
from heapq import heappop,heappush
import sys
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        #Your code here
        MOD = 10**9 + 7
        
        # Step 1: Build adjacency list
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
    
        # Step 2: Initialize distance and ways arrays
        dist = [sys.maxsize] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
    
        # Step 3: Dijkstra's algorithm using priority queue
        pq = [(0, 0)]  # (current time, node)
        while pq:
            curr_time, node = heappop(pq)
    
            # If the current time is greater than the recorded shortest distance, skip
            if curr_time > dist[node]:
                continue
    
            # Step 4: Explore neighbors
            for neighbor, time in graph[node]:
                new_time = curr_time + time
    
                # If a shorter path is found
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    ways[neighbor] = ways[node]
                    heappush(pq, (new_time, neighbor))
    
                # If another way to reach with the same shortest time
                elif new_time == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD
    
        # Step 5: Return the number of ways to reach node n-1
        return ways[n - 1]
    
n=7; m=10
edges= [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
