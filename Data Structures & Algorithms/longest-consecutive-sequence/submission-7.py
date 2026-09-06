class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = sorted(set(nums))
        length = 1
        maxLen = 1
        for i in range(1, len(n)):
            if (n[i] - n[i-1]) > 2:
                length = 1
            length += 1
            maxLen = max(maxLen, length)
        return maxLen

