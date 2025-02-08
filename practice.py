from collections import deque

def dfs(r,c,r0,c0,shape_list,visited):
    
    visited[r][c] = 1
    shape_list.append((r-r0,c-c0))
    
    for dr,dc in directions:
        nr,nc = r+dr,c+dc
        if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1 and visited[nr][nc] == 0:
            dfs(nr,nc,r0,c0,shape_list,visited)
    
    

directions = [(-1,0),(1,0),(0,1),(0,-1)]      

            
grid = [
    [1,0,0,0],
    [1,0,1,0],
    [0,1,1,0],
    [0,0,0,1],  
]

rows = len(grid)
cols = len(grid[0])

visited = [[0] * cols for _ in range(rows)]
queue = deque([])
shapes = set()
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 1 and not visited[i][j]:
            shape_list = []
            dfs(i,j,i,j,shape_list,visited)
            shapes.add(tuple(shape_list))


        
print(shapes)
# exit()  
# import pdb;pdb.set_trace()
while queue:
    r,c = queue.popleft()
    
    for  dr,dc in directions:
        
        nr,nc = r+dr,c+dc
        
        if 0<= nr<rows and 0<= nc<cols and grid[nr][nc]  == 1 :
            visited[nr][nc] = 1
            queue.append((nr,nc))
            
print(visited)
count = 0
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 1 and visited[i][j] == 0:
            count += 1
print(count) 
            
            
    
    
            