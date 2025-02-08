'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3


'''

#Solution 1:

class Solution:
    def rob(self, nums):
        return max(nums[0],self.robber(nums[1:]),self.robber(nums[:-1]))
    
    def robber(self,nums):
        first_rob, second_rob = 0,0
        for current in nums:
            max_rob = max(first_rob+current,second_rob)
            first_rob = second_rob
            second_rob = max_rob
        return second_rob
  
################################################################################  
#solution 2:

def rob(nums):
    def simple_rob(nums):
        prev, curr = 0, 0
        for num in nums:
            prev, curr = curr, max(prev + num, curr)
        return curr
    
    # If there is only one house, return its value
    if len(nums) == 1:
        return nums[0]
    
    # If there are more than one house, consider two cases:
    # 1. Rob the first house and exclude the last house.
    # 2. Exclude the first house and consider the last house.
    return max(simple_rob(nums[1:]), simple_rob(nums[:-1]))

# Example usage:
print(rob([2,3,2]))  # Output: 3
print(rob([1,2,3,1]))  # Output: 4
print(rob([1,2,3]))  # Output: 3

################################################################################
#solution 3:

def rob(nums):
    def simple_rob(nums):
        prev, curr = 0, 0
        for num in nums:
            prev, curr = curr, max(prev + num, curr)
        return curr
    
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums[0], nums[1])
    else:
        # Rob houses from 1 to n-1
        max1 = simple_rob(nums[:-1])
        
        # Rob houses from 2 to n
        max2 = simple_rob(nums[1:])
        
        # Return the maximum of the two scenarios
        return max(max1, max2)

# Example usage:
print(rob([2, 3, 2]))  # Output: 3
print(rob([1, 2, 3, 1]))  # Output: 4
print(rob([1, 2, 3]))  # Output: 3
