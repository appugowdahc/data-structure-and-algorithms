"""
    
283. Move Zeroes
Solved
Easy
Topics
Companies
Hint
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

"""
from typing import List

################## optimal solution

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]  # Swap
                slow += 1  # Move slow pointer
                
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        # new_arr = [num for num in nums if num != 0]
        # count_zero = len(nums)-len(new_arr)
        # nums[:] = new_arr+[0]*count_zero

        if len(nums) ==0:
            return nums
        slow = 0
        fast = 0
        # while fast < len(nums):
        #     if nums[fast] == 0:
        #         fast += 1
        #     else:
        #         nums[slow] = nums[fast]
        #         slow+= 1
        #         fast += 1
        # nums[slow:] = [0] * (len(nums)-slow)
        while fast<len(nums):
            if nums[fast] != 0:
                nums[slow],nums[fast] = nums[fast],nums[slow]
                slow += 1
            fast +=1

############## brute force
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        new_arr = [num for num in nums if num != 0]
        count_zero = len(nums)-len(new_arr)
        nums[:] = new_arr+[0]*count_zero


        