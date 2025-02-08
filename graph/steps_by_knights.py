from collections import deque

class Solution:
    
    # Function to find out minimum steps Knight needs to reach target position.
    def minStepToReachTarget(self, KnightPos=[3,3], TargetPos=[2,1], N=6):
        # Adjust for 1-based indexing to 0-based indexing
        KnightPos = [KnightPos[0] - 1, KnightPos[1] - 1]
        TargetPos = [TargetPos[0] - 1, TargetPos[1] - 1]

        # Initialize the grid and visited array
        visited = [[False] * N for _ in range(N)]

        # Starting position marked as visited
        visited[KnightPos[0]][KnightPos[1]] = True

        # Queue for BFS with (row, col, steps)
        queue = deque([(KnightPos[0], KnightPos[1], 0)])

        # All possible moves for a knight
        directions = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1), (-1, -2), (1, -2)]

        # BFS loop
        while queue:
            r, c, steps = queue.popleft()

            # If we reach the target, return the number of steps
            if r == TargetPos[0] and c == TargetPos[1]:
                return steps

            # Explore all valid moves
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if 0 <= row < N and 0 <= col < N and not visited[row][col]:
                    visited[row][col] = True
                    queue.append((row, col, steps + 1))

        # If target cannot be reached
        return -1
