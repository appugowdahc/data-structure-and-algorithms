'''

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

'''

#solution 1:

class Solution:
    def rob(self, nums):
        first_rob,second_rob = 0,0
        for current_rob in nums:
            max_rob = max(first_rob+current_rob,second_rob)
            first_rob = second_rob
            second_rob = max_rob

        return second_rob


#########################################################

#solution 2:

def rob(nums):
    if not nums:
        return 0
    
    n = len(nums)
    
    # Initialize two variables to keep track of the maximum amount robbed
    prev_robbed = 0  # Maximum amount robbed when the previous house was robbed
    prev_skipped = 0  # Maximum amount robbed when the previous house was skipped
    
    # Iterate through the houses and update the variables
    for num in nums:
        current_robbed = prev_skipped + num  # Rob the current house
        current_skipped = max(prev_robbed, prev_skipped)  # Skip the current house
        
        # Update variables for the next iteration
        prev_robbed = current_robbed
        prev_skipped = current_skipped
    
    # The final result is the maximum of the two scenarios: robbing the last house or skipping it
    return max(prev_robbed, prev_skipped)

# Example usage:
print(rob([1, 2, 3, 1]))  # Output: 4
print(rob([2, 7, 9, 3, 1]))  # Output: 12


#########################################################
#solution 3

def rob(nums):
    if not nums:
        return 0
    
    n = len(nums)
    
    if n == 1:
        return nums[0]
    
    # Initialize variables for robbing or skipping the first house
    include_first = nums[0]
    exclude_first = 0
    
    # Iterate from the second house to the last
    for i in range(1, n):
        # Calculate the new values for including or excluding the current house
        new_include = exclude_first + nums[i]
        new_exclude = max(include_first, exclude_first)
        
        # Update the variables for the next iteration
        include_first = new_include
        exclude_first = new_exclude
    
    # Return the maximum amount after considering all houses
    return max(include_first, exclude_first)

# Example usage:
print(rob([1, 2, 3, 1]))  # Output: 4
print(rob([2, 7, 9, 3, 1]))  # Output: 12
