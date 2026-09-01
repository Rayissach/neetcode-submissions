class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)
        for idx, curr in freq.items():
            res.append((curr, idx))
        res = sorted(res, reverse=True)
        return [item[1] for item in res][:k]

            