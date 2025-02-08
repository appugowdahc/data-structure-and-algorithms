from heapq import heappop, heappush
from collections import deque

class Solution:
    
    # Function to return the minimum cost to reach the bottom
    # right cell from the top left cell.
    def minimumCostPath(self, grid):
        # Initializing cost matrix with infinity
        cost = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]
        cost[0][0] = grid[0][0]
        
        # Min-heap to keep track of minimum path cost so far
        heap = [(grid[0][0], 0, 0)]
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        
        while heap:
            current_cost, row, col = heappop(heap)
            
            # If we reached the bottom-right cell, return its cost
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return current_cost
            
            # Explore neighbors
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                    new_cost = current_cost + grid[r][c]
                    # If a cheaper cost is found, update cost and push to heap
                    if new_cost < cost[r][c]:
                        cost[r][c] = new_cost
                        heappush(heap, (new_cost, r, c))
        
        # Return cost to bottom-right cell
        return cost[-1][-1]
