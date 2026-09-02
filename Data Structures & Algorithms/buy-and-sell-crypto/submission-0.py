class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_price = 0
        curr_price = 0
        for r in range(1, len(prices)):
            max_price = max(max_price, curr_price)
            if prices[l] < prices[r]:
                curr_price = prices[r] - prices[l]
            else:
                l = r
        return max_price
            