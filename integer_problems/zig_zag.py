'''

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"

'''

#solution 1

class Solution:
    def convert(self, s, numRows):
        if numRows == 0 or numRows ==1:
            return s
        res = ""
        for row in range(numRows):
            increment = (numRows-1)*2
            for i in range(row,len(s),increment):
                res += s[i]
                if row >0 and row < numRows-1 and (i+increment-row*2) < len(s):
                    res += s[i+increment-row*2]
        return res
    
    
################################################################################

#slution2

class Solution2():
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 0 or numRows ==1:
            return s
        rows = [''] * min(numRows, len(s))
        print(rows)
        current_row = 0
        going_down = False

        for char in s:
            rows[current_row] += char

            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            current_row += 1 if going_down else -1

        result = ''.join(rows)
        return result

v = Solution2()
v.convert("appugowda",4)