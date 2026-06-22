class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # P = X ie the distance of the start of the cycle from the starting node will always be equal to the distance of the start of the cycle from the intersection of the first slow pointer and the fast pointer
        #O(n) and O(1)
        slow, fast = 0,0
        while True: #while true that slow and fast are both equal or intersection but we used while True so that it doesnt count the instance where both are at 0,0 where theyre already intersecting.
              slow = nums[slow]
              fast = nums[nums[fast]]
              if slow==fast:
                break 
        slow2=0
        while True:
            slow = nums[slow]
            slow2= nums[slow2]
            if slow==slow2:
                return slow 
                
            
        
        