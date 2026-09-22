class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        def profit(price):
            return max([price[i] - price[0] for i in range(len(price))])

        maxx = 0
        best_buy = float('inf')

        for i in range(len(prices)):
            if prices[i] < best_buy:
                new_maxx = profit(prices[i:])
                if new_maxx > maxx:
                    maxx = new_maxx
                    best_buy = prices[i]
        return maxx

        