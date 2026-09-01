class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        trapped = 0 
        max_rain = 0
        while l < r:
            trapped = min(heights[l], heights[r]) * (r - l)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            max_rain = max(max_rain, trapped)
        return max_rain