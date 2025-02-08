from heapq import heappush, heappop

class Solution:
    def shortest_distance(self, matrix):
        n = len(matrix)
        
        # Step 1: Replace -1 with infinity, except the diagonal
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == -1 and i != j:
                    matrix[i][j] = float('inf')
        
        # Step 2: Update distances using the Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
        
        # Step 3: Replace infinity with -1 to indicate no path
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = -1
        
        return matrix
