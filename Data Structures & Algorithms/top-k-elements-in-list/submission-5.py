class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        freq = [[]for i in range(len(nums)+1)]

        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        
        for i, c in dic.items():
            freq[c].append(i)

        res = []
        for j in range(len(freq)-1,0,-1):
            for i in freq[j]:
                res.append(i)
                if len(res)==k:
                    return res
        