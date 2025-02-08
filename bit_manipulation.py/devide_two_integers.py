def divide(dividend: int, divisor: int) -> int:
    # Constants for the 32-bit signed integer range
    MAX_INT = 2**31 - 1
    MIN_INT = -2**31
    
    # Edge case: if divisor is 0, return MAX_INT
    if divisor == 0:
        return MAX_INT
    
    # Edge case: if dividend is 0, the result is 0
    if dividend == 0:
        return 0
    
    # Edge case: handle overflow
    if dividend == MIN_INT and divisor == -1:
        return MAX_INT
    
    # Determine the sign of the result
    negative = (dividend < 0) ^  (divisor < 0)
    print(negative)
    
    # Work with positive values for simplicity
    dividend = abs(dividend)
    divisor = abs(divisor)
    
    quotient = 0
    # Count the number of times we can subtract the divisor from the dividend
    while dividend >= divisor:
        temp = divisor
        multiple = 1
        # Double the divisor until it is greater than the dividend
        while dividend >= (temp << 1):
            temp <<= 1
            multiple <<= 1
        # Subtract the largest multiple of divisor
        dividend -= temp
        quotient += multiple
    
    # Apply the sign to the result
    if negative:
        quotient = -quotient
    
    # Ensure the result is within the 32-bit signed integer range
    return max(MIN_INT, min(MAX_INT, quotient))

# Example usage:
dividend = 10
divisor = 3
print(divide(dividend, divisor))  # Output: 3

dividend = -7
divisor = -3
print(divide(dividend, divisor))  # Output: -2
