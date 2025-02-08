nodes =[
    [0,1,1,0],
    [1,0,0,1],
    [1,0,0,1],
    [0,1,1,0]
    
]
adjacency_list = {i+1:[] for i in range(len(nodes))}
# for i in range(len(nodes)):
#     adjacency_list[i+1] = []
for row in range(len(nodes)):

    for col in range(len(nodes[0])):
        if nodes[row][col] == 1 and row !=col:
            if col+1 not in  adjacency_list[row+1]:
                adjacency_list[row+1].append(col+1)
            if row+1 not in adjacency_list[col+1]:
                adjacency_list[col+1].append(row+1)

    adjacency_list[row+1].sort()    
print(adjacency_list)