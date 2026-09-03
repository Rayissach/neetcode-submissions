class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        currSum = {}
        for i, v in enumerate(nums):
            numDiff = target - v
            if numDiff in currSum:
                return [currSum[numDiff], i]
            currSum[v] = i
        return 