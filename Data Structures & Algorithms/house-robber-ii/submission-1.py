class Solution:
    def rob(self, nums: List[int]) -> int:
        # recurrence relation:
        # skip = robRec(n + 1)
        # pick = nums[n] + robRec(n + 2)
        # max(skip, pick)
        memo1 = [-1] * len(nums)
        memo2 = [-1] * len(nums)

        def robRec(i, memo, fromFirst):
            if len(nums) == 1:
                return nums[0]
            if i >= len(nums) - int(fromFirst):
                return 0
            if memo[i] != -1:
                return memo[i]
            skip = robRec(i + 1, memo, fromFirst)
            pick = nums[i] + robRec(i + 2, memo, fromFirst)
            memo[i] = max(skip, pick)
            return memo[i]

        return max(robRec(0, memo1, True), robRec(1, memo2, False))
