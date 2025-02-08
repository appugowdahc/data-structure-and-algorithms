from collections import deque

class Solution:
    # Function to find unit area of the largest region of 1s.
    def findMaxArea(self,grid):
        # Direction vectors for 8 neighbors
        dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (0, -1), (1, -1), (-1, -1)]
        

        rows = len(grid)
        cols = len(grid[0])

        # Visited matrix to track visited cells
        vis = [[0] * cols for _ in range(rows)]
        total = 0

        # Depth-First Search function to explore the region
        def dfs(i, j, vis, grid):
            # Mark the cell as visited
            vis[i][j] = 1
            # Initialize the region size
            area = 1

            # Explore all 8 neighbors
            for dr, dc in dirs:
                r, c = i + dr, j + dc
                # Check boundaries and if the cell is part of the region
                if 0 <= r < rows and 0 <= c < cols and not vis[r][c] and grid[r][c] == 1:
                    # Recursively calculate area for this part of the region
                    area += dfs(r, c, vis, grid)

            return area

        # Iterate over the grid to find regions
        for i in range(rows):
            for j in range(cols):
                # If cell is part of a region and not yet visited
                if not vis[i][j] and grid[i][j] == 1:
                    # Calculate area of this region
                    res = dfs(i, j, vis, grid)
                    # Update maximum area found
                    total = max(total, res)

        return total
    
grid =  [
            [1, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]
s = Solution()
print(s.findMaxArea(grid))