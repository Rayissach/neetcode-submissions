class Solution:
    def maxArea(self, h: List[int]) -> int:
        l, r = 0, len(h)-1
        res = 0
        while l <= r:
            maxH = min(h[r], h[l]) * (r - l)
            if h[l] > h[r]:
                r -= 1
            else:
                l += 1
            if maxH >= res:
                res = maxH
        return res
