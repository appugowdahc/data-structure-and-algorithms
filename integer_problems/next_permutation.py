################### brute force approach

def generate_permutations(nums):
    def backtrack(first=0):
        if first == len(nums):
            result.append(nums[:])
        for i in range(first, len(nums)):
            nums[first], nums[i] = nums[i], nums[first]  # Swap
            backtrack(first + 1)  # Recurse
            nums[first], nums[i] = nums[i], nums[first]  # Backtrack

    result = []
    backtrack()
    print(result)
    exit(1)
    return result

def nextPermutation(nums):
    # Step 1: Generate all permutations
    all_permutations = generate_permutations(nums)
    
    # Step 2: Sort the permutations lexicographically
    all_permutations.sort()
    
    # Step 3: Find the index of the current permutation
    for i, perm in enumerate(all_permutations):
        if perm == nums:
            break
    
    # Step 4: Find the next permutation
    if i + 1 < len(all_permutations):
        next_perm = all_permutations[i + 1]
    else:
        next_perm = all_permutations[0]  # Wrap around to the first permutation
    
    # Step 5: Modify the input list in place
    nums[:] = next_perm

# Example usage:
nums = [1, 2, 3]
nextPermutation(nums)
print(nums)  # Output: [1, 3, 2]




####################### optimize solution 

def nextPermutation(nums):
    n = len(nums)
    i = n - 2
    
    # Step 1: Find the pivot
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    
    if i >= 0:
        # Step 2: Find the successor
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        # Step 3: Swap pivot and successor
        nums[i], nums[j] = nums[j], nums[i]
    
    # Step 4: Reverse the suffix
    nums[i + 1:] = reversed(nums[i + 1:])


#####################################

def nextPermutation(nums):
    # Step 1: Find the first decreasing element from the end
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    # Step 2: If such an element was found, find the element to swap with
    if i >= 0:
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        # Step 3: Swap the elements
        nums[i], nums[j] = nums[j], nums[i]

    # Step 4: Reverse the suffix
    nums[i + 1:] = reversed(nums[i + 1:])

# Example usage:
nums = [1, 2, 3]
nextPermutation(nums)
print(nums)  # Output: [1, 3, 2]
