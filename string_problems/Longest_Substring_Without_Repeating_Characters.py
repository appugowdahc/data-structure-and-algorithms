class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        char_set = set()
        res = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            res = max(res,right-left+1)
        return res
    
    
    
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