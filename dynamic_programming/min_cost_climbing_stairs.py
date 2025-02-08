'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.


'''

#Solution 1:

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost)-3,-1,-1):
            cost[i] += min(cost[i+1],cost[i+2])
        return min(cost[0],cost[1])
    
##########################################################

#Solution 2:

def minCostClimbingStairs(cost):
    n = len(cost)
    
    # Initialize an array to store the minimum cost to reach each step
    dp = [0] * n
    
    # Base cases
    dp[0] = cost[0]
    dp[1] = cost[1]
    
    # Iterate from step 2 to n-1, calculating the minimum cost for each step
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    
    # The minimum cost to reach the top is the minimum of the last two steps
    return min(dp[-1], dp[-2])

# Example usage:
print(minCostClimbingStairs([10,15,20]))  # Output: 15
print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))  # Output: 6


#######################################################################

#Solution 3:

def minCostClimbingStairs(cost):
    n = len(cost)
    
    # Create an array to store the minimum cost to reach each step
    min_cost = [0] * n
    
    # Set the base cases for the first two steps
    min_cost[0] = cost[0]
    min_cost[1] = cost[1]
    
    # Iterate from the third step to the top, calculating the minimum cost for each step
    for i in range(2, n):
        min_cost[i] = cost[i] + min(min_cost[i - 1], min_cost[i - 2])
    
    # The minimum cost to reach the top is the minimum of the costs of the last two steps
    return min(min_cost[-1], min_cost[-2])

# Example usage:
print(minCostClimbingStairs([10,15,20]))  # Output: 15
print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))  # Output: 6
