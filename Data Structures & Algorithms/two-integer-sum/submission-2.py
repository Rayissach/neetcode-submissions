class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapped = {}

        for i, v in enumerate(nums):
            currSum = target - v
            if currSum in mapped:
                return [mapped[currSum], i]
            mapped[v] = i