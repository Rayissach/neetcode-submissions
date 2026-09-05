class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = Counter(nums).most_common(k)
        # return [i for i, j in count]
        freq = {}
        #Find the occurence of each value in nums
        for i in nums:
            freq[i] = 1 + freq.get(i,0)
        res = []
        #Append tuple of Value and Frequency to res array
        for i, j in freq.items():
            res.append((i,j))
        #Sort res array by the Frequency and reverse order for highest occurences
        n = sorted(res, key=lambda x: x[1], reverse=True)
        #return list comprehension with values up to k items in array
        return [v for v,f in n][:k]

        