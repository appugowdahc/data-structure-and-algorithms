'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

 

Example 1:

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.
Example 2:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 3:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

'''


# solution 1

class Solution:
    def intToRoman(self, num: int) -> str:
        data = [['I',1],['IV',4],['V',5],['IX',9],['X',10],['XL',40],['L',50],['XC',90],['C',100],['CD',400],['D',500],['CM',900],['M',1000]]
        res = ""
        
        for char,value in reversed(data):
            
            #just check num devide value equal to one or dont add this character
            if num // value:
                #how many time it can multiply or divisible that many time we should use this num
                no_times = num//value
                res += char*no_times
                num = num%value
        return res
    
    
###################################################################

#solution 2



def int_to_roman(num):
    # Define the symbols and their corresponding values
    symbols = [
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1)
    ]

    # Initialize an empty string to store the result
    result = ""

    # Iterate through the symbols
    for symbol, value in symbols:
        # Repeat the symbol as many times as possible
        while num >= value:
            result += symbol
            num -= value

    return result

# Test cases
print(int_to_roman(3))    # Output: "III"
print(int_to_roman(58))   # Output: "LVIII"
print(int_to_roman(1994)) # Output: "MCMXCIV"

#####################################################

#solution 3

def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

# Test cases
print(int_to_roman(3))     # Output: "III"
print(int_to_roman(58))    # Output: "LVIII"
print(int_to_roman(1994))  # Output: "MCMXCIV"
