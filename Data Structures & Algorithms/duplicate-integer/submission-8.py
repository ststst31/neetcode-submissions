class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashh = set()
        for i in nums:
            if i in hashh:
                return True 
            else:
                hashh.add(i)
        return False
        