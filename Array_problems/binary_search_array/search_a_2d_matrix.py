"""

74. Search a 2D Matrix
Attempted
Medium
Topics
Companies
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""

from typing import List

############# brute force
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or not matrix[0]:
            return False  # Edge case: Empty matrix
    
        m, n = len(matrix), len(matrix[0])  # Rows and columns
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target:
                    return True
        return False


############## optimal solution 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or not matrix[0]:
            return False  # Edge case: Empty matrix
    
        m, n = len(matrix), len(matrix[0])  # Rows and columns
        left, right = 0, m * n - 1  # Flattened search space

        while left <= right:
            mid = (left + right) // 2
            row, col = mid // n, mid % n  # Convert mid index to matrix coordinates
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1  # Search in the right half
            else:
                right = mid - 1  # Search in the left half
        
        return False
