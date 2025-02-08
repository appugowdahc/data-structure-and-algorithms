"""

118. Pascal's Triangle
Solved
Easy
Topics
Companies
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
    
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1    
  
Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]


"""

from typing import List

################ brute force
def generate(numRows):
    triangle = []

    for i in range(numRows):
        row = [1] * (i + 1)  # Initialize row with 1s
        for j in range(1, i):  # Compute inner values
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)

    return triangle

# Example Usage
print(generate(5))



################### my solution 

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        res = [[] for _ in range(numRows)]
        res[0].append(1)

        for i in range(1,numRows):
            for j in range(i+1):
                if j == 0:
                    res[i].append(res[i-1][0])
                elif j == i:
                    res[i].append(res[i-1][-1])
                else:
                    val = res[i-1][j-1]+res[i-1][j]
                    res[i].append(val)

        return res
        
        
################# optimal solution
"""
Optimal Approach (Using Combination Formula)
Using the binomial coefficient, each element in Pascal's triangle at row i and column j can be directly computed as:


C(i,j)= j!(i−j)!
            i!
​
 
Using this formula, we can compute each row without using previous rows, reducing space complexity.

Code (Optimal - O(n²) Time Complexity, O(1) Space Complexity)
python
Copy
Edit

Complexity Analysis
Time Complexity: 

O(1), since no extra storage is used apart from the result.
Comparison of Approaches
Approach	Time Complexity	Space Complexity	Explanation
Brute Force	

Uses previous rows to compute the next one
Optimized (Combinations)	

Time comlexity is O(n2)	
space complexity is O(1)	
Uses mathematical formula without storing previous rows
The optimal approach is more efficient in terms of space complexity while maintaining the same time complexity.
"""

import math

def generate_optimized(numRows):
    triangle = []
    for i in range(numRows):
        row = [math.comb(i, j) for j in range(i + 1)]
        triangle.append(row)
    return triangle

# Example Usage
print(generate_optimized(5))