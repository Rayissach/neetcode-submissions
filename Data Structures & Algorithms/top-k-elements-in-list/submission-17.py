class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)
        for i, j in freq.items():
            res.append((i,j))
        res.sort(key=lambda x: x[1], reverse=True)
        return [x[0] for x in res][:k]