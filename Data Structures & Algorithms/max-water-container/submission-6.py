class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, 1
        rain = 0   #determines max total height * length
        res = 0
        while r < len(heights):
            rain = min(heights[r], heights[l]) * (r - l)
            if heights[r] > heights[l]:
                l, r = r, r + 1
            res = max(res, rain)
            r += 1
        return res
        