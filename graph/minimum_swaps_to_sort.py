"""

To solve the problem of finding the minimum number of swaps required to sort an 
array, we can leverage the idea of cycle decomposition of a graph. Here's a 
step-by-step approach:

Approach:

Understanding the problem as a graph problem:

Think of the array as a graph where each element points to its correct position in 
the sorted array.
Each cycle in this "graph" represents a group of elements that need to be cyclically 
permuted in order to get them to their correct positions.
The number of swaps needed to sort each cycle of size k is k - 1. So, for each cycle, 
the number of swaps is the size of the cycle minus one.

Steps:

Create an array of pairs where each pair consists of the value of the element and its 
original index in the array.
Sort this array of pairs based on the values of the elements.
Using the sorted array, detect cycles in the array by checking if elements are 
already in their correct position. If not, track the cycle, and count the number of 
swaps needed for that cycle.
"""
"""

Explanation:

Create an array of pairs:

The array arrpos stores tuples where each tuple contains an element from the input 
array nums and its corresponding index.
Sort the array based on values:

The array is sorted by the values of the elements. This gives us a reference for where 
each element should be in the sorted array.

Cycle detection and counting swaps:

We use a visited array to keep track of which elements have already been processed.
For each unvisited element, we trace a cycle in the "graph" (represented by the original
indices and their positions in the sorted array).
The number of swaps needed to sort the elements in a cycle is equal to the length of 
the cycle minus 1.

Counting the swaps:

For each cycle of size k, k - 1 swaps are required. Hence, we accumulate this in the 
swaps variable.
"""
class Solution:
    def minSwaps(self, nums=[3,4,2,1]):
        # Create a list of tuples where each tuple contains the element and its index
        n = len(nums)
        arrpos = [(nums[i], i) for i in range(n)]
        
        # Sort the array based on the values of the elements
        arrpos.sort(key=lambda it: it[0])
        
        # Initialize visited array to mark visited elements
        visited = [False] * n
        
        swaps = 0
        
        # Traverse the array and count cycles
        for i in range(n):
            # If element is already visited or it is already in the correct place
            if visited[i] or arrpos[i][1] == i:
                continue
            
            # Initialize cycle length
            cycle_size = 0
            k = i
            
            # import pdb;pdb.set_trace()
            # Visit all nodes in this cycle
            while not visited[k]:
                visited[k] = True
                k = arrpos[k][1]  # Move to the index of the next element in the cycle
                cycle_size += 1
            
            # If cycle size is greater than 1, then (cycle_size - 1) swaps are required
            if cycle_size > 1:
                swaps += (cycle_size - 1)
            
            if swaps == n-1:
                return swaps
        
        return swaps
s = Solution()
print(s.minSwaps())