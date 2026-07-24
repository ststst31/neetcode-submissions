class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #first we make a dictionary 
        #declare l pointer and res = 0 and maxf = 0 
      #add the s[r] to the dictionary 
        #then update maxf from values of dictionary values
        #then check if window is invalid and if yes then inc l ptr and remove s[l]
        #then calculate max res 
        #then return res 
        count = {}
        l = 0
        res = 0
        maxf = 0 
        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]]=1
            else:
                count[s[r]]+=1
            maxf = max(maxf, max(count.values()))
            while (r-l+1)-maxf > k:
                count[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
        return res 
        
        
