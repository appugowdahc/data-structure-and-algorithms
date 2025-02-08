class Solution:
    def numIslands(self, grid=[[0,1],[1,0],[1,1],[1,0]]):
        Row = len(grid)
        Col = len(grid[0])
        def dfs(row,col,visited,grid ):
            visited[row][col] = 1
            directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
            for dr,dc in directions:
                nr,nc = row+dr,col+dc
                if 0<=nr<Row and 0<= nc<Col and grid[nr][nc] == 1 and not visited[nr][nc]:
                    dfs(nr,nc,visited,grid)
                
                
                
        visited = [[0]*len(grid[0]) for _ in range(len(grid))]
        
        count = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] ==1 and not visited[row][col]:
                    dfs(row,col,visited,grid)
                    count += 1
                    
        return count
    
s = Solution()
print(s.numIslands())


###############################BFS

from collections import deque
class Solution:
    def numIslands(self, grid):
        Row = len(grid)
        Col = len(grid[0])
        def bfs(row,col,visited,grid ):
            queue = deque([(row,col)])
            visited[row][col] = 1
            directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
            while queue:
                r,c = queue.popleft()
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if 0<=nr<Row and 0<= nc<Col and grid[nr][nc] == 1 and not visited[nr][nc]:
                        queue.append((nr,nc))
                        visited[nr][nc] =1
                
                
                
        visited = [[0]*len(grid[0]) for _ in range(len(grid))]
        
        count = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] ==1 and not visited[row][col]:
                    bfs(row,col,visited,grid)
                    count += 1
                    
        return count