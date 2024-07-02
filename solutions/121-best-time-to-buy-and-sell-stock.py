class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_at, sell_at = 0, 1
        max_profit = 0

        while sell_at < len(prices):
            if prices[buy_at] < prices[sell_at]:
                profit = prices[sell_at] - prices[buy_at]
                if profit > max_profit:
                    max_profit = profit
            else:
                buy_at = sell_at
            sell_at += 1

        return max_profit


# Two-pointer problem
# Track maximum profit, pointer for the index to buy at, pointer to sell at
# If the price at buy < price at sell, the trade is profitable
# Calculate the profit and update the max if greater than current max
# Else the sell pointer is on a new lowest price, so update the buy pointer
# equal to the sell pointer
# Increment the sell pointer every iteration
