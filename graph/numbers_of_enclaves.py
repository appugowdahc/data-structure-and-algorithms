
from typing import List

class Solution:    
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        # code here
        
        rows,cols = len(grid),len(grid[0])
        
        vis = [[0]*cols for _ in range(rows)]
        dirs = [(0,1),(0,-1),(-1,0),(1,0)]
        def dfs(r,c,grid,vis):
            vis[r][c] = 1
            grid[r][c] =0
            for dr,dc in dirs:
                row,col = r+dr,c+dc
                if 0<= row <rows and 0<= col < cols and not vis[row][col] and  grid[row][col] == 1:
                    dfs(row,col,grid,vis)
        
        for i in range(cols):
            if grid[0][i] ==1 and  not vis[0][i]:
                dfs(0,i,grid,vis)
            if grid[-1][i] == 1 and not vis[-1][i]:
                dfs(rows-1,i,grid,vis)
                
        for j in range(rows):
            if grid[j][0] == 1 and not vis[j][0] :
                dfs(j,0,grid,vis)
            if grid[j][-1] == 1 and not vis[j][-1]:
                dfs(j,cols-1,grid,vis)
                
        enclaves = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] ==1:
                    enclaves += 1
                    
        return enclaves