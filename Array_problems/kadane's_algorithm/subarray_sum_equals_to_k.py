"""
560. Subarray Sum Equals K
Medium
Topics
Companies
Hint
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
    """
from typing import List

######### brute force solution
class Solution1:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for index1 in range(len(nums)):
            summ = 0
            for index2 in range(index1,len(nums)):
                summ += nums[index2]

                if summ == k:
                    count += 1
                #if in negative number case we cannot use this like k =0 and nums = [1,-1,0]
                # if summ > k:
                #     break
        return count 
        
        
######### optimal solution
from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # Base case for subarrays starting at index 0
        
        for num in nums:
            curr_sum += num
            
            # Check if there's a prefix sum that results in the required sum
            if curr_sum - k in prefix_sums:
                count += prefix_sums[curr_sum - k]
            
            # Update the prefix sum count
            prefix_sums[curr_sum] += 1
        print(prefix_sums)
        return count
    
s = Solution()
print(s.subarraySum([-2,3,1,5,6,8,9],1))