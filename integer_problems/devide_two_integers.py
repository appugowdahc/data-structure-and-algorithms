class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Handle edge cases
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Get the sign of the result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        # Convert dividend and divisor to positive integers
        dividend, divisor = abs(dividend), abs(divisor)
        
        # Initialize quotient
        quotient = 0
        
        # Keep subtracting divisor from dividend until dividend becomes less than divisor
        while dividend >= divisor:
            # Initialize the number of times we can subtract divisor
            multiple = 1
            temp = divisor
            
            # Check if we can subtract multiple * divisor from dividend
            # while keeping the result positive
            while dividend >= temp << 1:
                temp <<= 1
                multiple <<= 1
                
            # Subtract multiple * divisor from dividend
            dividend -= temp
            # Add multiple to quotient
            quotient += multiple
        
        # Apply the sign to the quotient
        return sign * quotient
