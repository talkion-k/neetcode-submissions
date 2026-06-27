import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.kth = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.kth:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]