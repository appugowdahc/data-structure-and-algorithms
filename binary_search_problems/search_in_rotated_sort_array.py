class Solution:
    def search(self, nums, target) :

        left, right = 0, len(nums) - 1
    
        while left <= right:
            mid = (left + right) // 2
            print(mid)
            if nums[mid] == target:
                return mid
            
            # Check if the left half is sorted
            if nums[left] <= nums[mid]:
                # Check if target is in the left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # The right half must be sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1

        
        
ll = Solution()
print(ll.search([3,1],1))