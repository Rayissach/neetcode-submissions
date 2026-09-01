class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)
        for i, v in freq.items():
            if v > 1:
                return True
        return False
        