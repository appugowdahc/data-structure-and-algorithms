"""
53. Maximum Subarray
Medium
Topics
Companies
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


"""

from typing import List

########### brute force 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        for index1 in range(len(nums)):
            curr_sum = 0
            for index2 in range(index1,len(nums)):
                curr_sum += nums[index2]
                max_sum = max(max_sum,curr_sum)
        return max_sum
    

###########optimal solution 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        curr_sum = 0
        for num in nums:
            curr_sum += num
            max_sum = max(max_sum,curr_sum)
            if curr_sum <0:
                curr_sum = 0
            
        return max_sum