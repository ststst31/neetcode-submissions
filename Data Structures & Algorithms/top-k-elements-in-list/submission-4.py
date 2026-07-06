class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashh = {}
        
        for i,a in enumerate(nums):
            if a not in hashh:
                hashh[a]=1
            else:
                hashh[a]+=1

        oplist = list(hashh.keys())
        oplist.sort(key = hashh.get, reverse = True)
        return oplist[:k]
        


        