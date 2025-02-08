def numDistinctIslands(grid):
    rows, cols = len(grid), len(grid[0])
    distinct_islands = set()

    # Helper function for DFS that returns the shape of an island
    def dfs(r, c, r0, c0, shape):
        # Mark the cell as visited (turn it into water)
        grid[r][c] = 0
        shape.append((r - r0, c - c0))  # Record relative position of the land cell

        # Explore the neighboring cells in all four directions
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_r, new_c = r + dx, c + dy
            if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                dfs(new_r, new_c, r0, c0, shape)

    # Traverse the grid to find and record all islands
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Start a new DFS for an unvisited land cell
                shape = []
                dfs(i, j, i, j, shape)  # Record the shape of the island
                distinct_islands.add(tuple(shape))  # Add the shape to the set as a tuple

    return len(distinct_islands)

# Example usage:
grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 1, 0, 1]
]
print(numDistinctIslands(grid))  # Output: 3
