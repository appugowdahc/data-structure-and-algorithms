'''
Explanation:
Initialization:

index: to track the current position in the string.
n: the length of the string.
sign: to store the sign of the number (1 for positive, -1 for negative).
result: to store the resultant integer.
INT_MAX and INT_MIN: to store the 32-bit signed integer range.
Ignore Leading Whitespace:

Iterate through the string until we encounter a non-whitespace character.
Check for Optional Sign:

If the current character is '+' or '-', set the sign variable accordingly and 
move to the next character.

Convert Digits to Integer:

Loop through the string and convert each digit character to an integer.
Before updating result, check for overflow. If result is about to exceed the 32-bit 
range, return the appropriate boundary value (INT_MAX or INT_MIN).
Return the Final Result:

Multiply the result by the sign and return it.
This implementation ensures that the function adheres to the specified constraints and 
handles edge cases, including leading/trailing spaces, signs, and non-digit characters, 
appropriately.
'''

class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        l = len(s)
        sign = 1
        i = 0
        while  i<l and (s[i] == ' ' or s[i] in ['-','+']):
            if s[i] in ['-','+']:
                sign =-1 if s[i]=='-'else 1
                i += 1
                break
            i
        
            i+=1
        while i < l:
            if s[i].isdigit():
                res =res*10+ int(s[i])
            else:
                break
            i += 1
        res = res *sign
        if res < -2**31:
            return -2**31
        if res > 2147483647:
            return 2**31-1
        return res




#################################
def myAtoi(s: str) -> int:
    # Initialize variables
    index = 0
    n = len(s)
    sign = 1
    result = 0
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    # Step 1: Ignore leading whitespace
    while index < n and s[index].isspace():
        index += 1

    # Step 2: Check for optional sign
    if index < n and (s[index] == '+' or s[index] == '-'):
        sign = -1 if s[index] == '-' else 1
        index += 1

    # Step 3: Convert digits to integer
    while index < n and s[index].isdigit():
        digit = int(s[index]) 

        # Check for overflow and underflow conditions
        if result > (INT_MAX - digit) // 10:
            return INT_MIN if sign == -1 else INT_MAX

        result = result * 10 + digit
        index += 1

    return sign * result

# Example usage
print(myAtoi("42"))           # Output: 42
print(myAtoi("+-42"))       # Output: -42
print(myAtoi("4193 with words"))  # Output: 4193
print(myAtoi("words and 987"))    # Output: 0
print(myAtoi("-91283472332"))     # Output: -2147483648
