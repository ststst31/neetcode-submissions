class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s):
            return False
        countS,countT={},{}
        for i in range(len(s)):
            charS=s[i]
            if charS in countS:
                countS[charS]+=1
            else:
                countS[charS]=1
            charT=t[i]
            if charT in countT:
                countT[charT]+=1
            else:
                countT[charT]=1
        return countT==countS
        
            
        
