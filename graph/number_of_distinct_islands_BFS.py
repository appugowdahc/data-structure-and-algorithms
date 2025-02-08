from collections import deque


grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 1, 1, 0, 0],
    [0, 1, 1, 0, 1]
]
count  = 0
rows = len(grid)
cols = len(grid[0])
visited = [[0]*cols for _ in range(rows)]
shapes_set = set()
print(f"the shapes set is : ",shapes_set)
queue = deque([])
directions = [(-1,0),(0,1),(1,0),(0,-1)]

def bfs(r,c,r0,c0,shapes,visited):
    shapes.append((r-r0,c-c0))
     
    queue.append((r,c))
    visited[r][c] = 1
    while queue:
        row,col = queue.popleft()
        for dr,dc in directions:
            nr,nc = row+dr,col+dc
            
            if 0<=nr < rows and 0<= nc< cols and grid[nr][nc] == 1 and not visited[nr][nc]:
                print("C")
                visited[nr][nc] = 1
                queue.append((nr,nc))
                shapes.append((nr-r0,nc-c0))
        

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 1 and not visited[i][j]:
            print("Calll")
            shapes= []
            bfs(i,j,i,j,shapes,visited)
            shapes_set.add(tuple(shapes))

print(count)