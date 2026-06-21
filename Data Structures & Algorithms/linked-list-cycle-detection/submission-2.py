# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #floyds tortoise hare algo
        #there are two pointer: fast and slow the fast one jumps by 2 and the slow jumps by 1. 
        #if the two pointers meet---> cycle. 

        slow,fast = head, head
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True 
        return False 
        