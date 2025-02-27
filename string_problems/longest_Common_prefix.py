"""

Code


Testcase
Testcase
Test Result
14. Longest Common Prefix
Solved
Easy
Topics
Companies
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        shortest_str = min(strs,key=len)

        res = ""

        for i in range(len(shortest_str)):
            for word in strs:
                if word[:i+1] != shortest_str[:i+1]:
                    return res
            res += shortest_str[i]
        return res
        