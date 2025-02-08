''''

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21

'''
# solution 1

def reverse_integer(x):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    if x >= 0:
        reversed_x = int(str(x)[::-1])
    else:
        reversed_x = -int(str(-x)[::-1])

    if reversed_x not in range(INT_MIN, INT_MAX):
        return 0
    else:
        return reversed_x

# Example 1
x1 = 123
print(reverse_integer(x1))  # Output: 321

# Example 2
x2 = -123
print(reverse_integer(x2))  # Output: -321

# Example 3
x3 = 120
print(reverse_integer(x3))  # Output: 21

################################################

#solution 2

def reverse_integer(x):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    # Handling negative numbers
    sign = -1 if x < 0 else 1
    x = abs(x)
    
    reversed_num = 0
    while x != 0:
        # Get the last digit
        digit = x % 10
        
        # Check for overflow before adding the new digit
        if reversed_num > (INT_MAX - digit) // 10:
            return 0
        
        reversed_num = reversed_num * 10 + digit
        x //= 10

    return reversed_num * sign

# Example cases
print(reverse_integer(123))    # Output: 321
print(reverse_integer(-123))   # Output: -321
print(reverse_integer(120))    # Output: 21

############################################
# solution 3

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x = x*-1
        res  = 0
        while x > 0:
            val = x % 10
            res = res*10 + val 
            x = x//10
        if res < -2**31 or res > 2**31 -1:
            return 0
        return res*sign