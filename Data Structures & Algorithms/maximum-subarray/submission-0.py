class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0] #set the max subarray to the first index 
        carSum = 0 # initializing
        for i in nums:
            if carSum<0:
                carSum = 0
            carSum += i
            maxSub = max (maxSub, carSum)
        return maxSub
        