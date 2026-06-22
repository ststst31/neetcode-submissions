class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashh=set()
        for i in nums:
            if i not in hashh:
                hashh.add(i)
            else:
                return i 
        #how to do this with using nums itself as ahas set?
        
        