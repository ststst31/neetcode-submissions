class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashh = set()
        for i in nums:
            if i not in hashh:
                hashh.add(i)
            else:
                return True
        return False

        