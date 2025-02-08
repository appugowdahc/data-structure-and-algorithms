'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
'''



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeBrackets = { ')':'(','}':'{',']':'['
        }
        for i in range(len(s)):
            if s[i] in closeBrackets:
                if stack and  closeBrackets[s[i]] ==  stack[-1]:
                    stack.pop()
                else:
                    print(stack)
                    return False
            else:
                stack.append(s[i])
                
        return True if not stack else False