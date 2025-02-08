from collections import deque

class Solution:
    def shortestPath(self, grid, source, destination):
        n = len(grid)
        m = len(grid[0])
        
        # If the source or destination is invalid, return -1
        if grid[source[0]][source[1]] == 0 or grid[destination[0]][destination[1]] == 0:
            return -1
        
        # Directions for movement: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Queue for BFS: stores (row, col, distance)
        queue = deque([(source[0], source[1], 0)])
        visited = [[False] * m for _ in range(n)]
        visited[source[0]][source[1]] = True
        
        while queue:
            x, y, dist = queue.popleft()
            
            # If we reach the destination, return the distance
            if (x, y) == (destination[0], destination[1]):
                return dist
            
            # Explore all 4 possible directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Check if the new cell is valid and not visited
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))
        
        # If we cannot reach the destination, return -1
        return -1
