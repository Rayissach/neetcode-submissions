class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for i, v in enumerate(nums):
            currSum = target - nums[i]
            if currSum in freq:
                return [freq[currSum], i]
            freq[v] = i
        return 