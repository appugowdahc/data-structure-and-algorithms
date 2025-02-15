# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# This is my solution
def findMedianSortedArrays(nums1,nums2):
    i = 0
    j = 0
    k = 0
    arr = [0]*(len(nums1)+len(nums2))
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            arr[k] = nums1[i]
            i += 1
        else:
            arr[k] = nums2[j]
            j += 1
        k += 1
    while i < len(nums1):
        arr[k] = nums1[i]
        i += 1
        k +=1
    while j < len(nums2):
        arr[k] = nums2[j]
        j += 1
        k +=1
    if len(arr)%2 == 0:
        a = len(arr)//2
        val = (arr[a-1]+arr[a])/2
        return val
    else:
        return arr[(len(arr)//2)]/1

a1 = [[1,3],[0],[1,2,3,4]]
a2 = [[2],[],[5,6,7,8]]
# for i in range(len(a1)): 
#     print(findMedianSortedArrays(a1[i],a2[i]))
    
#T

def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1  # Ensure nums1 is the smaller array

    m, n = len(nums1), len(nums2)
    total_length = m + n
    half_length = (total_length + 1) // 2

    left, right = 0, m  # Binary search bounds for nums1

    while left < right:
        i = left + (right - left) // 2
        j = half_length - i-1
        print(nums1,nums2)
        print(i,j)
        if nums1[i] <= nums2[j] and nums2[j - 1] <= nums1[i]:
            # Found the correct median(s)
            max_of_left = max(nums1[i - 1] if i > 0 else float('-inf'), nums2[j - 1] if j > 0 else float('-inf'))
            min_of_right = min(nums1[i], nums2[j])
            if total_length % 2 == 0:
                # If total_length is even, return the average of two elements
                
                return (max_of_left + min_of_right) / 2.0
            else:
                # If total_length is odd, return the middle element
                return float(min_of_right)

        elif nums1[i] > nums2[j]:
            # Move left in nums1
            right = i
        else:
            # Move right in nums1
            left = i + 1

    # If we reach this point, it means one of the arrays is exhausted
    # Handle the remaining elements in nums2
    i = left
    j = half_length - left
    max_of_left = max(nums1[i - 1] if i > 0 else float('-inf'), nums2[j - 1] if j > 0 else float('-inf'))
    min_of_right = min(nums1[i] if i < m else float('inf'), nums2[j] if j < n else float('inf'))

    if total_length % 2 == 0:
        return (max_of_left + min_of_right) / 2.0
    else:
        return float(min_of_right)

# Example usage:
nums1 = [1]
nums2 = []
result = findMedianSortedArrays(nums1, nums2)
print(result)  # Output: 2.0


