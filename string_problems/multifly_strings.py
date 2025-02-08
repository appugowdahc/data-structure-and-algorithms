class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        
        # Reverse both numbers to facilitate the multiplication from least significant digit
        num1, num2 = num1[::-1], num2[::-1]
        
        # Multiply each digit from num1 with each digit from num2
        for i in range(m):
            for j in range(n):
                product = int(num1[i]) * int(num2[j])
                result[i + j] += product
                # Handle carry over to the next position
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10
        print(result)
        # The result array might have leading zeros that we need to skip
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        
        # Convert result to string and return
        return ''.join(map(str, result[::-1]))
a = Solution()
print(a.multiply("5638","456"))
###########################################

def karatsuba_multiply(num1: str, num2: str) -> str:
    if len(num1) == 1 or len(num2) == 1:
        return str(int(num1) * int(num2))
    
    m = min(len(num1), len(num2)) // 2
    
    high1, low1 = num1[:-m], num1[-m:]
    high2, low2 = num2[:-m], num2[-m:]
    
    # Recursively compute three products
    z0 = karatsuba_multiply(low1, low2)
    z1 = karatsuba_multiply(str(int(low1) + int(high1)), str(int(low2) + int(high2)))
    z2 = karatsuba_multiply(high1, high2)
    
    # Combine the results using Karatsuba's formula
    product = int(z2) * 10**(2 * m) + (int(z1) - int(z2) - int(z0)) * 10**m + int(z0)
    
    return str(product)

# Example usage:
print(karatsuba_multiply("123", "456"))  # Output: "56088"
