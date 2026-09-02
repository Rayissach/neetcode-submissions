class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        acc_rain = 0
        curr_lmax = height[l]
        curr_rmax = height[r]
        while l < r:
            curr_lmax = max(curr_lmax, height[l])
            curr_rmax = max(curr_rmax, height[r])
            if height[r] < curr_rmax:
                acc_rain += (curr_rmax - height[r])
            if height[l] < curr_lmax:
                acc_rain += (curr_lmax - height[l])
            l += 1
            r -= 1
        return acc_rain