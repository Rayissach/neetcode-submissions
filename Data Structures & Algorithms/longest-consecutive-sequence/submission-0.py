class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # num_set = defaultdict(set)
        # count = 0
        # for i in nums:
        #     while i - 1 in num_set:
        #         count += 1
        #     num_set[i].add(count)
        # print(num_set)

        nums_s = sorted(nums)
        print(nums_s)
        longest = 0
        res = []
        for i in range(1, len(nums_s)):
            if nums_s[i-1] != nums[i] + 1:
                res.append(longest)
                longest = 0
            longest +=1
        return len(res)