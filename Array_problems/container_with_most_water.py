'''
User
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
'''

#solution 1:

#brute force method

def max_area_brute_force(height):
    max_water = 0
    n = len(height)

    for i in range(n):
        for j in range(i + 1, n):
            # Calculate the current water container area for the pair (i, j)
            current_water = min(height[i], height[j]) * (j - i)
            max_water = max(max_water, current_water)

    return max_water

# Example usage:
height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area_brute_force(height1))  # Output: 49

height2 = [1, 1]
print(max_area_brute_force(height2))  # Output: 1


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#solution 2:

def maxArea(height):
    max_area = 0
    left = 0
    right = len(height) - 1
    
    while left < right:
        # Calculate the current area
        current_area = min(height[left], height[right]) * (right - left)
        # Update max_area if the current_area is greater
        max_area = max(max_area, current_area)
        
        # Move the pointers towards the center
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

# Test cases
height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height1))  # Output: 49

height2 = [1, 1]
print(maxArea(height2))  # Output: 1


