def countAndSay(n):
    if n == 1:
        return "1"
    
    def next_sequence(s):
        result = []
        i = 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1
            result.append(f"{count}{s[i]}")
            i += 1
        return "".join(result)
    
    current_seq = "1"
    for i in range(2, n + 1):
        current_seq = next_sequence(current_seq)
    
    return current_seq

# Example usage:
# print(countAndSay(4))  # Output: "1211"
# print(countAndSay(1))  # Output: "1"


##########################
class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        if n==1:
            return res
        # import pdb;pdb.set_trace()
        while  n >1:
            i = 0
            tmp = ""
            while i < len(res):
                count = 1
                char = res[i]
                while i+1 <len(res) and res[i]==res[i+1]:
                    count +=1
                    i+= 1
                i+=1
                tmp+=f"{str(count)}{char}"
            
            res = tmp
            n -= 1

        return res


s = Solution()
print(s.countAndSay(5))


        