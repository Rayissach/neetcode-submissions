class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = Counter(nums).most_common(k)
        return [num for num, freq in n]