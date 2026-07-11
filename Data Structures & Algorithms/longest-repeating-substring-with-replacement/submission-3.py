class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #initialize the dictionary, the left pointer, the res and maxf
        count ={} #we declare a dictionary to keep count of s[r]
        l=0
        maxf=0
        res = 0 
        for r in range(len(s)):
            #get a count of all s[r] and put it in the dict
            if s[r] not in count:
                count[s[r]]=1
            else:
                count[s[r]]+=1
            maxf = max(maxf, max(count.values())) #get the max of count.values()
            #if the window becomes invalid:
            while (r-l+1) - maxf > k:
                count[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
        return res             

        