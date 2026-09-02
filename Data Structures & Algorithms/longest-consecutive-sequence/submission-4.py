class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        max_len = 1
        length = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                length +=1 
            else:
                max_len = max(max_len, length)
                length = 1
        return max(max_len, length)