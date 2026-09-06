class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        maxLen = 0
        for i in nums:
            if (i - 1) not in n:
                length = 0
                while (i + length) in n:
                    length += 1
            maxLen = max(maxLen, length)
        return maxLen
