"""
349. Intersection of Two Arrays
Solved
Easy
Topics
Companies
Given two integer arrays nums1 and nums2, return an array of their 
intersection
. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.


"""
from typing import List

########### brute force approach
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res  = set()
        for num in nums1:
            if num in nums2 :
                res.add(num)
        return list(res)
    
    
###############optimal solution
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        return list(set(nums1) & set(nums2))
#################### another

def intersection(nums1, nums2):
    nums1.sort()
    nums2.sort()
    i, j = 0, 0
    result = set()
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            result.add(nums1[i])
            i += 1
            j += 1

    return list(result)

        