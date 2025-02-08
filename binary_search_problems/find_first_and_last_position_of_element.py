class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # if not target or not nums:
        #     return [-1,-1]
        
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right)//2
            print(mid)
            if nums[mid] == target:
                res = [mid,mid]
                i = mid+1
                while i < len(nums) and nums[i] == target:
                    res[1] = i
                    i+= 1
                j = mid -1
                while j >= 0 and nums[j] == target:
                    res[0] = j
                    j -= 1
                return res
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        return [-1,-1]
        
###########################################

def searchRange(nums, target):
    def findFirst(nums, target):
        left, right = 0, len(nums) - 1
        first = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                first = mid
                right = mid - 1  # Keep searching in the left half
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return first

    def findLast(nums, target):
        left, right = 0, len(nums) - 1
        last = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                last = mid
                left = mid + 1  # Keep searching in the right half
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return last

    first = findFirst(nums, target)
    if first == -1:  # Target not found
        return [-1, -1]
    
    last = findLast(nums, target)
    return [first, last]

# Example usage
print(searchRange([5, 7, 7, 8, 8, 10], 8))  # Output: [3, 4]
print(searchRange([5, 7, 7, 8, 8, 10], 6))  # Output: [-1, -1]
print(searchRange([], 0))                   # Output: [-1, -1]
