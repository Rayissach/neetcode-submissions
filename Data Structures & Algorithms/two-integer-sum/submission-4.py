class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        currSum = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in currSum:
                return [currSum[diff], i]
            currSum[v] = i
        return