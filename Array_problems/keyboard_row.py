"""

500. Keyboard Row
Solved
Easy
Topics
Companies
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

 

Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]

Output: ["Alaska","Dad"]

Explanation:

Both "a" and "A" are in the 2nd row of the American keyboard due to case insensitivity.

Example 2:

Input: words = ["omk"]

Output: []

Example 3:

Input: words = ["adsdf","sfd"]

Output: ["adsdf","sfd"]


    
"""

from typing import List
################brute force approach 

# but this will fail for like e.g "llllllllll","ddddddddd"

def findWordsBruteForce(words):
    row1 = set("qwertyuiop")
    row2 = set("asdfghjkl")
    row3 = set("zxcvbnm")
    
    result = []
    
    for word in words:
        lower_word = set(word.lower())  # Convert to lowercase and create a set of letters
        if lower_word <= row1 or lower_word <= row2 or lower_word <= row3:
            result.append(word)
    
    return result

# Test Cases
print(findWordsBruteForce(["Hello", "Alaska", "Dad", "Peace"]))  # Output: ["Alaska", "Dad"]
print(findWordsBruteForce(["omk"]))  # Output: []
print(findWordsBruteForce(["adsdf", "sfd"]))  # Output: ["adsdf", "sfd"]



########### optimal solution 

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        d = {}
        for char in "qwertyuiop":
            d[char] = 1
        for char in "asdfghjkl":
            d[char] = 2
        for char in "zxcvbnm":
            d[char] = 3
        res = []
        for word1 in words:
            word = set(word1.lower())
            words_set = set()
            for letter in word:
                words_set.add(d[letter])
            if len(words_set) == 1:
                res.append(word1)
        return res
        