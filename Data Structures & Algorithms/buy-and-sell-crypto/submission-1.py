class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        runningProfit = 0
        runningBuy = prices[0]

        for price in prices:
            runningProfit = max(runningProfit, price - runningBuy)
            runningBuy = min(runningBuy, price)
        
        return runningProfit