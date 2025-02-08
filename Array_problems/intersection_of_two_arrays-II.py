"""
350. Intersection of Two Arrays II
Solved
Easy
Topics
Companies
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""
from typing import List
############brute force approach
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num in nums1:
            if num in nums2:
                res.append(num)
                nums2.append(num)
        return res
        
        

############ optimal solution
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1.sort()
        nums2.sort()

        i,j = 0,0
        while i <len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1

            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i +=1
                j +=1
        return res
    
from collections import Counter

def intersect(nums1, nums2):
    counts = Counter(nums1)  # Count occurrences in nums1
    result = []
    
    for num in nums2:
        if counts[num] > 0:  # If num is in nums1 and not exhausted
            result.append(num)
            counts[num] -= 1  # Reduce count
            
    return result

        