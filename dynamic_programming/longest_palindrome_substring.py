'''
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

'''

#solution 1:

def longestPalindrome(s):
        res = ""
        max_len = 0
        for i in range(len(s)):

            #this will work for odd length
            left,right = i,i
            while left >=0 and right < len(s) and s[left] == s[right]:
                if (right - left +1) > max_len:
                    res = s[left:right+1]
                    max_len = right - left +1
                left -=1
                right +=1
            print(res)
            
            #this will work for even length
            left,right = i,i+1
            while left >= 0 and right <len(s) and s[left] == s[right]:
                if (right-left+1) > max_len:
                    res = s[left:right+1]
                    max_len = right -left +1


                left -= 1
                right +=1

        return res

print(longestPalindrome('bab'))


######################################################


#solution 2:

def longest_palindromic_substring(s):
    if not s:
        return ""
    
    n = len(s)
    start = 0
    max_len = 1
    
    # Create a table to store if substrings are palindromes
    dp = [[False] * n for _ in range(n)]
    
    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True
    
    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2
    
    # Check for substrings of length greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_len = length
    
    return s[start:start + max_len]

# Test cases
s1 = "babad"
print(longest_palindromic_substring(s1))  # Output: "bab" or "aba"

s2 = "cbbd"
print(longest_palindromic_substring(s2))  # Output: "bb"

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#solution 3:

