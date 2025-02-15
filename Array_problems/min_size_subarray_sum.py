"""
209. Minimum Size Subarray Sum
Solved
Medium
Topics
Companies
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

"""
from typing import List

######## brute force approach
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        min_len = float('inf')
        for i in range(len(nums)):
            curr_sum = 0
            # starting with i range i value also included e.g nums[i]=8,and target=8 in 
            # this case we cannot catch min len
            for j in range(i,len(nums)):
                curr_sum += nums[j]
                if curr_sum >= target:
                    min_len = min(j-i+1,min_len)
                    break
        return min_len

        

########### optimal solution
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        slow,fast = 0,0
        min_len = float('inf')
        res =  0
        while fast <  len(nums):
            res += nums[fast]
            while res >= target:
                min_len = min(fast-slow+1,min_len)
                res -= nums[slow]
                slow +=1
        
            fast += 1
        # min_len = min(fast-slow,min_len)
        return min_len

        