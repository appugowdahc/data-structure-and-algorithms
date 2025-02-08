from collections import deque
image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]


def flood_fill(sr:int,sc:int,new_colour:int,image:list[list[int]]):
    queue = deque([(sr,sc)])

    start_node = image[sr][sc]
    rows,cols = len(image),len(image[0])
    if start_node == new_colour:
        return "Given node already flooded"
    image[sr][sc] = new_colour
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    while queue:
        r,c = queue.popleft()
        
        for nr,nc in directions:
            nr = r+nr
            nc = c+nc
            if 0<= nr <rows and 0<= nc < cols and image[nr][nc] == start_node:
                image[nr][nc]=new_colour
                queue.append((nr,nc))
        
        
    return image

print(flood_fill(1,1,2,image))

