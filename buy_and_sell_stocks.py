class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        lp = 0
        rp = 1
        profit = 0

        while rp < len(prices):
            profit = max(profit, prices[rp] - prices[lp])

            if prices[lp] > prices[rp]:
                lp += 1
            else:
                rp += 1

            if lp == rp:
                rp += 1
        


        return profit
        