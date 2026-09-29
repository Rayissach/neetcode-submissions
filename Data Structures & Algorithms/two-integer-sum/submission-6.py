class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = defaultdict()
        for i, v in enumerate(nums):
            currSum = target - v
            if currSum in freq:
                return [freq[currSum], i]
            freq[v] = i
        return
