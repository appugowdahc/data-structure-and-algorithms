from collections import deque

class Solution:
    
    # Function to find whether a path exists from the source to destination.
    def is_Possible(self, grid):
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        vis = set()
        
        # Find the source and initialize the queue with the source cell
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    vis.add((i, j))
                    break
                    
        # BFS to find if there's a path to the destination
        while queue:
            row, col = queue.popleft()
            
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < rows and 0 <= c < cols:
                    if grid[r][c] == 2:
                        return 1  # Path to destination found
                    
                    if grid[r][c] == 0:
                        continue  # Skip walls
                    
                    if (r, c) not in vis and grid[r][c] == 3:
                        queue.append((r, c))
                        vis.add((r, c))
        
        return 0  # No path to destination
