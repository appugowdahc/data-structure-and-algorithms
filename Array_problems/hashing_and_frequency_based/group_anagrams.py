"""

Code
Testcase
Testcase
Test Result
49. Group Anagrams
Solved
Medium
Topics
Companies
Given an array of strings strs, group the 
anagrams
 together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]
"""

from typing import List

######## brute force approach
#Time Complexity Analysis
# Sorting each string takes O(m log m) (where m is the length of the string).
# Comparing each string against others takes O(n²).
# Overall Complexity: O(n² * m log m) (inefficient for large n).

from collections import Counter,defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        seen = [False] * len(strs)

        for i in range(len(strs)):
            if seen[i]: 
                continue
            anagram_group = [strs[i]]
            seen[i] = True

            for j in range(i + 1, len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    anagram_group.append(strs[j])
                    seen[j] = True

            res.append(anagram_group)

        return res


############# optimal solution
#Optimal Approach: Using HashMap (O(n * m log m))
# Sort each string and use it as a key in a hashmap.
# Group words with the same sorted key.

from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            anagrams[sorted_word].append(word)

        return list(anagrams.values())

        
        