class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i in range(len(nums)):
            minuend=nums[i]
            subtraend=target-minuend
            if subtraend in hash:
                return [hash[subtraend],i]
            hash[minuend]=i
