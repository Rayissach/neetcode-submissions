class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def nanaRate(rate):
            time = 0
            for i in range(len(piles)):
                time += (piles[i] + rate - 1) // rate
            return time
        l, r = 0, max(piles)
        while l < r:
            mid = (l + r) // 2
            if nanaRate(mid) > h:
                l = mid + 1
            else:
                r = mid 
        return l