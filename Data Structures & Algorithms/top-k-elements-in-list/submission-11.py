class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return heapq.nlargest(k, set(nums))