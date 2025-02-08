


###########################
class Solution:
    def firstMissingPositive(self, nums) -> int:
        n = len(nums)
        
        # Place each number in its right place
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with nums[nums[i] - 1]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # Find the first index where the index + 1 is not the value at that index
        for i in range(n):
            if nums[i] != i + 1:
                print(nums)
                return i + 1
        
        # If all values are in place, the first missing positive is n + 1
        return n + 1
s = Solution()
print(s.firstMissingPositive([5,4,1,5,4]))