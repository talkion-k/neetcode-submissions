class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 0
        while n:
            i += 1
            n &= n - 1
        return i