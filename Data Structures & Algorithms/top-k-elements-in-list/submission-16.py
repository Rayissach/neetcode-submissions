class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        stack = deque()
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)
        for i, v in freq.items():
            stack.append(i)
            while len(stack) > k:
                stack.popleft()
        return list(stack)