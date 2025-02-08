'''
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
'''
############################################################
#solution 1

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True

        # Mark patterns like "a*" or ".*" where * matches zero characters
        for i in range(1, len(p) + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]

        # Fill the DP table based on the matching conditions
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
        
        return dp[len(s)][len(p)]
    
    
    
################################################################

class Solution:
    
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        def DFS(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i>= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            match = i < len(s) and ((s[i] == p[j]) or (p[j] =='.'))

            if (j+1)< len(p) and p[j+1] == '*':
                cache[(i,j)] =  DFS(i,j+2) or (match and DFS(i+1,j))
                return cache[(i,j)]
            if match:
                cache[(i,j)] =  DFS(i+1,j+1)
                return cache[(i,j)]
            cache[(i,j)] = False
            return False
        return DFS(0,0)