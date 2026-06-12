class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        oplist=[]
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        countlist=list(count.keys())
        countlist.sort(key=lambda x: count[x], reverse=True)
        return countlist[:k]
        