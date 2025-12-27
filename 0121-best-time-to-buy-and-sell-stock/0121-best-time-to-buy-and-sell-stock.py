class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current_buy = float("inf")
        for price in prices:
            if price < current_buy:
                current_buy = price
            if (price - current_buy) > max_profit:
                max_profit = price - current_buy
        return max_profit
        