class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        maxCount = float('-inf')
        l = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            while freq[s[r]] > 1:
                freq[s[l]] -= 1
                l += 1
            maxCount = max(maxCount, r - l + 1)
        return maxCount 
            
