from collections import deque
class Solution:
    def countCoordinates(self, mat):
        # code here
        if not mat or not mat[0]:
            return []

        n, m = len(mat), len(mat[0])

        # Helper function for DFS
        def dfs(x, y, visited, prev_height):
            # import pdb;pdb.set_trace()
            if (x, y) in visited or x < 0 or y < 0 or x >= n or y >= m or mat[x][y] < prev_height:
                return
            visited.add((x, y))
            for dx, dy in directions:
                dfs(x + dx, y + dy, visited, mat[x][y])

        # Initialize visited sets for Pacific and Atlantic
        pacific = set()
        atlantic = set()

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        # Run DFS for cells adjacent to Pacific (left and top edges)
        for i in range(n):
            dfs(i, 0, pacific, mat[i][0])  # Left edge
            dfs(i, m - 1, atlantic, mat[i][m - 1])  # Right edge
        for j in range(m):
            dfs(0, j, pacific, mat[0][j])  # Top edge
            dfs(n - 1, j, atlantic, mat[n - 1][j])  # Bottom edge
        import pdb;pdb.set_trace()

        # Intersection of cells reachable by both oceans
        return len(list(pacific & atlantic))

# Example Usage
mat = [[1, 2, 2, 3, 5],
       [3, 2, 3, 4, 4],
       [2, 4, 5, 3, 1],
       [6, 7, 1, 4, 5],
       [5, 1, 1, 2, 4]]

solution = Solution()
result = solution.countCoordinates(mat)
print(result)