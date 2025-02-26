"""
451. Sort Characters By Frequency
Solved
Medium
Topics
Companies
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""
from typing import List 

###### optimal solution O(nlogn)
from collections import Counter,defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:

        char_dict = Counter(s) ## this will take O(n) to format the dict
        # d = defaultdict(list)
        # for char in s:
        #     d[char].append(char)
        res = sorted(char_dict.keys(),key=lambda x : -char_dict[x]) ## this will take O(nlogn)
        r = ""
        for char in res:
            r+= char * char_dict[char]
        return r

##### optimal solution2 O(nlogk)
import heapq
from collections import Counter

def frequencySort(s: str) -> str:
    freq_map = Counter(s)
    max_heap = [(-freq, char) for char, freq in freq_map.items()]  # Max heap (negative frequencies)
    heapq.heapify(max_heap)  # Convert list into a heap

    result = []
    while max_heap:
        freq, char = heapq.heappop(max_heap)  # Extract max frequency
        result.append(char * -freq)  # Append char `-freq` times

    return ''.join(result)

# Test Cases
print(frequencySort("tree"))  # Output: "eert" or "eetr"
print(frequencySort("cccaaa"))  # Output: "aaaccc" or "cccaaa"
print(frequencySort("Aabb"))  # Output: "bbAa" or "bbaA"


        