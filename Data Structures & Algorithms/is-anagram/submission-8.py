class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        k={}
        p={}
        for i in s:
            if i not in k:
                k[i]=1
            else:
                k[i]+=1
        for i in t:
            if i not in p:
                p[i]=1
            else:
                p[i]+=1
        return p==k

        