class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #firstly we create a minheap named array 
        #then for x,y in points we cal the distance
        #then we add the distance,x,y in the minheap such that distance is at the first index so that it gets considered while sorting in the minheap
        #then heapify minheap and then deca=lare res = 0. 
        #then while k>0 pop operation on x,y,distance and then dec k
        # we then append t res x and y and then finally return res
        minHeap = []
        
        for x, y in points:
            dist = (x**2)+(y**2)
            minHeap.append([dist,x,y])

        heapq.heapify(minHeap)
        res = []
        while k > 0:
            distance,x,y = heapq.heappop(minHeap)
            res.append([x,y])
            k-=1
        return res 




        