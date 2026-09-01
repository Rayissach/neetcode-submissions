class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_price = 0
        curr_price = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                curr_price = prices[r] - prices[l]
                max_price = max(max_price, curr_price)
            else:
                l = r
            r += 1
        return max_price
            