class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.minHeap, self.k= nums, k 
        heapq.heapify(self.minHeap)
        while len(self.minHeap)>k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        