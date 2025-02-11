"""

496. Next Greater Element I
Easy
Topics
Companies
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
 
"""
from typing import List

############# brute force approach

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        res = []
        for num in nums1:
            idx = nums2.index(num)
            great_el = -1
            for i in range(idx+1,len(nums2)):
                if nums2[i] > num:
                    great_el = nums2[i]
                    #when you get number bigger than current number break it
                    #if you dont break this it will go and check till end but we need to
                    # break ASAP when it get big num than curr num
                    break
            res.append(great_el)
        return res


##########optimal solution 

def nextGreaterElementOptimal(nums1, nums2):
    next_greater_map = {}  # Store next greater elements
    stack = []  # Monotonic decreasing stack

    for num in nums2:
        while stack and stack[-1] < num:
            next_greater_map[stack.pop()] = num  # Pop and map to next greater
        stack.append(num)

    # Fill result using precomputed next greater elements
    return [next_greater_map.get(num, -1) for num in nums1]

# Test Cases
print(nextGreaterElementOptimal([4,1,2], [1,3,4,2]))  # Output: [-1,3,-1]
print(nextGreaterElementOptimal([2,4], [1,2,3,4]))    # Output: [3,-1]

        
