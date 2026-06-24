class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        sumMax = 0
        for i in nums:
            if sumMax < 0:
                sumMax = 0
            sumMax += i
            maxSub = max(maxSub, sumMax)
        return maxSub

        