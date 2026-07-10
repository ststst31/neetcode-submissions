class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #firstly we create a range in which we need to binary search
        #this range is from 1 (least no of bananas that can be eaten in an hour) to the max no of bananas present in the pile 
        #we initialize a res at the postion r as r is at max(piles) if not anything res = r will be the ans
        #then we apply binary search 
        l, r = 1, max(piles)
        res = r 
        while l<=r:
            k = (l+r)//2 #binary search
            hours = 0
            for p in piles:
                hours += math.ceil(float(p)/k)
            if hours<=h: # total nos of hours is well within the hours
                res = k  #update result to newest min 
                r = k -1 # we try to search an even smaller no if present 
            else:
                l = k+1
        return res 