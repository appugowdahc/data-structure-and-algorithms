"""
136. Single Number
Solved
Easy
Topics
Companies
Hint
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1

    
    
"""
from typing import List

##################### my solution 
from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for i in range(len(nums)):
            d[nums[i]] += 1

        for key,val in d.items():
            if val == 1:
                return key
            
"""
Optimal Approach: Bitwise XOR (O(n) Time, O(1) Space)
Key XOR Properties
A ⊕ A = 0 (Same numbers cancel out)
A ⊕ 0 = A (XOR with 0 keeps the number unchanged)
XOR is commutative and associative (Order doesn't matter)
How XOR Solves the Problem
Since all duplicate numbers cancel out (A ⊕ A = 0), only the single number remains after XORing all elements.
Code (Optimal XOR Approach)

"""
########### optimal solution
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num  # XOR all numbers
    return result

# Example Usage
print(singleNumber([2,2,1]))  # Output: 1
print(singleNumber([4,1,2,1,2]))  # Output: 4
print(singleNumber([1]))  # Output: 1
