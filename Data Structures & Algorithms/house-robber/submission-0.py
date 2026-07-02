class Solution:
    def rob(self, nums: List[int]) -> int:
        # for any given house, find the max of two decisions:
        # skip it and find the max money gained from the next house onward
        # rob this and find the max money gained from the next 2 houses onward
        # max(rob(n + 1), nums[n] + rob(n + 2))
        memo = [-1] * (len(nums))
        def robRec(i, memo):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            skip = robRec(i + 1, memo)
            pick = nums[i] + robRec(i + 2, memo)
            memo[i] = max(skip, pick)
            return memo[i]
        return robRec(0, memo)
            
