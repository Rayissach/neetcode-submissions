class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)
        res = []
        for v, curr in freq.items():
            res.append((v, curr))
        res = sorted(res, key=lambda item: item[1], reverse=True)
        return [items[0] for items in res][:k]