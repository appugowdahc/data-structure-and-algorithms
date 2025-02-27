"""
557. Reverse Words in a String III
Solved
Easy
Topics
Companies
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"

"""

class Solution:
    def reverseWords(self, s: str) -> str:
        list_words = s.split(' ')
        res =""
        res += list_words[0][::-1]
        for i in range(1,len(list_words)):
            res += f" {list_words[i][::-1]}"
        return res