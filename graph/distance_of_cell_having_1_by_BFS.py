from collections import deque
def nearest_1_distance(grid:list[list[int]])-> any:
    
    rows = len(grid)
    cols = len(grid[0])
    
    queue = deque([])
    distance_list = [[float('inf')]*cols for i in range(rows)]
    print(distance_list)
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                distance_list[row][col] = 0
                queue.append((row,col))
    directions = [(-1,0),(1,0),(0,-1),(0,1)]      
    while queue:
        row,col = queue.popleft()
        
        for dr,dc in directions:
            
            nr,nc = row+dr,col+dc
            
            if 0<=nr<rows and 0<= nc <cols and distance_list[nr][nc] > distance_list[row][col]+1:
                
                distance_list[nr][nc] = distance_list[row][col] + 1
                queue.append((nr,nc))
                
            
            
    
    return distance_list
    



grid = [
    [1,0,0],
    [0,0,0],
    [0,0,0]
]

print(nearest_1_distance(grid))