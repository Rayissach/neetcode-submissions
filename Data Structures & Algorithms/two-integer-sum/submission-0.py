class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        fin = {}
        calc = 0
        for i in range(len(nums)):
            calc = target - nums[i]
            if calc in fin:
                return [fin[calc], i]
            fin[nums[i]] = i
        