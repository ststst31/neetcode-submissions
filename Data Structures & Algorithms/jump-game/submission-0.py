class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #firstly start a goal pointer at the end of the nums and then travel backways
        #for loop. 
        #if i + nums[i] >= goal then goal = i 
        #return True if goal == 0 else False 

        goal = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i]>=goal:
                goal = i 
        return True if goal == 0 else False    
        