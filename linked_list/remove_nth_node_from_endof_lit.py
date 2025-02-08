'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
'''

########################################################

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        # Calculate the length of the linked list
        l = 0
        tail = head
        while tail is not None:
            l += 1
            tail = tail.next

        # Handle the case where the target node is the head
        if l == n:
            return head.next

        # Find the node before the target node
        target_node = l - n
        tail = head
        match = 1
        while tail is not None:
            if match == target_node:
                # print(tail.val,match,l)
                break
            match += 1
            tail = tail.next

        # Remove the target node
        tail.next = tail.next.next

        return head


######################################################


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy

    # Move the first pointer ahead by n+1 steps
    for i in range(n + 1):
        first = first.next

    # Move both pointers together until the first pointer reaches the end
    while first is not None:
        first = first.next
        second = second.next

    # Remove the nth node from the end
    second.next = second.next.next

    return dummy.next

# Helper function to print the linked list
def printLinkedList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

# Test cases
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n1 = 2
result1 = removeNthFromEnd(head1, n1)
printLinkedList(result1)  # Output: 1 2 3 5

head2 = ListNode(1)
n2 = 1
result2 = removeNthFromEnd(head2, n2)
printLinkedList(result2)  # Output: (empty list)

head3 = ListNode(1, ListNode(2))
n3 = 1
result3 = removeNthFromEnd(head3, n3)
printLinkedList(result3)  # Output: 1


###################################################

