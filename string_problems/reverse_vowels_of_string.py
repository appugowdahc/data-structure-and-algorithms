"""
345. Reverse Vowels of a String
Solved
Easy
Topics
Companies
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = set(["a","e","i","o","u"])
        s = list(s)
        left = 0
        right = len(s)-1
        while left < right:
            
            while left<right and  s[left].lower() not in vowels:
                left += 1
            while right > left and s[right].lower() not in vowels:
                right -= 1
            s[left],s[right]=s[right],s[left]
            left += 1
            right -= 1     
        return ''.join(s)