class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapped = {}
        for i in nums:
            mapped[i] = 1+ mapped.get(i, 0)
        for k, v in mapped.items():
            if v >= 2:
                return True
        return False