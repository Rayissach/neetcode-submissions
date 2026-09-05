class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # n = Counter(nums).most_common(k)
        # return [num for num, freq in n]
        freq = {}
        res = []
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)
        for char, count in freq.items():
            res.append((char, count))
        n = sorted(res, key=lambda x: x[1], reverse=True)
        return [i for i, j in n][:k]

        