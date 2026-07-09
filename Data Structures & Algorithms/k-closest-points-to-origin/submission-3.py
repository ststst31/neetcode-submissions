class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #firstly we created a minheap = []
        #then for x,y in points: we calculate the d 
        #then we append [d,x,y] to the minheap 
        #then we heapify minheap 
        #while k > 0: we pop from minheap and append the popped elements to res = []
        # then decerement k 
        # return res 
        minheap =[]
        for x,y in points:
            d = (x**2) + (y**2)
            minheap.append([d,x,y])
        heapq.heapify(minheap)
        res = []
        while k > 0:
            d,x,y = heapq.heappop(minheap)
            res.append([x,y])
            k-=1
        return res 
        