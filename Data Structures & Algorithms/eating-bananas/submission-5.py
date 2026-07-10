class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #firstly we create a range to binary search within
        #the range is from 1 to max(piles) as 1 is the least no of bananas that can be eaten per hour anf max(piles is the mos)
        #we also initilize a res(result) to r as thats the max and can be the result in anything
        #then while l<=r: we define the middle 
        #then for p in piles : we calculate the total hours and then see if they're within h
        #if yes then res is updated to k 
        #then return res 
        l, r = 1, max(piles)
        res = r
        while l<=r:
            k = (l+r)//2
            hours = 0
            for p in piles:
                hours += math.ceil(float(p)/k)
            if hours<=h:
                res =k
                r = k -1
            else:
                l = k+1
        return res
