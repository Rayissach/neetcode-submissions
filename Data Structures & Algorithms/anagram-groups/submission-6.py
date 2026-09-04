class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashS = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            hKey = tuple(count)
            if hKey not in hashS:
                hashS[hKey] = []
            hashS[hKey].append(s)
        return list(hashS.values())