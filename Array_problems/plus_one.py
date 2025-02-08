"""

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

"""
from typing import List
########################my solution
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        res = []
        digits[-1] =digits[-1] +1
        if digits[-1] <= 9:
            return digits
        carry = 0
        while i >= 0:
            val = (digits[i]+carry)%10
            carry = (digits[i]+carry)//10
            res.append(val)
            i -=1

        if carry:
            res.append(carry)
        res.reverse()
        return res
    
    
#################### brute force approach
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = int("".join(map(str,digits)))
        nums += 1
        res = [int(num) for num in str(nums)]
        return res

############# optimal solution
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
    
        for i in range(n - 1, -1, -1):  # Start from last digit
            if digits[i] < 9:
                digits[i] += 1
                return digits  # No carry, return result
            digits[i] = 0  # If 9, set to 0 and continue
        
        return [1] + digits  # If all digits were 9, add a leading 1
        
        