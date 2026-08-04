class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #first we declare a dictionary and initialize it 
        #we calculate maxf which is max of count.values()
        #we check if window is still valid and if it isnt we remove s[l] and increment l ptr
        
        count = {}
        maxf = 0 
        l = 0 
        res= 0 
        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]]=1
            else:
                count[s[r]]+=1
            maxf = max(maxf, max(count.values()))
            while (r-l+1)-maxf>k:
                count[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
        return res
        