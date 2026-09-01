class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for k, v in enumerate(nums):
            diff = target - v
            if diff in freq:
                return [freq[diff], k]
            freq[v] = k
        return 