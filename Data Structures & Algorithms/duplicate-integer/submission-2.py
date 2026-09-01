class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)
        for v, k in freq.items():
            if k > 1:
                return True
        return False