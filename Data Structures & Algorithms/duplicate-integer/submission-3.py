class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for i, v in freq.items():
            if v > 1:
                return True
        return False