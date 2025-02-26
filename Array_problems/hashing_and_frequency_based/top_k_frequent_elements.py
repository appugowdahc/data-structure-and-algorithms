"""
347. Top K Frequent Elements
Attempted
Medium
Topics
Companies
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

"""

from typing import List

####### bruteforce









######## optimal solution
from collections import Counter,defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_dict = Counter(nums)
        res = sorted(freq_dict.keys(), key=lambda x: -freq_dict[x])

        return res[:k]
############# optimal 2
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        return [num for num, _ in Counter(nums).most_common(k)]