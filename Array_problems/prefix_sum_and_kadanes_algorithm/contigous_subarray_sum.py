"""
523. Continuous Subarray Sum
Medium
Topics
Companies
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false

"""
from typing import List

###### brute force 
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    
        for index1 in range(len(nums)):
            summ = nums[index1]
            for index2 in range(index1+1,len(nums)):
                summ += nums[index2]
                if summ %k ==0 :
                    return True

        return False
        
############optimal solution
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0: -1}  # Store remainder -> index
        prefix_sum = 0
        
        for i, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k
            
            if remainder in remainder_map:
                if i - remainder_map[remainder] > 1:
                    return True
            else:
                remainder_map[remainder] = i  # Store first occurrence of remainder
        
        return False
        