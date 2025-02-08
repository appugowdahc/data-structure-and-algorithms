"""
169. Majority Element
Solved
Easy
Topics
Companies
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""

from typing import List
from collections import defaultdict,Counter

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        count = Counter(nums)
        for num in count:
            if count[num] > n:
                return num
        
        ########### using dict
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            if count[num] > n:
                return num
            
############## optimal approach
class Solution:
    def majorityElement(self,nums):
        candidate, count = None, 0

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
