
"""Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

Explanation:
Initialization:

left and right pointers are initialized to the start and end of the list, respectively.
Binary Search Loop:

The loop continues as long as left is less than or equal to right.
Calculate the middle index mid.
If the middle element nums[mid] is equal to the target, return mid (target found).
If nums[mid] is less than the target, move the left pointer to mid + 1 (search in the right half).
If nums[mid] is greater than the target, move the right pointer to mid - 1 (search in the left half).
Return the Insertion Point:

If the target is not found, left will be the insertion point where the target should be placed to maintain the sorted order.
This method ensures an 

)
O(logn) runtime complexity by using binary search, making it efficient for large input arrays.

"""

def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left

# Example usage
print(searchInsert([1, 3, 5, 6], 5))  # Output: 2
print(searchInsert([1, 3, 5, 6], 2))  # Output: 1
print(searchInsert([1, 3, 5, 6], 7))  # Output: 4
print(searchInsert([1, 3, 5, 6], 0))  # Output: 0

############################################

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1] < target:
            return len(nums)
        if nums[0] > target:
            return 0
        
        left = 0
        right = len(nums)-1


        while left<= right:
            mid = (left + right)//2

            if nums[mid] ==  target:
                return mid
            if mid+1 < len(nums) and (nums[mid] < target < nums[mid+1]):
                return mid+1
            if mid-1 >=0 and (nums[mid-1] < target < nums[mid]):
                return mid

            if nums[mid] < target:
                left = mid +1
            else:
                right = mid -1
        return -1 
            
            
        
