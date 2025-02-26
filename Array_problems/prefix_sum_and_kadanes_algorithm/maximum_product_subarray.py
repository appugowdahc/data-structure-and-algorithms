"""

152. Maximum Product Subarray
Medium
Topics
Companies
Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""
from typing import List

########## bruteforce solution

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = float('-inf')
        
        for index1 in range(len(nums)):
            curr_prod = 1

            for index2 in range(index1,len(nums)):
                curr_prod *= nums[index2]
                max_prod = max(max_prod,curr_prod)
                # if curr_prod <0:
                #     break
        return max_prod 
        
        
###########optimal solution

