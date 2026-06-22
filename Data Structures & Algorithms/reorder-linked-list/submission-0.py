# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the middle 
        fast, slow = head.next, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #revrse the second list
        second = slow.next 
        prev = slow.next = None  #imp remember
        while second:
            temp = second.next
            second.next = prev
            prev = second 
            second = temp 
        
        #now merge the two halves 
        first,second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1 #inc pointer
            second = temp2  #inc pointer 

        


        

        
            