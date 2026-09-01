class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)
        min_heap = []
        for n, count in freq.items():
            heapq.heappush(min_heap, (count, n))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [items[1] for items in min_heap]