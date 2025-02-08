
################# brute force method

def isValid(s):
    balance = 0
    for char in s:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance < 0:
            return False
    return balance == 0

def longestValidParentheses(s):
    max_length = 0
    n = len(s)

    # Step 1: Generate all possible substrings
    for i in range(n):
        for j in range(i + 2, n + 1, 2):  # Consider substrings of even length only
            # Step 2: Check if the substring is valid
            if isValid(s[i:j]):
                # Step 3: Track the longest valid substring
                max_length = max(max_length, j - i)

    return max_length

# Example usage:
print(longestValidParentheses("(()"))       # Output: 2
print(longestValidParentheses(")()())"))    # Output: 4
print(longestValidParentheses(""))          # Output: 0




##############################33 optimized solution #####################
def longestValidParentheses(s):
    stack = [-1]
    max_length = 0

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if stack:
                max_length = max(max_length, i - stack[-1])
            else:
                stack.append(i)

    return max_length
####################### dynamic programming

def longestValidParentheses(s):
    n = len(s)
    dp = [0] * n
    max_length = 0

    for i in range(1, n):
        if s[i] == ')':
            if s[i - 1] == '(':
                dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
            elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) + 2
            max_length = max(max_length, dp[i])

    return max_length

# Example usage:
print(longestValidParentheses("(()"))       # Output: 2
print(longestValidParentheses(")()())"))    # Output: 4
print(longestValidParentheses(""))          # Output: 0


# Example usage:
print(longestValidParentheses("(()"))       # Output: 2
print(longestValidParentheses(")()())"))    # Output: 4
print(longestValidParentheses(""))          # Output: 0
