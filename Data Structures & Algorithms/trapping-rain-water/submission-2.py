class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        acc_rain = 0
        curr_lmax = height[l]
        curr_rmax = height[r]
        while l < r:
            if curr_lmax < curr_rmax:
                l += 1
                curr_lmax = max(curr_lmax, height[l])
                acc_rain += (curr_lmax - height[l])
            else:
                r -= 1
                curr_rmax = max(curr_rmax, height[r])
                acc_rain += (curr_rmax - height[r])
        return acc_rain