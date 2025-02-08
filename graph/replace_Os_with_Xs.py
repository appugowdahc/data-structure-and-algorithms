#User function Template for python3
import copy
class Solution:
    def fill(self, n=4, m=5):
        # code here
        mat =[
    ['O', 'X', 'X', 'O', 'O', 'X', 'O', 'X', 'O'],
    ['O', 'X', 'O', 'X', 'X', 'O', 'X', 'X', 'O'],
    ['X', 'O', 'X', 'X', 'X', 'O', 'O', 'O', 'O'],
    ['X', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O'],
    ['O', 'O', 'X', 'X', 'X', 'X', 'O', 'O', 'X'],
    ['O', 'X', 'O', 'O', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'X'],
    ['X', 'O', 'O', 'X', 'X', 'O', 'X', 'O', 'X'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
    ['O', 'O', 'O', 'X', 'X', 'O', 'X', 'X', 'X'],
    ['X', 'X', 'O', 'X', 'O', 'X', 'X', 'X', 'O']
]

        mat2 = copy.deepcopy(mat)
        vis = [[False]*m for _ in range(n)]
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        def  dfs(r,c,mat,vis):
            vis[r][c] = True
            mat[r][c] = 'X'
            for dr,dc in directions:
                row,col = r+dr,c+dc
                
                if 0<= row<n and 0<= col<m and mat[row][col] == 'O' and not vis[row][col]:
                    
                    dfs(row,col,mat,vis)
        for r in range(m) :
            if mat[0][r] == 'O' and not vis[0][r]:
                dfs(0,r,mat,vis)
            if mat[-1][r] == 'O' and not vis[-1][r]:
                dfs(n-1,r,mat,vis)
        for j in range(n):
            if mat[j][0] == 'O' and not vis[j][0]:
                dfs(j,0,mat,vis)
            if mat[j][-1] == 'O' and not vis[j][-1]:
                dfs(j,m-1,mat,vis)
                

        found = False       
        for r in range(1,n-1):
            for c in range(1,m-1):
                if mat[r][c] == 'O' and not vis[r][c]:
                    print(found)
                    dfs(r,c,mat,vis)
                    found = True
        for row in mat:
            print(row)       
        # return mat if found else mat2
    
s = Solution()
print(s.fill())