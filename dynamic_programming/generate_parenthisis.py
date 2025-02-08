'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

'''

########################################################

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        res = []

        def backtracking(open,close):
            if open==close==n:
                res.append(''.join(stack))
                return res
            if open < n:
                stack.append('(')
                backtracking(open+1,close)
                stack.pop()
            if close < open:
                stack.append(')')
                backtracking(open,close+1)
                stack.pop()
            
        backtracking(0,0)
        return res
        
        
#####################################################

def generate_parentheses(n):
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    result = []
    backtrack('', 0, 0)
    return result

# Example usage:
n1 = 3
print(generate_parentheses(n1))  # Output: ["((()))","(()())","(())()","()(())","()()()"]

n2 = 1
print(generate_parentheses(n2))  # Output: ["()"]
