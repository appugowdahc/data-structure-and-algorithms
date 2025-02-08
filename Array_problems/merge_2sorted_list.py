'''


Code
Testcase
Testcase
Test Result
21. Merge Two Sorted Lists
Solved
Easy
Topics
Companies
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
'''

###################################################

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        l1,l2 = list1,list2
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = ListNode(0)
        head = dummy

        while l1 and l2:
            if l1.val > l2.val:
                head.next = l2
                head = l2
                l2 = l2.next
            else:
                head.next = l1
                head = l1
                l1 = l1.next
            
        if l1:
            head.next = l1
        if l2:
            head.next = l2
         
        return dummy.next
        