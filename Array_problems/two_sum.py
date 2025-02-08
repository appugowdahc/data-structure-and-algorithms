"""
1. Two Sum
Solved
Easy
Topics
Companies
Hint
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""
from typing  import List
from collections import defaultdict

############# brute force solution

class Solution1:
    def twoSum(self,nums: List[int],target:int) -> List[int]:
        #approach1
        for i,num1 in enumerate(nums):
            for j,num2 in enumerate(nums):
                if i != j and num1+num2 == target:
                    return [i,j]
                
        #better approach 2
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]

            return []


############# final solution ##################
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = defaultdict(int)
        for i in range(len(nums)):
            rem_val = target-nums[i]
            if rem_val in table:
                    return [i,table[rem_val]]
            else:
                table[nums[i]] = i

        return []
    

    
