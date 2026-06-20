# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # time : O(n+m) and space:  O(1)
        dummy = ListNode()
        tail = dummy
        while list1 and list2: #while both are not empty
            if list1.val < list2.val:
                tail.next = list1
                list1=list1.next
            else:
                tail.next=list2
                list2=list2.next
            tail = tail.next #shifting tail node regardless
        if list1: #if l1 not empty and l2 empty
            tail.next=list1
        elif list2: #if l2 non empty and l1 empty
            tail.next=list2
        return dummy.next 
