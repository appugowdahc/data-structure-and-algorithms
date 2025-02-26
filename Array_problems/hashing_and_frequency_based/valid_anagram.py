"""
242. Valid Anagram
Solved
Easy
Topics
Companies
Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false


"""

from typing import List

####brute force O(nlogn)
def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

#######optimal solution
from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

# Example Test Cases
print(isAnagram("anagram", "nagaram"))  # Output: True
print(isAnagram("rat", "car"))  # Output: False
##########optimal solution 2
from collections import Counter,defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        for char in s:
            s_dict[char] += 1
        
        t_dict=defaultdict(int)
        for char in t:
            t_dict[char] +=1
        
        for char in set(s+t):
            if t_dict[char] != s_dict[char]:
                return False
        return True