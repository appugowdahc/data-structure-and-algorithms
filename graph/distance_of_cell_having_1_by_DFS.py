def dfs(x, y, grid, dist, current_distance):
    rows, cols = len(grid), len(grid[0])
    
    # Check if we are out of bounds or if the current distance is already smaller
    if x < 0 or x >= rows or y < 0 or y >= cols or dist[x][y] <= current_distance:
        return
    
    # Update the distance grid
    dist[x][y] = current_distance
    
    # Visit all four neighbors
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        dfs(x + dx, y + dy, grid, dist, current_distance + 1)

def nearest_1_distance_dfs(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    # Initialize the distance grid with a large value
    dist = [[float('inf')] * cols for _ in range(rows)]
    
    # Perform DFS for each cell containing '1'
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                dfs(i, j, grid, dist, 0)
    
    return dist
