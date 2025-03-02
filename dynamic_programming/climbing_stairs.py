'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

'''
#solution 1:


class Solution:
    def climbStairs(self, n: int) -> int:
        first,second = 1,1
        for i in range(n-1):
            tmp = first 
            first = first + second
            second = tmp
        return first
    
##############################################################################
#solution 2:
def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # Initialize an array to store the number of ways to reach each step
    ways = [0] * (n + 1)
    ways[1] = 1
    ways[2] = 2
    
    # Iterate from step 3 to n, calculating the number of ways for each step
    for i in range(3, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]
    
    return ways[n]

# Example usage:
print(climbStairs(2))  # Output: 2
print(climbStairs(3))  # Output: 3

