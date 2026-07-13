class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort algo 
        freq = [ [] for num in range(len(nums)+1)]
        count = {}
        for i in nums:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        for i, cnt in count.items():
            freq[cnt].append(i)
        res = []
        for j in range(len(freq)-1,0,-1):
            for i in freq[j]:
                res.append(i)
                if len(res)==k:
                    return res 
        