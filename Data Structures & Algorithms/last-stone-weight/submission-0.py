class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            x, y = heapq.heappop_max(stones), heapq.heappop_max(stones)
            if x > y:
                heapq.heappush_max(stones, x - y)
        if len(stones) == 0:
            return 0
        else:
            return stones[0]