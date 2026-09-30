class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Trick keep track of the maxfreq and count
        #when current position of i is greater than count k + max freq restrict the window
        #e.x. k = 2, X: 2 maxFreq = 4, i = 3, l = 0, i - l + 1 = 4
        #..... freq[X] - 1 = 1, return 4
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