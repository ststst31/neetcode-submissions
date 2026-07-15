class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        k ={}
        p={}
        if len(s)!=len(t):
            return False
        for i in s:
            if i not in k:
                k[i] =1
            else:
                k[i]+=1
        for j in t:
            if j not in p:
                p[j]=1
            else:
                p[j]+=1
        return p == k 
        