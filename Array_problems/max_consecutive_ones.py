"""
485. Max Consecutive Ones
Solved
Easy
Topics
Companies
Hint
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2    
    
"""
from typing import List

############# brute force approach
def findMaxConsecutiveOnesBruteForce(nums):
    max_count = 0
    for i in range(len(nums)):  # Start index
        count = 0
        for j in range(i, len(nums)):  # End index
            if nums[j] == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                break  # Stop counting if we hit 0

    return max_count

# Test Cases
print(findMaxConsecutiveOnesBruteForce([1,1,0,1,1,1])) # Output: 3
print(findMaxConsecutiveOnesBruteForce([1,0,1,1,0,1])) # Output: 2


########optimal solution

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = float('-inf')
        curr_len = 0
        slow=fast = 0

        while fast<len(nums):
            if nums[fast] == 1:

                fast+=1
            else:
                max_len = max(max_len,fast-slow)
                slow = fast+1
                fast += 1
        max_len = max(max_len,fast-slow)

        return max_len
        
        
def findMaxConsecutiveOnesOptimal(nums):
    max_count = 0
    current_count = 0

    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0  # Reset if we hit 0

    return max_count

# Test Cases
print(findMaxConsecutiveOnesOptimal([1,1,0,1,1,1])) # Output: 3
print(findMaxConsecutiveOnesOptimal([1,0,1,1,0,1])) # Output: 2
