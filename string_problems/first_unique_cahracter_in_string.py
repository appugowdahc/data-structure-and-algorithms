"""

387. First Unique Character in a String
Solved
Easy
Topics
Companies
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1

"""

from typing import List

############### brute force
from collections import Counter,defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        letter_set = set()
        for index, char in enumerate(s):
            if char in letter_set:
                continue
            if index == len(s)-1:
                return index
            found = False
            for i in range(index+1,len(s)):
                if s[i] == char:
                    letter_set.add(char)
                    found = True
                    break
            if not found:
                return index
        return -1
        
############### optimal solution
from collections import Counter,defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        letter_map = Counter(s)
        for char,occurance in letter_map.items():
            if occurance == 1:
                return s.index(char)

        return -1
        