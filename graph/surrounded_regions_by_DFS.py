def solve(board):
    if not board:
        return

    rows, cols = len(board), len(board[0])

    # Helper function to perform DFS and mark the 'O's connected to the border
    def dfs(r, c):
        # Mark the current cell as 'S' (safe)
        board[r][c] = 'S'
        # Explore all four directions
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_r, new_c = r + dx, c + dy
            if 0 <= new_r < rows and 0 <= new_c < cols and board[new_r][new_c] == 'O':
                dfs(new_r, new_c)

    # Step 1: Start DFS from the borders
    for i in range(rows):
        if board[i][0] == 'O':
            dfs(i, 0)
        if board[i][cols - 1] == 'O':
            dfs(i, cols - 1)
    for j in range(cols):
        if board[0][j] == 'O':
            dfs(0, j)
        if board[rows - 1][j] == 'O':
            dfs(rows - 1, j)

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

###########################################
#User function Template for python3

class Solution:
    mat = [
            ['X', 'X', 'X', 'X'], 
            ['X', 'O', 'X', 'X'], 
            ['X', 'O', 'O', 'X'], 
            ['X', 'O', 'X', 'X'], 
            ['X', 'X', 'O', 'O']
       ]
    rows = len(mat)
    cols = len(mat[0])
    def dfs(self,r,c,visited):
        visited[r][c] = 1
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        
        for dr,dc in directions:
            nr,nc = r+dr,c+dc
            
            if 0<= nr < self.rows and 0<= nc < self.cols and self.mat[nr][nc] == 'O' and visited[nr][nc] == 0:
                self.dfs(nr,nc,visited)
        
        return
    
    
    
    def fill(self, n, m):
        
        visited = [[0]*m for i in range(n)]
        for i in range(m):
            if self.mat[0][i] == 'O' and visited[0][i] == 0:
                self.dfs(0,i,visited)
            if self.mat[n-1][i] == 'O' and visited[n-1][i] == 0:
                self.dfs(n-1,i,visited)
                
        for j in range(n):
            if self.mat[j][0] == 'O' and visited[j][0] == 0:
                self.dfs(j,0,visited)
            if self.mat[j][m-1] == 'O' and visited[j][m-1] == 0:
                self.dfs(j,m-1,visited)
                
        for i in range(n):
            for j in range(m):
                print(self.mat[i][j],visited[i][j])
                if self.mat[i][j] == 'O' and visited[i][j] == 0:
                    self.mat[i][j] = 'X'
                    
        print(self.mat)
cc = Solution()
cc.fill(5,4)



