# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #its a two pointer solution so O(n)
        #firstly we create a dummy node 
        #we initialize left and right pointers and then we make the pointers travel to the end of the node.
        #then we delete the nth node by left = left.next.next 

        dummy = ListNode(0,head)
        left = dummy 
        right = head 

        while n > 0 and right: #meaning till right reaches the end of the list
            right = right.next
            n -=1 
        while right:
            left = left.next 
            right= right.next 
        #now deletion
        left.next = left.next.next #skipping the nth node
        return dummy.next 


        

        