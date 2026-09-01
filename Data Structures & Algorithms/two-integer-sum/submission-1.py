class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapped = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in mapped:
                return [mapped[diff], i]
            mapped[v] = i
        