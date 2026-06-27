class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        j = 0
        for i in nums:
            j = i ^ j
        return j