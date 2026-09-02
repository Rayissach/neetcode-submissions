class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # num_set = defaultdict(set)
        # count = 0
        # for i in nums:
        #     while i - 1 in num_set:
        #         count += 1
        #     num_set[i].add(count)
        # print(num_set)

        nums_s = sorted(list(set(nums)))
        longest = 1
        max_num = 1
        for i in range(1, len(nums_s)):
            if nums_s[i] == nums_s[i-1] + 1:
                longest += 1
            else:
                max_num = max(max_num, longest)
                longest = 1
        return max(longest, max_num)