class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        rain = 0   #determines max total height * length
        res = 0
        while l < r:
            rain = min(heights[r], heights[l]) * (r - l)
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
            res = max(res, rain)
        return res
        