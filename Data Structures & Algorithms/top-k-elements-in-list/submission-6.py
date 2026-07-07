class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #using bucket sort 
        #1.we create a dictionary to maintain a count
        #2.we maintain a frequency table of lenght nums+1
        count = {}
        freq = [[]for i in range(len(nums)+1)]
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
        