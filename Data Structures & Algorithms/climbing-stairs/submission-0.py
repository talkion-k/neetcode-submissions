class Solution:
    def climbStairs(self, n: int) -> int:
        def climbDP(i, memo):
            if i <= 2:
                return i
            elif memo[i] != -1:
                return memo[i]
            else:
                memo[i] = climbDP(i - 1, memo) + climbDP(i - 2, memo)
                return memo[i]
        memo = [-1] * (n + 1)
        return climbDP(n, memo)
            
            
        
        