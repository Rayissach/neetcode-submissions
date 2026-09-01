class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_price = 0
        total = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                total = prices[r] - prices[l]
                max_price = max(max_price, total)
            else:
                l = r
            r += 1
        return max_price
            