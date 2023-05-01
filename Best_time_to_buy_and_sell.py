# Best Time to Buy and Sell Stock II

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        max_profit = 0
        for i in range(1, len(prices)):
            # print(prices[i])
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]

        return max_profit

#         max_profit = 0
#         min_price = prices[0]

#         for price in prices[1:]:
#             if price < min_price:
#                 min_price = price
#             else:
#                 profit = price - min_price
#                 if profit > max_profit:
#                     max_profit = profit

#         return max_profit
