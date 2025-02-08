image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

def flood_fill(sr:int,sc:int,new_color:int,image:list[list[int]]) -> int:
    rows,cols = len(image),len(image[0])
    start_node = image[sr][sc]
    if start_node == new_color:
        return "Given node is already has new colour"
    
    def dfs(r,c):
        if r<0 or r>= rows or c<0 or c>= cols or image[r][c] != start_node:
            return
        image[r][c]=new_color
        
        dfs(r-1,c)
        dfs(r+1,c)
        dfs(r,c-1)
        dfs(r,c+1)
    
    dfs(sr,sc)
    return image
    
sr,sc,new_color = 0,1,2
print(flood_fill(sr,sc,new_color,image))