'''
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

Example 1:
Input: head = [1]
Output: []

Example 2:
Input: head = [1,2,3,4]
Output: [1,2,4]

Example 3:
Input: head = [2,1]
Output: [2]

Example 4:
Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
'''




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        
        prev.next = slow.next
        return head