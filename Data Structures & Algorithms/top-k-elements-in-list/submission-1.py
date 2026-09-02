class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fin = {}
        res = []
        for n in nums:
            fin[n] = 1 + fin.get(n, 0)
        for i, v in fin.items():
            if v >= k:
                res.append(i)
        return res if res else nums