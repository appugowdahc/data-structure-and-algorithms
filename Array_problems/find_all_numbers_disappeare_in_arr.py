    
"""
448. Find All Numbers Disappeared in an Array
Solved
Easy
Topics
Companies
Hint
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]  
    
"""
from typing import List

##################optimal solution/
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # for num in nums:
        #     index = abs(num) - 1 
        #     nums[index] = -abs(nums[index])  
        
        # print(nums)
        # return [i + 1 for i in range(len(nums)) if nums[i] > 0] 
        for num in nums:
            index = abs(num) - 1  # Convert number to index
            nums[index] = -abs(nums[index])  # Mark as visited by making it negative
        print(nums)
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
        
s = Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))

############# brute force approach

class Solution1:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = len(nums)
        nums = list(set(nums))
        nums.sort()
        res =[]
        j = 0
        for i in range(1,l+1):
            if j<len(nums) and  nums[j] == i:
                j +=1
            else:
                res.append(i)


        return res
    
def findDisappearedNumbers(nums):
    n = len(nums)
    return list(set(range(1, n+1)) - set(nums))

# # Test Cases
# print(findDisappearedNumbers([4,3,2,7,8,2,3,1])) # Output: [5,6]
# print(findDisappearedNumbers([1,1]))             # Output: [2]
