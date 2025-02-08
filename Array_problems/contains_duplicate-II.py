"""

"""
from typing import List

############# optimal solution

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # d = {}
        # for i in range(len(nums)):
        #     if nums[i] in d and i - d[nums[i]] <= k:
        #         return True
        #     else:
        #         d[i] = i
        # return False
        index_map = {}  # Stores last index of each number
        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True
            index_map[num] = i  # Update the last index of num
        return False
    
    
####################### brute force 

def containsNearbyDuplicate_brute(nums, k):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, min(i + k + 1, n)):  # Check within k distance
            if nums[i] == nums[j]:
                return True
    return False

