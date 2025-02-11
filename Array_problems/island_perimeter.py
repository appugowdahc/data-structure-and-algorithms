"""
463. Island Perimeter
Easy
Topics
Companies
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4

"""
from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        grid = [
            [1,0,1,0],
            [1,1,1,0],
            [1,1,1,0],
            [0,1,0,0],
            ]
        
        perimeter = 0
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    perimeter += 4 #one cell perimeter is 4
                    # if any cell attached to in top and left will be subtracted by because
                    # two cell have same edge each one contribute one edge so will be 
                    # subtracting 2
                    if i >0 and grid[i-1][j] == 1:#top cell
                        perimeter -= 2
                    if j >0 and grid[i][j-1] ==1:#left cell
                        perimeter -= 2
                    #each cell will count left and top for the next adjacent cell current 
                    # cell side will be left cell bottom will be top edge
        return perimeter
    
grid = [
            [1,0,1,0],
            [1,1,1,0],
            [1,1,1,0],
            [0,1,0,0],
            ]

s = Solution()
print(s.islandPerimeter(grid))