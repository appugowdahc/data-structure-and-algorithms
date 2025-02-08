"""
217. Contains Duplicate
Solved
Easy
Topics
Companies
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 
    
"""
from typing import List

########### my solution

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            else:
                s.add(num)
        return False
        
from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = defaultdict(int)
        for num in nums:
            s[num] += 1
            if s[num] == 2:
                return True
          
        return False
    

############optimal solutiuon

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()  # O(n log n)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False