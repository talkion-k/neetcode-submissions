class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def minCostDP(i, memo):
            if i >= len(memo):
                return 0
            elif memo[i] != -1:
                return memo[i]
            else:
                oneStep = minCostDP(i + 1, memo)
                twoSteps = minCostDP(i + 2, memo)
                memo[i] = cost[i] + min(oneStep, twoSteps)
                return memo[i]
        memo = [-1] * len(cost)
        return min(minCostDP(0, memo), minCostDP(1, memo))