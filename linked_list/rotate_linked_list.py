'''

Given a singly linked list of size N. The task is to left-shift the linked list by k nodes, where k is a given positive integer smaller than or equal to length of the linked list.

Example 1:

Input:
N = 5
value[] = {2, 4, 7, 8, 9}
k = 3
Output: 8 9 2 4 7
Explanation:
Rotate 1: 4 -> 7 -> 8 -> 9 -> 2
Rotate 2: 7 -> 8 -> 9 -> 2 -> 4
Rotate 3: 8 -> 9 -> 2 -> 4 -> 7
Example 2:

Input:
N = 8
value[] = {1, 2, 3, 4, 5, 6, 7, 8}
k = 4
Output: 5 6 7 8 1 2 3 4

Your Task:
You don't need to read input or print anything. Your task is to complete the function rotate() which takes a head reference as the first argument and k as the second argument, and returns the head of the rotated linked list.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 103
1 <= k <= N
'''



# Your task is to complete this function

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        if not head or k == 0:
            return head
        node = head
        length = 1
        while node.next:
            length+=1 
            node = node.next

        old_tail = node
        
        rotation = k%length
        
        if rotation == 0:
            return head
            
        new_tail_position = rotation
        new_tail = head
        while new_tail_position>1:
            new_tail = new_tail.next
            new_tail_position -= 1
            
        new_head = new_tail.next
        new_tail.next = None
        old_head = head
        old_tail.next = old_head
        head = new_head
        return head