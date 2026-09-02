class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sum_map = {}

        for k, v in enumerate(numbers, start=1):
            sum_map[k] = v
        for i in numbers:
            curr_sum = target - i
            if curr_sum in sum_map:
                return [sum_map[i], sum_map[curr_sum]]
        return