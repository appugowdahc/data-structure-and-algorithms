"""
128. Longest Consecutive Sequence
Solved
Medium
Topics
Companies
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 
"""
from typing import List

############## brute force 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_len = 1
        nums.sort()
        curr_len = 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i]+1 == nums[i+1]:
                curr_len += 1
            else:
                max_len = max(curr_len,max_len)
                curr_len =1
        max_len = max(curr_len,max_len)
        return max_len

#########optimal approach

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        num_set = set(nums)  # Store all numbers in a set for O(1) lookups
        longest = 0

        for num in num_set:
            
            # Check if num is the start of a sequence
            if num - 1 not in num_set:# e.g 1,2,3,4 this code has to start on 1 not every 2,3,4
                current_num = num
                current_streak = 1

                # Expand sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest = max(longest, current_streak)

        return longest



        