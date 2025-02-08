from collections import deque
from colorama import Fore,Style


print("\033[91m")
oranges = [
    [1,0,0,0],
    [1,0,2,0],
    [1,1,0,0],
    [1,0,1,1],
]

def is_make_all_rotten_oranges(oranges:list) -> str:
    rows = len(oranges)
    cols = len(oranges[0])
    
    queue = deque()
    fresh_oranges = 0  # count all fresh oranges whose value is one
    minutes = 0 # count minutes to rot all fresh oranges 
    
    directions = [
        (-1,0),# top neighbor
        (0,1),#right neighbor
        (1,0),# bottom neighbor
        (0,-1), #left neighbor
    ]
    
    for row in range(rows):
        for col in range(cols):
            if oranges[row][col] == 2:
                queue.append((row,col))
            elif oranges[row][col] == 1:
                fresh_oranges += 1
                
    while  queue and fresh_oranges > 0:
        minutes += 1
        for _ in range(len(queue)):
            row,col = queue.popleft()
            
            for dr,dc in directions:
                # row and col value of neioghbor
                nr,nc = row+dr,col+dc  #get neighbor up and down,left ,right direction value and add to curent value    
                
                
                if 0<= nr < rows  and 0<= nc <cols  and oranges[nr][nc] == 1:
                    oranges[nr][nc] = 2
                    fresh_oranges -= 1
                    queue.append((nr,nc))
                    
    # return minutes if fresh_oranges == 0 else -1
    return "All fresh oranges rotten in 6 minutes." if fresh_oranges == 0 else "All fresh oranges cannot rot by given rotten apples.."
                    
print(is_make_all_rotten_oranges(oranges=oranges))                   





                    