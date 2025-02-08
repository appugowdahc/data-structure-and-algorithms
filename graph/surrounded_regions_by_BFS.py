from collections import deque

def solve(board):
    if not board:
        return

    rows, cols = len(board), len(board[0])

    # Helper function to perform BFS and mark the 'O's connected to the border
    def bfs(r, c):
        queue = deque([(r, c)])
        board[r][c] = 'S'  # Mark as safe
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < rows and 0 <= new_y < cols and board[new_x][new_y] == 'O':
                    board[new_x][new_y] = 'S'
                    queue.append((new_x, new_y))

    # Step 1: Start BFS from the borders
    for i in range(rows):
        if board[i][0] == 'O':
            bfs(i, 0)
        if board[i][cols - 1] == 'O':
            bfs(i, cols - 1)
    for j in range(cols):
        if board[0][j] == 'O':
            bfs(0, j)
        if board[rows - 1][j] == 'O':
            bfs(rows - 1, j)

    # Step 2: Flip surrounded 'O' to 'X' and 'S' back to 'O'
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'O':
                board[i][j] = 'X'  # Flip surrounded 'O' to 'X'
            elif board[i][j] == 'S':
                board[i][j] = 'O'  # Restore safe 'O's back

# Example usage:
board = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X']
]
solve(board)
for row in board:
    print(row)
