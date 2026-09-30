class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        maxCount = 0
        l = 0
        for i in range(len(s)):
            freq[s[i]] = 1 + freq.get(s[i], 0)
            while freq[s[i]] > 1:
                freq[s[l]] -= 1
                l += 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
            maxCount = max(maxCount, i - l + 1)
        return maxCount