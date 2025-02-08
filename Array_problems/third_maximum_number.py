"""

414. Third Maximum Number
Solved
Easy
Topics
Companies
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
"""
from typing import List

############### optimal solution

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        if len(nums) ==2:
            return nums[-1]
        return nums[-3]
        
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first=second=third = float('-inf')

        for num in nums:
            if num in (first,second,third):
                continue
            if num > first:
                third,second,first = second,first,num
            elif num > second:
                third,second = second,num
            elif num > third:
                third = num
        return third if third != float('-inf') else first
        
        
############ brute force approach
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort(reverse=True)
        return nums[2] if len(nums) >=3 else nums[0]
        