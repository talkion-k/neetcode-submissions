class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dictionary to track frequencies
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for key in freq:
            buckets[freq.get(key)].append(key)
        ans = []
        for i in range(-1, len(buckets) * -1, -1):
            if len(ans) >= k:
                return ans
            ans.extend(buckets[i])
        return ans