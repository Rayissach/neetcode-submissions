class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        ans = [True if v > 1 else False for i, v in freq.items()]
        return True if True in ans else False
