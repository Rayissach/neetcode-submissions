class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Trick is remove chars while length of the dict is > 1
        freq = {}
        maxFreq, maxCount = 0, 0
        l = 0
        for i in range(len(s)):
            freq[s[i]] = 1 + freq.get(s[i], 0)
            #Keep track of themax freq of curr char
            maxFreq = max(maxFreq, freq[s[i]])
            while k + maxFreq < i - l + 1:
                freq[s[l]] -= 1
                l += 1
            maxCount = max(maxCount, i - l + 1)
        return maxCount