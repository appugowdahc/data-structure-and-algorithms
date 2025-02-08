
# This is my solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0
        i = 0
        j = 0
        short = ""
        while j < len(s):
            if s[j] not in short:
                short += s[j]
            else:
                max_l = max(max_l,len(short))
                short = ""
                j = i
                i += 1
                short += s[j]
            j += 1
        max_l =max(max_l,len(short))
        return max_l
    
    
# This is Other solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 1 
        sub_str ='' 
        if(len(s)<=0):
            return 0  
        if(len(s)==1):
            return 1
        sub_str += s[0]
        left = 0
        right = 1 
        while(left<len(s) and right<len(s)):
            if right<len(s) and s[right] not in sub_str:
                sub_str += s[right]
                right += 1
                result = max(result,len(sub_str))
            
            else:
                result = max(result,len(sub_str))
                sub_str = ''
                right = left+2
                left += 1
                sub_str += s[left]
            
        return (result)