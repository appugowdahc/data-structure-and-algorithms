"""
566. Reshape the Matrix
Attempted
Easy
Topics
Companies
Hint
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

 

Example 1:


Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
Example 2:


Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
 
    
"""
from typing import List

###############
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        # Check if reshape is possible
        if m * n != r * c:
            return mat

        # Initialize new matrix
        reshaped = [[0] * c for _ in range(r)]

        # Fill new matrix directly
        for i in range(m * n):
            reshaped[i // c][i % c] = mat[i // n][i % n]

        return reshaped

############### my solution
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        

        if (r*c) != (rows*cols):
            return mat
        
        res = [ [0]*c for _ in range(r)]
        nr = 0
        nc = 0

        for row in range(rows):
            for col in range(cols):
                if nr < r and nc < c:
                    res[nr][nc] = mat[row][col]
                
                nc += 1
                if nc >= c:
                    nr+= 1
                    nc = 0
        return res

        