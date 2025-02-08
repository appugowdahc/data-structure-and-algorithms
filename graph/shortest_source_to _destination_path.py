from collections import deque
class Solution:
    def shortestDistance(self,N=3,M=4,A=[[0 ,0 ,0 ,0],
[1, 1, 0 ,1],
[0 ,1, 1, 1]],X=2,Y=3):

        visited = [[False]*M for _ in range(N)]
        queue= deque([])
        if A[0][0] ==1:
            visited[0][0] =True
            queue.append((0,0,0))
        directions = [(0,-1),(0,1),(-1,0),(1,0)]
        while queue:
            row,col,steps = queue.popleft()
            if row == X and Y == col:
                return steps
            for dr,dc in directions:
                r,c = row+dr,col+dc
                
                if 0<=r<N and 0<=c<M and A[r][c] == 1 and not visited[r][c] :
                    visited[r][c] =True
                    queue.append((r,c,steps+1))
        return -1
    
s = Solution()
print(s.shortestDistance())